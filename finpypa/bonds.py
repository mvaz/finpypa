#!/usr/bin/env python

from scipy.optimize import fmin

class Bond(object):
    def __init__(self, p=None, r=None, maturity=None):
        self.rate = r
        self.par = p
        self.maturity = maturity

    def get_rate(self, price, **kwargs):
        def f_aux(rate):
            return ( price - self.value(rate=rate) ) ** 2
        return fmin( f_aux, self.rate, xtol=0.00000000001)[0]

    def value(self, rate=None, t=0):
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
        return self.value(rate=rate, t=t) - self.value()
        # tmp = ZeroCoupon( self.par, rate, self.maturity - t, compound_fraction=self.compound_fraction)
        # return self.value() - tmp.value()


class CouponBond(Bond):
    def __init__(self, p=1000, compound=40, r=None, maturity=None, compound_fraction=1):
        super(CouponBond, self).__init__(p=p, r=r, maturity=maturity)
        self.compound_fraction = compound_fraction
        self.number_fractions = maturity * compound_fraction
        self.compound = compound

    def value(self, rate=None, t=0):
        rate = ( rate or self.rate ) / (1.0 * self.compound_fraction)
        total_rates = self.compound_fraction * self.maturity
        return self.compound / rate + (self.par - self.compound / rate) * pow(1 + rate, - total_rates)
