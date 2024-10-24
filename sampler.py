import click
from cell import Sampler


@click.command()
@click.option("-p", "--pids", required=True, type=str)
@click.option("-f", "--file_name", required=True, type=str)
@click.option("-o", "--others", type=str, default="")
def run(pids: str, file_name: str, others: str):
    sampler = Sampler(pids=pids, file_name=file_name, others=others)
    sampler.verify_connection()
    sampler.collect()


if __name__ == "__main__":
    run()
