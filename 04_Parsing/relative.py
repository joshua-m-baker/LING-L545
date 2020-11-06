
# names = [
#     "UD_Croatian-SET/hr_set-ud-train.conllu", 
#     "UD_Galician-TreeGal/gl_treegal-ud-train.conllu",
#     "UD_English-GUM/en_gum-ud-train.conllu",
#     "UD_Turkish-GB/tr_gb-ud-test.conllu",
#     "UD_Russian-GSD/ru_gsd-ud-train.conllu"
# ]

names = [
    "UD_Afrikaans-AfriBooms/af_afribooms-ud-train.conllu",
    "UD_Belarusian-HSE/be_hse-ud-train.conllu",
    "UD_Coptic-Scriptorium/cop_scriptorium-ud-train.conllu",
    "UD_Lithuanian-ALKSNIS/lt_alksnis-ud-train.conllu", 
    "UD_Slovak-SNK/sk_snk-ud-train.conllu"
]

sentences = {}
for fname in names:
    print(fname)
    sentences[fname] = []
    with open(fname) as f:    
        s = []
        sentence = True
        for line in f.readlines():
            if not line[0].isdigit():
                if len(s) != 0:
                    sentences[fname].append(s)
                    s = []
                continue
            parts = line.split("\t")
            #s.append((parts[3], parts[7]))
            if "obj" in parts[7]:
                s.append(parts[7])
            elif "VERB" in parts[3]:
                s.append(parts[3])
            else:
                s.append(parts[3])

scores = {}
for l, data in sentences.items():

    score = {
        "ov": 0,
        "vo": 1
    }
    for vo in data:
        for s in data:
            for i in range(len(s)-1):
                pair = s[i: i+2]
                if "obj" in pair[0] and "VERB" in pair[1]:
                    score["ov"] += 1
                elif "obj" in pair[1] and "VERB" in pair[0]:
                    score["vo"] += 1

                # pair = s[i: i+2]
                
                # if pair == ["obj", "verb"]:
                #     score["ov"] += 1
                #     continue
                # elif pair == ["obj", "verb"]:
                #     score["vo"] += 1
                #     continue
    
    print(f"{l}: {score['ov']/sum(score.values())}")

    scores[l] = {
        "ov": score['ov']/sum(score.values()),
        "vo": score['vo']/sum(score.values()),
    }
    #print(score["vo"]/sum(score.values()))

with open("scores.py", "w") as f:
    print(scores, file=f)
