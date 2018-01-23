class Utils():

    def __init__(self):
        self.init =0

    def getObjectListbyName(self, list_objects, object_names):
        newObjectList = []
        list_object_names=object_names.replace('[','').replace(']','').split(',')
        for i in list_object_names :
            for j in list_objects :
                if j.name in i :
                    newObjectList.append(j)
        return newObjectList

    def getObjectListbyListName(self, list_objects, list_object_names):
        newObjectList = []
        for i in list_object_names :
            for j in list_objects :
                if j.name in i :
                    newObjectList.append(j)
        return newObjectList