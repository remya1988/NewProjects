import colorama
GREEN = '\033[32m '
RED = '\033[31m'
RESET = '\u001b[0m'
def colour_print(text: str,effect: str)-> None:
    output_string = "{0}{1}{2}".format(effect,text,RESET)
    print(output_string)

colorama.init()
from colorama import Fore, Back, Style,init
init(autoreset=True)
print(Fore.RED + 'some red text')
print('automatically back to default color again')
colour_print("Red",GREEN)

colorama.deinit()
