import pyttsx3

engine = pyttsx3.init()
engine.save_to_file("Hello Vaibhav! You have been selected for a research internship in Switzerland. Please provide your statement of interest via email. Thank you!", "alert.wav")
engine.runAndWait()