import operator

def inc():
    global count
    count+=1
    print(count) if count % 2 else 0
    return count

count = 0
inc()
inc()















