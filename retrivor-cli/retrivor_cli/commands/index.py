import typer

app = typer.Typer()

@app.command(name="index")
def index() -> None:
    typer.echo("Hello, World!")
    return None
