# Create ReactPy App

This is create-react-app for your ReactPy projects!

## Creating an App

You'll need to have Python 3.8 or later installed on your machine. You can use `python --version` to check your current version.

1. First, install the package using pip:

```bash
pip install create-reactpy-app
```

> Note: You can either install this globally or in a virtual environment.

2. Create a new project:

```bash
create-reactpy-app my-app --backend flask
```

> Note: You can replace `flask` with `fastapi` or `starlette` if you want to use those frameworks instead. The default is already set to `flask`.

3. Change directory to your new project:

```bash
cd my-app
```

4. Install the dependencies:

```bash
pip install -r requirements.txt
```

5. Start the server; depending on the backend framework you chose, you can run the following commands:

Flask:

```bash
gunicorn main:app
```

FastAPI or Starlette:

```bash
uvicorn main:app
```