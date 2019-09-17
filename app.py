from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    # TODO: Extract the query term from url using request.args.get()
    query_term = request.args.get('q')
    # TODO: Make 'params' dictionary containing:
    # a) the query term, 'q'
    # b) your API key, 'key'
    # c) how many GIFs to return, 'limit'
    params = {
        'q': query_term,
        'key': "BAI80UHWOVOB",
        'limit': '10'
    }
    # TODO: Make an API call to Tenor using the 'requests' library. For
    # reference on how to use Tenor, see:
    # https://tenor.com/gifapi/documentation
    # TODO: Use the '.json()' function to get the JSON of the returned response
    # object
    r = requests.get("https://api.tenor.com/v1/search", params =  params)
    data = r.json()
    # if r.status_code == 200:
    #     # load the GIFs using the urls for the smaller GIF sizes
    #     top_8gifs = json.loads(r.content)
    #     print top_8gifs
    # else:
    #     top_8gifs = None

    # TODO: Using dictionary notation, get the 'results' field of the JSON,
    # which contains the GIFs as a list
    results = data["results"]
    # [0:100]

    # TODO: Render the 'index.html' template, passing the list of gifs as a
    # named parameter called 'gifs'

    gifs = render_template('index.html',
    query_term = query_term,
    results=results)

    return gifs
if __name__ == '__main__':
    app.run(debug=True)
