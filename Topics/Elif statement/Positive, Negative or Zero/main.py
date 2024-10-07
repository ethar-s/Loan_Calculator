def number_value(num1):
    if num1 > 0:
        return 'positive'
    elif num1 < 0:
        return 'negative'
    else:
        return 'zero'


num = float(input())
print(number_value(num))