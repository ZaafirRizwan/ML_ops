from wallet import Wallet

def test_getamount():
  obj = Wallet()
  obj.setamount(20)
  assert(obj.getamount(),20)
