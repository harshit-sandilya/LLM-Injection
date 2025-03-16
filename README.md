# LLM-Injection

This repository contains various scripts that demonstrate different types of prompt injection attacks on language models, inspired by the paper ["Indirect Prompt Injection Attacks on Language Models"](https://arxiv.org/pdf/2302.12173).

## Overview

The scripts in this repository showcase different methods of injecting malicious prompts into language models to manipulate their outputs. These methods include denial-of-service attacks, information gathering, prompt injection, and poisoning of input data.

## Files

- **`/threats/dos.py`**: Demonstrates a denial-of-service (DoS) attack by sending a large number of requests to the language model.
- **`/threats/info_gather.py`**: Shows how an attacker can gather information by injecting a malicious prompt that instructs the model to include sensitive information in its responses.
- **`/prompt_injection.py`**: Illustrates a basic prompt injection attack where the attacker manipulates the model's output by including specific instructions in the user prompt.
- **`/api.py`**: Demonstrates how to use the language model API to answer questions based on provided text data.
- **`/passive.py`**: Shows a passive attack where the input data is poisoned with hidden instructions that alter the model's behavior.
- **`/nlc.py`**: Demonstrates a natural language computing task where the model is asked to perform a matrix multiplication.
- **`/test.md`**: Contains text data used in the `/api.py` and `/passive.py` scripts.

## Usage

1. **Install Dependencies**: Ensure you have the required dependencies installed. You can install them using pip:
    ```sh
    pip install openai
    ```

2. **Run Scripts**: You can run each script individually to see the different types of prompt injection attacks in action. For example:
    ```sh
    python /workspaces/LLM-Injection/threats/dos.py
    ```

## Disclaimer

This repository is for educational purposes only. The techniques demonstrated here should not be used for malicious purposes. Always use language models responsibly and ethically.

## References

- ["Indirect Prompt Injection Attacks on Language Models"](https://arxiv.org/pdf/2302.12173)