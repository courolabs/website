from dotenv import load_dotenv
from openai import OpenAI
import random
import os


load_dotenv()


def read_file(path) -> str:
    with open(path, 'r') as file:
        return file.read()


def write_file(path, contents):
    with open(path, 'w') as file:
        file.write(contents)
    

def hash() -> str:
    hash = random.randint(0, 65535)
    
    return f"{hash:04x}"



class Model:
    def __init__(self) -> None:
        self.client = OpenAI()


    def query(self, prompt: str):
        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": ""},
                {"role": "user", "content": prompt}
            ])
        
        return completion.choices[0].message.content
    

if __name__ == '__main__':
    model = Model()

    for f in os.listdir('survey/responses/'):
        prompt = read_file(f'survey/profile.xml')
        prompt += read_file(f'survey/responses/{f}')
        prompt += read_file(f'survey/survey.xml')

        response = model.query(prompt)

        write_file(f'survey/s/{hash()}.xml', response)