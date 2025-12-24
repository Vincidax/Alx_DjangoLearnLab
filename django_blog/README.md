# Django Blog Project

A comprehensive Django-based blog application featuring user authentication, CRUD blog post management, comments, tagging, and search functionality.

---

## **Table of Contents**

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Database Configuration](#database-configuration)
5. [Running the Project](#running-the-project)
6. [Usage](#usage)
7. [Project Structure](#project-structure)
8. [Contributing](#contributing)
9. [License](#license)

---

## **Project Overview**

This project is a Django blog application designed for learning and development purposes. Users can register, log in, create, edit, and delete blog posts, comment on posts, assign tags, and search for posts.

---

## **Features**

- **User Authentication**
  - Registration, login, logout
  - Profile management
  - Password security via Django's hashing
- **Blog Post Management**
  - Create, Read, Update, Delete (CRUD) operations
  - Only authors can edit/delete their posts
  - Post list and detail views
- **Comments**
  - Authenticated users can add, edit, and delete comments
  - Only comment authors can edit or delete their comments
- **Tagging**
  - Posts can have multiple tags
  - Tag pages show all posts associated with a tag
- **Search**
  - Search posts by title, content, or tags

---

## **Installation**

1. Clone the repository:

```bash
git clone https://github.com/vincidax/alx_DjangoLearnLab.git
cd django_blog
```

2. Create a virtual environment and activate it:

```bash
python -m venv env
# Windows
env\Scripts\activate
# macOS/Linux
source env/bin/activate
```

3. Install dependecies:

```bash
pip install -r requirements.txt
```

## **Database Configuration**

The project uses PostgreSQL. Configure your database in django_blog/settings.py:

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog_database_amwb',
        'USER': 'vincidax',
        'PASSWORD': 'your_password_here',
        'HOST': 'dpg-d55sjkje5dus73ce32e0-a.virginia-postgres.render.com',
        'PORT': '5432',
    }
}
```

## **Apply migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

## **Running the Project**

Start the development server:

```bash
python manage.py runserver
```

Access the blog at http://127.0.0.1:8000/

## **Usage**

    ## Authentication

- /register/ → Register a new user

- /login/ → Log in

- /logout/ → Log out

- /profile/ → View or edit profile

  ## Posts

- /posts/ → List all posts

- /posts/new/ → Create a new post

- /posts/<int:pk>/ → View post details

- /posts/<int:pk>/edit/ → Edit a post (author only)

- /posts/<int:pk>/delete/ → Delete a post (author only)

  ## Comments

Add, edit, delete comments from the post detail page

URLs:

/post/<int:post_id>/comments/new/

/comments/<int:pk>/edit/

/comments/<int:pk>/delete/

    ## Tags

Tags are displayed on posts

/tags/<slug:tag_slug>/ → View posts by tag

Search

Search bar in the navigation

/search/?q=keyword → Display posts matching title, content, or tags

## **Project Structure**

django_blog/
├── blog/
│ ├── migrations/
│ ├── templates/
│ │ └── blog/
│ │ ├── base.html
│ │ ├── post_detail.html
│ │ ├── post_form.html
│ │ ├── comment_form.html
│ │ ├── posts_by_tag.html
│ │ └── search_results.html
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── urls.py
│ └── views.py
├── django_blog/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── manage.py
└── requirements.txt
