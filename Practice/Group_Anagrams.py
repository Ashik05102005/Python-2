items = ["eat", "tea", "tan", "ate", "nat", "bat"]
item_dict = {}

for item in items :
    res = sorted(item)
    res = "".join(res)

    if res in item_dict :
        item_dict[res].append(item)

    else:
        item_dict[res] = [item]

result = list(item_dict.values())
print(result)

