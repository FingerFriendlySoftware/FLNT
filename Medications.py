
class Reference:

    def __init__(self,*args,**kwargs):

        self.class_to_build = kwargs.pop("class_to_make", None)
        self.class_kwarguments = kwargs
        self.class_arguments = args

    def create_new_class(self):

        temp = self.class_to_build(*self.class_arguments, **self.class_kwarguments)
        return temp



class DictionaryStarter:

    def __init__(self,*args,**kwargs):

        self.equivalence_list = kwargs.pop("equivalence", None)
        values = kwargs.pop("values", None)
        # equivalence is a dictionary with the matching equivalence
        base_variables = kwargs.pop("base", None)
        new_dict = dict(zip(self.equivalence_list.values(), self.equivalence_list.keys()))

        for value in values:
            if value in new_dict:
                self.__dict__[new_dict[value]] = values[value]

    def convert_to_dic(self, *args, **kwargs):

        to_convert = kwargs.get("new_names",self.equivalence_list)
        returner = dict()

        for names in to_convert:
            # print (names)
            # print("in for loop")
            if self.__dict__[names] is not None:
                # print("in if statement")
                returner[to_convert[names]] = self.__dict__[names]

        return returner

class ListStarter:

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

    def convert_to_dic(self, *args, **kwargs):

        to_convert = kwargs.get("new_names",self.equivalence_list)
        returner = dict()


        for names in to_convert:
            print (names)
            print("in for loop")
            if self.__dict__[names] is not None:
                print("in if statement")
                returner[to_convert[names]] = self.__dict__[names]

        return returner






print(dir())