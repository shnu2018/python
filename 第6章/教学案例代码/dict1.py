
d = {0: "john", "name": "dog"}
print(d["name"])
print(d.get("name"))
print(d.get("tom"))
# print(d["tom"])  # 异常，KeyError


# In[568]:

d = {0: "john", "zoo": ["dog", "cat", "tigger"]}
d[0] = "tom"
d["zoo"][1] = "dog"
d["monkey"] = "king"
print(d)


# In[569]:

d = {0: 'tom', 'zoo': ['dog', 'dog', 'tigger'], 'monkey': 'king'}
del d["zoo"], d[0]
print(d)

