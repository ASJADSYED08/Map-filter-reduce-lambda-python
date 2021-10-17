# numbers=["22","3","14","5"]
# numbers=list(map(int,numbers))
# numbers[2]=numbers[2]+2
# print(numbers[2])


# def sq(a):
#     return a*a
# numbers=[2,3,4,5,6,7,8]
# square=list(map(sq,numbers))
# print(square)    

#lambda
# numbers=(4,2,3,4,5,6,7,8)
# square=tuple(map(lambda x:x*x,numbers))
# print(square) 

# def sq(a):
#     return a*a
# def cube(a):
#     return a*a*a
# numbers=[2,3,4,5,6,7,8]
# for i in numbers:
#     square=list(map(lambda x:x(i),(sq,cube)))
#     print(square)        


#FILTER
# list1=[1,2,12,3,4,5,6,7,8,9]
# def num_greater_5(num):
#     return num>5
# gr_than_5=list(filter(num_greater_5,list1))
# print(gr_than_5)    
# gr_than_5.sort()
# print(gr_than_5)    


#REDUCE
from functools import reduce
list1=[18,2,3,4,5,6]
num=reduce(lambda x,y:x+y,list1)
print(num)  
