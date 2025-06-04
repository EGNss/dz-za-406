# 1
def unique_elements(list):
    return list(set(list))

print(unique_elements([1, 2, 2, 3, 4, 4, 5]))

# 2
def merge_dicts(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value;
    return result;
merge_dicts()

firstDict = {
    'name':'Первый словарь'
    
    
}

secondDict = {
    'name1':'Второй словарь'
}


# 3 задание
def count_frequency(list):
    freq = {}
    for item in list:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

print(count_frequency(['яблоко', 'банан', 'яблоко', 'опельсин', 'банан', 'яблоко']))
