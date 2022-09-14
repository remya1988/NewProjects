

from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.BLUE + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print(Fore.YELLOW+ 'back to normal now')

Blue = '\033[1;32m'
print(Blue,"this")