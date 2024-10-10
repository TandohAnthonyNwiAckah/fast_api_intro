# Todo App with FastAPI and SQLite3

A simple and efficient Todo application built with [FastAPI](https://fastapi.tiangolo.com/) and SQLite3. This app
provides a RESTful API for creating, retrieving, updating, and deleting todo tasks.

## Features

- **CRUD Operations**: Create, Read, Update, and Delete todos.
- **SQLite3 Integration**: Lightweight and serverless SQL database for quick setup.
- **API Documentation**: Interactive API docs using Swagger and Redoc.

### Prerequisites

- Python 3.7+
- FastAPI
- Uvicorn
- SQLite3
- `pip` for package management

## SQLite3 Database Setup

The application uses SQLite3 as its database. Below are some useful commands to interact with the database:

1. **Open the SQLite3 Database**:

    ```bash
    sqlite3 todos.db
    ```

2. **View the Database Schema**:

    ```sql
    .schema
    ```

3. **View All Tables**:

    ```sql
    .tables
    ```

4. **Describe a Table**:

    ```sql
    PRAGMA table_info(table_name);
    ```

   Replace `table_name` with the name of your table, e.g., `todos`.


5. **Change Output Mode**:

    - **Column Mode**: Formats the output as a table with columns aligned.

      ```sql
      .mode column
      ```

    - **CSV Mode**: Outputs data as comma-separated values.

      ```sql
      .mode csv
      ```

    - **Line Mode**: Prints each column value on a new line.

      ```sql
      .mode line
      ```

