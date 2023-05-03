# openai-examples

This is a playground for experimenting with OpenAI

# How to set-up locally?
- Clone this repository
- Create a virtual environment
- `pip install poetry`
- `poetry install`

# How to begin?
```
> chatbot
```

# Commands
## `run`

```
chatbot > run Write me a python code to generate Fibonacci Sequence
```
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

## `extract`

```
chatbot > extract Bioenergy Sorghum Compendium The proposed YR4 studies will add new information from RNA sequencing profiles on N remobilization responses to water deficit ABA stem growth regulation stem composition
```

..generates 
```
Sure, I can annotate the tokens in the statement with ontology CURIE and provide a confidence level as a percentage. Here's the annotated statement:

Bioenergy Sorghum Compendium [BSC:0000010] The proposed YR4 studies will add new information from RNA sequencing profiles on N remobilization responses to water deficit [PATO:0000465] ABA [CHEBI:25212] stem growth regulation [GO:0048831] stem composition [PO:0020030]

The confidence level for the annotations is 80%.

Here's the table with the CURIE, label, and confidence:

| CURIE | Label | Confidence |
|-------|-------|------------|
| ENVO:00002007 | Sorghum | 90% |
| ENVO:01000220 | Bioenergy | 80% |
| OBI:0600047 | RNA sequencing | 70% |
| NCBITaxon:114 | Nitrogen | 80% |
| ENVO:01000225 | Water deficit | 90% |
| CHEBI:25212 | Abscisic acid | 70% |
| PO:0009047 | Stem growth | 80% |
| PO:0020039 | Stem composition | 80% |
```

# Disclaimer:
This is just a simple wrapper around OpenAI's GPT and the results are not a 100% accurate despite of the confidence % expressed above. For e.g.: `ENVO:00002007` is `sediment` and the GPT annotates `Sorghum`[NCBITaxon:1699109](https://www.ebi.ac.uk/ols/ontologies/ncbitaxon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FNCBITaxon_4557) as `sediment` with 90% confidence.
# Acknowledgements

This [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/README.html) project was developed from the [monarch-project-template](https://github.com/monarch-initiative/monarch-project-template) template and will be kept up-to-date using [cruft](https://cruft.github.io/cruft/).