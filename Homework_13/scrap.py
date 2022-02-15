import urllib.request, json, csv, pandas as pd


shopee_url = "https://shopee.co.id/api/v4/search/search_items?by=relevancy&keyword=kipas%20angin&limit=60&newest=0&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2"
#print(shopee_url)
with urllib.request.urlopen(shopee_url) as url:
     data_shopee = json.loads(url.read().decode('ascii', 'ignore'))

header = ['Product Name','Price'] #
with open('Data_kipas_angin_Shopee_Wisnu.csv','w') as file: 
   writer = csv.writer(file, lineterminator='\n')
   writer.writerow(header) 
   
   items = data_shopee['items']
   for item in items:
      name = item['item_basic']['name']
      price = item['item_basic']['price']
      data_price = [name, int(price/100000)]
      #print(data_price)
      writer.writerow(data_price)
