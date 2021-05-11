from textblob import TextBlob
print("Hi! ako si CSRP :slight_smile: Anong pangalan mo? ")
ed = input()
blob = TextBlob("How are you " + ed + "?" + "Are you here to complain about your recent parcel?")
#lang = blob.detect_language()
#print(lang)
t=blob.translate(to='tl')
print(t)
