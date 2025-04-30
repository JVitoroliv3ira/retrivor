import typer
from retrivor_cli.commands import index

app = typer.Typer()

app.add_typer(index.app)

if __name__ == '__main__':
    app()