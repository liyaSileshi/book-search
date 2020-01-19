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
        response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={search_term}&maxResults=20')
        

        books = response.json()
        book_array = []
        results = books['items']
        # print(results)
        for book in results:
            book_array.append(book['volumeInfo']['imageLinks']['thumbnail'])

    return render_template('index.html', book_array = book_array)

# @app.route('/<book_id>')
# def show_book():
#     pass  

if __name__ == '__main__':
    
    app.run(debug=True)
