import typer
from pathlib import Path
from retrivor_cli.core.indexer import index_project

app = typer.Typer()

@app.command(name="index")
def index(
    path: Path = typer.Argument(..., help="Caminho para o diretório do repositório."),
    persist_dir: str = typer.Option("./code_index", help="Diretório onde o índice será salvo.")
) -> None:
    typer.echo(f"Iniciando indexação do repositório em: {path}")
    chunks = index_project(path, persist_dir)
    typer.echo(f"Indexação concluída com sucesso. {chunks} trechos de código foram processados.")
    typer.echo(f"O índice foi salvo em: {persist_dir}")
