from textblob import TextBlob
print("Hi! ako si CSRP Anong pangalan mo? ")
ed = input()
k = TextBlob("How are you " + ed + "?" + "Are you here to complain about your recent parcel?")
while True:
    g = (input()).lower()
    if g == ("yes","oo","sige","opo","yeah"):
        t=k.translate(to='tl')
        print(t)
        u= input()
        p=TextBlob("What Company/Courier catered your parcel? (Please choose a number.") 
        c=p.translate(to='tl')
        u=k.translate(to='tl')
        print (c) 
        print("[1] J&T Express")
        print("[2] Ninjavan")
        print("[3] 2GO Express")
        print("[4] Mr. Speedy")
        print("[5] Xpress")
        print("[6] Entrego")
        print("[7] GoGo Express")
        print("[8] LEX.ph")
            while True:
                h = input()
                if h == ('1', '2','3','4','5','6','7','8'):
                    print ("Where was it delivered?")
                else: 
                    print("I could'nt quite get that. Please choose again.")
                continue
    else: 
        print("I could'nt quite get that. Please choose again.")
    continue