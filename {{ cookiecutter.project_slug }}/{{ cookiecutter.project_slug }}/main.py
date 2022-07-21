import click
from loguru import logger as log

@click.command()
def cli() -> None:
    log.info("Hello World")
