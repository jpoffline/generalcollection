def to_table(data):
    colnames = data[0]
    rows = data[1]
    head = '<thead><th>'
    for nm in colnames:
        head += '<td>' + nm + '</td>'
    head += '</th></thead>'
    body = '<tbody>'
    for row in rows:
        rr = '<tr>'
        for col in row:
            rr += '<td>' + col + '</td>'
        body += rr + '</tr>'
    return '<table>' + head + body + '</tbody>' + '</table>'