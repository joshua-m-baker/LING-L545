I used the two suggested segmenters, the Ruby pragmatic\_segmenter, and the Python NLTK Punkt.

It seems that the Python segmenter correctly separated all of the example paragraphs, but the Ruby segmenter failed on at least one.

In the 50 lines from the corpus that I tested, there was one line that had '..' The Python segmenter correctly left those together and continued the paragraph, but the Ruby segmenter split it, and started the next paragraph with a '.' which is obviously incorrect 

There was also one instance where the Ruby segmenter stripped off a quotation mark that probably should have been left. 
