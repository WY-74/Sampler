import click
from cell import Parser


@click.command()
@click.option("-p", "--pids", required=True, type=str)
@click.option("-f", "--file_path", required=True, type=str)
def run(pids: str):
    parser = Parser(pids=pids)
    # sampler.verify_connection()
    # sampler.collect()


if __name__ == "__main__":
    run()
