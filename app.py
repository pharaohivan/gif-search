from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    #  Extracted the query term from url using request.args.get()
    query_term = request.args.get('q')
    """
    Made a 'params' dictionary containing:
    a) the query term, 'q'
    b) my API key, 'key'
    c) how many GIFs to return, 'limit'
    """
    params = {
        'q': query_term,
        'key': "BAI80UHWOVOB",
        'limit': '12'
    }

    """Made an API call to Tenor using the 'requests' library"""
    r = requests.get("https://api.tenor.com/v1/search", params =  params)

    #  Used the '.json()' function to get the JSON of the returned response
    # object
    data = r.json()

    # Using dictionary notation, we get the 'results' field of the JSON,
    # which contains the GIFs as a list
    results = data["results"]
    # [0:100]

    # We rendered the 'index.html' template, passing the list of gifs as a
    # named parameter called 'gifs'

    gifs = render_template('index.html',
    query_term = query_term,
    results=results)

    return gifs
if __name__ == '__main__':
    app.run(debug=True)
