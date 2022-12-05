from typer import style, colors

DEBUG_SYMBOL = style("[#] ", fg=colors.BRIGHT_WHITE)
INFO_SYMBOL = style("[*] ", fg=colors.WHITE)
SUCCESS_SYMBOL = style("[+] ", fg=colors.GREEN)
ABORT_SYMBOL = style("[-] ", fg=colors.BRIGHT_RED)
PROMPT_SYMBOL = style("[?] ", fg=colors.YELLOW)
