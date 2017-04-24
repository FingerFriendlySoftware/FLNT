import json
import pprint
from Medications import DictionaryStarter
from Medications import  Reference

def openandprint(file, *args, **kwargs ):

    with open(file) as json_data:
        obj = json.load(json_data)

        for member in obj:
            print(member)

       # print(json.dumps(obj, indent=4))

    return obj

code = {"reference":"system",
        "drugID":"code",
        "name":"display"}

codes = Reference()


basic = {"resource_type":"resourceType",
         "identity":"id",
         "drug":"code",
         "status":"status",
         "is_brand":"isBrand",
         "is_over_the_counter":"isOverTheCounter",
         "form": "form",
         "ingredients":"ingredient",
         "package":"package"}

ugly = {"resource_type":"WRONG",
         "identity":"handsup",
         "drug":"code",
         "status":"status",
         "is_brand":"isBrand",
         "is_over_the_counter":"isOverTheCounter",
         "form": "form",
         "ingredients":"ingredient",
         "package":"package"}




med = openandprint("medication0301.json")

pray = Reference(equivalence = basic, values = med, class_to_make = DictionaryStarter)


test = DictionaryStarter(equivalence = basic, values = med)

if isinstance(test.resource_type, str):
    print("you didnt fuck up")


#print(json.dumps(vars(test),indent=4))

edited = test.convert_to_dic(new_names=ugly)

print(json.dumps(edited,indent=4))

