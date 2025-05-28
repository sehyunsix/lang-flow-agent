from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Kioskcrew():
    """Kioskcrew crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    # @agent
    # def researcher(self) -> Agent:
    # 	return Agent(
    # 		config=self.agents_config['researcher'],
    # 		verbose=True
    # 	)

    # @agent
    # def reporting_analyst(self) -> Agent:
    # 	return Agent(
    # 		config=self.agents_config['reporting_analyst'],
    # 		verbose=True
    # 	)

    @agent
    def screen_analyst(self) -> Agent:
        return Agent(

			config=self.agents_config['screen_analyst'],
			verbose=True
		)

    @agent
    def action_planner_with_screenshots(self) -> Agent:
        return Agent(
			config=self.agents_config['action_planner_with_screenshots'],
			verbose=True
		)

    @agent
    def computer_action_generator(self) -> Agent:
        return Agent(
			config=self.agents_config['computer_action_generator'],
			verbose=True
		)

    @task
    def action_planning_task(self) -> Task:
        return Task(
			config=self.tasks_config['action_planning_task'],
			output_file='action_plan.json'
		)

    @task
    def screen_analysis_task(self) -> Task:
        return Task(
			config=self.tasks_config['screen_analysis_task'],
			output_file='screen_analysis.json'
		)

    @task
    def computer_action_generation_task(self) -> Task:
        return Task(
            config=self.tasks_config["computer_action_generation_task"],
            output_file="computer_action.json",
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    # @task
    # def research_task(self) -> Task:
    # 	return Task(
    # 		config=self.tasks_config['research_task'],
    # 	)

    # @task
    # def reporting_task(self) -> Task:
    # 	return Task(
    # 		config=self.tasks_config['reporting_task'],
    # 		output_file='report.md'
    # 	)

    @crew
    def crew(self) -> Crew:
        """Creates the Kioskcrew crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
