import os

from openai import OpenAI

openai_client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),
)


def ask_gpt(sys_prompt, model="gpt-3.5-turbo-0125"):
    messages = [
        {"role": "system", "content": sys_prompt},
    ]

    response = openai_client.chat.completions.create(
        model=model,
        messages=messages,
    )

    return response.choices[0].message.content
