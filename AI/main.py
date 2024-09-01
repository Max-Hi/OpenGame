import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_anthropic import ChatAnthropic


# Load environment variables from .env file
load_dotenv()

model = {
    "sonnet": "claude-3-sonnet-20240229",
    "haiku": "claude-3-haiku-20240307",
}

def generate_text(prompt: str, model: str = model["haiku"], max_tokens: int = 100) -> str:
    llm = ChatAnthropic(anthropic_api_key = os.getenv('ANTHROPIC_API_KEY'), model=model, temperature=0.2, max_tokens=max_tokens)
    # template = PromptTemplate(input_variables=["prompt"], template="{prompt}")
    template = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a storyteller. You are given the beginning of a story and then you complete it.",
        ),
        ("human", "{prompt}"),
        ])
    chain = template | llm
    response = chain.invoke({
                    "prompt": prompt,
                    })
    # response.metadata, response.id and response.usage_metadata might be interesting in the future. 
    return response.content 



print(generate_text("One night the lonly wanderer spoke at the fireplace: ", model=model["haiku"]))