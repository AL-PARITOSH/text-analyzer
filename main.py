from flask import Flask,render_template,request


app = Flask(__name__)

@app.get("/")
def showPage():
    return render_template('index.html')

@app.post('/analyze')
def analyze():
    text = request.form['text']
    action = request.form['action']
    answer = ""
    if(action == "cntchr"):
        #counter number of characters
        answer = f"The number of characters are:- {len(text)}"
    if(action == "cntws"):
        #count number of whitespaces
        answer = f"The number of white spaces are:- {text.count(' ')}"
    if(action == "cts"):
        #count number of whitespaces
        answer = f"Capitalize of the sentence is:- {text.capitalize()}"
    if(action == "scoaad"):
        #count number of whitespaces
        answer = f"The sentence contains only alphabets and digits:- {text.isalnum()}"
    if(action == "scoa"):
        #count number of whitespaces
        answer = f"The sentence contains only alphabets:- {text.isalpha()}"
    if(action == "scod"):
        #count number of whitespaces
        answer = f"The sentence contains only digits:- {text.isspace()}"
    if(action == "siilc"):
        #count number of whitespaces
        answer = f"The sentence is in lower case:- {text.islower()}"
    if(action == "siiuc"):
        #count number of whitespaces
        answer = f"The sentence is in upper case:- {text.isupper()}"
    if(action == "scs"):
        #count number of whitespaces
        answer = f"The sentence contains spaces:- {text.isspace()}"
    if(action == "csilc"):
        #count number of whitespaces
        answer = f"Convert the sentence in lower case:- {text.lower()}"
    if(action == "csiuc"):
        #count number of whitespaces
        answer = f"Convert the sentence in upper case:- {text.upper()}"
    if(action == "rtts"):
        #count number of whitespaces
        answer = f"Remove the starting spaces:- {text.lstrip(' ')}"
    if(action == "rtes"):
        #count number of whitespaces
        answer = f"Remove the ending spaces:- {text.rstrip(' ')}"
    if(action == "rts"):
        #count number of whitespaces
        answer = f"Remove the spaces:- {text.strip(' ')}"
    if(action == "csitc"):
        #count number of whitespaces
        answer = f"Convert sentence in title case:- {text.title()}"
    if(action == "sts"):
        #count number of whitespaces
        answer = f"Spliting the sentence:- {text.split(' ')}"
    if(action == "pts"):
        #count number of whitespaces
        answer = f"Partioning the sentence:- {text.partition(' ')}"
    if(action == "stcos"):
        #count number of whitespaces
        answer = f"Swap the cases of the sentence:- {text.swapcase()}"
    
    return render_template('index.html',output = answer)


app.run(debug=True)