# -*- coding: utf-8 -*-
"""
Created on Sun May 2 01:09:36 2021

@author: beste

"""

import hashlib
import datetime

class Block(object):
    num = 0
    nonce = 0
    data = None
    prev_hash = None
    hash = 0
    timestamp = datetime.datetime.now()
        
    def __init__(self, message):
        self.data = message
        
    def createHeader(self, data):
        self.num = 1
        self.nonce = None # ??
        self.data = data
        self.hash = 0000000000000000000000000000000000000000000000000000000000000000
        
        
    def cal_hash(self): # for eklenecek (omp)
        hash_maker = hashlib.sha256()
        hash_maker.update(str(self.num).encode('ascii') + 
                          str(self.data).encode('ascii') + 
                          str(self.prev_hash).encode('ascii') + 
                          str(self.nonce).encode('ascii'))
        
        return hash_maker.hexdigest()
#        
