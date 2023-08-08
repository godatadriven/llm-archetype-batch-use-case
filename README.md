# LLM batch

General solution to an archetype batch use case for LLMs.
For a given set of input documents (pdf or txt), we apply an LLM to extract the relevant information and store it in a structured format (json).

Update the `schema.json` file to your needs, upload your documents in `data/input_txt` and run `poetry run python src/llm_batch/main.py`.