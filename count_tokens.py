#!/usr/bin/env python3
# Purpose: Count the number of GPT-4 tokens in a text.
import sys
from count_gpt4_tokens import count_gpt4_tokens

if __name__ == "__main__":
    # check if stdin is empty
    if sys.stdin.isatty():
        print("No input on stdin.")
        sys.exit(1)

    # read from stdin
    text_to_count = sys.stdin.read()

    token_count = count_gpt4_tokens(text_to_count)
    print(f"The text contains {token_count} GPT-4 tokens.")

