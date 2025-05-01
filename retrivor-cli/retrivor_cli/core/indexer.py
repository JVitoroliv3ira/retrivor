import typer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from pathlib import Path

def load_and_split_documents(path: Path, exts: set = None) -> int:
    exts = exts or {".py", ".ts", ".js", ".go", ".rb", ".rs"}
    files = [f for f in path.rglob("*") if f.suffix in exts]
    
    docs = []
    for file in files:
        try:
            loader = TextLoader(str(file))
            docs.extend(loader.load())
        except Exception as e:
            typer.echo(f"Erro ao ler {file}: {e}")
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    chunks = splitter.split_documents(docs)
    return chunks

def index_chunks(chunks: list, persist_dir) -> None:
    Chroma.from_documents(chunks, OpenAIEmbeddings(), persist_directory=persist_dir)
