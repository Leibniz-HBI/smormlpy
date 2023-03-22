import click

@click.command()
@click.argument("name", type=str)
def cli(name: str) -> None:
    """Entry point for our CLI.

    In here we delegate incoming commands from the terminal to our program;
    for this example, we receive a string, which we want to interpolate.
    Decoupling the user interface code (which goes in to this function) from
    the implementation of the internal logic is important.

    E.g. testing the `greet`-function on it's own is trivial, while testing the
    same functionality if we would program the functionality into the `cli`-function
    would be quite difficult. Same is true, if we would want to change and extend
    the behavior of the implementation.

    Parameters :
        name : str : name argument passed by click
    """
    click.echo(greet(name))

def greet(name: str) -> str:
    """Greet someone or something by name.

    Parameters:
        name : str : Whom to greet

    Return:
        str : Greeting
    """
    return f"Hello {name}!"
