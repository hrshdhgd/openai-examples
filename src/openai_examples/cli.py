"""Command line interface for openai-examples."""
import logging

import click
from click_shell import shell

from openai_examples import __version__
from openai_examples.chatbot import extract, run

__all__ = [
    "main",
]

logger = logging.getLogger(__name__)
input_argument = click.argument("input", required=True, nargs=-1)


@shell(prompt="chatbot > ", intro="Starting the chatbot app...")
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


@main.command("run")
@input_argument
def click_run(input: str):
    """
    Chatbot's `run` command.

    Example:

        run Write me a python code to generate Fibonacci Sequence

    generates the corresponding python code.
    """
    click.echo(run(" ".join(input)))


@main.command("extract")
@input_argument
def click_extract(input: str):
    """
    Chatbot's `extract` command.

    Example:

        extract Bioenergy Sorghum Compendium The proposed YR4 studies will add
        new information from RNA sequencing profiles on N remobilization
        responses to water deficit ABA stem growth regulation stem composition.

    generates a result containing annotations of tokens in the input and
    a tabular representation of the same.
    """
    click.echo(extract(" ".join(input)))


if __name__ == "__main__":
    main()
