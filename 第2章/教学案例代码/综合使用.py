s = 0
for i in range(10):
    s += i
    if i % 2 == 0:
        continue
    else:
        pass
    if s > 200:
        break
else:
    print("[else] result: " + str(s))
print("[while] result: " + str(s))


# In[76]:

a = [x for x in range(10) if x % 2 == 0]
print(a)


# -------------------------------------------

name = ["tom", "kitty", "bob"]
age = [200, 100, 500]
print(list(zip(name, age)))
for name, age in zip(name, age):
    print(name + ", " + str(age))

	
	
