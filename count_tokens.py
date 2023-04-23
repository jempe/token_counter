import sys
import openai
from tiktoken import Tokenizer
from tiktoken.tokenizer import Tokenizer as TikToken


def count_gpt3_tokens(file_name):
    with open(file_name, "r") as f:
        text = f.read()

    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(text)
    token_count = len(tokens)

    return token_count


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file_name>")
        sys.exit(1)

    file_name = sys.argv[1]
    token_count = count_gpt3_tokens(file_name)
    print(f"The file contains {token_count} GPT-3 tokens.")

