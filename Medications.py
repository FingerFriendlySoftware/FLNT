import json
import pprint


def openandprint(file, *args, **kwargs ):

    with open(file) as json_data:
        obj = json.load(json_data)

        for member in obj:
            print(member)

       # print(json.dumps(obj, indent=4))

    return obj

basic = {"resource_type":"resourceType",
         "identity":"id",
         "drug":"code",
         "status":"status",
         "is_brand":"isBrand",
         "is_over_the_counter":"isOverTheCounter",
         "form": "form",
         "ingredients":"ingredient",
         "package":"package"}


class Medication:
    empty = ""

    def __init__(self,*args,**kwargs):

        self.equivalence_list = kwargs.pop("equivalence", None)
        equivalence_dictionary = kwargs.pop("values", None)
        # equivalence is a dictionary with the matching equivalence
        if self.equivalence_list is not None and equivalence_dictionary is not None:
            print("passed")
            self.resource_type = equivalence_dictionary.pop(self.equivalence_list.get("resource_type"), None)
            self.identity = equivalence_dictionary.pop(self.equivalence_list.get("identity"), None)
            self.drug = equivalence_dictionary.pop(self.equivalence_list.get("drug"), None)
            self.status = equivalence_dictionary.pop(self.equivalence_list.get("status"), None)
            self.is_brand = equivalence_dictionary.pop(self.equivalence_list.get("is_brand"), None)
            self.is_over_the_counter = equivalence_dictionary.pop(self.equivalence_list.get("is_over_the_counter"), None)
            self.form = equivalence_dictionary.pop(self.equivalence_list.get("form"), None)
            self.ingredients = equivalence_dictionary.pop(self.equivalence_list.get("ingredients"), None)
            self.package = equivalence_dictionary.pop(self.equivalence_list.get("package"), None)
            self.dose = equivalence_dictionary.pop(self.equivalence_list.get("dose"), None)
            self.next_dose_time = equivalence_dictionary.pop(self.equivalence_list.get("next_dose_time"), None)
            self.perscriber = equivalence_dictionary.pop(self.equivalence_list.get("perscriber"), None)
            self.refill_date = equivalence_dictionary.pop(self.equivalence_list.get("refill_date"), None)

        elif equivalence_dictionary is not None:
            print("FAILED")
            self.resource_type = equivalence_dictionary.pop("resource_type", None)
            self.identity = equivalence_dictionary.pop("identity", None)
            self.drug = equivalence_dictionary.pop("drug", None)
            self.status = equivalence_dictionary.pop("status", None)
            self.is_brand = equivalence_dictionary.pop("is_brand", None)
            self.is_over_the_counter = equivalence_dictionary.pop("is_over_the_counter", None)
            self.form = equivalence_dictionary.pop("form", None)
            self.ingredients = equivalence_dictionary.pop("ingredients", None)
            self.package = equivalence_dictionary.pop("package", None)
            self.dose = equivalence_dictionary.pop("dose", None)
            self.next_dose_time = equivalence_dictionary.pop("next_dose_time", None)
            self.perscriber = equivalence_dictionary.pop("perscriber", None)
            self.refill_date = equivalence_dictionary.pop("refill_date", None)

        else:

            self.resource_type = kwargs.pop("resource_type", None)
            self.identity = kwargs.pop("identity", None)
            self.drug = kwargs.pop("drug", None)
            self.status = kwargs.pop("status", None)
            self.is_brand = kwargs.pop("is_brand", None)
            self.is_over_the_counter = kwargs.pop("is_over_the_counter", None)
            self.form = kwargs.pop("form", None)
            self.ingredients = kwargs.pop("ingredients", None)
            self.package = kwargs.pop("package", None)
            self.dose = kwargs.pop("dose", None)
            self.next_dose_time = kwargs.pop("next_dose_time", None)
            self.perscriber = kwargs.pop("perscriber", None)
            self.refill_date = kwargs.pop("refill_date", None)






med = openandprint("medication0301.json")

test = Medication(equivalence = basic, values = med)

print(json.dumps(vars(test),indent=4))

