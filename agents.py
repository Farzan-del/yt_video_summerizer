from crewai import Agent
from tools import yt_tool
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI  # Correct LLM import

# Load environment variables
print("[DEBUG] Loading .env variables...")
load_dotenv()

# Check and print API key
api_key = os.getenv("OPENAI_API_KEY")
print(f"[DEBUG] OPENAI_API_KEY = {api_key}")

# Setup LLM (OpenAI)
try:
    llm = ChatOpenAI(
        model="gpt-4-0125-preview",
        temperature=0.7,
        api_key=api_key
    )
    print("[DEBUG] LLM initialized successfully.")
except Exception as e:
    print(f"[ERROR] Failed to initialize LLM: {e}")
    llm = None  # So it doesn't crash later

# Blog Researcher Agent
try:
    blog_researcher = Agent(
        role='Blog researcher from yt videos',
        goal='Get the relevant video content for the topic {topic} from YouTube channel',
        verbose=True,
        memory=True,
        backstory='Expert in understanding videos in AI, Data Science, Machine Learning, and Gen AI and providing suggestions.',
        llm=llm,
        tools=[yt_tool],
        allow_delegation=True
    )
    print("[DEBUG] blog_researcher agent initialized successfully.")
except Exception as e:
    print(f"[ERROR] Failed to initialize blog_researcher agent: {e}")

# Blog Writer Agent
try:
    blog_writer = Agent(
        role='Blog writer',
        goal='Narrate compelling tech stories about the video {topic}',
        verbose=True,
        memory=True,
        backstory='Engages and captivates the audience with informative writing.',
        llm=llm,
        tools=[yt_tool],
        allow_delegation=False
    )
    print("[DEBUG] blog_writer agent initialized successfully.")
except Exception as e:
    print(f"[ERROR] Failed to initialize blog_writer agent: {e}")
