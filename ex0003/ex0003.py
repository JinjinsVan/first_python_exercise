import redis
import random

r = redis.Redis(host='localhost',port=6379,db=0)

# r.flushdb()

couponSet = set()
while len(couponSet)<200:
	couponSet.add(random.randint(1000,9999))

i=1
for coupon in couponSet:
	i+=1
	r.set(str(i),str(coupon))


print(r.keys())



