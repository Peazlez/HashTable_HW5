# # Author: Mason Peasley
# Description: Hash Table
# Date: 11/13/25
# Hash Table: Adding to tables (quote and title tables), improving overall program
# Collaboration: Troy Schotter

#### NOTES ####
# prime numbers can be helpful with splitting up the hash table placements
# csv library to easily load in movie csv file

# methods for avoiding collisions(data being placed in same spot in array hash table)
# 1. keep a linked list in each array location
# 2. linear probe, if it cant be placed in "correct spot" look at next spot, so on
# 2a. searching for something that isnt in the list will go on until it reaches the end of the list or hits an empty spot

import csv

size = 1000
hashTitleTable = [None] * size
hashQuoteTable = [None] * size

file = "MOCK_DATA.csv"
counter = 0
with open(file, 'r', newline='', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile)
    # row is an array that has split each item for DataItem
    for row in reader:
        if counter == 0:
            continue
        # split information into appropriate dataitem fields
        # get a key from hash function
        # try to insert dataitem into hash table
        # handle collisions
        counter += 1
print(counter)

# create a class data item to hold movie info
class DataItem:
    def __init__(self, line):
        self.movie_name
        self.genre
        self.release_date
        self.director
        self.revenue
        self.rating
        self.min_duration
        self.production_company
        self.quote

# hash function to spit out key, then:
# location = key % len(list)
# n[location] = DataItem

def hashFunction(stringData):
    # returns key
    pass

def handleCollision():
    pass
