
"""
    Portfolio Task - Week 4

    By submitting this code you are declaring that all work in this file,
    other than any provided template code, was written and developed by
    you independently.

    Name: Teagan Liddle
"""

def currency_converter(amount, from_currency, to_currency):

    conversion_rate = {
        'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
        'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
        'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45},
        'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
    }
    if from_currency == "GBP" and to_currency == "CNY":
        GBP_to_CNY = round(conversion_rate["GBP"]["CNY"],2)
        print(f"Conversion: {GBP_to_CNY * amount}")

    elif from_currency == "GBP" and to_currency == "PHP":
        GBP_to_PHP = round(conversion_rate["GBP"]["PHP"],2)
        print(f"Conversion:{GBP_to_PHP * amount}")

    elif from_currency == "GBP" and to_currency == "INR":
        GBP_to_INR = round(conversion_rate["GBP"]["INR"])
        print(f"Conversion:{GBP_to_INR * amount}")

    elif from_currency == "CNY" and to_currency == "GBP":
        CNY_to_GBP = round(conversion_rate["CNY"]["GBP"],2)
        print(f"Conversion:{CNY_to_GBP * amount}")

    elif from_currency == "CNY" and to_currency == "PHP":
        CNY_to_PHP = round(conversion_rate["CNY"]["PHP"])
        print(f"Conversion:{CNY_to_PHP * amount}")

    elif from_currency == "CNY" and to_currency == "INR":
        CNY_to_INR = round(conversion_rate["CNY"]["INR"])
        print(f"Conversion:{CNY_to_INR * amount}")
        

     # for each currency, check currency and check the change currency, then work out costs 





    # your code here

    return None
print(currency_converter(300,'GBP', "CNY"))

# Submit only this file currency_converter.py with the completed function.

# Remove any additional code you may have added during development and testing.
