from typing import Optional
from crewai import Agent, Task, Crew, Process
from crewai.tools.base_tool import BaseTool
import requests
from bs4 import BeautifulSoup

class ScrapeTool(BaseTool):
    """Simple tool to scrape text from a webpage using BeautifulSoup."""

    name: str = "web_scraper"
    description: str = (
        "Fetches a URL and returns the text of the first element matching a CSS selector."
    )

    def _run(self, url: str, selector: str) -> str:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        element = soup.select_one(selector)
        return element.get_text(strip=True) if element else ""


def create_crew(url: str, selector: str) -> Crew:
    tool = ScrapeTool()
    agent = Agent(
        role="Web Scraper",
        goal="Collect information from websites",
        backstory="Uses HTTP requests and BeautifulSoup to read page data",
        tools=[tool],
        allow_delegation=False,
        llm="gpt-3.5-turbo",
    )

    task = Task(
        description=f"Scrape {url} using selector '{selector}'",
        expected_output="Extracted text from the page.",
        agent=agent,
    )

    return Crew(agents=[agent], tasks=[task], process=Process.sequential)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run a simple CrewAI web scraper")
    parser.add_argument("url", help="URL to scrape")
    parser.add_argument(
        "selector", help="CSS selector to extract", default="title", nargs="?"
    )
    args = parser.parse_args()

    crew = create_crew(args.url, args.selector)
    result = crew.kickoff()
    print(result)
