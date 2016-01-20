## THAssistant.py
##
## Written by Matthew Egan - January 2016
##
## A class that helps process different calculations for 
## a home game poker tournament.

import math

class THAssistant:
    def __init__(self, players, prizepool, payable):
        self.players = int(players)
        self.prizepool = int(prizepool)
        self.payablePlayers = int(payable)

        self.distFuncs = {"uniform" : self.uniform,
                          "linear" : self.linear,
                          "geometric" : self.geometric,
                          "lognormal" : self.lognormal,
                          "exponential" : self.exponential}

    def prizeDist(self, dist):
        if isinstance(dist, str):
            if dist in self.distFuncs:
                return self.distFuncs[dist]()
            else:
                print "ValueError: dist not a valid value"
                print "Please choose [linear, quadratic, hyperbolic, exponential]"
        else:
            print "TypeError: dist is not a string"

    def uniform(self):
        ## All the same, prizepool/payable
        val = self.prizepool/self.payablePlayers
        remaining = self.prizepool
        table = []

        for p in xrange(self.payablePlayers):
            table.append(val)
            remaining -= val
        table[0] += remaining
        
        return table

    def linear(self):
        ## y = 1  - (1/players)position
        pass

    def geometric(self):
        ## y = 1/(2^position)
        pass

    def lognormal(self):
        pass

    def exponential(self):
        pass