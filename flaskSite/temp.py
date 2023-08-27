import pandas as pd

fo = pd.read_csv(r"C:\Users\dzine\Downloads\MVP Data  - Sheet2.csv")

# print(fo.head())

tempstorenames = []
for i in range(len(fo['URLS'])):
    tempstorenames.append("StoreName{i}".format(i = i))
    
print(tempstorenames)
