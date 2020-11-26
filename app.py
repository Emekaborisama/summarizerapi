#import torch
#from transformers import *
#from summarizer import Summarizer, TransformerSummarizer
from flask import Flask,jsonify,request,render_template, make_response
#GPT2_model = TransformerSummarizer(transformer_type="GPT2", transformer_model_key="gpt2-medium")

app = Flask(__name__)

import pymongo
import dns

client = pymongo.MongoClient("mongodb+srv://emekaboria:jmapLBIwaO5Xrnow@cluster0.g6tlp.mongodb.net/summa_db?retryWrites=true&w=majority")
db = client.get_database('summa_db')

record = db.summa_collection

@app.route('/')
def home():
  return("summarizer api")


@app.route('/summary/<string:ref_id>', methods = ['GET', 'POST'])
def get_summary(ref_id):
  request_data = request.get_json()
  find_tweet = record.find_one({'idd':ref_id})
  return render_template("index.html", value = find_tweet['summary'])


"""@app.route('/summarizer', methods= ['GET', 'POST'])
def summarize():
  request_tweet = requests.get_json()
  ree = request_tweet['text']
  full = ''.join(GPT2_model(ree, min_length=50))
  return full
    
"""

@app.route('/summa/ref_id', methods = ['GET', 'POST'])
def get_summa(ref_id):
  request_d = request.get_json()
  find_tweets = record.find_one({'idd':ref_id})
  return find_tweets['summary']


if __name__ == '__main__':
    app.run(host= '0.0.0.0', port = 8000, debug=True)
