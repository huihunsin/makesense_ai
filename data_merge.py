import json

#read first file
with open('file_01.json', 'r') as f_1:
    json_string_01 = f_1.read() #file_dic_01 =json.load(f_1)
    
file_dic_01 = json.loads(json_string_01) #string to dict
image_string_01 = json.dumps(file_dic_01["images"]) #key(image) string extract
image_list_01 = json.loads(image_string_01) #image string to list

file_dic_01 = json.loads(json_string_01) #string to dict
annotation_string_01 = json.dumps(file_dic_01["annotations"]) #key(annotation) string extract
annotation_list_01 = json.loads(annotation_string_01) #annotation string to list

#read second file
with open('file_02.json', 'r') as f_2:
    json_string_02 = f_2.read()

file_dic_02 = json.loads(json_string_02) #string to dict
image_string_02 = json.dumps(file_dic_02["images"]) #key(image) string extract
image_list_02 = json.loads(image_string_02)  #image string to list

file_dic_02 = json.loads(json_string_02) #string to dict
annotation_string_02 = json.dumps(file_dic_02["annotations"]) #key(annotation) string extract
annotation_list_02 = json.loads(annotation_string_02) #annotation string to list

#extract the number of id and image id in first file
file_image_id_01 = image_list_01[-1]["id"]
file_id_01 = annotation_list_01[-1]["id"]

#modify the number of id and image id in second file
for i in image_list_02:
    id_int = i["id"]
    new_id = id_int + file_image_id_01
    i["id"] = new_id
    
    image_list_01.append(i)
    
image_list = image_list_01
    
for i in annotation_list_02:
    id_int = i["id"]
    new_id = id_int + file_id_01 + 1
    i["id"] = new_id
    
    image_id_int = i["image_id"]
    new_image_id = image_id_int + file_image_id_01
    i["image_id"] = new_image_id
    
    annotation_list_01.append(i)

annotation_list = annotation_list_01

#images, annotations overwrite on the first file
file_dic = file_dic_01

file_dic["images"] = image_list
file_dic["annotations"] = annotation_list

#dict to str export json
file_str = json.dumps(file_dic)

with open('new_file_merged.json', 'w') as nf:
    nf.write(file_str)