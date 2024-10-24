import click
from cell import Cell


@click.command()
@click.option("-p", "--pids", required=True, type=str)
@click.option("-f", "--file_name", required=True, type=str)
@click.option("-o", "--others", type=str, default="")
def run(pids: str, file_name: str, others: str):
    cell = Cell(pids=pids, file_name=file_name, others=others)
    cell.verify_connection()
    cell.collect()
    # cell.get_result()


if __name__ == "__main__":
    run()
