import tiktoken

encoding_name = "cl100k_base"
encoding_model = "gpt-4"

encoding = tiktoken.get_encoding(encoding_name)
encoding = tiktoken.encoding_for_model(encoding_model)

def count_gpt4_tokens(string: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

