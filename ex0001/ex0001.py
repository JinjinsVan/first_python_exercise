import random

couponNumsSet = set()
for i in range(1,200):
	couponNumsSet.add(random.randint(1000, 9999))



print(couponNumsSet)
