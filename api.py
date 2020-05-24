from flask import Flask, request, jsonify, abort
import os
import dotenv
import pymongo
dotenv.load_dotenv()
def connect():
    cluster = pymongo.MongoClient(os.getenv('URL_DB'))
    db = cluster["birthday"]
    coll = db['birthday']
    return coll


app = Flask(__name__)
@app.route('/')
@app.route("/<string:name>", methods = ["GET"])
def req_name(name = None):
  if request.headers.get('key')==os.getenv('API_KEY'):
    if name is not None:
      req = None
      for i in coll:
        if i['name']==name:
          req = i
          break
      if req is None:return "Invalid request.pls try again"
      else:
        return jsonify(req)
    else:return 'Change the url!'
  else:abort(401)
    

if __name__=="__main__":
    coll = eval(os.getenv('DATA'))
    print(type(coll))
    app.run()


