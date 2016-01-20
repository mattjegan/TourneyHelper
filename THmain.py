#!/usr/bin/python
##
## THmain.py
##
## Written by Matthew Egan - January 2016
##
## The main function for the CL version of TourneyHelper

from THAssistant import THAssistant

def main():
    director = THAssistant(10, 100, 5)
    total = 0
    for e, pos in enumerate(director.prizeDist("geometric")):
        print e, ":", pos
        total += pos
    print "Total:", total

if __name__ == "__main__": main()