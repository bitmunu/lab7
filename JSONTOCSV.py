import json
print("введите название файла")
s = input()
csvname = s.strip(".json")
csvname += ".csv"

try:
    with open(s, 'r') as f:
        data = json.loads(f.read())
    data = list(data.values())[0]
    result = ','.join(data[0].keys())
    for i in range(0, len(data)):
        result += '\n' + ','.join(data[i].values())
    print(result)

    with open(csvname, 'w') as f:
        print(result, file=f)

except Exception as e:
    print(f"Error: {str(e)}")


