Resume Information Extractor
============================

This project provides a web application for extracting key information from PDF resumes using a combination of machine learning and PDF parsing tools. The application is built with Streamlit for the frontend, and leverages LangChain and Groq for the natural language processing tasks.

Features
--------

*   File Upload: Upload a PDF file containing a resume.
    
*   Information Extraction: Extracts key information such as personal details, education, work experience, and skills.
    
*   Output Display: Displays the extracted information in a structured JSON format.
    
*   Temporary File Handling: Safely handles temporary storage of uploaded files.
    

Installation
------------

To set up the project locally, follow these steps:

1.  Clone the Repository: git clone cd
    
2.  Create a Virtual Environment: python -m venv venv source venv/bin/activate # On Windows use venv\\Scripts\\activate
    
3.  Install the Dependencies: pip install -r requirements.txt
    
4.  Set Up Environment Variables:
    
    *   Create a .env file in the root directory of the project.
        
    *   Add the following lines to the .env file with your API keys:
    *        LANGCHAIN\_API\_KEY=your\_langchain\_api\_key
    *        GROQ\_API\_KEY=your\_groq\_api\_key
    *        HUGGINGFACE\_API\_KEY=your\_huggingface\_api\_key
        

Running the Application
-----------------------

To run the application, execute the following command:

    streamlit run app.py

The Streamlit application will start and can be accessed in your web browser at http://localhost:8501.

Project Structure
-----------------

├── app.py # The main application script 
    ├── requirements.txt # Project dependencies 
    ├── .env # Environment variables file 
    ├── temp\_files # Directory for storing uploaded files 
    └── README.md # This file

Usage
-----

1.  Upload a PDF:
    
    *   Use the "Upload a PDF file" button to select and upload a PDF resume.
        
2.  Extract Information:
    
    *   Once the file is uploaded, the application will process the PDF and extract the relevant information.
        
3.  View Results:
    
    *   The extracted information will be displayed on the web page in JSON format.
        

Acknowledgements
----------------

*   LangChain for providing powerful NLP tools.
    
*   Groq for advanced language model capabilities.
    
*   Streamlit for the intuitive web application framework.
    

Contributing
------------

If you'd like to contribute to this project, please fork the repository and use a feature branch. Pull requests are welcome.
