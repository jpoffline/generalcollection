
#import src.gencoll as gencoll



def main2():
    collections = gencoll.GeneralCollections()
    
    collections.add_field_to_collection('coffee','hello')
    collections.add_field_to_collection('coffee','world')
    
    collections.add_record_to_collection('coffee', {'taste':'nice', 'smell': 'this'})
    collections.add_record_to_collection('coffee', {'taste':'gross', 'world': 'this'})

    collections.add_collection('wine shops')
    collections.add_fields_to_collection('wine shops',['name','music', 'price'])
    collections.add_record_to_collection('wine shops', {'name': 'this one','price':12})

    collections.detail()

from api import app
app.run(host='0.0.0.0', port=80, debug = True)

#if __name__== "__main__":
    #main()

