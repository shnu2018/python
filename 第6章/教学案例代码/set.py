
s = {3, 4, 5, 5, 6}
print(s)
s = set([2, 3, 3, 4, 4])
print(s)
s = {0, {4, 4}, {"name": "john"}, [3, 4, 4, 6]}  # 错误
print(s)


# In[615]:

s1 = {2, 3, 4}
# s = set([2, 3, 4]) #可行
s2 = {3, 5, 8}
print(s1 - s2) # 差集
print(s1 | s2) # 并集
print(s1 & s2) # 交集
s3 = {(2, 3), "hello", 30, 998.9} # 可以， # tuple, str, int , float是hashable type
#s4 = {[2, 3, 4], {3, 4, 5},{3: 5}}  # 错误 list，dict，set 都是unhashable 类型


# In[621]:

s1 = {2, 3, 4}
s2 = {3, 5, 8}
print(s1 - s2) # 差集
print(s1 | s2) # 并集
print(s1 & s2) # 交集
print(s1 ^ s2) # 对称差集(不会同时出现在两个集合的元素)

s1 -= s2  # 等价于 s1 = s1 - s2
print(s1) 

# s1 |= s2  # 等价于 s1 = s1 | s2
# s1 &= s2  # 等价于 s1 = s1 & s2
# s1 ^= s2  # 等价于 s1 = s1 ^ s2

s3 = [2, 2, 3, 4, 5, 5, "john", "john"]
print(set(s3))  # 去重


# In[626]:

s1 = {2, 3, 4}
s1.add(5)  # 添加一项
s1.update([3, 8, 10]) # 添加一组
s1.issubset({3})  # 判断3是否在集合中
s1.copy()  # 浅层复制
s1.remove(5)  # 删除元素，如果元素不存在则引发异常
s1.discard(5)  # 删除元素，元素不存在不会抛错
s1.pop() # 从集合中随机剔除一个元素，如果是空集合则抛错
s1.clear() # 清除集合
{x**2 for x in s1}  # 类似列表
len(s1)  # 集合大小
for x in s1:
    print(x)   
