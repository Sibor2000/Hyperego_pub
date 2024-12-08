from typing import List
from g4f import Provider, models
from langchain_g4f import G4FLLM
from langchain.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain.output_parsers import YamlOutputParser
import yaml

from hyperego.scrapers import ScrapeResult

class AnalysisResult(BaseModel):
    """The evaluation of the post"""
    
    quality: int = Field(description='The quality of the post on a scale of 1 to 10')
    improvements: List[str] = Field(description='A list of improvements that can be made to the post')
    verdict: str = Field(description='The final verdict of the post, one of (professional, neutral, unprofessional)')

class PostAnalyzer:
    def __init__(self):
        self.llm = G4FLLM(
            model=models.gemini_pro,
            provider=Provider.Blackbox,
        )

        # Get a parser for the structure of the expected response
        self.parser = YamlOutputParser(pydantic_object=AnalysisResult)

        self.prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                "You are a social media analyzer that evaluates posts.\n{format_instructions}"
            ),
            ("user", "{post}"),
        ]).partial(format_instructions=self.parser.get_format_instructions())

    def analyze(self, post: dict) -> AnalysisResult:
        chain = self.prompt | self.llm | self.parser

        # Get the yaml representation of the post
        data = yaml.dump(post)

        # Run the post through the language model
        try:
            return chain.invoke({
                "post": data
            })
        except Exception as e:
            print('Error analyzing post:', e)
            return AnalysisResult(
                quality=3,
                improvements=[],
                verdict="neutral"
            )