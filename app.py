from flask import Flask,jsonify,request,render_template, make_response


app = Flask(__name__)

import pymongo
import dns


client = pymongo.MongoClient("mongodb+srv://emekaboria:1kgJNTP2YpNe0CNM@cluster0.g6tlp.mongodb.net/tweetid?retryWrites=true&w=majority")
db = client.get_database('tweetid')

record = db.summa_collection

@app.route("/")
def home():
  return("welcome to summa api")



@app.route('/summa/', methods = ['GET', 'POST'])
def get_summa():
  ref_id = request.args.get("ref_id")
  find_tweets = record.find_one({"idd":int(ref_id)})
  #summary = jsonify(data = find_tweets['Summary'])
  response = make_response(render_template("index.html", value = find_tweets['Summary']))
  return response

"""

@app.route('/summa/', methods = ['GET', 'POST'])
def get_summa():
  ref_id = request.args.get("ref_id")
  find_tweets = record.find_one({"idd":int(ref_id)})
  return jsonify(Summary = find_tweets['Summary'])
"""

if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)
