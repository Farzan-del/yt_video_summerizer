from crewai import Crew, Process
from task import research_task,write_task
from agents import blog_researcher,blog_writer

CREW=Crew(
    agents=[blog_researcher,blog_writer],
    task=[research_task,write_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

result=Crew.kickoff(inputs={'topic':'Ai vs ml vs dl vs data science'})
print(result)