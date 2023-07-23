import json

first_0 = int(input("Enter the starting number of the data to extract: "))
last = int(input("Enter the last number of the data to extract: "))

first = first_0 - 1


#read file
with open('file_divide.json', 'r', encoding='utf-8') as f_1:
    json_string_01 = f_1.read()
    
file_dic_01 = json.loads(json_string_01) #string to dict
image_string_01 = json.dumps(file_dic_01["images"]) #key(image) string extract
image_list_01 = json.loads(image_string_01) #image string to list

file_dic_01 = json.loads(json_string_01) #string to dict
annotation_string_01 = json.dumps(file_dic_01["annotations"]) #key(annotation) string extract
annotation_list_01 = json.loads(annotation_string_01) #annotation string to list

#get annotation first index
for i in annotation_list_01:
    if i["image_id"] == first_0:
        annotation_first_id = i["id"]
        break
#get annotation last index
for i in annotation_list_01:
    
    if last == image_list_01[-1]["id"]:
        annotation_last_id = annotation_list_01[-1]["id"]
        break
    elif i["image_id"] == last + 1 :
        annotation_last_id = i["id"] - 1
        break

#image, annotation indexing       
modified_image = image_list_01[ first : last ]
modified_annotation = annotation_list_01[ annotation_first_id : annotation_last_id + 1 ]
#id variableization(to use  for i in List)
first_image_id = modified_image[0]["id"] - 1
last_id = modified_annotation[0]["id"]
#modify image id
for i in modified_image:
    id_int = i["id"]
    new_id = id_int - first
    i["id"] = new_id
#modify annotation id, image_id   
for i in modified_annotation:
    id_int = i["id"]
    new_id = id_int - last_id
    i["id"] = new_id
    
    image_id_int = i["image_id"]
    new_image_id = image_id_int - first_image_id
    i["image_id"] = new_image_id

#replace ingredient
file_dic_00 = file_dic_01
file_dic_00["images"] = modified_image
file_dic_00["annotations"] = modified_annotation
#transfer to json
file_str = json.dumps(file_dic_00)

with open('new_file_divided.json', 'w', encoding='utf-8') as nf:
    nf.write(file_str)