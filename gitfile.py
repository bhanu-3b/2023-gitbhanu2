print("creating code for github")
s=["srinu","babu","mani"]
def fun():
    for i in s:
        yield i
        print("commit means snapshot")
o=fun()
for j in o:
 print(j)
print("editing on githubADE-1")
print("trying to push after editing file which is pulled from remotte")
