import os
import openai
from dotenv import find_dotenv, load_dotenv
from typing_extensions import Protocol
from langchain.llms import OpenAI

load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")

import os
api_key = os.environ.get('OPENAI_API_KEY')
# from langchain.llms import OpenAI

# llm = OpenAI(openai_api_key=api_key,model_name="text-davinci-003",temperature=0.9)
# x = llm(prompt='"What would be a good company name for a company that makes colorful socks?"')

# print(x)


# llm_model = "gpt-4"
# llm_model = "text-davinci-003"
llm_model = "gpt-3.5-turbo-instruct"

llm = OpenAI(temperature =0.7)
llm = OpenAI(openai_api_key=api_key,model_name=llm_model,temperature=0.9)
print('*******************'+os.environ.get("OPENAI_API_KEY"))
print(llm(prompt  ='What is the weather in  Chicago IL'))
