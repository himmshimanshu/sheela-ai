import wolframalpha
from speak import speak

def WolfRamAlpha(query):
    apikey = "94VARV-7JQ4VELEYP"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("Sorry ,Nothing Found")

def Calc(query):
    Term = str(query)
    Term = Term.replace("sheela","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divide","/")

    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        print(f"{result}")
        speak(result)

    except:
        speak("Nothing Found")

        