import xmltodict
import os

list_dir = os.listdir("D:/Barcode/Annotation file/test")
# print(len(list_dir))
for j in list_dir:
    if j.endswith('.xml'):
        print(j,"\n")
        file = open(f"D:/Barcode/Annotation file/test/{j}", "r")
        xml_string = file.read()
        # print("The XML string is:")
        # print(xml_string)
        python_dict = xmltodict.parse(xml_string)
        print("The dictionary created from XML is:")
        # print(python_dict)

        # Checking wheather there is two classes or one
        check_list = python_dict['annotation']['object']

        # This is for 2 classes
        if isinstance(check_list, list):
            file_path = python_dict['annotation']['path']
            new_path = file_path.replace(os.sep, '/')  # Path name of the file
            obj_1 = python_dict['annotation']['object'][0]['bndbox']

            # Name of Object 1
            class_name_1 = python_dict['annotation']['object'][0]['name']

            # Bounding Box of object 1
            # --> xmin
            xmin_1 = python_dict['annotation']['object'][0]['bndbox']['xmin']
            # --> ymin
            ymin_1 = python_dict['annotation']['object'][0]['bndbox']['ymin']
            # --> xmax
            xmax_1 = python_dict['annotation']['object'][0]['bndbox']['xmax']
            # --> ymax
            ymax_1 = python_dict['annotation']['object'][0]['bndbox']['ymax']

            # Name of Object 2
            class_name_2 = python_dict['annotation']['object'][1]['name']

            # Bounding Box of object 2
            # --> xmin
            xmin_2 = python_dict['annotation']['object'][1]['bndbox']['xmin']
            # --> ymin
            ymin_2 = python_dict['annotation']['object'][1]['bndbox']['ymin']
            # --> xmax
            xmax_2 = python_dict['annotation']['object'][1]['bndbox']['xmax']
            # --> ymax
            ymax_2 = python_dict['annotation']['object'][1]['bndbox']['ymax']

            with open("test_annotation.txt", 'a') as tx:
                tx.writelines(
                    f"{new_path},{xmin_1},{ymin_1},{xmax_1},{ymax_1},{class_name_1}\n")
                tx.writelines(
                    f"{new_path},{xmin_2},{ymin_2},{xmax_2},{ymax_2},{class_name_2}\n")
            tx.close()
        # This is for two classes
        else:
            # File Path
            file_path = python_dict['annotation']['path']
            new_path = file_path.replace(os.sep, '/')

            # Class Name
            class_name = python_dict['annotation']['object']['name']

            # Bounding Box
            xmin = python_dict['annotation']['object']['bndbox']['xmin']
            ymin = python_dict['annotation']['object']['bndbox']['ymin']
            xmax = python_dict['annotation']['object']['bndbox']['xmax']
            ymax = python_dict['annotation']['object']['bndbox']['ymax']
            # print(xmin, ymin, xmax, ymax)

            with open("test_annotation.txt", 'a') as tx:
                tx.writelines(
                    f"{new_path},{xmin},{ymin},{xmax},{ymax},{class_name}\n")
            tx.close()

        file.close()
    else:
        print("This is not an XML file !!!!!")


# l = ["hello", 123]
# if isinstance(l, list):
#     print("yes")
# else:
#     print("No")
