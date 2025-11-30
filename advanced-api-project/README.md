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
