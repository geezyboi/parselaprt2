def Choice():
    while True:
        ans=input("End The Chat?[Y/N]:")
        ansoption=["Y","N","YES","NO"]
        if ans.upper() in ansoption:
            if ans.upper()=='N' or ans.upper()=="NO":
                break
            elif ans.upper()=='Y' or ans.upper()=="YES":
                input("Thank you for using Chatbot Courrier Service.")
                exit()
               
        else:
            print("Invalid Entry!")
    return ans
while True:
    print ("   ♛                                        ♛")
    print ("(っ◔◡◔)っ ♥ c͓̽a͓̽r͓̽l͓̽o͓̽s͓̽ ͓̽p͓̽r͓̽o͓̽g͓̽r͓̽a͓̽m͓̽ ♥ (っ◔◡◔)っ")
    print ("====================================================")
    print ("----------HELLO----------")
    print ("===========================")
    print ("|-Chatbot-Courrier-Service-|")
    print ("============================")
    print ("|-------Chat Menu----------|")
    print ("============================")
    print ("|--[S]tart-----------------|")
    print ("|--[E]xit------------------|")
    print ("============================")
    while True:
            z = (input("Enter Your Choice:")).lower()
            if z == 's':
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
                            h=input("lagay mo 1")
                            if h==('1'):
                                print ("panget mo mindoro")
                            else:
                                print("I could'nt quite get that. Please choose again.")
                            continue

            elif z == 'e':
                ans=Choice()
                if ans.upper()=="Y" or ans.upper()=="YES":
                        break
            else:
                print("Please only choose form the options.")
            continue
