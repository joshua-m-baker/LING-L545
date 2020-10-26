cat ../UD_English-EWT/en_ewt-ud-train.conllu | python3 tagger_og.py -t en-ud-og.dat
cat ../UD_English-EWT/en_ewt-ud-test.conllu | python3 tagger_og.py en-ud-og.dat > en-ud-og.out
python3 ../evaluation_script/conll17_ud_eval.py --verbose ../UD_English-EWT/en_ewt-ud-test.conllu en-ud-og.out 

OG
AllTags    |     93.47 |     93.47 |     93.47 |     93.47

Updated
AllTags    |     93.05 |     93.05 |     93.05 |     93.05


cat ../UD_Portuguese-GSD/pt_gsd-ud-train.conllu | python3 tagger.py -t pt-ud.dat;
cat ../UD_Portuguese-GSD/pt_gsd-ud-test.conllu | python3 tagger.py pt-ud.dat > pt-ud-test.out;
python3 ../evaluation_script/conll17_ud_eval.py --verbose ../UD_Portuguese-GSD/pt_gsd-ud-test.conllu pt-ud-test.out 


Updated
UPOS       |     96.16 |     96.16 |     96.16 |     96.16

Updated (surrounding bigrams)
UPOS       |     96.76 |     96.76 |     96.76 |     96.76

Original
UPOS       |     96.34 |     96.34 |     96.34 |     96.34

All 4 bigrams 
AllTags    |     96.68 |     96.68 |     96.68 |     96.68


cat ../UD_Portuguese-GSD/pt_gsd-ud-train.conllu | python3 tagger.py -t pt-ud.dat;
cat ../UD_Portuguese-GSD/pt_gsd-ud-dev.conllu | python3 tagger.py pt-ud.dat > pt-ud-dev.out;
python3 ../evaluation_script/conll17_ud_eval.py --verbose ../UD_Portuguese-GSD/pt_gsd-ud-dev.conllu pt-ud-dev.out


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
Add back tags -> 96.73