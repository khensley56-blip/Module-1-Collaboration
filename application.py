from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), unique=True, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)

    def json(self):
        return {
            'id': self.id,
            'book_name': self.book_name,
            'author': self.author,
            'publisher': self.publisher
        }

@app.route('/')
def index():
    return "Book CRUD API"

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    output = []
    for book in books:
        output.append(book.json())
    return jsonify({"books": output})

@app.route('/books/<id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify(book.json())

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Book(
        book_name=data['book_name'],
        author=data['author'],
        publisher=data['publisher']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'id': new_book.id}), 201

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return jsonify({"error": "book not found"}), 404
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "book deleted"})

if __name__ == '__main__':
    app.run(debug=True)