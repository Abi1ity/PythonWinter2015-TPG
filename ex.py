import rlcompleter
import readline
import sys


readline.parse_and_bind("tab: complete")

PS1='--> '

Stop=False
while not Stop:
    line = raw_input(PS1)
    print line

