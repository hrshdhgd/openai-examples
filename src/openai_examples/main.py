"""Main python file."""
import os

import openai
from dotenv import find_dotenv, load_dotenv

_ = load_dotenv(find_dotenv())  # read local .env file


class OpenAIClient:
    model: str = "gpt-3.5-turbo"
    context = [
        {
            "role": "system",
            "content": """You are ChatBot whose duty is to answer questions from users.""",
        }
    ]

    def __post_init__(self):
        if not openai.api_key:
            openai.api_key = os.getenv("OPENAI_API_KEY_2")

    def get_completion(self, prompt):
        self.context.append({"role": "user", "content": prompt})
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.context,
            temperature=0,  # this is the degree of randomness of the model's output
        )
        return response.choices[0].message["content"]

    def get_completion_from_messages(self, messages, temperature=0):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            temperature=temperature,  # this is the degree of randomness of the model's output
        )
        return response.choices[0].message["content"]

    def update_context(self, role, content):
        self.context.append({"role": role, "content": content})


def demo(input: str):
    """Define API."""
    client = OpenAIClient()
    client.update_context(role="user", content=input)
    return client.get_completion_from_messages(client.context)
    # text = """
    # You should express what you want a model to do by \
    # providing instructions that are as clear and \
    # specific as you can possibly make them. \
    # This will guide the model towards the desired output, \
    # and reduce the chances of receiving irrelevant \
    # or incorrect responses. Don't confuse writing a \
    # clear prompt with writing a short prompt. \
    # In many cases, longer prompts provide more clarity \
    # and context for the model, which can lead to \
    # more detailed and relevant outputs.
    # """
    # prompt = f"""
    # Summarize the text delimited by triple backticks \
    # into a single sentence.
    # ```{text}```
    # """
    # response = client.get_completion(prompt)
    # print(response)

    # messages = [
    #     {"role": "system", "content": "You are an assistant that speaks like Shakespeare."},
    #     {"role": "user", "content": "tell me a joke"},
    #     {"role": "assistant", "content": "Why did the chicken cross the road"},
    #     {"role": "user", "content": "I don't know"},
    # ]
    # response = client.get_completion_from_messages(messages, temperature=1)
    # print(response)


if __name__ == "__main__":
    demo()
