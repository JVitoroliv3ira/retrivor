def build_prompt(context: str, question: str) -> str:
    return f"""
Você é um assistente técnico que analisa o código-fonte de uma aplicação.

Baseando-se **exclusivamente** nos trechos de código abaixo, responda com precisão e detalhes técnicos à pergunta do usuário. 
Se o código mostrar claramente o uso de bibliotecas ou algoritmos específicos, **mencione-os explicitamente** (ex: AES, Fernet, PBKDF2, hashlib, etc). 
Evite respostas genéricas ou vagas. Cite nomes de funções, métodos e arquivos se possível.

--- TRECHOS DE CÓDIGO ---
{context}
-------------------------

Pergunta: {question}
Resposta:
"""