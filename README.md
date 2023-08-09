# LLM batch

General solution to an archetype batch use case for LLMs.
For a given set of input documents (`pdf` or `txt`), we apply an LLM to extract the relevant information and store it in a structured format (`json`).

1. Configure your `.env`
2. Update the `schema.yaml` file to your needs
3. Upload your documents in `data/input_txt` or `data/input_pdf`
4. If you have uploaded pdf documents, run `poetry run llm-batch preprocess`, otherwise skip this step
5. Run `poetry run llm-batch run` to process your documents. 
6. Check the results in the `output` folder! 🎉 

To configure input parameters such as paths, run `poetry run llm batch --help` to see what's possible.
