import os

def read_questions(file_path):
    questions = []
    # control if the file exists
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist")
        return questions
    print(f"Reading questions from {file_path}")
    with open(file_path, 'r') as file:
        lines = file.readlines()
        current_line = 0
        while current_line < len(lines):
            # if the line starts with a number followed by a dot, then it is a question. multiple answers questions are defined by the following format:
            # <number>. <question>
            # <A, B, C, D> answers
            # there could also be free answers questions
            current_line_strip = lines[current_line].split(".")# use the dot to split the number from the question
            if current_line_strip[0].isdigit():
                # get the question
                question = lines[current_line]
                # control if the question is a multiple answers question or a free answer question
                if current_line + 1 < len(lines) and not lines[current_line + 1][0].isdigit():
                    # get the answers (append every line to the question string , until the next question is found)
                    answers = []
                    # for i in range(4):
                    #     answers.append(lines[current_line + 1 + i])
                    current_line += 1
                    while current_line < len(lines) and not lines[current_line][0].isdigit():
                        answers.append(lines[current_line].strip())
                        current_line += 1
                    question += " ".join(answers)
                    questions.append(question)
                    current_line += 5
                else:
                    questions.append(question)
                    current_line += 1
            
    return questions

def list_txt_files(folder):
    # list all the text files in the folder
    files = os.listdir(folder)
    txt_files = []
    for file in files:
        if file.endswith(".txt"):
            txt_files.append(file)
    return txt_files

def list_pdf_files(folder):
    # list all the pdf files in the folder
    files = os.listdir(folder)
    pdf_files = []
    for file in files:
        if file.endswith(".pdf"):
            pdf_files.append(file)
    return pdf_files