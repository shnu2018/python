
# In[465]:

a = [3, 4, 1, 2]
a.sort()
b = [["cat", 100], ["tigger", 200], ["dog", 500]]
b.sort(key=lambda x: x[0])    # 指定按照每个元素中的第一个元素排序
print(a)
a.reverse()    #  序列反转, 等价于a.sort(reverse=True)
print(a)
print(b)


# In[466]:

a = [3, 4, 1, 2]
a_sorted = sorted(a, reverse=True)
b = [["cat", 100], ["tigger", 200], ["dog", 500]]
b_sorted = sorted(b, key=lambda x: x[0])    # 指定按照每个元素中的第一个元素排序

print("排序后, a: %s" % str(a))
print("sorted(a)返回值：%s" % str(a_sorted))
print("-"*10)
print("排序后, b: %s" % str(b))
print("sorted(b)返回值：%s" % str(b_sorted))


# In[467]:

a = ["cat", "dog", 999]
for element in a:
    print(element)


# In[478]:

print(list(range(5)))
print(list(range(1, 8)))
print(list(range(8, 1, -1)))
print(list(range(1, 8, 2)))


# In[479]:

nums = [1, 2, 3, 4, 5, 6  ,7, 8, 9]
for i in range(len(nums)):  #  len(nums)求出列表长度，range生成长度大小的索引序列
    nums[i] = nums[i] ** 2
print(nums)


# In[480]:

nums = [1, 2, 3, 4, 5, 6  ,7, 8, 9]
nums = [num ** 2 for num in nums]
print(nums)


# In[482]:

nums = [1, 2, 3, 4, 5, 6  ,7, 8, 9]
nums = [num for num in nums if num % 2 == 0]
print(nums)


# In[487]:

nums = [1, 2, 3, 4, 5, 6  ,7, 8, 9]

nums = [i*j for i in nums if i % 2 == 0 for j in nums if j % 2 != 0]

print(nums)


# In[488]:

nums = [1, 2, 3, 4, 5, 6  ,7, 8, 9]

nums = [str(i)+"->"+str(j) for i in nums if i % 2 == 0 for j in nums if j % 2 != 0]

print(nums)


# In[507]:

nums = [1, 2, 3, 4, 5, 6  ,7, 8, 9]
print(nums[:])      # 取所有
print(nums[::])     # 取所有
print(nums[:-1])    # 除去第len(nums)-1位置的数字
print(nums[::-1])   # 所有元素反转
print(nums[2:])     # 第二个元素开始反转
print(nums[-1:])    # 取最后一个元素
print(nums[:5])     # 取前五个元素
print(nums[5:2:-1]) # 从第6个位置到第3个位置(nums[2]不取)，反向取值。截取并反向。
print(nums[-8:-2:2]) # 等价于[1:7:2]
print(nums[:5:])      # 等价于[:5]


# In[521]:

a = [2, 4, 6, 8]
b = [1, 3, 5, 7, 9]
c = ["cat", "tigger"]
d = a + b + c
print(d)


# In[522]:

a = [2, 4, 6, 8]
b = [1, 3, 5, 7]
c = [i+j for i, j in zip(a, b)]
print(c)


# In[524]:

import numpy as np
a = np.array([2, 4, 6, 8])
b = np.array([1, 3, 5, 7])
c = a + b
print(c)