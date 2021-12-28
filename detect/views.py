from django.shortcuts import render
from detection.settings import LANGUAGE_CODE
import speech_recognition as sr

# Create your views here.
def home(request):
    return render(request,'home.html')


def text(request):
    print("check button")
    speech_r = ''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")
    
    try:
        speech_r = r.recognize_google(audio_text)
        # print("Text: "+r.recognize_google(audio_text))
        print("text :"+r.recognize_google(audio_text,language = "hi-IN"))
        print("Text: "+speech_r)

    except:
         print("Sorry, I did not get that")
    context = {'speech_r':speech_r}
    return render(request,'home.html',context)