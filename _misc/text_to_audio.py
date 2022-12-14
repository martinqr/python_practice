
# Import the required module for text 
# to speech conversion
from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
import os
  
# The text that you want to convert to audio
mytext = '''El señor y la señora Dursley, que vivían en el número 4 de Privet Drive,
estaban orgullosos de decir que eran muy normales, afortunadamente. Eran las
últimas personas que se esperaría encontrar relacionadas con algo extraño o
misterioso, porque no estaban para tales tonterías.
El señor Dursley era el director de una empresa llamada Grunnings, que
fabricaba taladros. Era un hombre corpulento y rollizo, casi sin cuello, aunque
con un bigote inmenso. La señora Dursley era delgada, rubia y tenía un cuello
casi el doble de largo de lo habitual, lo que le resultaba muy útil, ya que pasaba
la mayor parte del tiempo estirándolo por encima de la valla de los jardines
para espiar a sus vecinos. Los Dursley tenían un hijo pequeño llamado Dudley,
y para ellos no había un niño mejor que él.
Los Dursley tenían todo lo que querían, pero también tenían un secreto, y
su mayor temor era que lo descubriesen: no habrían soportado que se supiera
lo de los Potter.'''
  
# Language in which you want to convert
language = 'es'
  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)
  
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("welcome.mp3")
  
# Playing the converted file
os.system("welcome.mp3")
