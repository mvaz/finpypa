from finpypa import bonds
from nose.tools import assert_almost_equals

def test_bond_value():
    b1 = bonds.ZeroCoupon(r=0.06, maturity=20)
    assert_almost_equals( b1.value(), 311.8, places=2)
    
    b3 = bonds.ZeroCoupon(r=0.07, maturity=19.5, compound_fraction=2)
    assert_almost_equals( b3.value(), 261.41, places=2)
    

def test_profit_loss():
    b2 = bonds.ZeroCoupon(r=0.06, maturity=20, compound_fraction=2)
    assert_almost_equals( b2.value(), 306.56, places=2)
    
    assert_almost_equals( b2.profitLoss(rate=0.07, t=0.5), -45.14, places=2) 