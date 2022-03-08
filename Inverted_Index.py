### 
#SQL Query used to extract data on https://data.stackexchange.com/ 
#select
#Id,
#CreationDate as Date_Posted,
#Title, 
#Body,
#Tags
#From Posts
#Where CreationDate LIKE '%2021%' 
#AND tags LIKE '%python%'
#ORDER BY CreationDate 
###
import re
from collections import defaultdict, Counter
import csv
import json
import os
import pandas as pd
os.chdir('C:\\Users\\*filepath')
csvFilePath = r'stack2.csv'
jsonFilePath = r'stack.json'

def csv_to_json(csvFilePath, jsonFilePath):
    jsonStack = []
    with open(csvFilePath, encoding='utf-8') as csvf: 
        csvReader = csv.DictReader(csvf)
        for row in csvReader:
            jsonStack.append(row)
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonStack, indent=4)
        jsonf.write(jsonString)
    
csv_to_json(csvFilePath, jsonFilePath)

def bold(txt):
    return '\x1b[1m%s\x1b[0m' % txt

Token = re.compile(r'[^a-zA-Z0-9]')
def tokenize(text):
    yield from SPLIT_RE.split(text)

def text_only(tokens):
    for t in tokens:
        if t.isalnum():
            yield t

synonyms = {
    'Linux': 'Unix','Plotly': 'Dash', 'Jupyter': 'Anaconda', 'conda': 'pip', 'matplotlib': 'pyplot'
}

def synonyms(tokens):
    for t in tokens:
        yield synonyms.get(t, t)
        
def analyze(text):
    tokens = tokenize(text)
    for token_filter in (text_only, synonyms):
        tokens = token_filter(tokens)
    yield from tokens
    
def index_docs(docs, *fields):
    index = defaultdict(lambda: defaultdict(Counter))
    for Id, doc in enumerate(docs):
        for field in fields:
            for token in analyze(doc[field]):
                index[field][token][id] += 1
    return index
    
def combine_and(*args):
    if not args:
        return Counter()
    out = args[0].copy()
    for c in args[1:]:
        for doc_id in list(out):
            if doc_id not in c:
                del out[doc_id]
            else:
                out[doc_id] += c[doc_id]
    return out
    
def combine_or(*args):
    if not args:
        return Counter()
    out = args[0].copy()
    for c in args[1:]:
        out.update(c)
    return out
 
combine = {
    'OR': combine_or,
    'AND': combine_and,
}

def search_in_fields(index, query, fields):
    for t in analyze(query):
        yield combine['OR'](*(index[f][t] for f in fields))

def search(index, query, operator='AND', fields=None):
    combine = combine[operator]
    return combine(*(search_in_fields(index, query, fields or index.keys())))
    
def query(index, query, operator='AND', fields=None)
index = index_docs(DATA, 'Post_Id', 'Title', 'Body', 'Tags')

### SAMPLE QUERIES TO INDEX
#query(index, 'python', 'AND', 'Dash', fields=['Title'])
#query(index, 'Python', 'AND', 'web', fields=['Body'])
#query(index, 'IndentationError: unexpected indent')
