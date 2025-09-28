# Advanced API Project

## Book API Endpoints

- `GET /api/books/` → List all books (public)
- `GET /api/books/<id>/` → Retrieve a book by ID (public)
- `POST /api/books/create/` → Create a new book (requires authentication)
- `PUT /api/books/<id>/update/` → Update a book (requires authentication)
- `DELETE /api/books/<id>/delete/` → Delete a book (requires authentication)

## Permissions
- Read-only for unauthenticated users
- Write operations (create, update, delete) restricted to authenticated users
