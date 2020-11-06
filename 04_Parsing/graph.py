
from scores_p1 import s1
from scores_p2 import s2

scores = {
    **s1,
    **s2
}

import sys
import matplotlib.pyplot as plt
from adjustText import adjust_text

labels = {0:'eng', 1:'rus', 2:'gle',3:'tur',4:'spa'}

ov = [s["ov"] for s in scores.values()]
vo = [s["vo"] for s in scores.values()]

#x = [0.1, 0.5, 0.3, 0.7, 0.4]  # proportion of OV
#y = [0.9, 0.5, 0.7, 0.3, 0.6]  # proportion of VO
plt.plot(ov, vo, 'ro')
plt.title('Relative word order of verb and object')
plt.xlim([0,1]) # Set the x and y axis ranges
plt.ylim([0,1])
plt.xlabel('OV') # Set the x and y axis labels
plt.ylabel('VO')
texts = []
for name, vals in scores.items():  # Add labels to each of the points
    n = name.split("/")[0]
    n = n.split("_")[1]
    n = n.split("-")[0]
    texts += [plt.text(vals["ov"], vals["vo"], n, fontsize=9)]
adjust_text(texts, arrowprops=dict(arrowstyle='->', color='blue', lw=.5))
plt.savefig("word_order.png")
plt.show()