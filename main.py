import io
import json
from json.decoder import JSONDecodeError
from textwrap import TextWrapper
import click
from src import analyzer
import logging

LOG = logging.Logger(__name__)


@click.command()
@click.argument("har_data", type=click.File("r"))
def cli(har_data: io.TextIOWrapper):
    try:
        analyzer.analyze(json.loads(har_data.read()))
    except JSONDecodeError as e:
        LOG.warning(e, exc_info=e)


if __name__ == "__main__":
    cli()
