import time

t = time.time()
s = int(t % (24 * 3600))
m = int(s/60)
h = int(m/60) + 8
print(h, '时', m%60, '分', s%60, '秒')