from flask import Flask, render_template, request, url_for
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)


@app.route('/', methods=['GET'])
def booksearch():
    # TODO: Extract query term from url
    if request.method == 'GET':
        search_term = request.args.get('q')
    #search_term = request.args.get("q")

    # TODO: Make an API call to Tenor using the 'requests' library
    
        response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={search_term}&maxResults=4')
        
        # TODO: Get the first 10 results from the search results
        # books = json.loads(response.content)
        books = response.json()
        book_array = []
        results = books['items']
        # print(results)
        for book in results:
            book_array.append(book['volumeInfo']['imageLinks']['thumbnail'])
        # images = books['items'][0]['volumeInfo']['imageLinks']['thumbnail']
    # return author
    return render_template('index.html', book_array = book_array)

    


if __name__ == '__main__':
    # gifsearch()
    app.run(debug=True)
