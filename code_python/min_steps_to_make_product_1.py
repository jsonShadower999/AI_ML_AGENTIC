#balance the equation :::fact!!!
# arr=[-2,4,0]
# res=0
# for i in arr:
#     if i<0:
#         current_ans=check_steps_toreach_negative1(i)
#     else:
#         current_ans=check_steps_toreach_1(i) 
# res=res+current_ans 

# def check_steps_toreach_negative(n):
#     if(n==-1):
#         res

#     res=1+check_steps_toreach_negative(n-1)

    

# def check_steps_toreach_1(n):
#     if(n==1):
#         res

#     res=1+check_steps_toreach_1(n-1)

def check_steps_toreach_negative1(n):
    if n == -1:
        return 0
    return 1 + check_steps_toreach_negative1(n - 1)

def check_steps_toreach_1(n):
    if n == 1:
        return 0
    return 1 + check_steps_toreach_1(n - 1)

arr = [-2, 4, 0]
res = 0

for i in arr:
    if i < 0:
        current_ans = check_steps_toreach_negative1(i)
    else:
        current_ans = check_steps_toreach_1(i)
    res += current_ans

print("Total steps:", res)


def check_steps_toreach_negative1(n):
    if n == -1:
        return 0
    return 1 + check_steps_toreach_negative1(n - 1)

def check_steps_toreach_1(n):
    if n == 1:
        return 0
    return 1 + check_steps_toreach_1(n - 1)

# If the number of -1s is odd, the product
# becomes -1. So, you need to add logic to fix
# this—possibly using a 0 if available (turn it into 1 instead of -1), 
# or doing two more steps.

arr = [-2, 4, 0]
res = 0
neg_count = 0
zero_count = 0

for i in arr:
    if i < 0:
        current_ans = check_steps_toreach_negative1(i)
        if i != -1:
            neg_count += 1
        else:
            neg_count += 1
    elif i == 0:
        current_ans = check_steps_toreach_1(i)
        zero_count += 1
    else:
        current_ans = check_steps_toreach_1(i)
    res += current_ans

# If number of -1s is odd and no zero to flip, add 2 steps
if neg_count % 2 == 1 and zero_count == 0:
    res += 2

print("Minimum steps to make product equal to 1:", res)


    

