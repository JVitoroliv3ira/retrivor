import typer
from retrivor_cli.core.asker import answer_question

app = typer.Typer()

@app.command(name="ask")
def ask(
    question: str = typer.Argument(..., help="Pergunta a ser feita sobre o repositório indexado"),
    persist_dir: str = typer.Option("./code_index", help="Diretório do banco indexado"),
    k: int = typer.Option(3, help="Número de trechos retornados")
) -> None:
    typer.echo("Gerando resposta com a OpenAI...")
    resposta = answer_question(question, persist_dir, k)
    typer.echo("\nResposta:\n")
    typer.echo(resposta)