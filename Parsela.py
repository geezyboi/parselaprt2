from textblob import TextBlob
print("Hi! ako si CSRP Anong pangalan mo? ")
ed = input()
k = TextBlob("How are you " + ed + "?" + "Are you here to complain about your recent parcel?")
t=k.translate(to='tl')
print(t)
u= input()
p=TextBlob("What Company/Courier catered your parcel?") 
c=p.translate(to='tl')
u=k.translate(to='tl')  
print (c) 
#lang = blob.detect_language()
#print(lang)




