# CookWithMe

CookWithMe is a platform designed for sharing, browsing, and managing recipes. It encourages culinary creativity and community by allowing users to create, categorize, and discover recipes, all while supporting a hierarchical category system (umbrella categories and subcategories) and robust ingredient management.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Clone the Repository](#clone-the-repository)
3. [Setup Instructions](#setup-instructions)
    - [3.1 Creating a Virtual Environment](#31-creating-a-virtual-environment)
    - [3.2 Activating the Virtual Environment](#32-activating-the-virtual-environment)
    - [3.3 Installing Dependencies](#33-installing-dependencies)
4. [Database Setup](#database-setup)
    - [4.1 Database Models Overview](#41-database-models-overview)
    - [4.2 Making Migrations](#42-making-migrations)
    - [4.3 Applying Migrations](#43-applying-migrations)
5. [Running the Server](#running-the-server)
6. [User Registration and Login](#user-registration-and-login)
7. [API Endpoints](#api-endpoints)
8. [Testing with Postman](#testing-with-postman)
9. [Seeding the Database](#seeding-the-database)
10. [Contributing](#contributing)
11. [License](#license)
12. [Acknowledgments](#acknowledgments)

---

## Introduction

CookWithMe is a Django-based web application for food enthusiasts to share and discover recipes. It features user authentication, hierarchical recipe categorization (umbrella and subcategories), ingredient management, and a RESTful API for integration with other platforms.

---

## Clone the Repository

First, clone the GitHub repository to your local machine:

```sh
git clone https://github.com/yourusername/CookWithMe.git
cd CookWithMe
```

---

## Setup Instructions

### 3.1 Creating a Virtual Environment

Create a virtual environment in your project directory:

```sh
python -m venv venv
```

### 3.2 Activating the Virtual Environment

- **On Windows:**
  ```sh
  venv\Scripts\activate
  ```
- **On macOS/Linux:**
  ```sh
  source venv/bin/activate
  ```

### 3.3 Installing Dependencies

With the virtual environment activated, install the required dependencies:

```sh
pip install -r requirements.txt
```

---

## Database Setup

### 4.1 Database Models Overview

CookWithMe uses a relational database to manage users, recipes, ingredients, and categories. Here’s a summary of the main models:

- **User**: Handles authentication and user profiles.
- **Profile**: Stores additional user information.
- **Category**: Supports hierarchical categories (umbrella and subcategories) for recipes.
- **Recipe**: Represents a recipe, linked to users and categories.
- **Ingredient**: Represents an ingredient.
- **RecipeIngredient**: Associates ingredients with recipes, including quantity and unit.

### 4.2 Making Migrations

To create migrations for the database, run:

```sh
python manage.py makemigrations
```

### 4.3 Applying Migrations

Apply the migrations to set up your database schema:

```sh
python manage.py migrate
```

---

## Running the Server

Start the development server with:

```sh
python manage.py runserver
```

The server will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## User Registration and Login

- **Register:** Visit [http://127.0.0.1:8000/register/](http://127.0.0.1:8000/register/) to create a new account.
- **Login:** Visit [http://127.0.0.1:8000/login/](http://127.0.0.1:8000/login/) to log in.
- **Logout:** Visit [http://127.0.0.1:8000/logout/](http://127.0.0.1:8000/logout/) to log out.

---

## API Endpoints

Here are the main API endpoints for CookWithMe:

- **GET /api/recipes/**: List all recipes.
- **POST /api/recipes/**: Add a new recipe (requires authentication).
- **GET /api/recipes/<id>/**: Retrieve details of a specific recipe.
- **PUT /api/recipes/<id>/**: Update a specific recipe (requires authentication).
- **DELETE /api/recipes/<id>/**: Delete a specific recipe (requires authentication).
- **GET /api/ingredients/**: List all ingredients.
- **POST /api/ingredients/**: Add a new ingredient (requires authentication).
- **GET /api/categories/**: List all categories.
- **POST /api/categories/**: Add a new category (superuser only).
- **GET /api/accounts/**: User and profile management.

*Replace `<id>` with the actual recipe or ingredient ID.*

---

## Testing with Postman

To test the API, you can use Postman:

1. Open Postman.
2. Import the API collection or manually create requests using the endpoints above.
3. For endpoints that require authentication, obtain a token or session cookie by logging in, and include it in your request headers.

This README provides a comprehensive guide to setting up and running the CookWithMe project, including how to register and log in as a user, and interact with the API endpoints. Adjust any specific URLs or paths according to your actual project setup.