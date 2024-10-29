import click
from calculators import CMAP
from cells.parser_cell import Parser


@click.command()
@click.option("-f", "--file_path", required=True, type=str)
@click.option("-c", "--calculator", type=str, default="e245dmips", help="e245dmips, dfcpus, threads")
def run(file_path: str, calculator: str):
    CALCULATOR = CMAP[calculator]

    parser = Parser(file_path=file_path)
    parser.calculator(CALCULATOR)


if __name__ == "__main__":
    run()
