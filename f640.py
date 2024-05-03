token = input().split()
index = 0
def ev():
    global index
    func = token[index]
    index = index + 1
    if func == 'f':
        return f()
    if func == 'g':
        return g()
    if func == 'h':
        return h()
    return int(func)
    
def f():
    x = ev()
    return 2*x-3

def g():
    x = ev()
    y = ev()
    return 2*x+y-7

def h():
    x = ev()
    y = ev()
    z = ev()
    return 3*x-2*y+z


print(ev())