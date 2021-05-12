from textblob import TextBlob
print("Hi! ako si CSRP Anong pangalan mo? ")
ed = input()
k = TextBlob("Kamusta ka " + ed + "?" + "Nandito ka ba para mag reklamo para iyong parsela?")
t=k.translate(to='en')
print(t)
u= input()
p=TextBlob("What Company/Courier catered your parcel?") 
c=p.translate(to='tl')
u=k.translate(to='tl')  
print (c) 
#lang = blob.detect_language()
#print(lang)




