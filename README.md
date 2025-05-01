# retrivor

**retrivor** é uma ferramenta de linha de comando para indexação e consulta semântica de repositórios de código-fonte. Ela permite buscar informações em projetos usando linguagem natural com apoio de embeddings e LLMs, integrando busca vetorial com geração de respostas.

## ✨ Funcionalidades

- Indexação de repositórios (ex: `.py`, `.go`, `.js`, etc.)
- Armazenamento vetorial com ChromaDB
- Geração de embeddings via OpenAI
- Consulta semântica com respostas em linguagem natural (RAG)
- Suporte a múltiplos formatos de arquivo de código
- Integração com `typer` para comandos CLI organizados

## 🛠 Tecnologias utilizadas

- [Typer](https://typer.tiangolo.com/)
- [LangChain](https://www.langchain.com/)
- [ChromaDB](https://www.trychroma.com/)
- [OpenAI](https://platform.openai.com/)
- [Python 3.10+](https://www.python.org/)

## 📄 Licença

Este projeto está licenciado sob os termos da **GPL-3.0-or-later**.
