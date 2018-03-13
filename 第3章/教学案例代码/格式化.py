
print("my name is %s , i am %.1f kg" % ("john", 80.98123))


# In[34]:

'%f, %.2f, %*.f' % (1/3.0, 1/3.0, 4, 1/3.0)


# In[36]:

x = 10.22134
print('%(x).3f' % {"x": x})


# In[37]:

print("hello %(name)s, i am %(age)d years old!" % {"name": "john", "age": 100})


# In[40]:

print("{3}, {0}, {2}, {1}".format("tom", "kitty", "jerry", "david"))


# In[41]:

print('{t}, {k}, {j}, {d}'.format(k="kitty", j="jerry", t="tom", d="david"))


# In[52]:

print('{t}, {0.title}, {j}, {d}'.format("kitty", j="jerry", t="tom", d="david"))


# In[65]:

import sys
print('{0[1]}, {1[name]}, {d}, {s.platform}'.format("kitty",{"name": "tom"}, j="jerry", d="david", s=sys))


# In[71]:

print("{t[name]}".format(t={"name": "john"}))


# In[76]:

import sys
print("{0.platform}".format(sys))  # sys.platform <=> win32
