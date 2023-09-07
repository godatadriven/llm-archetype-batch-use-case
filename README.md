# 💬 LLM batch

General solution to an archetype batch use case for LLMs.
For a given set of input documents (`pdf` or `txt`), we apply an LLM to extract the relevant information and store it in a structured format (`json`). The outputs are validated with Pydantic.

# Getting started 💻

1. Clone this repo
2. Install the dependencies with [Poetry](https://python-poetry.org/): `poetry install`
3. Configure your `.env`
   - Copy the `.env.example` file to `.env`
   - If you're from Xebia, use `OPENAI_API_BASE="https://xebia-openai-us.openai.azure.com"`
   - Copy the OpenAI key from [Azure](https://portal.azure.com/#@xebia.com/resource/subscriptions/5ddf05c0-b972-44ca-b90a-3e49b5de80dd/resourceGroups/xebia-openai-us/providers/Microsoft.CognitiveServices/accounts/xebia-openai-us/cskeys)

4. Update the `schema.yaml` file to your needs. This file defines the output structure of the LLM.
5. Upload your documents in `data/input_txt` or `data/input_pdf`.
6. If you have uploaded pdf documents, run `poetry run llm-batch preprocess`, otherwise skip this step
7. Run `poetry run llm-batch run` to process your documents. 
8. Check the results in the `output` folder! 🎉 

To configure input parameters such as paths, run `poetry run llm-batch run --help` or `poetry run llm-batch preprocess --help` to see what's possible.
