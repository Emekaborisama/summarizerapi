from flask import Flask,jsonify,request,render_template, make_response


app = Flask(__name__)

import pymongo
import dns

client = pymongo.MongoClient("mongodb+srv://emekaboria:jmapLBIwaO5Xrnow@cluster0.g6tlp.mongodb.net/summa_db?retryWrites=true&w=majority")
db = client.get_database('summa_db')

record = db.summa_collection

@app.route("/")
def home():
  return("welcome to summa api")


@app.route('/summary/<string:ref_id>', methods = ['GET', 'POST'])
def get_summary(ref_id):
  request_data = request.get_json()
  find_tweet = record.find_one({'idd':int(ref_id)})
  return render_template("index.html", value = find_tweet['summary'])


@app.route('/summa/', methods = ['GET', 'POST'])
def get_summa():
  ref_id = request.args.get("ref_id")
  find_tweets = record.find_one({"idd":int(ref_id)})
  return jsonify(Summary = find_tweets['Summary'])


if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)
