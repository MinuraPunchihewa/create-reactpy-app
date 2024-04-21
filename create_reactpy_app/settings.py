from pydantic import BaseSettings


class CreateReactPyAppSettings(BaseSettings):
    """
    Configuration for Mthe package.

    Attributes
    ----------

    COOKIECUTTER_REPO_URL : str
        The URL of the cookiecutter repo that will be used to generate the project.
    """

    COOKIECUTTER_REPO_URL = "https://github.com/MinuraPunchihewa/cookiecutter-create-reactpy-app.git"


settings = CreateReactPyAppSettings()
