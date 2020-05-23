from flask import Flask, request, jsonify, abort
import pymongo
def connect():
    cluster = pymongo.MongoClient("mongodb+srv://Jofin:JT9wYx0RQKObQVvO@cluster0-e29hp.mongodb.net"
                                  "/test?retryWrites=true&w=majority")
    db = cluster["birthday"]
    coll = db['birthday']
    return coll


app = Flask(__name__)
@app.route('/')
@app.route("/<string:name>", methods = ["GET"])
def req_name(name = None):
    if request.headers.get('key')=="1234":
        if name is not None:
            req = coll.find({'name':name})
            if req.count()==0:return "Invalid request.pls try again"
            else:
                for i in req:
                    return jsonify(i)
        else:
            return 'Change the url!'
    else:
        abort(401)

if __name__=="__main__":
    coll = connect()
    app.run(debug=False, port=5001,)


