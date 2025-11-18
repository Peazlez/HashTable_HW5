# # Author: Mason Peasley
# Description: Hash Table
# Date: 11/13/25
# Hash Table: Adding to tables (quote and title tables), improving overall program
# Collaboration: Troy Schotter

#### NOTES ####
# prime numbers can be helpful with splitting up the hash table placements
# csv library to easily load in movie csv file
# Start with linear probe
# keep track of empty spots (first make it just decrease total empty spots as it adds)

# location = key % len(list)
# n[location] = DataItem

# methods for avoiding collisions(data being placed in same spot in array hash table)
# 1. keep a linked list in each array location
# 2. linear probe, if it cant be placed in "correct spot" look at next spot, so on
# 2a. searching for something that isnt in the list will go on until it reaches the end of the list or hits an empty spot

import csv

size = 15001
hashTitleTable = [None] * size
hashQuoteTable = [None] * size

# create a class data item to hold movie info
class DataItem:
    def __init__(self, row):
        self.movie_name = row[0]
        self.genre = row[1]
        self.release_date = row[2]
        self.director = row[3]
        self.revenue = row[4]
        self.rating = row[5]
        self.min_duration = row[6]
        self.production_company = row[7]
        self.quote = row[8]

def hashFunction(stringData):
    # LATER: maybe try to use division by prime number and using remainder for key
    strLength = len(stringData)
    key = strLength * 2
    # returns key
    return key

def handleCollision(insertionIndex, insertionTable):
    # Breaking here, "infinite loop"
    size = len(insertionTable)

    while insertionTable[insertionIndex] != None:
        insertionIndex += 1
        # if index gets out of range, set to first spot
        if insertionIndex >= size:
            insertionIndex = 0
        
        
    return insertionIndex

def main():
    # variables for optimization analysis

    # Collisions
    titleCollisions = 0
    quoteCollisions = 0

    # empty spots in each array
    emptyTitles = 0
    emptyQuotes = 0

    # time for each construction as well

    file = "MOCK_DATA.csv"
    counter = 0
    with open(file, 'r', newline='', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        # row is an array that has split each item for DataItem
        for row in reader:
            if counter == 0:
                counter += 1
                continue
            newItem = DataItem(row)
            # split information into appropriate dataitem fields
            # get a key from hash function
            key = hashFunction(newItem.movie_name)
            # hash function to spit out key, then:
            insertionIndex = key % len(hashTitleTable)
            # try to insert dataitem into hash table
            if hashTitleTable[insertionIndex] != None:
                # handle collisions
                insertionIndex = handleCollision(insertionIndex, hashTitleTable)
            # insert Item
            hashTitleTable[insertionIndex] = newItem

            counter += 1
    print(counter)

if __name__ == "__main__":
    main()