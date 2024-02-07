import pyttsx3
import PyPDF2
from gtts import gTTS

with open('sample.pdf', 'rb') as book:
    reader=PyPDF2.PdfReader(book)
    audio_reader=pyttsx3.init()
    audio_reader.setProperty("rate", 100)
    full_text=""
   
    for page in range(len(reader.pages)):
        print(page)
        next_page=reader.pages[page]
        content=next_page.extract_text()
        full_text+=content
        
        #audio_reader.say(content)
    
    tts = gTTS(text=full_text, lang='en')
    tts.save("response.mp3")
    