#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 10:54:59 2018

@author: abdulliaqat
"""

import pandas as pd

# regular function

def function_a():
    return 'a'

def generator_a():
    yield 'a'
    
    
def multiple_yields():
    yield 'a'
    yield 'b'
    yield 'c'
    
def read_csv_generator():
    file = 'recipeData.csv'
    for row in open(file, encoding = 'ISO-8859-1'):
        yield row
        
# list comprehension 
lc_example = [n**2 for n in [1,2,3,4,5]]
        
# generator expression
gc_example = (n**2 for n in [1,2,3,4,5])

# read file as generator expression
lines = (line for line in open('recipeData.csv', encoding = "ISO-8859-1"))


df = pd.read_csv('recipeData.csv', chunksize=1, iterator = True)
df = pd.read_csv('recipeData.csv', chunksize=1, iterator = True)
df.get_chunk()
