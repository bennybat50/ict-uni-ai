import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('API_KEY')
print(".... Welcome to Your Sassy Assistant.....")
than


def getChoice():
    print("Choose an option \n1) Start Chat\n0) Exit Chat\n")
    choice=input("Choose a number\n")
    
    if(choice=="1"):
        getInput()
    elif (choice=="0"):
          print("Bye bye")
          exit()

              
    
        
    
def getInput() :
    content=input("Type Anything....")

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": content}])
    print(completion.choices[0].message.content)
    getChoice()
    
    

getChoice()