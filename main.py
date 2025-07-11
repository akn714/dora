import os
from dotenv import load_dotenv
from groq import Groq

from colored import *
from get_input import get_input

load_dotenv()

INTRO_TEXT = """
.________       ____     _______           __            ________        ____     _______          __                    
|_   ___ `.   .'    `.  |_   __ \         /  \          |_   ___ `.    .'    `.  |_   __ \        /  \           _       
  | |   `. \ /  .--.  \   | |__) |       / /\ \           | |   `. \  /  .--.  \   | |__) |      / /\ \         | |      
  | |    | | | |    | |   |  __ /       / ____ \          | |    | |  | |    | |   |  __ /      / ____ \        | |      
 _| |___.' / \  `--'  /  _| |  \ \_   _/ /    \ \_       _| |___.' /  \  `--'  /  _| |  \ \_  _/ /    \ \_      | |      
|________.'   `.____.'  |____| |___| |____|  |____|     |________.'    `.____.'  |____| |___||____|  |____|     |_|      
                                                                                                                (_)      
""".strip()

os.system('clear')

class GroqAI:
    model = "llama-3.3-70b-versatile"

    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def get_llm_response(self, messages):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
        )
        output = response.choices[0].message.content.strip()

        if output and (output[0] == output[-1]) and output.startswith(("'", '"')):
            output = output[1:-1]

        return output
    pass

def get_prompt():
    prompt = get_input('>>> ').strip()
    return prompt

# def get_input(start_str):
#     # print("Enter multiple lines (press Ctrl+D to finish):")
#     print(start_str, end='')
#     try:
#         lines = []
#         while True:
#             line = input()
#             lines.append(line)
#     except EOFError:
#         pass

#     multi_line_string = '"""\n' + '\n'.join(lines) + '\n"""'
#     return multi_line_string


def greet():
    print(INTRO_TEXT)
    print('[esc+enter]: submit the prompt | [enter]: enter a new line')
greet()

llm = GroqAI()

messages = [
    {
        'role': 'system',
        'content': """
        You are an helpful assistant named mini-dora, that runs on a CLI. Your name comes from a character in doremon, the mini-doremon (3 mini versions of doremon).
        You respond to users in a short and concise way, and you responses should be formated in a way that should be clearly visible on cli
        """
    }
]

while True:
    try:
        prompt = get_prompt()
        if prompt=='exit' or prompt=='bye': break
        if prompt=='clear': os.system('clear'); greet(); continue;
        messages.append({
            'role': 'user',
            'content': prompt
        })
        res = llm.get_llm_response(messages)
        messages.append({
            'role': 'assistant',
            'content': res
        })
        cprint('>>>', res, RED)
    except Exception as e:
        cprint('>>>', "Sorry I'm unable to responsed", RED)

