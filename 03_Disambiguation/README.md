I tested a number of combinations of features to discern which were most effective. 

I started with just the bias and suffixes of the word and its neighbors as features. This is a rather small feature set, but still achieved 90.68% accuracy. This shows that a lot of information is contained in the last letter of each word (since it strongly implies morphological information). 

To put extra emphasis on suffix emphasis, I also tested adding additional features for just the last letters of the surrounding words, which did improve the accuracy slightly to 90.85, but it was not terribly impactful. 

Adding features for the word itself and the surrounding words boosted the accuracty to 94.36%. This is another fairly large boost, so to build off of that I also tried adding the surrounding bigrams. This boosted the accuracy slightly to 94.64%, but again, is not a terribly useful contribution. 

After adding the i, i-1, and i-2 prefixes, the accuracy improves again to 96.54%. Testing the i+1, i+2 prefixes gave no improvement, which is to be expected, because they don't contain information like the suffixes do. However, adding in longer prefixes did provide some benefit, to 96.76%. 

Finally, I tried multiple combinations features incorporating the previuos tag information, but none of these produced positive results. This was slightly surprising, as I would have expected the tag infromation, but I believe the information contained in these tags was already covered by the previous suffix features, and possibly the raw word features as well. 


