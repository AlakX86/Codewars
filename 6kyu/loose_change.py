def loose_change(cents):
    cents = int(cents)
    change_dict = {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    if cents <= 0:
        return change_dict
    while cents > 0:
        if cents >= 25:
            change_dict['Quarters'] = change_dict['Quarters'] + 1
            cents -= 25
            continue
        if cents >= 10:
            change_dict['Dimes'] = change_dict['Dimes'] + 1
            cents -= 10
            continue
        if cents >= 5:
            change_dict['Nickels'] = change_dict['Nickels'] + 1
            cents -= 5
            continue
        if cents >= 1:
            change_dict['Pennies'] = change_dict['Pennies'] + 1
            cents -= 1
            continue
    return change_dict
            
print(loose_change(3.9))