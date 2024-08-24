import spacy
from spacy.matcher import Matcher


Nlp = spacy.load("en_core_web_md")

def nlp(text):
    return Nlp(text)

def match(pattern, text,img=True):
    doc = Nlp(text)
    matcher = Matcher(Nlp.vocab)
    matcher.add("pattern", [pattern])
    matches = matcher(doc)  
    matcher.remove("pattern")
    indexes = []
    for _, s, e in matches:
        indexes.append([s,e])
    if img and indexes:
         capture()
    return indexes

def match3_color(text):
     match_clean=match([{"LOWER":'clean'}],text)
     match_brown=match([{"LOWER":'brown'}],text)
     val = 1 if match_clean else  0 if match_brown else -1
     if val == -1:
          capture() 

def match3(text):
        match_good=match([{"LOWER":'good'}],text)
        match_ok=match([{"LOWER":'ok'}],text)
        val =  1 if match_good else  0 if match_ok else -1 
        if val == -1:
          capture()
    
def capture():
     pass