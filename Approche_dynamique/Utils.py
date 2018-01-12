class Utils():

    def __init__(self):
        self.init =0

    def getObjectListbyName(self, list_objects, object_names):
        newObjectList = []
        print object_names.replace(',',' ').split()
        list_object_names= object_names.split()
        for i  in list_object_names :
            for j in list_objects :
                if i==j.name:
                    print "match !"
                    newObjectList.append(j)
        return newObjectList

