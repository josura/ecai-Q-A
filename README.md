# ecai-Q-A
Code for a conference about AI

## Requirements
- python

## Usage
add text and pdf data to the folder in *data/text*, for every corresponding document in pdf or txt format, have a txt file in the *data/questions* folder with the same name containing the questions to give to chat-gpt. Only one file can be defined with all the questions for a particular document.

For some examples see the *data* folder.

You also need to define a **.env** file with `OPEN_AI_KEY=yourOpenAIAPIkey`

After having added the documents and questions to the corresponding folders, run the following commands:


```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

The answers to the questions will be available in the *results* folder with the corresponding names of the documents