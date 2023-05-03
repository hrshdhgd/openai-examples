"""Main python file."""
import os

import openai
from dotenv import find_dotenv, load_dotenv

_ = load_dotenv(find_dotenv())  # read local .env file


class OpenAIClient:
    """Client class."""

    model: str = "gpt-3.5-turbo"
    context = [
        {
            "role": "system",
            "content": """You are ChatBot whose duty
            is to answer questions from users.""",
        }
    ]

    def __post_init__(self):
        """Initialize the object."""
        if not openai.api_key:
            openai.api_key = os.getenv("OPENAI_API_KEY_2")

    def get_completion(self, prompt) -> str:
        """Return response via API."""
        self.context.append({"role": "user", "content": prompt})
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.context,
            temperature=0,  # this is the degree of randomness of the model's output
        )
        return response.choices[0].message["content"]

    def get_completion_from_messages(self, messages, temperature=0) -> str:
        """Return response via API."""
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            temperature=temperature,  # this is the degree of randomness of the model's output
        )
        return response.choices[0].message["content"]

    def update_context(self, role, content):
        """Update the context of OpenAIClient object."""
        self.context.append({"role": role, "content": content})


def demo(input: str):
    """Define API."""
    client = OpenAIClient()
    client.update_context(role="user", content=input)
    return client.get_completion_from_messages(client.context)


if __name__ == "__main__":
    demo(input="Hello, world!")
