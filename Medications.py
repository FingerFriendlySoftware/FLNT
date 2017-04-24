
class Reference:

    def __init__(self,*args,**kwargs):

        self.class_to_build = kwargs.pop("class_to_make", None)
        self.name = kwargs.get("name",None)
        self.class_kwarguments = kwargs
        self.class_arguments = args
        
    def create_new_class(self):

        temp = self.class_to_build(*self.class_arguments, **self.class_kwarguments)
        return temp

    def name(self):
        return self.name


class DictionaryStarter:

    def __init__(self,*args,**kwargs):

        self.name = kwargs.pop("name",None)
        self.equivalence_list = kwargs.pop("equivalence", None)
        values = kwargs.pop("values", None)
        # equivalence is a dictionary with the matching equivalence
        base_variables = kwargs.pop("base", None)
        new_dict = dict(zip(self.equivalence_list.values(), self.equivalence_list.keys()))

        for value in values:
            if value in new_dict:
                self.__dict__[new_dict[value]] = values[value]

        self.ingredients = ListStarter(values = self.ingredients)

    def convert_to_dic(self, *args, **kwargs):

        to_convert = kwargs.get("new_names", self.equivalence_list)
        returner = dict()

        for names in to_convert:
            # print (names)
            # print("in for loop")
            try:
                if self.__dict__[names] is not None:
                   # print("in if statement")
                   returner[to_convert[names]] = self.__dict__[names]

            except KeyError:
                pass

        return returner

class ListStarter(list):

    def __init__(self,*args,**kwargs):
        list.__init__(self,*args)
        self.name = kwargs.pop("name",None)
        self.equivalence_list = kwargs.pop("equivalence", None)
        listvalues = kwargs.pop("values", None)

        try:
          self.extend(listvalues)
          print("it worked")

        except TypeError:
            print("idk")

    def convert_to_list(self, *args, **kwargs):
        return self






print(dir())