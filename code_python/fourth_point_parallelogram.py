#Missing Point of a Parallelogram
#two adjacent A+c=B+d
#d=a+c-b 

# Input:
# A = (3, 2)
# B = (3, 4)
# c = (2, 2)
# Output:
# 2.000000 0.000000

# list_coordiates=[(3,2),(3,4),(2,2)]
# diff=list_coordiates[0][1]-list_coordiates[1][1]
# if(diff<0):
  
   
#     x=list_coordiates[2][0]
#     y=list_coordiates[1][1]-diff 
#     print((x,y))
# else:
#     x=list_coordiates[2][0]
#     y=list_coordiates[1][1]+diff 
#     print((x,y))

# Given points
A = (3, 2)
B = (3, 4)
C = (2, 2)

# Calculate the missing point D = A + C - B
D_x = A[0] + C[0] - B[0]
D_y = A[1] + C[1] - B[1]
   

    
