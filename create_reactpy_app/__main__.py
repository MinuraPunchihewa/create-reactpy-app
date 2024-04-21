import click

@click.command()
@click.argument('app_name')
def main(arg):
    """
    This command creates a template for a Reactpy app.
    """

    click.echo(f'You entered: {arg}')


if __name__ == "__main__":
    main()