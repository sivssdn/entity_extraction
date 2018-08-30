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


# PERSON People, including fictional.
# NORP Nationalities or religious or political groups.
# FACILITY Buildings, airports, highways, bridges, etc.
# ORG Companies, agencies, institutions, etc.
# GPE Countries, cities, states. (That is, Geo-Political Entitites)
# LOC Non-GPE locations, mountain ranges, bodies of water.
# PRODUCT Objects, vehicles, foods, etc. (Not services.)
# EVENT Named hurricanes, battles, wars, sports events, etc.
# WORK_OF_ART Titles of books, songs, etc.
# LANGUAGE Any named language.
# LAW A legislation related entity(?)
# DATE Absolute or relative dates or periods.
# TIME Times smaller than a day.
# PERCENT Percentage, including “%”.
# MONEY Monetary values, including unit.
# QUANTITY Measurements, as of weight or distance.
# ORDINAL “first”, “second”, etc.
# CARDINAL Numerals that do not fall under another type.

'''
Sample Output:
{u'\n': [u'GPE'], u'776': [u'CARDINAL'], u'the Ancient Olympic Games': [u'EVENT'], u'\n Athletics': [u'ORG']}
'''