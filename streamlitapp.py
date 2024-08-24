import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file,get_table_data
import streamlit as st
from src.mcqgenerator.MCQGenerater import generate_evaluate_chain
from src.mcqgenerator.logger import logging

#loading the json file
with open("response.json", 'r') as file:
    RESPONSE_JSON = json.load(file)

#creating the title for the app
st.title("MCQ Generator Application with Langchain 😎🐦🔗🔗")

#Creating a form using st.form
with st.form("user_inputs"):
    #file upload
    uploaded_file = st.file_uploader("Upload the file as PDF or txt")

    #input fields
    mcq_count = st.number_input("No. of MCQs",min_value=3,max_value=50)

    #subject
    subject = st.text_input("Enter a subject",max_chars=20)

    #quiz tone
    tone = st.text_input("Complexity level of questions",max_chars=20,placeholder='Simple')

    #add button
    button = st.form_submit_button("Create MCQs")

    #check if the button is clicked and all the fields are added

    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("loading...."):
            try:
                text = read_file(uploaded_file)
                response = generate_evaluate_chain(
                    {
                        "text": text,
                        "number": mcq_count,
                        "subject": subject,
                        "tone": tone,
                        "response_json": json.dumps(RESPONSE_JSON)
                    }
                )
                #st.write(response)

            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error("Error")
            
            else:
                if isinstance(response,dict):
                    #extract the quiz data from the response
                    quiz = response.get("quiz",None)
                    quiz_string = quiz.replace("```json", "").replace("```", "").strip()   
                    if quiz_string is not None:
                        table_data = get_table_data(quiz_string)
                        if table_data is not None:
                            df = pd.DataFrame(table_data)
                            df.index = df.index + 1
                            st.table(df)
                            #display the review in a text box as well
                            st.text_area(label="Review",value=response["review"])
                        else:
                            st.error("Error in the table data")
                    else:
                        st.write(response)
                
        


