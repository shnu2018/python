
bigger = lambda a, b : a if a > b else b
print(bigger(4, 10))


# In[285]:

funs = [lambda x: 1, lambda x: x , lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]
print(funs[0](2))  # 返回1
print(funs[1](2))  # 返回2
print(funs[2](2))  # 返回2的2次方
print(funs[3](2))  # 返回2的3次方
print(funs[4](2))  # 返回2的4次方


# In[286]:

key = 'got'
fun_dicts = {'already': (lambda: 2 + 2), 'got': (lambda: 2 * 4), 'one': (lambda: 2 ** 6)}
print(fun_dicts[key]())


# In[292]:

def action(x):
    return (lambda y: x + y)
print(type(action(100)) , action(100)(200))

f = action(100)
print(f(200))

