# file = open('test.txt')
# print(file.read())
# print(file.read(10))
# print(file.readline())
# file.close()

with open('test.txt','r') as reader:
    content = reader.readlines()
    content2 = reversed(content)
with open('test.txt','w') as writer:
    for i in content2:
        writer.write(i)