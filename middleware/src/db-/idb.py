class iCollectionsDB:
    def __init__(self):
        pass

    def connect(self):
        raise NotImplementedError("NEED TO BE IMPLEMENTED")

    def add_field_to_collection(self, collection, field):
        raise NotImplementedError("")

    def add_record_to_collection(self, collection, record):
        raise NotImplementedError("")

    def add_collection(self, collection, prettyname):
        raise NotImplementedError("")

    def get(self, nm):
        raise NotImplementedError("NEEDS TO BE IMPLEMENTED")