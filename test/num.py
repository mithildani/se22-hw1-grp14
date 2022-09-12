from app.objects.num import Num

def test_num():
  num=Num()
  for i in range(1,100):
    num.add(i)
  mid,div = num.mid(), num.div()
  print(mid ,div)
  return 50<= mid and mid<= 52 and 30.5 <div and div<32