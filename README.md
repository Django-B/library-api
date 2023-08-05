# library-api
Example of using Django Rest Framework in a Django project

### API using
- List all books: GET http://localhost:8000/api/books/
- Create a new book: POST http://localhost:8000/api/books/
- Payload: { "title": "Book Title", "author": "Author Name"}
- Retrieve a book by ID: GET http://localhost:8000/api/books/1/
- Update a book by ID: PUT http://localhost:8000/api/books/1/  Payload: { "title": "Updated Title" }
- Delete a book by ID: DELETE http://localhost:8000/api/books/1/
