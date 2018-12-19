from flask import Flask, request
import sys
import flipkartParse, amazonParse

app = Flask(__name__)

@app.route('/query_flipkart')
def query_flipkart():
    query = request.args.get('query') #if key doesn't exist, returns None
    price_min = request.args.get('min')
    price_max = request.args.get('max')
    if(query==None):
    	query = request.args.get('brand')

    if(price_min==None):
    	price_min = -1

    if(price_max==None):
    	price_max = -1
    
    return flipkartParse.flipkart_query(query, price_min, price_max)


@app.route('/query_amazon')
def query_amazon():
    query = request.args.get('query') #if key doesn't exist, returns None
    if(query==None):
    	query = request.args.get('brand')
    
    return amazonParse.amazon_query(query)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
