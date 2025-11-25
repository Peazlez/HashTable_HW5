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

# change hashing methods, jump ahead for collision by prime numbers
# change size to work with any sized input file

# location = key % len(list)
# n[location] = DataItem

# methods for avoiding collisions(data being placed in same spot in array hash table)
# 1. keep a linked list in each array location
# 2. linear probe, if it cant be placed in "correct spot" look at next spot, so on
# 2a. searching for something that isnt in the list will go on until it reaches the end of the list or hits an empty spot

# create node class that holds dataItem and a .next variable
# maybe make a list class as well that looks keeps track of the last node item
# check csv for length to see if you can generate the size of the data without hard coding it in

# double array size, next largest prime number for table size

import csv
import time
import math

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

# create class to hold dataitem and a .next property for linked list usage
class DataBucket:
    def __init__(self, item: DataItem):
        self.item = item
        self.next = None

# create class that keeps track of last item in each linked list?
class BucketList:
    def __init__(self, bucket: DataBucket):
        self.head = bucket
        self.end = bucket

def is_prime(n):
    # check if given number is prime
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_next_prime(start_num):
    # finds next prime number bigger than starting number
    num = start_num + 1
    while True:
        if is_prime(num):
            print(f"The next prime number after {start_num} is {num}")
            return num
        num += 1
    

# hashing function using ASCII values and prime number
def hashFunction(stringData):
    key = 0
    primeNum = 31
    # large modulus prime number to avoid overflow
    modNum = 10**9 + 9

    for letter in stringData:
        key = (key * primeNum + ord(letter)) % modNum
    # returns key
    return key

# linear probing collision method
def handleCollision(insertionIndex, insertionTable):
    size = len(insertionTable)
    collisions = 0

    while insertionTable[insertionIndex] != None:
        # count number of collisions 
        collisions += 1

        insertionIndex += 1
        # if index gets out of range, set to first spot
        if insertionIndex >= size:
            insertionIndex = 0
         
    return insertionIndex, collisions

# linked list collision method
def handleLinkedCollision(newBucket, insertionIndex, insertionTable):
    collisions = 0
    curBucket = insertionTable[insertionIndex]

    # traverse to proper bucket
    while curBucket.next != None:
        curBucket = curBucket.next
        # update collisions
        collisions += 1 

    # insert to linked list (set curbucket.next = to newBucket)
    curBucket.next = newBucket
    
    # return collisions counter for incrementor
    return collisions

def handleBucketListCollision(newBucket, insertionIndex, insertionTable):

    # add newBucket to end of Bucket list
    bucketList = insertionTable[insertionIndex]
    bucketList.end.next = newBucket
    bucketList.end = newBucket

def main():
    # start timer
    start_time = time.time()
    # variables for optimization analysis
    numRows = 0
    file = "MOCK_DATA.csv"
    with open(file, 'r', newline='', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            numRows += 1

    # remove header from number of rows
    numRows -= 1
    # create tables
    targetSize = int(numRows * 1.5)
    # find next largest prime number
    tableSize = find_next_prime(targetSize)

    hashTitleTable = [None] * tableSize
    hashQuoteTable = [None] * tableSize

    # Collisions
    titleCollisions = 0
    quoteCollisions = 0
    # empty spots in each array
    emptyTitles = 0
    emptyQuotes = 0
    counter = 0
    
    with open(file, 'r', newline='', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        # row is an array that has split each item for DataItem
        for row in reader:
            if counter == 0:
                counter += 1
                continue
            # split information into appropriate dataitem fields
            newItem = DataItem(row)
            # Add datitem to buckets (linked list method)
            titleBucket = DataBucket(newItem)
            quoteBucket = DataBucket(newItem)
            # standardize strings
            movieName = newItem.movie_name.lower().strip()
            movieQuote = newItem.quote.lower().strip()
            # get a key from hash function
            titleKey = hashFunction(movieName)
            quoteKey = hashFunction(movieQuote)
            # hash function to spit out key, then:
            titleInsertionIndex = titleKey % len(hashTitleTable)
            quoteInsertionIndex = quoteKey % len(hashQuoteTable)
            
            # try to insert dataitem into hash title table
            if hashTitleTable[titleInsertionIndex] != None:
                # handle Title collision
                handleBucketListCollision(titleBucket, titleInsertionIndex, hashTitleTable)
                # update title collisions
                titleCollisions += 1

            else:
                # insert Item into Title table
                newBucketTitleList = BucketList(titleBucket)
                hashTitleTable[titleInsertionIndex] = newBucketTitleList

            # try to insert dataitem into has quote table
            if hashQuoteTable[quoteInsertionIndex] != None:
                #handle quote collision
                handleBucketListCollision(quoteBucket, quoteInsertionIndex, hashQuoteTable)
                # update quote collisions
                quoteCollisions += 1
            else:
                # insert Item into Quote table
                newBucketQuoteList = BucketList(quoteBucket)
                hashQuoteTable[quoteInsertionIndex] = newBucketQuoteList
            
            counter += 1

    # should change the range to size variable when that gets changed over to auto read size of movie list
    for i in range(len(hashQuoteTable)):
        if hashQuoteTable[i] == None:
            emptyQuotes += 1
        if hashTitleTable[i] == None:
            emptyTitles += 1

    # end timer
    total_time = (time.time()-start_time)
        
    # print Time analytics
    print(f"Total Time: {total_time:.2f} seconds\n")
    # hashTitle analytics
    print(f"Title Table Collisions: {titleCollisions}\nTitle Table Empty Indexes: {emptyTitles}\n")
    # hashQuotes analytics
    print(f"Quote Table Collisions: {quoteCollisions}\nQuote Table Empty Indexes: {emptyQuotes}\n")

if __name__ == "__main__":
    main()