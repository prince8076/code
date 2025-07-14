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
                try:
                    start_str, end_str = i.split(j)
                    start, end = int(start_str), int(end_str)
                    if start<=end:
                        step=1
                    else:
                       step= -1

                    result.extend(range(start, end + step,step))
                    matched=True
                    break
                except ValueError:
                    raise ValueError(f"Invalid range: '{i}'")

        if not matched:
            try:
                result.append(int(i))
            except ValueError:
                raise ValueError(f"Invalid range: '{i}'")
    return result

try:
    user_input = input("Enter range = ")
    print(generate_number(user_input))

except ValueError as e:
    print(f"Error: {e}")