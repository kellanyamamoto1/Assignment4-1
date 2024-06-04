# ADMIN FILE


# Kellan Yamamoto
# 28388886
# kellany@uci.edu

"""
Module that processes the admin mode.
Will print the Admin syntax instructions
"""


from pathlib import Path
import ui

ADMIN_INSTRUCTIONS = """Print Full File using syntax:
[COMMAND] [INPUT] [[-]OPTION] [INPUT]
-------------------------------------
"""


def start():
    print("ADMINISTARION ON")
    ui.administration(1)
    ui.handle_command()