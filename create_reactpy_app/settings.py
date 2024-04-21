from typing import Text
from pydantic_settings import BaseSettings


class CreateReactPyAppSettings(BaseSettings):
    """
    Configuration for the package.

    Attributes
    ----------

    COOKIECUTTER_REPO_URL: Text
        The URL of the cookiecutter repo that will be used to generate the project.
    """

    COOKIECUTTER_REPO_URL: Text = "https://github.com/MinuraPunchihewa/cookiecutter-create-reactpy-app.git"


settings = CreateReactPyAppSettings()
