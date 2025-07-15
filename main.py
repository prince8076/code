def generate_number(n,output_format='list'):
    result = []
    seen=set()
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
                    if ':' in i:
                        range_part,step_str = i.split(':')
                        step=int(step_str)
                    else:
                        range_part=i
                        step = None
                    start_str, end_str = range_part.split(j)
                    start, end = int(start_str), int(end_str)
                    if step is None:
                        if start<=end:
                            step=1
                        else:
                            step= -1
                    elif start> end and step >0:
                        step=-step
                    if step > 0:
                        stop = end + 1
                    else:
                        stop = end - 1
                    for k in range(start,stop,step):
                        if k not in seen:
                            result.append(k)
                            seen.add(k)
                    matched=True
                    break
                except ValueError:
                    raise ValueError(f"Invalid range: '{i}'")

        if not matched:
            try:
                num =int(i)
                if num not in seen:
                    result.append(int(num))
                    seen.add(num)
            except ValueError:
                raise ValueError(f"Invalid range: '{i}'")

    if output_format == "csv":
        return '"' + ",".join(str(n) for n in result) + '"'
    elif output_format == "set":
        return "{" + ", ".join(str(n) for n in result) + "}"
    return result

try:
    user_input = input("Enter range = ")
    output_format= input("choose output format(list / csv / set):").strip().lower()
    print(generate_number(user_input,output_format))

except ValueError as e:
    print(f"Error: {e}")