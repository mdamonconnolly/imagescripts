"""
image.py
Contains the image object used for storing image data.
"""

class image():
    
    def __init__(self, path, name):
        self.path = path
        self.name = name
        self.opchain = []
        

    #Op chain functions
    def add_op(self, operation, index):
        self.opchain.append(operation)

    def remove_op(self, index):
        self.opstring.remove(index)


    def addDetail(self, key, *args):
        """
        Add a value to one of the details in the "details" dict.
        :param key: The detail to be changed
        :param *args: The arguments to be added. 
        """
        if key not in self.details:
            print('incorrect key')
            return

        if len(args) < 1:
            print('no args provided')
            return

        if key == 'tags':
            details['tags'].append(args)

        self.details[key][args[0]]

    def save_opchain(self, opchain, file=None):
        """
        Saves the opchain to a file locally, for fast use.
        :param opchain: the opchain to save.
        :param file: the file to write to.
        """

    def load_opchain(self, opchain, file):
        """
        Loads opchain from file.
        :param opchain: the name of the opchain to load.
        :param file: the file to load the opchain from.
        """

    details = {
        "name" : "",
        "tags" : [],
        "date" : "",
        "imageID" : "" #imageID is an ID given to every image.
    }
