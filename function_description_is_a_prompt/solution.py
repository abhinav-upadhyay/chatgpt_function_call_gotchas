from typing import List, Dict
import openai
import requests
from pprint import pprint

GPT_MODEL = "gpt-3.5-turbo-0613"
SYSTEM_PROMPT = """
    You are a helpful AI assistant. You answer the user's queries.
    When you are not sure of an answer, you take the help of
    functions provided to you.
    NEVER make up an answer if you don't know, just respond
    with "I don't know" when you don't know.
    Ask clarifying questions when you need more information
    """

functions = [
    {
        "name": "python",
        "description": """
                    Read the value printed by the given python code.
                    The code SHOULD explicitly call print so that
                    this function returns the output.
                    
                    For example: "import math; print(math.pi)"
                    is correct

                    But "import math; math.pi" is incorrect because
                    it doesn't print the value            
            """,
        "parameters": {
            "type": "object",
            "properties": {
                "code": {
                    "type": "string",
                    "description": "Python code which needs to be executed"
                }
            }
        }
    }
]

def _chat_completion_request(messages) -> Dict:
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + openai.api_key,
    }
    body = {
        "model": GPT_MODEL,
        "messages": messages,
        "functions": functions,
        "temperature": 0.7
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers=headers,
        json=body,
    )
    return response.json()["choices"][0]["message"]

messages: List[Dict] = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": "what is today's date?"}
]
response = _chat_completion_request(messages)

if (response.get('function_call')):
    pprint(response.get('function_call'))
else:
    pprint(response)