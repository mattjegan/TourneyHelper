#!/usr/bin/python
##
## THmain.py
##
## Written by Matthew Egan - January 2016
##
## The main function for the CL version of TourneyHelper

from THAssistant import THAssistant

def main():
    print "Welcome to TourneyHelper"
    print "What would you like to do?"
    print "\t1 - Calculate Prize Pool Distribution"
    print "\t2 - Calculate Blinds Structure"
    print "\t3 - Initial Stack Size Calculator"
    print "\t4 - Initial Chip Distribution"
    command = int(raw_input())

    {1:ppDist, 2:blindsStruct, 3:stackSize, 4:chipDist}[command]()

def ppDist():

    players = int(raw_input("How many players are there: "))
    prizepool = int(raw_input("What is the prizepool: "))
    paidPos = int(raw_input("How many paid positions would you like: "))

    print "What distribution would you like?"
    print "\t1 - Uniform"
    print "\t2 - Geometric"
    print "\t3 - Log-Normal"
    print "\t4 - Exponential"
    distType = int(raw_input())

    director = THAssistant(players, prizepool, paidPos)
    total = 0
    print ""
    print "Prize Pool Distribution:"
    for e, pos in enumerate(director.prizeDist({1:"uniform", 2:"geometric", 3:"lognormal", 4:"exponential"}[distType])):
        print e+1, ":", pos
        total += pos
    print "Total:", total

def blindsStruct():
    
    startingStack = int(raw_input("What is your starting stack: "))
    hours = int(raw_input("How long do you want the game to go for in hours? Enter 0 if unsure: "))

    director = THAssistant()

    print ""
    print "Blinds Structure"
    
    structure, period = director.blindsStructure(startingStack, hours)

    for e, blinds in enumerate(structure):
        print e+1, ":", blinds

    print "Each blind period should go for", period, "minutes."

def stackSize():

    bigBlind = int(raw_input("What is the initial big blind: "))
    chipValueArr = map(int, raw_input("What are your chip values? Separated by spaces: ").split(" "))

    director = THAssistant()

    print ""
    print "Initial Stack Size Calculator"

    stackSize = director.stackCount(bigBlind, chipValueArr)
    print "With a starting BB of", bigBlind, "the stack should be", stackSize

def chipDist():
    
    stackSize = int(raw_input("What is the stack size: "))
    chipValueArr = map(int, raw_input("What are your chip values? Separated by spaces: ").split(" "))

    director = THAssistant()

    print ""
    print "Initial Chip Distribution"

    for val, count in enumerate(director.chipDist(chipValueArr)):
        print val, ":", count

if __name__ == "__main__": main()