
a = [0, {"a": 100}]
a[1]
type(a)


# In[356]:

[]
[1, 2, 3]
[1, [1, 2], "hello"]
["world", [4, 5, "world"]]
[1, {"name": "john"}, 4, [3, 4]]
[2, {"name": "john"}, (2, 3), {4, 6, 7}]
[5, 100 == 100, 200 if True else 999]
[(3, 4), 4, lambda x: x+100, list]
# [x for x in range(100)]


# In[357]:

animals = ["tigger", "monkey", "cat", "dog"]
print(animals[0], animals[3])


# In[367]:

animals = ["tigger", "monkey", 999, "dog"]
print(animals[-1].title(), animals[0].islower())
animals[2] = "tom"
print(animals)


# In[372]:

a = ["tigger", "monkey"]
print("before append: %s" % a)
a.append("dog")
print("after append: %s" % a)


# In[373]:

a = []
a.append("tigger")
a.append("dog")
a.append("cat")
a.append(888)
a.append([2, 3, 4])
print("new list: %s" % a)


# In[399]:

a = ['tigger', 'monkey', 'tom', 'dog']
a.insert(0, 999)
print("after insert: %s" % a)
a.insert(2, [888, 999])
print("after insert: %s" % a)


# In[405]:

a = [999, 'tigger', [888, 999], 'monkey', 'tom', 'dog']
print("before del: %s" % a)
# del a[0], a[1], a[0]
del a[0] ; del a[1] ; del a[0]
print("after del: %s" % a)


# In[414]:

a = ["cat", "dog", "tigger"]
ele = a.pop(1)
print("pop element：%s" % ele)
print("after pop(), list: %s" % a)


# In[433]:

s = input("input animal to del: ")  # 键盘上输入字符串
a = ["cat", "dog", "tigger", "dog"]
if s in a:
    a.remove(s)
else:
    print("%s not in list, del failed..." % s)
print(a)


# In[423]:

"hello" in a


# In[444]:

a = [999, 'tom', 'dog', "dog", "dog", 999, 99]
print("dog occurences number: %d" % a.count("dog"))
print("999 occurences number: %d" % a.count(999))


# In[445]:

users = [["john", 123456], ["jerry", 888], ["tom", 999]]
login_user = ["jerry", 888]
if login_user in users:
    print("login successful!")
else:
    print("do failed bussiness...")
