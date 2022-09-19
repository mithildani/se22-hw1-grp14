from app.objects.num import Num
from app.utilities.strings import oo

def test_bignum():
	num=Num()
	#   the.nums = 32
	for i in range(1,1000):
		num.add(i)
	oo(num.nums())
	return 32==len(num.has)