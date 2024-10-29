import click
import importlib
from cells.parser_cell import Parser


@click.command()
@click.option("-f", "--file_path", required=True, type=str)
@click.option("-c", "--calculator", type=str, default="e245dmips", help="e245dmips, dfcpus, threads")
def run(file_path: str, calculator: str):
    full_module_name = f"calculators.c_{calculator}"
    module = importlib.import_module(full_module_name)
    CALCULATOR = getattr(module, calculator.title())

    parser = Parser(file_path=file_path)
    parser.calculator(CALCULATOR)


if __name__ == "__main__":
    run()
