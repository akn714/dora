# Colored prints

# ANSI chars for colors
RED = '\033[31m'
YELLOW = '\033[93m'
LGREEN = '\033[92m'
CLEAR = '\033[0m'
BOLD = '\033[01m'
CYAN = '\033[96m'
WHITE = '\u001b[37m'
MAGENTA = '\033[35m'
RESET = '\033[m'

# color print
def cprint(*args, color=WHITE):
    print(color,end="")
    print(*args, RESET)

