# FastAPI Article Management System

This project is a simple article management system built with FastAPI. It features user authentication, article creation, and management functionalities. Users can view, add, update, and delete articles, with certain routes restricted to admin users only.

## Features

- **User Authentication**: Users can log in, and their credentials are verified against hashed passwords. Tokens are stored in cookies for authentication.
- **Article Management**: Users can view a list of articles, view individual articles, and add or update articles. Admin users have full access to article management features.
- **Templating**: HTML templates are used for rendering web pages, allowing for a server-side rendering approach without a separate frontend framework.

## Requirements

- Python 3.7+
- FastAPI
- Jinja2
- pydantic
- jwt
- [Your Custom Libraries](./requirements.txt) (e.g., `passwordHashing`, `getTokenFuncs`)

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd <project-directory>
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

- Set your `SECRET_KEY` and other environment variables as needed. Make sure you have a `.env` file or set these variables in your environment.

## Running the Application

To run the FastAPI application, use the following command:

```bash
uvicorn main:app --reload


This README covers basic information about the project, including installation instructions, endpoint details, and project structure. Adjust it according to your project's specifics and additional features.
```

the project idea was form here
https://roadmap.sh/projects/personal-blog
