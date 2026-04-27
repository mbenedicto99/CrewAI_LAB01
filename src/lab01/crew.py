from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class Lab01:
    """Lab01 crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def analista_incidente(self) -> Agent:
        return Agent(
            config=self.agents_config["analista_incidente"],
            verbose=True
        )

    @agent
    def redator_rca(self) -> Agent:
        return Agent(
            config=self.agents_config["redator_rca"],
            verbose=True
        )

    @task
    def analise_incidente(self) -> Task:
        return Task(
            config=self.tasks_config["analise_incidente"]
        )

    @task
    def relatorio_rca(self) -> Task:
        return Task(
            config=self.tasks_config["relatorio_rca"]
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
