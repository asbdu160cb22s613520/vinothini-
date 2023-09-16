def linear_search_product(product_list,target_product):
  indices=[]
  for i,product in enumerate(product_list):
    if product==target_product:
      indices.append(i)
      return indices
#example usage:
products=["laptop","tablet","phone","phone","desktop"]
target_product="phone"
result=linear_search_product(products,target_product)
print(result)
