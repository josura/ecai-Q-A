## program that uses langchain to send Q&A to OpenAI's GPT-3

# Imports
import os
from dotenv import load_dotenv,find_dotenv
from langchain_community.llms import OpenAI
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI

# Use the chat messages to store the documents
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
 

import utilities


load_dotenv(find_dotenv())


# Set API keys and the models to use
model_id = "gpt-3.5-turbo"

OpenAI_key = os.environ.get("OPEN_AI_KEY")




textFolder = 'data/text'
questionsFolder = 'data/questions'
answersFolder = 'results/answers'

max_iterations = 10

# for every text file in the text folder, search for the corresponding questions file in the questions folder and ask the questions
docs = []
pdfs = []

docs = utilities.list_txt_files(textFolder)
pdfs = utilities.list_pdf_files(textFolder)

for i in range(max_iterations): 
    for doc in docs:
        full_path = os.path.join(textFolder, doc)
        # Define the LLM we plan to use. Here we are going to use ChatGPT 3.5 turbo
        current_temperature = 0.2
        current_max_tokens = 100
        llm=ChatOpenAI(model_name = model_id, temperature=current_temperature, max_tokens=current_max_tokens, api_key=OpenAI_key)

        # Get the list of questions (multiple answers of questions)
        # the questions are organized in the file with the following format:
        # <number>. <question>
        # <A, B, C, D> answers

        questions = utilities.read_questions(os.path.join(questionsFolder, doc))

        # Load the document
        document_loader = TextLoader(full_path)
        document = document_loader.load()
        # # Define the index creator
        # index_creator = VectorstoreIndexCreator()
        # # Add the document to the index
        # index_creator.add_document(document)
        # define the prompt template with the document
        prompt = ChatPromptTemplate.from_messages([
            document[0].page_content,
            MessagesPlaceholder(variable_name="question")
        ])

        # define the chain with the prompt, the question and the LLM
        chain = prompt | llm

        for question in questions:
            print("Question: ", question)
            # answers = llm.ask_question(question, index)
            answers = chain.invoke(
                {
                    "question": [
                        HumanMessage(question),
                        HumanMessage(content="What is the answer to the question?"),
                    ]
                }
            )
            answers = answers.content
            print("Answers: ", answers)
            print("\n\n")
            # save the answers in a csv file where the format is the following:
            # <question>, <answer>, <document>, <temperature>, <max_tokens>, <iterations>
            file_name = doc.split(".")[0]
            output = answersFolder + '/' + file_name + '.csv'
            with open(output, 'a') as f:
                f.write(question + ', ' + answers + ', ' + doc + ', ' + str(current_temperature) + ', ' + str(current_max_tokens) + ', ' + str(i) + '\n')


for i in range(max_iterations):
    for pdf in pdfs:
        full_path = os.path.join(textFolder, pdf)
        # Define the LLM we plan to use. Here we are going to use ChatGPT 3.5 turbo
        current_temperature = 0.2
        current_max_tokens = 100
        llm=ChatOpenAI(model_name = model_id, temperature=current_temperature, max_tokens=current_max_tokens, api_key=OpenAI_key)

        # Get the list of questions (multiple answers of questions)
        # the questions are organized in the file with the following format:
        # <number>. <question>
        # <A, B, C, D> answers

        questions = utilities.read_questions(os.path.join(questionsFolder, pdf))

        # Load the document
        document_loader = PyPDFLoader(full_path)
        document = pdf_loader.load()
        # # Define the index creator
        # index_creator = VectorstoreIndexCreator()
        # # Add the document to the index
        # index_creator.add_document(document)
        # define the prompt template with the document
        prompt = ChatPromptTemplate.from_messages([
            document[0].page_content,
            MessagesPlaceholder(variable_name="question")
        ])

        # define the chain with the prompt, the question and the LLM
        chain = prompt | llm

        for question in questions:
            print("Question: ", question)
            # answers = llm.ask_question(question, index)
            answers = chain.invoke(
                {
                    "question": [
                        HumanMessage(question),
                        HumanMessage(content="What is the answer to the question?"),
                    ]
                }
            )
            answers = answers.content
            print("Answers: ", answers)
            print("\n\n")
            # save the answers in a csv file where the format is the following:
            # <question>, <answer>, <document>, <temperature>, <max_tokens>, <iterations>
            file_name = pdf.split(".")[0]
            output = answersFolder + '/' + file_name + '.csv'
            with open(output, 'a') as f:
                f.write(question + ', ' + answers + ', ' + pdf + ', ' + str(current_temperature) + ', ' + str(current_max_tokens) + ', ' + str(i) + '\n')