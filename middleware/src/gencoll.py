
import src.html.table as htmltable
import src.log as log
import src.data as data
import src.generalcollection as gc


class GeneralCollections():
    def __init__(self, log = log.Log()):
        self._logger = log
        self._all_collections = {}
        self._collection_names = []
        self._load_all_collections()

    def _load_all_collections(self):
        for c in data._COLLECTIONS['collection_names']:
            cd = data._COLLECTIONS['collections'][c]
            self.add_collection(
                c, 
                cd.get('name', c),
                cd.get('fields', []), 
                cd.get('records', [])
            )
            

    def _is_collection(self, collection_name):
        if collection_name in self._collection_names:
            return True
        return False

    def add_collection(self, name, prettyname='', fields=[], records=[]):
        self._logger.write('adding collection: ' + name)
        if not self._is_collection(name):
            self._collection_names.append(name)
            self._all_collections[name] = gc.GeneralCollection(
                name,
                prettyname, fields, records
            )
        else:
            raise TypeError('COLLECTION ALREADY EXISTS: ' + name)

    def names(self):
        return self._collection_names

    def get_collection(self, name):
        self._all_collections
        if self._is_collection(name):
            return self._all_collections[name]
        else:
            raise TypeError('CANNOT FIND COLLECTION FOR ' + name)

    def collection_to_table(self, collection_name):
        return self._all_collections[collection_name].to_table()

    def add_record_to_collection(self, collection_name, record):
        self._all_collections[collection_name].add_record(record)

    def add_fields_to_collection(self, collection_name, fields):
        for field in fields:
            self._all_collections[collection_name].add_field(field)

    def add_field_to_collection(self, collection_name, field):
        self._all_collections[collection_name].add_field(field)

    def get_collection_fields(self, collection_name):
        return self._all_collections[collection_name].fields()

    def summary(self):
        for collection in self._collection_names:
            print('collection: ' + collection)
            print('categories: '+ ', '.join(self._all_collections[collection].fields()))
    
    def get_collection_json(self, nm):
        return {
            'collection': self._all_collections[nm].name(),
            'name': self._all_collections[nm].prettyname(),
            'records': self._all_collections[nm].to_table()
        }

    def detail(self):
        for collection in self._collection_names:
            print('* collection: ' + collection)
            print('** categories: '+ ', '.join(c[1] for c in self._all_collections[collection].fields()))
            print(self._all_collections[collection].to_csv())
            print(self._all_collections[collection].records_json())