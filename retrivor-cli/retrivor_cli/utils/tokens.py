import tiktoken
from typing import List, Tuple
from langchain_core.documents import Document

PRICING_PER_1K = {
    "text-embedding-3-small": 0.00002,
    "text-embedding-3-large": 0.00013,
}

def estimate_embedding_tokens_and_cost(
    chunks: List[Document],
    model_name: str = "text-embedding-3-small"
) -> Tuple[int, float]:
    try:
        encoding = tiktoken.encoding_for_model(model_name=model_name)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
    
    total_tokens = sum(len(encoding.encode(chunk.page_content)) for chunk in chunks)
    price_per_1k = PRICING_PER_1K.get(model_name, 0.00002)
    estimated_cost = (total_tokens / 1000) * price_per_1k
    
    return total_tokens, estimated_cost