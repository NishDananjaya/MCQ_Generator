import os
import json
import pandas as pd
import traceback
from dotenv import load_dotenv
# from utils import read_file,get_table_data
# from logger import logging

# importing the necessary packages from langchain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
import PyPDF2

# load the enviorenmental varables from the dot env file
load_dotenv()

# access the enviorenment varaibles 
key = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro",temperature=0.5, google_api_key=key)

TEMPLATE = """
Text:{text}
You are an expert mcq maker. Given above the text, it is your job to \
create a quiz of {number} multiple questions for {subject} students in {tone} tone.
Make sure to format your response like RESPONSE_JSON below and use it as guide.\
Ensure to make {number} MCQs
### RESPONSE_JSON
{response_json}

"""

quiz_generation_prompt = PromptTemplate(
    input_variables=["text", "number","subject","tone","response_json"],
    template=TEMPLATE
)

quiz_chain = LLMChain(llm = llm, prompt = quiz_generation_prompt,output_key="quiz",verbose=True)

TEMPLATE2 = """
You are an expert grammerian and writer. Given a multiple choice question for {subject} students.\
you need to evaluate the complexicity of the question and give a complete analysis of the quiz. only use at max 50 words for complexicity
if the quiz is not at par with the cognitive and analytical abilities of the student,\
update the quiz questions which needs to be changed and the change the tone such that it perfectly fit the students ability.\
Quiz_MCQs:
{quiz}

Check from an expert English writer of the above quiz:
"""

quiz_evaluation_prompt = PromptTemplate(
    input_variables=["subject","quiz"],
    template=TEMPLATE2
)

review_chain = LLMChain(llm=llm, prompt=quiz_evaluation_prompt,output_key="review",verbose=True)

generate_evaluate_chain = SequentialChain(
    chains = [quiz_chain,review_chain],
    input_variables = ["text", "number","subject","tone","response_json"],
    output_variables = ["quiz","review"],
    verbose = True
)



