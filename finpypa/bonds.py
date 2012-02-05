#!/usr/bin/env python

class Bond(object):
    def __init__(self, p=None, r=None, maturity=None):
        self.rate = r
        self.par = p
        self.maturity = maturity
    
    def value(self, cur_rate, t=0):
        pass
        
class ZeroCoupon(Bond):
    def __init__(self, p=1000, r=None, maturity=None, compound_fraction=1):
        super(ZeroCoupon, self).__init__(p=p, r=r, maturity=maturity)
        self.compound_fraction = compound_fraction
    
    def value(self, rate=None, t=0):
        rate = rate or self.rate
        val = self.par * pow( 1 + rate/self.compound_fraction, - (self.maturity - t) * self.compound_fraction)
        return val
    
    def profitLoss(self, rate=None, t=0):
        rate = rate or self.rate
        return self.value(rate=rate, t=t) - self.value()
        # tmp = ZeroCoupon( self.par, rate, self.maturity - t, compound_fraction=self.compound_fraction)
        # return self.value() - tmp.value()
        
        