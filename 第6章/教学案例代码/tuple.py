
# In[536]:

t2 = (2, "john", {"name": "dog"}, 10)
# t2[2] = "hello world" 出错，元组元素不可变
t2[2]["name"] = "cat"  # 正确，因为元素是可变对象dict
print(t2)


# In[552]:

d = {0: "john", "name": "dog"}
print(d["name"])
print(d.get("name"))
print(d.get("tom"))
# print(d["tom"])  # 异常，KeyError
