print("creating code for github")
s=["srinu","babu","mani"]
def fun():
    for i in s:
        yield i
o=fun()
for j in o:
 print(j)
