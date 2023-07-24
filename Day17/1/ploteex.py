# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
# df=pd.read_csv('Car_sales.csv')
# print(df.head())
# df=df.sort_values('Sales in thousands')
# plt.plot(df['Sales in thousands'])
# plt.show()
# for g,d in df.groupby('Manufacturer'):
    # plt.barh(g,d['4-year resale value'].mean())
    # plt.barh(g,d['Price in thousands'].mean(),left=d['4-year resale value'].mean())
#     # print(g,d['Sales in thousands'].sum())
#     plt.barh(g,d['Sales in thousands'].sum(),color='red')
#     # plt.bar(g,d['Sales in thousands'].sum(),color='red')
# plt.ylabel("Model Name")
# plt.xlabel("Total Sales")
# plt.show()
# def add(x,y):
#     for i in range(len(x)):
#         plt.text(i,y[i]+5,y[i],ha='center',color='red',alpha=.2)


# for g,d in df.groupby('Vehicle type'):
#     # print(g,d['Vehicle type'].count())
#     plt.bar(g,d['Vehicle type'].count(),color='blue')
# add(df.groupby('Vehicle type')['Vehicle type'],df.groupby('Vehicle type')['Vehicle type'].count())

# plt.show()
# df['Price in thousands']=df['Price in thousands'].fillna(df['Price in thousands'].mean())
# # print(df[df['Manufacturer']=='Acura'])

# plt.hist(df['Price in thousands'],bins=4)
# plt.show()

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv('Car_sales.csv')
# print(df.head())
# res=set(df['Vehicle type'])
# print(res)
x=dict()
# print(df[df['Vehicle type']=='Car'].count())
# for i in set(df['Vehicle type']):
#     x[i]=df[df['Vehicle type']==i]['Vehicle type'].count()

# # # print(x.keys())
# plt.pie(x.values(),labels=x.keys())
# plt.legend()
# plt.scatter(df['Fuel capacity'],df['Fuel efficiency'])
# df['Curb weight']=df['Curb weight'].fillna(df['Curb weight'].mean())
# plt.boxplot(df['Curb weight'],)
car=df[df['Vehicle type']=='Car']['Sales in thousands']
pas=df[df['Vehicle type']=='Passenger']['Sales in thousands']
plt.plot(np.arange(len(car)),car,linestyle='--',label='Car')
plt.plot(np.arange(len(pas)),pas,linestyle='-.',label='Passenger')
plt.xticks(np.arange(0,150,10))
plt.yticks(np.arange(0,600,50))
plt.title('Sales in thousands for different vehicle types')
plt.legend()
plt.show()
