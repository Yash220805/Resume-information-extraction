import streamlit as st
from langchain.prompts import ChatPromptTemplate,PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from langchain.output_parsers.json import SimpleJsonOutputParser
from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader
import tempfile


import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
os.environ["HUGGINGFACE_API_KEY"]=os.getenv("HUGGINGFACE_API_KEY")

##Setting up the schema ensures that the output (info) that we extract at the end adheres to specific variable constraints

from typing import Optional,List
import pydantic

class Experience(pydantic.BaseModel):
    start_date: Optional[str]
    end_date: Optional[str]
    description: Optional[str]

class Study(Experience):
    degree: Optional[str]
    university: Optional[str]
    country: Optional[str]
    grade: Optional[str]

class WorkExperience(Experience):
    company: str
    job_title: str

class Resume(pydantic.BaseModel):
    first_name: str
    last_name: str
    linkedin_url: Optional[str]
    email_address: Optional[str]
    nationality: Optional[str]
    skill: Optional[str]
    study: Optional[Study]
    work_experience: Optional[WorkExperience]
    hobby: Optional[str]

parser = PydanticOutputParser(pydantic_object=Resume)
prompt = PromptTemplate(
    template="Extract information from the provided document.\n{format_instructions}\n{document}\n",
    input_variables=["document"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)
llm = ChatGroq()
chain = prompt | llm | SimpleJsonOutputParser() 

st.title("Resume Information Extractor") 


uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Save the uploaded file to a temporary directory
    temp_dir = "temp_files"
    os.makedirs(temp_dir, exist_ok=True)  # Ensure the temp directory exists
    temp_file_path = os.path.join(temp_dir, uploaded_file.name)

    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"File uploaded and saved at: {temp_file_path}")
    st.write(f"Path for PyPDFLoader: {temp_file_path}")
    

    pdf_loader=PyPDFLoader(temp_file_path)
    docs=pdf_loader.load_and_split()
    output=chain.invoke({"document": docs})
    st.success("Resume information extracted successfully!")
    st.json(output)

