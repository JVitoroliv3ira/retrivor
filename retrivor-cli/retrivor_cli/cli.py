import typer
from retrivor_cli.commands import index
from retrivor_cli.commands import ask

app = typer.Typer()

app.add_typer(index.app)
app.add_typer(ask.app)

if __name__ == '__main__':
    app()