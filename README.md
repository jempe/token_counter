# Count Tokens

`count_tokens.py` is a Python script that counts the number of GPT-3 tokens in a given text file. It uses OpenAI's `tiktoken` library for tokenization.

## Requirements

- Python 3.6 or higher
- openai
- tiktoken

You can install the required packages using the following command:

```sh
pip install openai tiktoken
```

## Usage

To use the script, run the following command:

```sh
python count_tokens.py <file_name>
```

Replace `<file_name>` with the name of the text file you want to analyze.

## Example

If you have a text file called `sample.txt`, you can count its GPT-3 tokens using the following command:

```sh
python count_tokens.py sample.txt
```

The script will output the token count, for example:

```
The file contains 150 GPT-3 tokens.
```

## How it works

The script reads the content of the input text file and uses the `tiktoken` library to tokenize the text according to GPT-3's tokenizer. It then counts the number of tokens and displays the result.

