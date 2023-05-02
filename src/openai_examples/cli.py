"""Command line interface for openai-examples."""
import logging

import click
from click_shell import shell
from openai_examples import __version__
from openai_examples.main import demo

__all__ = [
    "main",
]

logger = logging.getLogger(__name__)
input_argument = click.argument("input", required=True, nargs=-1)

# @click.group()
@shell(prompt='ontobot > ', intro='Starting my app...')
@click.option("-v", "--verbose", count=True)
@click.option("-q", "--quiet")
@click.version_option(__version__)
def main(verbose: int, quiet: bool):
    """CLI for openai-examples.

    :param verbose: Verbosity while running.
    :param quiet: Boolean to be quiet or verbose.
    """
    if verbose >= 2:
        logger.setLevel(level=logging.DEBUG)
    elif verbose == 1:
        logger.setLevel(level=logging.INFO)
    else:
        logger.setLevel(level=logging.WARNING)
    if quiet:
        logger.setLevel(level=logging.ERROR)



@main.command()
@click.argument("subcommand")
@click.pass_context
def help(ctx, subcommand):
    """Echoes help for subcommands."""
    subcommand_obj = main.get_command(ctx, subcommand)
    if subcommand_obj is None:
        click.echo("The command you seek help with does not exist.")
    else:
        click.echo(subcommand_obj.get_help(ctx))


@main.command()
@input_argument
def run(input: str):
    """Run the openai-examples's demo command."""
    click.echo(demo(" ".join(input)))


if __name__ == "__main__":
    main()
