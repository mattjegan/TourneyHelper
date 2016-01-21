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
    command = int(raw_input())

    {1:ppDist}[command]()

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

if __name__ == "__main__": main()