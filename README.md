# Create ReactPy App
Copyright © 2023 Minura Punchihewa

This is `create-react-app` for your ReactPy projects!

## Quick Overview

```bash
create-reactpy-app my-app
cd my-app
make install
make run
```

Now, open http://localhost:8000 to see your app.

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
make install
```

Or

```bash
pip install -r requirements.txt
```

> Note: If create-reactpy-app was installed in a virtual environment, this does not need to be done on the same environment. You can switch to a different environment and install the dependencies there.

5. Start the server:

```bash
make run
```

Or, depending on the backend framework you chose, you can run the following commands:

- Flask:

```bash
gunicorn main:app
```

- FastAPI or Starlette:

```bash
uvicorn main:app
```

Your app will now be running on http://localhost:8000.

## License
This code is licensed under the GNU GENERAL PUBLIC LICENSE. See LICENSE.txt for details.
