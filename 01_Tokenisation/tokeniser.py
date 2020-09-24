import sys
import re

line = sys.stdin.readline()
while line != '':
    for s in [",", ":", "(", ")", "."]:
        line = line.replace(s, " {}".format(s))
    sys.stdout.write(line.replace(" ", "\n"))
    #    if token[-1] in '!?.':
    #        sys.stdout.write(token + '\n')
    #    elif token[-1] == '.':
    #        if abrev.match(token):
    #            sys.stdout.write(token + ' ')
    #        else:
    #            sys.stdout.write(token = '\n')
    #    else:
    #        sys.stdout.write(token + ' ')
    line = sys.stdin.readline()

