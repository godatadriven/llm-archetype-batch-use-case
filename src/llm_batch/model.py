import logging
import os

import dotenv
import openai
from langchain.llms import AzureOpenAI

dotenv.load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE")
openai.api_type = os.getenv("OPENAI_API_TYPE")
openai.api_version = os.getenv("OPENAI_API_VERSION")

logger = logging.getLogger(__name__)


def get_llm(model_name: str):
    if model_name == "gpt-4":
        llm = get_gpt_4()
    elif model_name == "gpt-3":
        llm = get_gpt_35_turbo()
    elif model_name == "palm-2":
        llm = get_palm2()
    else:
        raise ValueError(f"Invalid model: {model_name}")

    return llm


def get_gpt_4():
    logger.info("Loading LLM 'gpt-4'")
    return AzureOpenAI(
        model_name="gpt-4",
        temperature=0.7,
        max_tokens=256,
        top_p=1.0,
        verbose=False,
        engine="gpt-4-us",
    )


def get_gpt_35_turbo():
    # Different approach than gpt-4, as for gpt-3 we get an error:
    # "The completion operation does not work with the specified model, gpt-35-turbo."
    logger.info("Loading LLM 'gpt-35-turbo'")

    return lambda prompt: openai.ChatCompletion.create(
        model="gpt-35-turbo",
        engine="gpt-35-turbo-us",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=256,
        top_p=1,
    )["choices"][0]["message"]["content"]


def get_palm2():
    ...
