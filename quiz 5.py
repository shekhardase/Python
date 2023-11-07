#make a list print only numbers which are greater than 6
items = [00, 22, 34, 33, 1]
for item in items:
   if str(item).isnumeric and item>6:
      print(item)