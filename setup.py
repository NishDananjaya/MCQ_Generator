from setuptools import find_packages,setup

setup(
    name = "MCQ_Generator",
    version = "0.0.1",
    author="Nishan Dananjaya",
    author_email="nishandananjaya27038@gmail.com",
    install_requires = ["openai","Langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
    )

from langchain.chat_models import ChatOpenAI