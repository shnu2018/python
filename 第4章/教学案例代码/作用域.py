
outer = 999  #  outer为全局变量
def func1():
    inner = 888 # inner为局部变量
    print("func1内部：局部变量%s" % inner)  # 打印： func1内部：局部变量888
    print("func1内部：全局变量%s" % outer)  # 打印： func1内部：全局变量999
def func2():
#     print("func2内部：局部变量%s" % inner)  # 出错，无法访问
    print("func2内部：全局变量%s" % outer)  # 打印：  func2内部：全局变量999
    
func1()
func2()
# print("函数外部：局部变量%s" % inner)  # 出错，无法访问
print("函数外部：全局变量%s" % outer)  # 打印：  函数外部：全局变量999
