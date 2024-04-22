import click
from cookiecutter.main import cookiecutter

from create_reactpy_app.settings import settings


@click.command()
@click.argument('app_name')
def main(app_name):
    """
    This command creates a template for a Reactpy app.
    """

    cookiecutter(
        settings.COOKIECUTTER_REPO_URL,
        extra_context={'app_name': app_name},
        no_input=True
    )
                

if __name__ == "__main__":
    main()