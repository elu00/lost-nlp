import spacy

nlp = spacy.load('en_core_web_lg')
text = open('data/jinsun.txt', 'r').read() # open a document
doc = nlp(text) # process it
doc.to_disk('data/jinsun.bin') # save the processed Doc
