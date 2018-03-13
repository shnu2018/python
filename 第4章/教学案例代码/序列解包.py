
def find_min(first, second, *nums):
    """查找传入的所有数字中最小值"""
    print(type(nums))
    m = first if first < second else second
    for n in nums:
        if n < m:
            m = n
    return m

ns = (2, 3, 40, 50, 5, 1)
# ns = {2, 3, 40, 50, 5, 1}  # 可行
# ns = [2, 3, 40, 50, 5, 1]  # 可行
# print(find_min(100, 300, 2, 3, 40, 50, 5, 1))
print(find_min(100, 300, *ns))
# print(find_min(3, 4))


# In[260]:

def find_min(first, second, **nums):
    """查找传入的所有数字中最小值"""
    print(type(nums))
    m = first if first < second else second
    for k, n in nums.items():
        if n < m:
            m = n
    return m
ns = {"a": 2, "b": 3, "c": 40, "d": 50, "e": 5, "f": 1}
# print(find_min(100, 300, a=2, b=3, c=40, d=50, e=5, f=1))
print(find_min(100, 300, **ns))
