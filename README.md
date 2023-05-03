# openai-examples

This is a playground for experimenting with OpenAI

# How to set-up locally?
- Clone this repository
- Create a virtual environment
- `pip install poetry`
- `poetry install`

# How do I interact?
- `chatbot`

## The `run` command: This is a normal chatGPT wrapper.
- `run Write me a python code to generate Fibonacci Sequence`
..generates 
```
Sure, here's a simple Python code to generate the Fibonacci sequence up to a specified number of terms:

```python
# Function to generate the Fibonacci sequence up to n terms
def fibonacci(n):
    # Initialize the first two terms of the sequence
    a, b = 0, 1
    # Create an empty list to store the sequence
    fib_seq = []
    # Loop through n terms and add each term to the sequence
    for i in range(n):
        fib_seq.append(a)
        # Update the values of a and b for the next term
        a, b = b, a + b
    # Return the Fibonacci sequence
    return fib_seq

# Example usage: generate the first 10 terms of the Fibonacci sequence
fibonacci(10)
```

This will output the following sequence: `[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]`

## The `extract` command: This takes text as input and annotates it with ontology information along with confidence %
- `extract Bioenergy Sorghum Compendium The proposed YR4 studies will add new information from RNA sequencing profiles on N remobilization responses to water deficit ABA stem growth regulation stem composition`

..generates 
```
Here is the annotated statement with ontology CURIEs and confidence levels:

Bioenergy Sorghum Compendium [OBI:0001932] The proposed YR4 [OBI:0002021] studies will add new information from RNA sequencing profiles [OBI:0001853] on N remobilization responses [GO:0051704] to water deficit [PATO:0000144] ABA [CHEBI:25212] stem growth regulation [GO:0048825] stem composition [PO:0020030]. 

Confidence level: 90%
```
# Acknowledgements

This [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/README.html) project was developed from the [monarch-project-template](https://github.com/monarch-initiative/monarch-project-template) template and will be kept up-to-date using [cruft](https://cruft.github.io/cruft/).