import json
from flask import Flask, jsonify, request, session
app = Flask(__name__)

app.secret_key = "bf7e92050d9a17827708a6013101d857fc2cf38950421df956b53bf3c9baf162"

@app.route("/", methods=["POST"])
def updatenum():
    print ("before loading the request")
    record = json.loads(request.data)
    session["num"] = record["num"]
    num = session["num"]
    print ("post is called")
    print ("num " + str(num))
    return ("num " + str(num))

@app.route("/", methods=["GET"])
def getnum():
    print ("get is called")
    if "num" in session:
        return (str(session["num"]))
    else:
        print ("returning zero")
        return "0"

if __name__ == '__main__':
   app.run('0.0.0.0')
