import os

dir = "D:\python"
print(os.listdir(dir))
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    print(fullname)
    if os.path.isdir(fullname):
        print("{} is a directory".format(name))
    else:
        print("{} is a file".format(name))
