#import numpy as np
'''#Binary array operation
#create two arrays
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
print(arr1)
print(arr2)

#Elemnt wise addition
result1 = arr1 + arr2
print("Addition:", result1)

#Element wise multiplication
result2 = arr1 * arr2
print("Multiplication:",result2)

#Element wise sqare root
result3 = np.sqrt(arr2)
print("Square Root:",result3)'''





'''#Matrix Multiplication
#create two matrix
m1 = np.array([[1,2],[3,4]])
m2 = np.array([[5,6],[7,8]])


#perform matrix maltiplication
r1 = np.dot(m1,m2)

print("Matrix1:", m1)
print("Matrix2:", m2)
print("Mtarix Multiplication:\n", r1)'''




'''import numpy as np
#create an array 
data = np.array([10,20, 30, 40, 50])

#mean , median , standard deviation
mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)

print("Data:", data)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)'''






'''import pandas as pd
data = {
    "calories":[420,380,390],
    "duration":[50,40,45]
}

#Load data into a dataFrame object:
df = pd.DataFrame(data)
print(df)

print(df.iloc[0,1])      #indexing
print(df.iloc[:,0:1])    #slicing'''





'''import pandas as pd

data = {
    'Region':['East','West', 'East', 'West', 'North', 'East', 'North'],
    'Product':['A','A','B','B','A','B','B'],
    'Sales':[500,700,800,600,750,900,650]
}

df = pd.DataFrame(data)
print(df)

#Group by 'Region and 'Product' and calculate total sales
grouped_df = df.groupby(['Region'])['Sales'].sum()
print(grouped_df)

grouped_df1 = df.groupby(['Region','Product'])['Sales'].sum()
print(grouped_df1)'''





'''import pandas as pd

df1 = pd.DataFrame({
    'ID':[1,2,3,4],
    'Name':['Alice', 'Bob', 'Charlie', 'David'],
    'Dept': ['Hr', 'IT', 'Finance', 'IT']
})

df2 = pd.DataFrame({
    'ID':[3,4,5,6],
    'Salary': [60000,70000, 80000, 90000]
})
print((df1))
print((df2))
inner_join = df1.merge(df2, on='ID', how='inner')

left_join = df1.merge(df2, on='ID', how='left')

right_join = df1.merge(df2, on='ID', how='right')

outer_join = df1.merge(df2, on='ID', how='outer')

print("INNER JOIN: \n", inner_join)
print("LEFT JOIN: \n",left_join)
print("RIGHT JOIN: \n", right_join)
print("OUTER JOIN: \n", outer_join)'''


'''import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0,6])
ypoints = np.array([5,11])

plt.plot(xpoints, ypoints, '+')
plt.show()'''



'''import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([2,3,8,10])
ypoints = np.array([3,7,11,15])

plt.plot(xpoints, ypoints)
plt.show()'''




'''import matplotlib.pyplot as plt
import numpy as np


ypoints = np.array([3,8,1,10])

plt.plot( ypoints, marker = 'o')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Graph title")
plt.show()'''



'''import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0,6])
ypoints = np.array([5,11])

plt.plot(xpoints)
plt.plot(ypoints)
plt.show()'''




'''import matplotlib.pyplot as plt
import numpy as np


ypoints = np.array([3,8,1,10])

plt.plot(ypoints, linestyle = 'dotted', color='r', linewidth='10.2')
plt.show()'''




'''import matplotlib.pyplot as plt
import numpy as np

x = np.array([22,33,44,55,66])
y = np.array([25,35,45,55,65])

plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("SALES")

#plot 2

x = np.array([11,21,31,41,51])
y = np.array([14,24,34,44,54])

plt.subplot(1,2,2)
plt.plot(x,y)
plt.title("INCOME")
plt.show()'''


'''import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([98,86,87,88,111,86,103,87,94,78,77,86,86])

plt.scatter(x,y)
plt.show()'''




'''import matplotlib.pyplot as plt
import numpy as np 

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([98,86,87,88,111,86,103,87,94,78,77,86,86])
plt.scatter(x,y,color='red')

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,98,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x,y,color='green')

plt.show()'''




#Bar graph
'''import matplotlib.pyplot as plt
import numpy as np

x = ['A','B','C', 'D']
y = [3,9,1,10]

plt.bar(x,y)
plt.show()'''


#histogram
'''import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170,10,250)

plt.hist(x)
plt.show()'''


#Piechart
'''import matplotlib.pyplot as plt 
import numpy as np

y = np.array([5,25,25,15])
mylables = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels=mylables)
plt.show()'''





#DATABASE CONNECTION

'''import sqlite3

#create a database
conn = sqlite3.connect('example.db')
#creating a cursor
cursor = conn.cursor()
#create table
cursor.execute('''
'''CREATE TABLE IF NOT EXISTS users
               (id INTEGER PRIMARY KEY,
               name TEXT,
               age INTEGER)'''
''')

#insert data
cursor.execute("INSERT INTO users(name,age)VALUES('Alice',30)")
cursor.execute("INSERT INTO users(name,age)VALUES('Bob',40)")

#commit changes
conn.commit()
#Query the data
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

#display the data
for row in rows:
    print(row)

#close the connection
conn.close()'''

import pymysql



conn = pymysql.connect(
     host = 'localhost',
     user = 'root',
     password='chavijain@0209',
     database='DB2'
 )



cursor.execute('''CREATE TABLE IF NOT EXISTS users
               (id INT AUTO_INCREMENT PRIMARY KEY,
               name VARCHAR(100),
               age INT)
               ''')


cursor.execute("INSERT INTO users(name,age)VALUES('Alice',30)")
cursor.execute("INSERT INTO users(name,age)VALUES('Bob',40)")

conn.commit()

cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

for row in rows:
    print(row)


conn.close()