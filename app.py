from flask import Flask,request,render_template


app=Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to Flask"

@app.route('cal',methods=["GET"])
def math_operators():
    operations=request.json['operation']
    numbers1=request.json['numbers1']
    numbers2=request.json['numbers2']

    if operations=="add"
        result=numbers1+numbers1
    elif operations=="multiply":
        result=numbers1*numbers2
    elif operations=="division":
        result=numbers1/numbers2
    else:
        result=numbers1-numbers2
    return result

print(__name__)

if __name__== "__main__":
    app.run()