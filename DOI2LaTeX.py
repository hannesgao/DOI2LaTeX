import os
import requests

# DOI2LaTeX.py - A simple python script turning DOI list to LaTeX format for references using CrossRef API
#
# __author__     = "Yunhan Gao"
# __maintainer__ = "Yunhan Gao"
# __license__    = "MIT License"
# __email__      = "hannes.gao@gmail.com"
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Using CrossRef API to get metadata
def getMetaData(doi):
    r = requests.get("http://api.crossref.org/works/" + doi)
    if r.status_code == 200:
        data = r.json()
        nameStr = ""
        for name in data['message']['author']:
            nameStr = nameStr + name['given'] + " " + name['family'] + "; "
        nameStrNew = nameStr.removesuffix("; ")
        metaData = ""
        metaData = "\item " + data['message']['title'][0] + ", " + nameStrNew + ", \href{" + data['message']['URL'] + "}{DOI " + doi + "}."
    else:
        print(r, doi)
        metaData = "############# 404 not found with this doi:" + doi + " #############"
    return metaData

# Path for DOI list and results
DOIListPath = 'E:\Projects\Python\DOI-List.txt'
ResultPath = 'E:\Projects\Python\Result.txt'

# Read the entire DOI List as a list of string
with open(DOIListPath, 'rt') as f:
    data = f.readlines()

# Remove EOL from every entry
for i in range(len(data)):
    if data[i].endswith("\n"):
        data[i] = data[i].removesuffix("\n")
        
# Checking data length
print(len(data))

# Iterate over the data list
with open(ResultPath, 'wt', encoding = "utf-8") as r:
    for line in data:
        # process line
        metaData = []
        metaData = getMetaData(line)
        r.write(metaData + "\n")

