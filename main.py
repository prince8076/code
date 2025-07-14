def generate_number(n):
    result = []
    parts = n.split(',')
    for i in parts:
        i=i.strip()
        if not i:
            continue
        
        if '-' in i:
            start_str, end_str = i.split('-')
            start, end = int(start_str), int(end_str)
            result.extend(range(start, end + 1))
        else:
            result.append(int(i))
    return result

user_input = input("Enter range = ")
print(generate_number(user_input))
