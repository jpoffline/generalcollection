class GeneralCollection():
    def __init__(self, name, prettyname, fields, records):
        self._name = name
        self._prettyname = prettyname
        self._fields = fields
        self._records = records
        pass

    def add_record(self, record):
        data = {}
        for k in record.keys():
            id = None
            for f in self._fields:
                if k == f['name']:
                    id = f['id']
                    break
            if id is not None:
                data[id] = record[k]
            else:
                raise KeyError('CANT FIND RECORD KEY: ' + k)

        record = {
            'id' : len(self._records) + 1, 
            'data':data
        }
        
        self._records.append(record)

    def add_field(self, new_field):
        if len(self._fields) > 0:
            mx = self._fields[len(self._fields)-1]['id']
            nid = int(mx)+1
        else:
            nid = 1
        self._fields.append({'id':str(nid), 'name':new_field})

    def update_record(self, id, key, new_value):
        pass

    def fields(self):
        ff = []
        for f in self._fields:
            ff.append((f['id'], f['name']))
        return ff

    def name(self):
        return self._name

    def prettyname(self):
        return self._prettyname

    def records_json(self):
        table = self.to_table()
        names = table['colnames']
        rows = table['rows']
        rec = []
        for r in rows:
            row = {}
            for i in range(0, len(names)):
                row[names[i]] = r[i]
            rec.append(row)
        return rec

    def to_table(self):
        colnames = [f['name'] for f in self._fields]
        rows = []
        for rec in self._records:
            d = rec['data']
            row = []
            for f in self._fields:
                row.append(str(d.get(f['id'], 'NULL')))
            rows.append(row)
        return {'colnames':colnames,'rows': rows}
    
    def to_csv(self):
        table = self.to_table()
        names = table['colnames']
        rows = table['rows']
        header = ', '.join(names)
        rws = []
        for r in rows:
            rws.append(','.join(r)) 
        body = '\n'.join(rws)
        return(header + '\n' + body)