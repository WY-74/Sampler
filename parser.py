import click
from cell import Parser

import calculators


@click.command()
@click.option("-f", "--file_path", required=True, type=str)
@click.option("-c", "--calculator", type=str, default="E245Dmips", help="E245Dmips, DFcpus, Threads")
def run(file_path: str, calculator: str):
    print(f"Calculator: {calculator}")
    parser = Parser(file_path=file_path)
    CALCULATOR = getattr(calculators, calculator)
    parser.calculator(CALCULATOR)


if __name__ == "__main__":
    run()
