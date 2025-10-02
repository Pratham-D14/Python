import pandas as pd

df = pd.read_excel("sitemap.xlsx")
df_sheet1 = pd.read_excel("sitemap.xlsx", sheet_name="Sheet1")
# print(df_sheet1.head())
# print(df_sheet1.info())
urls = df_sheet1.columns[5]
allUrls = df[urls]

try:
    with open("urls.text", "w") as file:
        for url in allUrls:
            file.write(url + "\n")
except Exception as e:
    print(f"An error occurred: {e}")