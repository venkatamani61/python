##read mode
# file1=open("demo.txt",'r')
# print(file1.read())
# file1.close()
# with open("demo.txt",'r') as file2:
#     print(file2.read())
#     file2.seek(0)
#     print(file2.readline())
#     file2.seek(0)
#     print(file2.readline(3))
#     file2.seek(0)
#     print(file2.readlines())
#     file2.seek(0)
#     print(file2.readlines(1))
# with open("demo.txt",'w') as file2:
#     file2.write("this is written by using r mode")
# with open("demo.txt",'r') as file2:    
#     print(file2.read())
with open("demo.txt",'a') as file2:    
    file2.write("\nthis is written by using append mode")
    
with open("demo.txt",'r') as file2:
    print(file2.read())
    
