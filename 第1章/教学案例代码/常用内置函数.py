print(abs(-1)) # 求绝对值
print(range(1, 10, 2))  # 1~10，步长为2的数字序列
print(min([1, 4, 6, 7]))  # 求最小值
print(max([1, 4, 5, 7]))  # 求最大值
print(divmod(2, 4))  # 计算公式：((x - x % y) / y, x % y)
print(pow(2, 3, 2))   # 2 的 3次方再与2取余。计算公式：x**y % z
print(pow(2, 3))   # 2的3次方
print(round(3.3))  # 四舍五入

#int(x)转换为int类型
print(int(2.0))
#返回结果<type 'int'>
print(type(int(2.0)))
#long(x) 转换称长整形
# print(long(10.0))  # python3中废弃。使用int
#float(x) 转称浮点型
print(float(2))
#str(x)转换称字符串
print(str())
#list(x)转称list
print(list("123"))
#tuple(x)转成元祖
print(tuple("123"))
#hex(x)
print(hex(10))
#oct(x)
print(oct(10))
#chr(x)
print(chr(65))
#ord(x)
print(ord('A'))


name="zhang,wang"
#capitalize首字母大写
#Zhang,wang
print(name.capitalize())
#replace 字符串替换
#li,wang
print(name.replace("zhang","li"))
#split 字符串分割 参数：分割规则，返回结果：列表
#['zhang', 'wang']
print(name.split(","))


strvalue="123456"
a=[1,2,3]
b=[4,5,6]
#len 返回序列的元素的长度6
print(len(strvalue))
#min 返回序列的元素的最小值1
print(min(strvalue))
#max 返回序列元素的最大值6
print(max(strvalue))
#filter 根据特定规则，对序列进行过滤
#参数一：函数 参数二：序列
#[2]
def filternum(x):
    if x % 2 == 0:
        return True
print(filter(filternum, a))
#map 根据特定规则，对序列每个元素进行操作并返回列表
#[3, 4, 5]
def maps(x):
    return x+2
print(map(maps,a))

#reduce 根据特定规则，对列表进行特定操作，并返回一个数值

def reduces(x,y):
    return x+y
#zip 并行遍历
#注意这里是根据最序列长度最小的生成
#[('zhang', 12), ('wang', 33)]
name=["zhang","wang"]
age=[12,33,45]
print(zip(name,age))
#序列排序sorted 注意：返回新的数列并不修改之前的序列
print(sorted(a,reverse=True))
