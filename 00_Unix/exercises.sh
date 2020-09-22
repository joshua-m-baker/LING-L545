# Ç

# Grep
# 1) 
sed 's/[^A-Za-z]\+/\n/g' < wiki.txt | grep -c "^[A-Z]"

# 2) 
grep "^.\{4\}$" < wiki.words | wc -l
grep -i "^[a-z]\{4\}$" < wiki.words | wc -l

# 3) 
grep -i "^[^aeiou]*$" < wiki.words | wc -l
# 4) 
grep -i "^[^aeiou]*[aeiou][^aeiou]*$" < wiki.words | wc -l
# 5) 
grep -i "^[^aeiou]*[aeiou][^aeiou]*[aeiou][^aeiou]*$" < wiki.words | wc -l

# Sed
sed 's/[aeiou].*//gi' < wiki.words | grep -vc '^$' 
sed 's/[^BCDFGHJKLMNPQRSTVWXYZ].*//gi' < wiki.words | sort | uniq -c | sort -n

rev < wiki.words | sed 's/[^BCDFGHJKLMNPQRSTVWXYZ].*//gi' | rev  | sort | uniq -c | sort -n | tail

# handling non ascii characters?
