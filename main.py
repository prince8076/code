def generate_number(n):
    result = []
    delimiters = ['-','..','to','~']
    parts = n.split(',')
    for i in parts:
        i=i.strip()
        if not i:
            continue
            
        matched= False
        for j in delimiters:
            if j in i:
                start_str, end_str = i.split(j)
                start, end = int(start_str), int(end_str)
                result.extend(range(start, end + 1))
                matched=True
                break

        if not matched:
            result.append(int(i))
    return result

user_input = input("Enter range = ")
print(generate_number(user_input))
