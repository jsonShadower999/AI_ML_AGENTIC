#Count of sum of consecutives
#create a default window 
#count_ans=0;
#default window=sum+currentsum until it reaches N 
#variable size window question

# N=10
# list_no=[i for i in range(1,N+1)]

# for i in range (1,len(list_no)):
#     count=0
#     current_sum=0
#     start=0
#     end=0
    
#     store=current_sum+list_no[end]
#     if(store==N):
#         count=count+1
        
#     elif (store<=N):
#         store=current_sum+list_no[end]
#     else:
#         store=store-list_no[start]
#         start=start+1
#         end=end+1
N = 10
list_no = [i for i in range(1, N+1)]
count = 0
start = 0
current_sum = 0

for end in range(len(list_no)):
    current_sum += list_no[end]

    #  window compress it  while sum > N
    while current_sum > N and start <= end:
        current_sum -= list_no[start]
        start += 1

    # If window matches the target
    if current_sum == N:
        count += 1

print("Total ways:", count)

    


    

