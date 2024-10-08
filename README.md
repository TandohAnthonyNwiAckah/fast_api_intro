# FastAPI Introduction

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python
type hints. It is designed to be easy to use, allowing developers to build and deploy APIs quickly and efficiently.

## Key Features

- **Fast**: Very high performance, on par with Node.js and Go (thanks to Starlette and Pydantic).
- **Easy**: Designed to be easy to use and learn.
- **Built-in data validation**: Using Python type hints for input data validation and serialization.
- **Asynchronous support**: Native support for asynchronous programming with Python's async/await syntax.
- **Automatic interactive API documentation**: With Swagger UI and ReDoc.

## Installing a Virtual Environment Called `fastapi`

To start using FastAPI, it's a good practice to create a virtual environment. This ensures that your project
dependencies are isolated from your system-wide Python installation.

### Step 1: Create the Virtual Environment

Run the following command to create a virtual environment named `fastapi`.
You can use any name for your virtual environment.

```bash
python -m venv fastapi
```

## Activate the Virtual Environment

After creating the virtual environment, you need
to activate it. Use the following command
depending on your operating system:

For macOS/Linux:

```bash
source fastapi/bin/activate
```

For Windows:

```bash
source fastapi/bin/activate
```

> Once activated, your command prompt should change to indicate that you are now working within the fastapi virtual
> environment.

## Deactivate the Virtual Environment

You can deactivate the virtual environment by typing the command below.

```bash
deactivate
```


## Installing FastApi
Once your virtual environment is activated, you can
install FastAPI.

```bash
pip install fastapi
```


## Installing Uvicorn

```bash
pip install 'uvicorn[standard]'
```
