"""Welcome to {{ cookiecutter.project_slug }}.

Here we showcase our best practices for command line tool development.

## Version Option

Nearly all CL programs implement the `--version` option to display the currently
used version of the program. `click` implements this with a very concise decorator
that is applied to the top-level entry point, e.g. the below example `cli()` the
`@click.version_option(__version__)` sets the displayed version.
"""
import click
from loguru import logger as log

from . import __version__


@click.command()
@click.version_option(__version__)
@click.argument("name", type=str)
def cli(name: str) -> None:
    """ This internal function is called by the click-decorated function.
    The split into two functions is necessary for documentation purposes as pdoc3
    cannot process click-decorated functions.

    Parameters :
        name : str : name argument passed by click
    Returns:
        None: Nada   
    """
    log.info(cli_implementation(name))

def cli_implementation(name: str) -> None:
    """ Greet someone or something by name.

    Parameters:
        name : str : Whom to greet

    Return:
        str : Greeting
    """
    return f"Hello {name}!"

if __name__ == "main":
    cli()
