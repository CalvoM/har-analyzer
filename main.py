import io
import json
from textwrap import TextWrapper
import click
from src import analyzer


@click.command()
@click.argument("har_data", type=click.File("r"))
def cli(har_data: io.TextIOWrapper):
    analyzer.analyze(json.loads(har_data.read()))


if __name__ == "__main__":
    cli()
