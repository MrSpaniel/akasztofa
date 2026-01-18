import random
with open(konnyebbek.csv, "r", encoding="utf-8") as forrasfajl:
with open(kozepesek.csv, "r", encoding="utf-8") as forrasfajl:
with open(nehezebbek.csv, "r", encoding="utf-8") as forrasfajl:

def get_words(forrasfajl):
    word = random.choice(forrasfajl)
    rewturn word.upper()