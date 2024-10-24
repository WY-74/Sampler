import click
from cell import Parser
from calculator import E245Dmips


@click.command()
@click.option("-f", "--file_path", required=True, type=str)
def run(file_path: str):
    parser = Parser(file_path=file_path)
    parser.calculator(E245Dmips)


if __name__ == "__main__":
    run()
