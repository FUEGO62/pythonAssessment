import time

c = time.time()

print(c)

minute = int(c/60)

hour =int(minute/60)

print((hour+1)%24,":",minute%60)