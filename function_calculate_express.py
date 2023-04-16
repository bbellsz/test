def validate_input(weight_product,region):
    if type(region) != str:
        if weight_product == 0:
            return "All inputs are invalid"
        else:
            return "Input region as string"
    elif type(weight_product) == str:
        return "Input weight as integer or float"
    else:
        if region in ["Central", "Eastern", "Western", "North", "Northeast", "Southern"]:
            if weight_product == 0:
                return "Please Input as weight greater than 0"
            elif weight_product < 0:
                return "Invalid weight"
            else:
                return weight_product,region
        else:
            if weight_product <= 0:
                return "Input region and weight as invalid"
            else:
                return "Input region as invalid"
            
def calculate_price(weight_product,region):
    alert = validate_input(weight_product,region)
    if (type(region) == str and type(weight_product) != str) and (region in ["Central", "Eastern", "Western", "North", "Northeast", "Southern"] and weight_product > 0):
        if weight_product < 10:
            if region in ["Central", "Eastern", "Western"]:
                cost = 200
            elif region in ["North", "Northeast", "Southern"]:
                cost = 240
        elif weight_product <= 20:
            if region in ["Central", "Eastern", "Western"]:
                cost = 420
            elif region in ["North", "Northeast", "Southern"]:
                cost = 460
        else:
            cost = 500
        return cost
    return alert