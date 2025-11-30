# Book API

This Django REST Framework (DRF) API provides CRUD operations for the `Book` model. It includes views for listing, retrieving, creating, updating, and deleting books, with proper permission handling.

---

## **Table of Contents**

- [API Views](#api-views)
- [Custom Hooks](#custom-hooks)
- [Permissions](#permissions)
- [Usage](#usage)
- [Testing](#testing)

---

## **API Views**

| View             | URL                       | Method      | Permissions     | Description                                                                                  |
| ---------------- | ------------------------- | ----------- | --------------- | -------------------------------------------------------------------------------------------- |
| `BookListView`   | `/books/`                 | GET         | AllowAny        | List all books. Public read-only access.                                                     |
| `BookDetailView` | `/books/<int:pk>/`        | GET         | AllowAny        | Retrieve a single book by its ID. Public read-only access.                                   |
| `BookCreateView` | `/books/create/`          | POST        | IsAuthenticated | Create a new book. Authenticated users only. Uses `perform_create` hook for custom behavior. |
| `BookUpdateView` | `/books/<int:pk>/update/` | PUT / PATCH | IsAuthenticated | Update an existing book. Authenticated users only. Uses `perform_update` hook.               |
| `BookDeleteView` | `/books/<int:pk>/delete/` | DELETE      | IsAuthenticated | Delete a book by ID. Authenticated users only.                                               |

---

## **Custom Hooks**

- **`perform_create(serializer)`**  
  Called after validation during book creation. Can be extended to perform additional actions like logging, sending notifications, or attaching extra fields.

- **`perform_update(serializer)`**  
  Called after validation during book updates. Can be extended similarly to `perform_create`.

---

## **Permissions**

- **Read-only endpoints:**

  - `BookListView`
  - `BookDetailView`  
    → Accessible by anyone (AllowAny)

- **Write/delete endpoints:**
  - `BookCreateView`
  - `BookUpdateView`
  - `BookDeleteView`  
    → Accessible only by authenticated users (IsAuthenticated)

This ensures:

- Unauthenticated users can only view data.
- Authenticated users can perform full CRUD operations.

---

## **Usage**

- All endpoints expect and return **JSON data**.
- `BookSerializer` ensures validation (e.g., `publication_year` cannot be in the future).
- URLs must match those defined in `api/urls.py`:

```text
/books/                -> List all books
/books/<int:pk>/       -> Retrieve single book
/books/create/         -> Create new book
/books/<int:pk>/update/-> Update existing book
/books/<int:pk>/delete/-> Delete a book
```

## API Testing Documentation

### Overview

The `Book` API endpoints have been tested using Django REST Framework’s `APITestCase`.  
Tests cover:

- CRUD operations (Create, Retrieve, Update, Delete, List)
- Authentication & permissions
- Filtering, searching, and ordering
- Data integrity

---

### Test File

Test class: `BookAPITestCase(APITestCase)`

---

### Test Cases

**1. List all books**

- GET `/books/`
- Checks: Status `200 OK`, returns all books.

**2. Retrieve single book**

- GET `/books/<id>/`
- Checks: Status `200 OK`, returns the correct book.

**3. Create book**

- POST `/books/`
- Authenticated: `201 Created`, book is saved.
- Unauthenticated: `401 Unauthorized`, no book created.

**4. Update book**

- PUT `/books/<id>/`
- Only authenticated users can update.
- Status `200 OK`, changes reflected in DB.

**5. Delete book**

- DELETE `/books/<id>/`
- Only authenticated users can delete.
- Status `204 No Content`, book removed.

**6. Filtering by title**

- GET `/books/?title=<book_title>`
- Returns books matching the title.

**7. Searching by author**

- GET `/books/?search=<author_name>`
- Returns books whose author's name contains the keyword.

**8. Ordering by publication year**

- GET `/books/?ordering=<field_name>` or `?ordering=-<field_name>`
- Returns books sorted by the field, ascending or descending.

---

### How to Run Tests

1. Activate the virtual environment:

``bash
pipenv shell

```
2. Run tests

``bash
python manage.py test api
```
