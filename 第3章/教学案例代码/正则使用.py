# --------------------compile-----------------------


import re
s = "hello world, or nihao shijie"
r = re.compile(r'\w*or\w*')
print(re.findall(r'\w*or\w*', s))   

# --------------------match-----------------------

import re
print(re.match('he','hello world').group())
print(re.match('he','hello world'.upper(), re.I).group())


# In[184]:

print(re.search("he\d{2}dd", "helk yphe99dd87f world he1398ddkk").group())


# --------------------findall、match、search-----------------------


import re
tt = "Tina is a good girl, she is cool, clever, and so on..."
rr = re.compile(r'\w*oo\w*')
print(rr.findall(tt))
print(re.findall(r'(\w)*oo(\w)',tt))#()表示子表达式 


# In[190]:

a=re.search('[\d]',"abc33").group()
print(a)
b=re.match('[\d]',"abc33")
print(b)
c=re.findall('[\d]',"abc33")
print(c)

