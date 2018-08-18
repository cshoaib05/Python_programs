import pandas as pd

country_info= {
                'country':['india','usa','china','japan','uk'],
                'Population' : [1.3,1.4,0.3,0.9,1.2]
                }

df = pd.DataFrame(country_info)

print(df)