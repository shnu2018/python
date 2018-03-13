
d2 = dict([(0, "j"), [1, {"name", 999}]])
print(d2)


# In[575]:

from collections import OrderedDict
# d = OrderedDict({0: "cat", 1: "tigger", 2: "monkey"})  # 也可行
d = OrderedDict([[0, "cat"], [1, "tigger"], [2, "monkey"]])
print(d)
