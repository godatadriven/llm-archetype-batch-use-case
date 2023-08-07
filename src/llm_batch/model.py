import logging

logger = logging.getLogger(__name__)


def get_llm(model_name: str):
    logger.info(f"Loading LLM '{model_name}'")

    if model_name == "gpt4":
        llm = get_gpt4()

    elif model_name == "gpt3":
        llm = get_gpt3()

    elif model_name == "palm2":
        llm = get_palm2()

    else:
        raise ValueError(f"Invalid model: {model_name}")

    return llm


def get_gpt4():
    ...


def get_gpt3():
    ...


def get_palm2():
    ...
