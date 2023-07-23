from json import load, dump

id = int(input("Change the name of file 'error' you want to modify.\n Enter the number of category_id you want to label: "))

with open('error.json',) as f:
    data = load(f)

annotation_data = data["annotations"]

for i in annotation_data:
    if i.get("category_id", False):
        i["category_id"] = id

data["annotations"] = annotation_data

with open('modified.json', 'w', encoding='utf-8') as f:
    dump(data, f)
