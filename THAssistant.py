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

    def geometric(self):
        ## y = 1/(2^position)
        remaining = self.prizepool
        table = []

        for p in xrange(self.payablePlayers):
            val = int(self.prizepool * (1.0/(2.0**(p+1))))
            table.append(val)
            remaining -= val
        table[0] += remaining

        return table

    def lognormal(self):
        ## y = (1/x(scale)sqrt(2pi))e^((-ln(x-location)^2)/2scale^2)
        remaining = self.prizepool
        table = []

        scale = 0.6
        location = 0.999

        for p in xrange(self.payablePlayers):
            val = int(self.prizepool * ((1/((p+1)*scale*math.sqrt(2*math.pi))) * math.exp(-(math.log((p+1) - location) ** 2)/(scale * math.sqrt(2)))))
            table.append(val)
            remaining -= val
        table[0] += remaining

        return table

    def exponential(self):
        pass