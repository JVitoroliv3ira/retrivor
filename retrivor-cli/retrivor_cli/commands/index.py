import typer
from pathlib import Path
from retrivor_cli.core.indexer import load_and_split_documents, index_chunks
from retrivor_cli.utils.tokens import estimate_embedding_tokens_and_cost

app = typer.Typer()

@app.command(name="index")
def index(
    path: Path = typer.Argument(..., help="Caminho para o diretório do repositório."),
    persist_dir: str = typer.Option("./code_index", help="Diretório onde o índice será salvo."),
    dry_run: bool = typer.Option(False, help="Mostra a estimativa e não executa")
) -> None:
    typer.echo(f"Iniciando indexação do repositório em: {path}")
    chunks = load_and_split_documents(path)
    total_tokens, estimated_cost = estimate_embedding_tokens_and_cost(chunks)
    
    typer.echo(f"\nEstimativa de indexação:")
    typer.echo(f"   Trechos: {len(chunks)}")
    typer.echo(f"   Tokens estimados: {total_tokens:,}")
    typer.echo(f"   Custo (OpenAI): ~${estimated_cost:.5f}")
    
    if dry_run:
        typer.secho("Dry run ativado. Nenhuma indexação foi feita.")
        raise typer.Exit()
    
    typer.echo("Gerando embeddings e salvando no índice...")
    index_chunks(chunks, persist_dir)
    
    typer.echo(f"Indexação concluída com sucesso. {chunks} trechos de código foram processados.")
    typer.echo(f"O índice foi salvo em: {persist_dir}")
