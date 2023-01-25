import json
from flask import Flask, jsonify, request, session
app = Flask(__name__)

app.secret_key = "bf7e92050d9a17827708a6013101d857fc2cf38950421df956b53bf3c9baf162"

import os
import psycopg2

seed = 0

def insert_seed(seed):
    try:
        conn = psycopg2.connect(
                host="mp2.cagmjdwaareb.ap-northeast-1.rds.amazonaws.com",
                database="postgres",
                user="postgres",
                password="POSTgres")

        cur = conn.cursor()

        sql = "UPDATE seed SET seed = '{}';".format(str(seed))
        cur.execute (sql)

        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print ("error occurred on insert {}".format(e))
        cur.close()
        conn.close()

def read_seed():
    try:
        conn = psycopg2.connect(
                host="mp2.cagmjdwaareb.ap-northeast-1.rds.amazonaws.com",
                database="postgres",
                user="postgres",
                password="POSTgres")

        cur = conn.cursor()

        cur.execute ('SELECT seed from seed LIMIT 1;')
        seed = cur.fetchone()[0]
        
        cur.close()
        conn.close()

        return str(seed)

    except Exception as e:
        print ("error occurred on select {}".format(e))
        cur.close()
        conn.close()

@app.route("/", methods=["POST"])
def updatenum():
    global seed
    print ("before loading the request")
    record = json.loads(request.data)
    seed = record["num"]
    #insert_seed(seed)
    #session["num"] = record["num"]
    num = seed
    print ("post is called")
    print ("num " + str(num))
    return str(num)

@app.route("/", methods=["GET"])
def getnum():
    print ("get is called")
    global seed

    #seed = read_seed()
    print ("seed is " + str(seed))
    return str(seed)

if __name__ == '__main__':
   app.run('0.0.0.0')
