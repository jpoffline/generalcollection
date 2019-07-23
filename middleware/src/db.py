import src.gencoll as gencoll
#import src.db.idb as idb

class CollectionsDb():
    def __init__(self):
        self._collections = gencoll.GeneralCollections()
        self._insert_mock()
        pass

    def _insert_mock(self):

        self._collections.add_field_to_collection('coffee','hello')
        self._collections.add_field_to_collection('coffee','world')
        
        self._collections.add_record_to_collection('coffee', {'taste':'nice', 'smell': 'this'})
        self._collections.add_record_to_collection('coffee', {'taste':'gross', 'world': 'this'})

        self._collections.add_collection('wineshops', prettyname = 'Wine shops')
        self._collections.add_fields_to_collection('wineshops',['name','music', 'price'])
        self._collections.add_record_to_collection('wineshops', {'name': 'this one','price':12})

    
    def get(self, nm):
        return self._collections.get_collection_json(nm)