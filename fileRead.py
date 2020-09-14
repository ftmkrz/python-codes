# import os
# clear = lambda: os.system("clear")
# clear()
#sea = open("fatma.txt", "r")
#text = sea.readlines()
#for line in text:
    #print(line[:13])

# with open("rumi.txt", "r") as f:
#     print(f.read(35))
#     print(f.read(13))
#     print(f.tell())
#     f.seek(15)
#     print(f.read(20))

#print(sea.read(16))
#print(sea.read(5))
#sea.seek(0)
#print(sea.readline())
#print(sea.readline())
#print(sea.readlines())
#print(type(text))
#sea.close()
#f.close()


#write()

# with open('rumi.txt', 'a', encoding='utf-8')as f:
#     f.write('I like birds..')
# with open('rumi.txt', 'r', encoding='utf-8')as f:
#     f.read()

# with open("dummy_file.txt", 'w', encoding="utf-8") as file:  
# # we create and open the file

#     file.write('This is the first line of my text file')  
#     # writes str data into file

# with open("dummy_file.txt", 'r', encoding="utf-8") as file:
#     print(file.read()) 

# flowers = ['Jasmine', 'Rose', 'Lily', 'Daisy', 'Tulip']
# with open('flowers.txt', 'w', encoding='utf-8')as f:
#     for flower in flowers:f.write(flower + '\n' + '\n')
# with open('flowers.txt', 'r', encoding='utf-8')as f:
#     f.read()



# flower = ['Jasmine', 'Rose','Lily', 'Daisy', 'Tulip']
# with open('flowers.txt','w', encoding='utf-8') as flw:
#     for basket in flower:
#         flw.write(basket+ "\n")
# with open('flowers.txt','r', encoding='utf-8') as fr:
#     print(fr.read(), end="")



# fruits = ['Banana\n', 'Orange\n', 'Apple\n', 'Strawberry\n', 'Cherry\n']

# with open("fruits.txt", 'w', encoding="utf-8") as file:
#     file.writelines(fruits)  # takes an iterator for writing
#     for reef in fruits:
#         file.write(reef + '\n')
# with open("fruits.txt", 'r', encoding="utf-8") as file:
#     print(file.read())
