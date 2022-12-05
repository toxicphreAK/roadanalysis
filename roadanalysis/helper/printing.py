from typer import (
    prompt,
    secho
)
from .constants import (
    DEBUG_SYMBOL,
    INFO_SYMBOL,
    PROMPT_SYMBOL,
    ABORT_SYMBOL,
    SUCCESS_SYMBOL
)


def print_debug(debugstring: str):
    if DEBUG:
        secho(DEBUG_SYMBOL + debugstring)


def print_info(infostring: str):
    secho(INFO_SYMBOL + infostring)


def print_success(successstring: str):
    secho(SUCCESS_SYMBOL + successstring)


def print_abort(abortstring: str):
    secho(ABORT_SYMBOL + abortstring)


def userprompt(promtstring: str):
    return prompt(PROMPT_SYMBOL + promtstring)
