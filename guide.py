# # import os 
# # print(f'hello {os.getlogin()}') ; print("ok")


# # Lists 
# # there is no keyword in python 
p = []
q = [1,2,3,4,5]

# # add elements to list 
# q.append(6)
# print(q) # add the ele to the end of the list

# # to add an el to the beginning of the list insert()
# # list.insert(index = 0 in our case but the future ,  and the ele)
q.insert(0 , 0)

# for loop
# for ele in q:
#     print("element" , ele)

# enumerate : gives the element and its index in the list

# for i , e in enumerate(q):
#     print(f'index {i} element{e}')


# to loop at certain number we can user the range()
# range (start postion , end postion , optional how many postion you want to jump
# from one postion to another)
for num in range(0,10):
    print(num)


# how to loop for higher number to lower
# range (start , end , step)
for i in range(10,0 , -1):
    print("reverse:" , i)
