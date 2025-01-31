# Todo List API

A RESTful API for managing todo items with user authentication built using FastAPI and MySQL.

## Features

- User registration and authentication using JWT
- CRUD operations for todo items
- MySQL database integration
- Swagger UI documentation
- Secure password hashing
- User-specific todo lists

## Prerequisites

- Python 3.8+
- MySQL
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/todo-api.git
cd todo-api
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure the database:
- Create a MySQL database named `todo_db`
- Update the database connection string in `app/database.py` With Your Username And Password:
```python
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://username:password@localhost/todo_db"
```

5. Start the server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

After starting the server, you can access:
- Swagger UI documentation: `http://localhost:8000/docs`
- ReDoc documentation: `http://localhost:8000/redoc`

## API Endpoints

### Authentication
- `POST /users/` - Register a new user
- `POST /token` - Login and get access token

### Todo Operations
- `GET /todos/` - List all todos
- `POST /todos/` - Create a new todo
- `GET /todos/{todo_id}` - Get a specific todo
- `PUT /todos/{todo_id}` - Update a todo
- `DELETE /todos/{todo_id}` - Delete a todo

## Authentication

The API uses JWT (JSON Web Tokens) for authentication. To use protected endpoints:

1. Register a new user using `/users/` endpoint
2. Get a token using `/token` endpoint
3. Include the token in the Authorization header:
```
Authorization: Bearer <your_token>
```

## Example Usage

### Register a New User
```bash
curl -X POST "http://localhost:8000/users/" \
     -H "Content-Type: application/json" \
     -d '{"email": "user@example.com", "password": "password123"}'
```

### Login and Get Token
```bash
curl -X POST "http://localhost:8000/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=user@example.com&password=password123"
```

### Create a Todo
```bash
curl -X POST "http://localhost:8000/todos/" \
     -H "Authorization: Bearer <your_token>" \
     -H "Content-Type: application/json" \
     -d '{"title": "Buy groceries", "description": "Milk, bread, eggs"}'
```

## Project Structure
```
todo_app/
├── requirements.txt
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── auth.py
│   └── routers/
│       ├── __init__.py
│       ├── todos.py
│       └── users.py
```

## Development

To run tests:
```bash
pytest
```

To run with auto-reload for development:
```bash
uvicorn app.main:app --reload
```

## Security Considerations

- Passwords are hashed using bcrypt
- JWT tokens expire after 30 minutes
- Database credentials should be stored in environment variables
- API uses HTTPS in production

## Error Handling

The API returns appropriate HTTP status codes:
- 200: Successful operation
- 201: Resource created
- 400: Bad request
- 401: Unauthorized
- 404: Resource not found
- 500: Server error

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
