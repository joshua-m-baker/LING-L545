import sys
import re

abrev = re.compile("[^\s]+\.[^\s]+")

line = sys.stdin.readline()
while line != '':
    for token in line.split(" "):
        if token[-1] in '!?.':
            sys.stdout.write(token + '\n')
        elif token[-1] == '.':
            if abrev.match(token):
                sys.stdout.write(token + ' ')
            else:
                sys.stdout.write(token = '\n')
        else:
            sys.stdout.write(token + ' ')
    line = sys.stdin.readline()

