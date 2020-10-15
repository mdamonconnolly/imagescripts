

class image():
    
    def __init__(self, path, name):
        self.path = path
        self.name = name
        self.opstring = []

    def add_op(self, operation):
        self.opstring.append(operation)

    def remove_op(self, index):
        self.opstring.remove(index)

    def addDetail(self, key, *args):
        """
        Add a value to one of the details in the "details" dict.
        :param key: The detail to be changed
        :param *args: The arguments to be added. 
        """
        if len(args) < 1:
            print('no args provided')

    details = {
        "name" : "",
        "tags" : [],
        "commID" : "" #commID is an ID given to every commissioner.
    }
