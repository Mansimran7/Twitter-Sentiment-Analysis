# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 16:33:49 2018

@author: Mansimran Anand
"""

import goslate

text = "Hello World"

gs = goslate.Goslate()
translatedText = gs.translate(text,'pa')

print(translatedText)
