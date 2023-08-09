# LLM batch

General solution to an archetype batch use case for LLMs.
For a given set of input documents (pdf or txt), we apply an LLM to extract the relevant information and store it in a structured format (json).

Configure your `.env`, update the `schema.yaml` file to your needs, upload your documents in `data/input_txt` and run `poetry run llm batch` to pocess your documents!

To configure input parameters such as paths, run `poetry run llm batch --help` to see what's possible.
