# ----------------列表-----------------
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]  
tinylist = [123, 'john']  

print(list) # 输出完整列表  
print(list[0]) # 输出列表的第一个元素  
print(list[1:3]) # 输出第二个至第三个的元素  
print(list[2:]) # 输出从第三个开始至列表末尾的所有元素  
print(tinylist * 2) # 输出列表两次  
print(list + tinylist) # 打印组合的列表


# ----------------元组-----------------
t = ( 'abcd', 786 , 2.23, 'john', 70.2 )  
tinytuple = (123, 'john')  

print(t) 
print(t[0]) 
print(t[1:3])
print(t[2:]) 
print(tinytuple * 2) 
print(t + tinytuple) 

# ----------------字典-----------------

d = {}  
d['one'] = "This is one"  
d[2] = "This is two"  

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}  

print(d['one']) # 输出键为'one' 的值  
print(d[2]) # 输出键为 2 的值  
print(tinydict) # 输出完整的字典  
print(tinydict.keys()) # 输出所有键  
print(tinydict.values()) # 输出所有值

