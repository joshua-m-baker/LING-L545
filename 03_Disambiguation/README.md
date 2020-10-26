I tested a number of combinations of features to discern which were most effective. 

Tested with just the surrounding words, -2 bigrams and prefixes -> 94.54% 

Sentence start -> 94.44

Adding back -1, -2 surrounding tags -> 94.45

Add back suffixes -> 94.62

Add back prefixed -> 96.50

Add back prefixes and other thing -> 96.50

Just suffixes and bias -> 90.68
Pervious tags -> 90.89 / essentially no difference

Add actually surrounding words -> 94.44
surrounding bigrams -> 94.64 no difference

Adding prefixes -> 96.50
adding longer prefixes -> 96.57
