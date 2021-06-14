import pandas as pd
df = pd.read_csv("Automobile_data.csv")
car_Manufacturers = df.groupby('company')
volvoDf = car_Manufacturers.get_group('volvo')
print(volvoDf)