#!/bin/bash

sed 's/[^A-Za-z]\+/\n/g' | grep -v '^$' > $$words
tail -n +2 $$words > $$nextwords
paste $$words $$nextwords | sort | uniq -c 
rm $$words $$nextwords
