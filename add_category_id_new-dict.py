from json import load, dump

id = int(input("Enter the number of category_id you want to label: "))

with open('wrong.json',) as f:
    data = load(f)

annotation_data = data["annotations"]

new_dict = {}

for i in annotation_data:
    if i.get("category_id", True):
        continue
    else:
        new_dict["id"] = i["id"]
        new_dict["iscrowd"] = i["iscrowd"] 
        new_dict["image_id"] = i["image_id"]
        new_dict["category_id"] = id
        new_dict["segmentation"] = i["segmentation"]
        new_dict["bbox"] = i["bbox"]
        new_dict["area"] = i["area"]
  
data["annotations"] = new_dict

with open('modified.json', 'w', encoding='utf-8') as f:
    dump(data, f)