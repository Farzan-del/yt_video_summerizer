from crewai import Task
from tools import yt_tool
from agents import blog_researcher,blog_writer


research_task=Task(
    description=(
        "Identify the video {topic}."
        "Get detaile information about the vidofrom the channel."
    ),
    expected_output='a comprehensive 3 paragraphs long report based on the {topic}',
    tools=[yt_tool],
    agent=blog_researcher
)

write_task=Task(
    description=(
        "get info from the yt channel."
    ),
    expected_output='a summarized 3 paragraphs long report based on the {topic}',
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file='new-blog-post.md'
)