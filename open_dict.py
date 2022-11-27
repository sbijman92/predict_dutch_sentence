# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 13:03:15 2022

@author: stefa
"""

import json

tf = open("myDictionary.json", "r")
new_dict = json.load(tf)
print(new_dict)
