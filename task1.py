# Quick Task 
# 1
def largest(l):
    max = 0
    for i in l:
        if i > max :
            max = i 
            
    return max
print(largest([3,80,-9,0,100]))

# 2 

import requests 
url = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
data = url.json()
print(data["bpi"]["USD"]["rate"])