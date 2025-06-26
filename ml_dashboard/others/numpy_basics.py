
String : count(),split() , join() , find() , replace() , + 
List:   append() , pop(), reverse(),sort(), index() , clear() ,extend(), insert() , copy(),deepcopy(),remove()
Tuple : count() , index()
set: add(),clear(),remove(), pop() , union(), intersection(),dffernece(), symmetric_difference()
update() , | , reduce() , itertools.chain() , *operator(unpacking)

dict: {key:values}
dict2={k:v for(k,v) in zip(keys,values)}
dict1={1:"abc" , 2:"cde" , 3:"wdr"}
dict1.get(1)
dict1.keys()
dict1.values()
dict1.items()
dict1.pop(2)

conditional statement 
loops
break , continue , pass
function
import math
math.pow(10,2)
Lambda function ::: multiple parameter : only 1 expression
List cmp
reduce , filter , 




pip? python package installer
python -m pip install numpy'
Numpy + pandas + scipy + matplotlib

import numpy as np
np.array([[12,3,4],[1,4,5]])
np.zeros((3,3))
np.ones((3,3))
np.arange(start,end+1,gap)
np.arange(end+1).shape((end+1 multiple, end+1 multiple))
np.linspace(start,end,no_of_values)
np.random.random((2,3))
np.full((2,3),7)
Identity matrix: 

np.sum(list,axis=0)
#axis ==0, column wise'
np.sum(list,axis=1)

# two or more list manipulation at same time
for i , j , k  in in zip(list1,list2,list3):
             print(list1[i]*list2[j]*list3[k])
  
  
#math tool 
for i in list1:
     np.exp(i)
     np.sqrt(i)
     np.sin(i)
     np.cos(i)
     np.log(i)


np.sum(list)
np.sum(list1,list2)
np.subtract(list1,list2)
np.divide(list1,list2)
np.multiply(list1,list2)
np.exp(list!)
np.min(list)
np.max(list)
np.mean(list)
np.median(list)
np.std(list)
np.corrcoef(list)
Fourier Transformation + linear algebra 

np.concatenate((a,b)) #tuple of two array
np.hstack((a,b))
np.vstack((a,b))
np.column_stack()
np.hsplit()

SLICING ???

list1[row_slicing,column_slicing]
list1[:2] #first two row data , first two feature 
list1[:1,1:2] # show first feature with 2nd data_item





array_equal vs equal
array vs numpy which is fast n why? 
range(1000) vs np.arange(1000) difference ?
Numpy array ? interface {data, dimension , strides}
Array Inspection? shape +size + ndim +dtype
list.reshape(3,4,3)



Data collected is not pure 
Missing values + incorrect format + different units + unnecessary data

--------------------------------------------------------------------------------
pandas ---->panel data ---multi-dimension data
series , data  frame , panel 
merge , join , concate 



#file and dataset handling

import pandas as pd
#load data
cars_dts=pd.read_csv("cars231.csv")
type(cars_dts)
cars.head()
cars.tail()
cars.shape
cars.info(null_counts=True) # display all info 
cars.info() 
cars.describe()[cars.mean(),cars.meadian(),cars.std() , cars.min() , cars.max() ,cars.count()]

#clean data
cars_clean = cars.rename(columns={'unname':'model'})
cars_clean.fillna(cars.mpg.mean())
cars_clean.dropna()
cars.drop(columns={})
cars_clean=cars.drop(columns=['s.no','wt'])

#indexing n extracting

cars_clean.iloc[ :, 4]
cars_clean.iloc[:,3:7]
cars_clean.loc[:,"mpg"]
cars.loc[:7,"mpg":"hp"]

f=lambda x:x*2
cars["mpg"].apply(f) 
cars.sort_values(by='cyl',ascending=False)
cars_filtered[(cars['cyl']>7) & (cars['hp']>21 ])]





#Data Visualization :::
pictorial representation
matplotlib , seaborn , plotly , altair 

Types of Plot :
1. line plot 
2. area plot 
3. histogram 
4. scatter plot 
5. bar plot
6. violin plot
7. pie chart 
8. box plot

subplots::: compare all the plots 

matplotlib vs seaborn 
countplots
heatmaps for showing correlation
colormaps


import seaborn as sns
titans_dst=sns.load_dataset("titans_dts")
sns.countplot(x="gold_mines", data="titans_dts",palette={'red','green','blue'})
sns.heatmap(data="titans_dts",annot=True)
why to use annot ??





















  

