# Python program to translate
# speech to text and text to speech
import speech_recognition as sr
import pyttsx3
import google.generativeai as palm

palm.configure(api_key="put you api key where")

defaults = {
  'model': 'models/chat-bison-001',
  'temperature': 0.25,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
}
context = "you are now running inside a ai voice assistent , so please responed like  a voice assistent rsponed and i changed your name to palm , you are now palm and you are now a voice assistent"
examples = [
  [
    "hi\n",
    "Hi there! How can I help you today?"
  ]
]

def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
    
error_count = 0
r = sr.Recognizer()
while True:
  # Initialize the recognizer
  if error_count >= 3:
    input("type anything..")
    error_count = 0
  try:
    
    # use the microphone as source for input.
    with sr.Microphone() as source2:
      
      # wait for a second to let the recognizer
      # adjust the energy threshold based on
      # the surrounding noise level
      r.adjust_for_ambient_noise(source2, duration=0.2)
      
      #listens for the user's input
      audio2 = r.listen(source2)
      
      # Using google to recognize audio
      MyText = r.recognize_google(audio2)
      MyText = MyText.lower()
      
      print(f"user:\n\t{MyText}\n\n")
      
  except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
    
  except sr.UnknownValueError:
    print("unknown error occurred")
    error_count = error_count+1
    continue

    
  messages = MyText
  response = palm.chat(
    **defaults,
    context=context,
    examples=examples,
    messages=messages
  )
  print(f"google palm2:\n\t{response.last}\n\n")
  SpeakText(response.last)