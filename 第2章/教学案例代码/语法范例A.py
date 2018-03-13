
# In[24]:

a = 300
if a < 200:
    b = a + 100
else:
    b = a

print(b)

b = (a + 100) if a < 200 else a
print(b)


# In[32]:

while False:
    print("while...")
    break 
else:
    print("else...")

输出结果：else...


# In[41]:

s = 0
i = 1
while i <= 100:
    s += i
    i += 1
print(s)


# In[45]:

s = 0
i = 0
while True:
    i += 1
    if i % 2 == 0:
       continue 
    s += i
    if i > 100:
        break
print(s)


# In[46]:

s = 0
i = 1
while i <= 101:
    s += i
    i = i + 2
print(s)


# In[51]:

s = 0
for i in range(1, 101):
    s += i
print(s)


# In[55]:

s = 0
for i in range(100):
    s += i
    if i == 500:
        break
else:
    print("else...")
print(s)


# In[61]:

for c in 'abcd':
    print(c)
