# -*- coding: utf-8 -*-
"""
Created on Sun May 2 01:24:39 2021

@author: beste
"""
from datetime import date, datetime
from Blockchain import Block
import omp
import datetime
MAX_NONCE = 100000000000

class Blockchain:
    block = Block()
    header = Block.createHeader()  # genesis block
    chain = []
    difficulty = 3
    
    def __init__(self):
        self.chain = []  
        self.header = Block.createHeader()
        # self.chain.add(self.header)
        
    def newBlock(self, block):
        block.prev_hash = self.assign_prev_hash(block)
        block.num = len(self.chain)
        if mining(block):
            self.chain.add(block)
        else:
            print("Block is not valid.Can not added into chain.")

    def mining(self, block):  # time hesaplaması da yap
        for block.nonce in range(MAX_RANGE):
            text = str(block.num) + block.data + block.prev_hash + str(block.nonce)
            temp = Block.cal_hash()
            if temp.startswith('0' * self.difficulty):
                block.nonce = temp
                print("Finded matching nonce")
#                print("Ödevde istenilen txt")
                return block.nonce
            
            print("Can not find any match of nonce.")
    
    def assign_prev_hash(self, block):
        
        if len(self.chain) > 1 && block== self.chain[-1]:
            block.prev_hash = self.chain[-2].hash    
            
        else:
            print("error!")
    
    def add(self, block):
        self.chain.append(block)
        return self.chain[:]
    
    def is_chain_valid(self):   # zincirin tümünü de kontrol et
        if chain[0] == None:
            Block.createHeader()
        
    def lastBlock(self):
        return self.chain[-1]

# blockchain = Blockchain()        