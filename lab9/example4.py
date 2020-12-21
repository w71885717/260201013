import time
time.sleep(1)

def timer(t):
  if t == 0:
    print("done")
    
  else:
    print("Waits for", t, "seconds")
    time.sleep(1)
    return timer(t-1)
print(timer(5))