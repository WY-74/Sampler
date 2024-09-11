import click
from cell import Cell


@click.command()
@click.option("-p", "--pids", required=True, type=str, help="List of process pids")
@click.option("-d", "--delay", type=int, default=1)
@click.option("-n", "--nums", type=int, default=30)
@click.option("-f", "--filename", type=str, default="default_filename")
@click.option('--cpus', type=int, default=6, help='Number of CPUs, default is 6')
@click.option('--power', type=int, default=80, help='Power level, default is 80')
def run(pids: str, delay: int, nums: int, filename: str, cpus: int, power: int):
    cell = Cell(pids, delay, nums, filename, cpus, power)
    cell.verify_connection()
    cell.collect()
    cell.get_result()


if __name__ == "__main__":
    run()
