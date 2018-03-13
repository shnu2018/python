
s = str(12345)
print(s[:-1], s[:4:2], s[1:], s[1:-2:2], s[-3:-1])


# In[97]:

s = "hello"
s1 = s[:1] + s[2:]
s2 = s[:1] + "m" + s[2:]
print(s1, s2)


# In[110]:

s1 = s.replace(s[1], "")
s2 = s.replace(s[1], "m")
print(s1, s2)


# In[119]:

s = "hello world"
s = list(s)
s.insert(0, "F")
s.append("K")
s[1] = "M"
print("".join(s))

