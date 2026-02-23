import os
from langsmith import Client
from dotenv import load_dotenv

load_dotenv()

client = Client(
    api_key=os.getenv("LANGCHAIN_API_KEY"),
    project=os.getenv("LANGCHAIN_PROJECT")
)

def log_interaction(prompt, response):
    client.create_run(
        name="RealEstateAgent",
        inputs={"query": prompt},
        outputs={"answer": response}
    )