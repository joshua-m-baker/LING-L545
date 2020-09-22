import sys

from nltk.tokenize import sent_tokenize


lines = sys.stdin.read()
result = sent_tokenize(lines)
for line in result:
    print(line)