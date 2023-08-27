import pandas as pd

fo = pd.read_csv(r"C:\Users\dzine\Downloads\MVP Data  - Sheet2.csv")
shopUrls = fo['URLS']
shopContactInfo = fo['ContactInfo']

dict = {}
for i in range(len(shopUrls)):
    dict[shopUrls[i].lstrip("https://")] = shopContactInfo[i]
    
print(dict)