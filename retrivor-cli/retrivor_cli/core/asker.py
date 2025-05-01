from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from retrivor_cli.utils.prompt_builder import build_prompt

def answer_question(question: str, persist_dir: str, k: int = 3) -> str:
    db = Chroma(persist_directory=persist_dir, embedding_function=OpenAIEmbeddings())
    docs = db.similarity_search(question, k=k)
    if not docs:
        return "Nenhum conteúdo relevante encontrado."

    context = "\n\n".join([doc.page_content for doc in docs])
    prompt = build_prompt(context, question)
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2)
    return llm.invoke(prompt).content