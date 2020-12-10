import string
import copy
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords
nltk.download('averaged_perceptron_tagger')
import re
import pandas as pd
import altair as alt
import json

f = open("Data_Final.txt", encoding="utf8") 
raw = f.read()

actor1 = "Niklas_Maak"
actor2 = "Tony_Fadell"
actor3 = "Rem_Koolhaas"

## List of words with no punctuation but with stamps
tokenizer = nltk.RegexpTokenizer(r"\w+")
wordsNoPunct = tokenizer.tokenize(raw)

taggedWords = nltk.pos_tag(wordsNoPunct)

def pct_ofWords(pos, actorDict, actorWC):
    specList = [wordTup for wordTup in actorDict if wordTup[1] == pos]
    posCount = len(specList)
    return posCount / actorWC

def calc_lsm(lsmA1, lsmA2):
    if lsmA1 + lsmA2 == 0: return -1
    print(f'sytle match {1 - (abs(lsmA1 - lsmA2) / (lsmA1 + lsmA2))}')
    return 1 - (abs(lsmA1 - lsmA2) / (lsmA1 + lsmA2))

def avg_lsm(lsmDict): 
    avgLsm = 0
    forAvg = len(lsmDict)
    for wType, lsm in lsmDict.items():
        if lsm != -1:
            avgLsm += lsm
        else: forAvg -= 1
    return avgLsm / forAvg 

def lsm_calcs(actor1Words, actor2Words, posList):
    actor1WC = len(actor1Words)
    actor2WC = len(actor2Words)
    lsmDict = {}
    for pos in posList: 
        lsmA1 = pct_ofWords(pos, actor1Words, actor1WC)
        lsmA2 = pct_ofWords(pos, actor2Words, actor2WC)
        lsmCalc = calc_lsm(lsmA1, lsmA2)
        lsmDict[pos] = lsmCalc
    finalLsm = avg_lsm(lsmDict);
    lsmDict["final avg"] = finalLsm
    return lsmDict
        
############################
# WORD LISTS FOR REFERENCE #
############################

def makeWordListsByActor(words):
    wordList1 = []
    wordList2 = []
    wordList3 = []
    actor1_On = False
    actor2_On = False
    actor3_On = False

    for word in words: 
        ## Capturing actors' name in the corpus
        if word[0] == actor1:
            actor1_On = True
            actor2_On = False
            actor3_On = False
        elif word[0] == actor2:
            actor1_On = False
            actor2_On = True
            actor3_On = False
        elif word[0] == actor3:
            actor1_On = False
            actor2_On = False
            actor3_On = True

        ## Words in actors' phrases
        if actor1_On == True and word[0] != actor1: 
            wordList1.append(word)
        elif actor2_On == True and word[0] != actor2: 
            wordList2.append(word)
        elif actor3_On == True and word[0] != actor3: 
            wordList3.append(word)
    
    return wordList1, wordList2, wordList3

maakTagged, fadellTagged, koolTagged = makeWordListsByActor(taggedWords)
posList = ['PRP', 'IN', 'WRB', 'DET', 'CC']


kmLsmDict = lsm_calcs(koolTagged, maakTagged, posList)
mfLsmDict = lsm_calcs(maakTagged, fadellTagged, posList)
fkLsmDict = lsm_calcs(fadellTagged, koolTagged, posList)
print(f'km::: {kmLsmDict}')
print(f'mf::: {mfLsmDict}')
print(f'fk::: {fkLsmDict}')

## convert to json for small linked graphs ##
def makePOSJson(actor1, actor2, lsmDict):
    jsonBuild = {}
    jsonBuild["nodes"] = [{"id": actor1}, {"id": actor2}]
    jsonBuild["links"] = []
    for posType, pct in lsmDict.items():
        jsonBuild["links"].append({"source": actor1, 
                                "target": actor2,
                                "group": posType, 
                                "value": pct}) 
    if actor1 == "Koolhaas" and actor2 == "Maak": 
        writeOut = 'idsFinal/kmLSM.json'
    elif actor1 == "Maak" and actor2 == "Fadell":
        writeOut = 'idsFinal/mfLSM.json'
    elif actor1 == "Fadell" and actor2 == "Koolhaas":
        writeOut = 'idsFinal/fkLSM.json'
    with open(writeOut, 'w') as writeMeOut: 
        json.dump(jsonBuild, writeMeOut, indent = 2)
    return jsonBuild

kmLsmJson = makePOSJson("Koolhaas", "Maak", kmLsmDict)
mfLsmJson = makePOSJson("Maak", "Fadell", mfLsmDict)
fkLsmJson = makePOSJson("Fadell", "Koolhaas", fkLsmDict)

