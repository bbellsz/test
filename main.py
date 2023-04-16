from function_calculate_express import calculate_price

weight_product = int(input("please input weight of products: "))
try:
    try:
        weight_product = int(input(weight_product))
    except:
        weight_product = float(input(weight_product))
except:
     weight_product = str(input(weight_product))
    
region = str(input("please input region: "))
result = calculate_price(weight_product, region)
print(result)