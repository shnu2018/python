
def total():
    s = 0
    for i in range(100):
        s += i
    return s
def showString(s):
    print(s)
    t = total()
    print(t)
    
showString("hello world")


# In[196]:

def swap(a, b):
    t = a
    a = b
    b = t
a = 2
b = 3
swap(a, b)
print(a, b)


# In[197]:

def swap(pair):
    t = pair[0]
    pair[0] = pair[1]
    pair[1] = t
p = [2, 3]
swap(p)
print(p[0], p[1])


# In[224]:

def bigger(a, b):
    return a if a > b else b
