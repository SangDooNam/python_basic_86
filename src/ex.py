

#Task 1


# with open('data/task1.txt', 'rb') as task1:
#     ex = open('data/ex.txt', 'wb')
#     wr = ex.write(task1.readline(-1))
#     ex.close()

# with open('data/task1.txt', 'r') as task1:
#     ex = open('data/ex.txt', 'wb')
#     txt = task1.read()
#     encoding = txt.encode('utf-8')
#     wr = ex.write(encoding)


#Task 2


files = [
    {
        "name": "todos.txt",
        "content": ["My ToDos:", "", "Go shopping", "Finish module"]
    },
    {
        "name": "bookmarks.txt",
        "content": ["My links:", "", "https://google.com", "https://digitalcareerinstitute.org"]
    }
]



# def x(lst, path='data/', key='name', content='content'):
#     for i in lst:
#         with open(f'{path}{i[key]}', mode='x') as file:
#             for j in i[content]:
#                 file.write(j+'\n')

# x(files)



#Task 3

# additions = [
#     {
#         "name": "todos.txt",
#         "content": ["Call mom", "Walk the dog"]
#     },
#     {
#         "name": "bookmarks.txt",
#         "content": ["https://python.org", "https://www.djangoproject.com/"]
#     }
# ]

# def a(lst, path='data/', key='name', content='content'):
#     for i in lst:
#         with open(f'{path}{i[key]}', mode='a') as file:
#             for j in i[content]:
#                 file.write(j+'\n')
                
# a(additions)


#Task 4


changes = [
    {
        "name": "todos.txt",
        "change": ("Call mom", "Clean up house")
    },
    {
        "name": "bookmarks.txt",
        "change": ("https://google.com", "https://www.w3resource.com")
    }
]



# def c(lst, path='data/', key='name', content='change'):
#     for i in lst:
#         with open(f'{path}{i[key]}', mode='r') as file:
#             lines = file.readlines()
#         with open(f'{path}{i[key]}', mode='w') as file:
#             for line in lines:
#                 if line.strip() == i[content][0]:
#                     file.write(i[content][1]+'\n')
#                 else:
#                     file.write(line)

# c(changes)


#Task 5


# with open('data/todos.txt', mode='br') as task5:
#     lines = task5.readlines()
# with open('data/todos.secret', mode='w') as task5:
#     for line in lines:
#         for chr in line:
#             # print(chr)
#             task5.write(str(chr)+'\n')


with open('data/todos.secret', 'r') as task5:
    lines = task5.readlines()
    txt = ''
    for line in lines:
        char = chr(int(line))
        txt += char
    print(txt)
    




