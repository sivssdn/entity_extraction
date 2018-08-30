#coding: utf8
#from spacy.lang.en import English
import spacy
parser = spacy.load("en")

example=u"""
Athletics is mostly an individual sport, with the exception of relay races and competitions which combine athletes' performances for a team score, such as cross country.

Organized athletics are traced back to the Ancient Olympic Games from 776 BC.
"""

#Code "borrowed" from somewhere?!
def entities(example, show=False):
    if show: print(example)
    parsedEx = parser(example)
 
    #print("-------------- entities only ---------------")
    # if you just want the entities and nothing else, you can do access the parsed examples "ents" property like this:
    ents = list(parsedEx.ents)
    tags={}
    for entity in ents:
        #print(entity.label, entity.label_, ' '.join(t.orth_ for t in entity))
        term=' '.join(t.orth_ for t in entity)
        if ' '.join(term) not in tags:
            tags[term]= [entity.label_]
        else:
            tags[term].append(entity.label_)
    print(tags)
entities(example)


