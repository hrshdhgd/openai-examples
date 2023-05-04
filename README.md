# openai-examples

This is a playground for experimenting with OpenAI

# How to set-up locally?
- Clone this repository
- Create a virtual environment
- `pip install poetry`
- `poetry install`
- Save your OpenAI secret key as an environmental variable `OPENAI_API_KEY`

## Get list of models
```
make get-models
```
This runs the script 
```
curl https://api.openai.com/v1/models -H "Authorization: Bearer $OPENAI_API_KEY" > models.json
```
`models.json` lists all available models at your disposal.
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

'''python
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
'''

This will output the following sequence: `[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]`
```

## `extract`

```
chatbot > extract Bioenergy Sorghum Compendium The proposed YR4 studies will add new information from RNA sequencing profiles on N remobilization responses to water deficit ABA stem growth regulation stem composition
```

..generates 
```
CURIE: NCBITaxon:4558
Label: Sorghum
Confidence: 90%

CURIE: CHEBI:2365
Label: Abscisic acid (ABA)
Confidence: 95%

CURIE: SO:0000988
Label: RNA sequencing
Confidence: 90%

CURIE: GO:0015979
Label: Photosynthesis
Confidence: 80%

CURIE: GO:0008150
Label: Biological process
Confidence: 80%

CURIE: GO:0009628
Label: Response to abiotic stimulus
Confidence: 85%

CURIE: GO:0006970
Label: Response to osmotic stress
Confidence: 80%

CURIE: GO:0009414
Label: Response to water deprivation
Confidence: 85%

CURIE: GO:0048364
Label: Root development
Confidence: 80%

CURIE: GO:0003700
Label: DNA-binding transcription factor activity
Confidence: 80%

| CURIE         | Label                             | Confidence |
|---------------|-----------------------------------|------------|
| NCBITaxon:4558| Sorghum                           | 90%        |
| CHEBI:2365    | Abscisic acid (ABA)               | 95%        |
| SO:0000988    | RNA sequencing                    | 90%        |
| GO:0015979    | Photosynthesis                    | 80%        |
| GO:0008150    | Biological process                | 80%        |
| GO:0009628    | Response to abiotic stimulus      | 85%        |
| GO:0006970    | Response to osmotic stress        | 80%        |
| GO:0009414    | Response to water deprivation     | 85%        |
| GO:0048364    | Root development                  | 80%        |
| GO:0003700    | DNA-binding transcription factor  | 80%        |
```

# Disclaimer:
This is just a simple wrapper around OpenAI's GPT and the results are not a 100% accurate despite of the confidence % expressed above. 
# Acknowledgements

This [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/README.html) project was developed from the [monarch-project-template](https://github.com/monarch-initiative/monarch-project-template) template and will be kept up-to-date using [cruft](https://cruft.github.io/cruft/).