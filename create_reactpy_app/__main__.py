import click
from cookiecutter.main import cookiecutter

from create_reactpy_app.settings import settings


@click.command()
@click.argument('project_directory')
@click.option(
    '--backend',
    '-b',
    default='fastapi',
    help='The backend framework to use. Default is FastAPI.'
)
def main(project_directory, backend):
    """
    This command creates a template for a Reactpy app.
    """

    cookiecutter(
        settings.COOKIECUTTER_REPO_URL,
        extra_context={
            'project_directory': project_directory,
            'backend': backend
        },
        no_input=True
    )
                

if __name__ == "__main__":
    main()