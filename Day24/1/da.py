import pandas as pd
df = pd.read_csv("airbnb_data.csv")
n_sea = df[(df['city']=='Seattle')]['city'].count()
p_pvtINsea = round(1399/n_sea,3)
print(p_pvtINsea)