from datetime import datetime

DB_DATA = [

    {
    "nomenclatura" : "CL 12 C SUR CR 53 -73",
    "codInstalacion": "041512303000730000",
    "coordenadaX" : "-75.59284067",
    "coordenadaY" : "6.19676160",
    "nomenclaturaSui" : "C 12 C S 53 73",
    "datetime" : datetime.now()
    },
    {
    "nomenclatura" : "DIAG 53 B AVDA 14 -54 (INTERIOR 201 )",
    "codInstalacion": "095173204000540201",
    "coordenadaX" : "-75.52430902",
    "coordenadaY" : "6.34627490",
    "nomenclaturaSui" : "D 53 B 14 54 IN 201",
    "datetime" : datetime.now()
    },
    {
    "nomenclatura" : "AVDA 36 A DIAG 45 -106 (INTERIOR 201 )",
    "codInstalacion": "094336105001060201",
    "coordenadaX" : "-75.54093858",
    "coordenadaY" : "6.33263936",
    "nomenclaturaSui" : "A 36 A 45 106 IN 201",
    "datetime" : datetime.now()
    },
    {
    "nomenclatura" : "DIAG 53 AVDA 13 -44 (INTERIOR 103 )",
    "codInstalacion": "095173003000440103",
    "coordenadaX" : "-75.52310425",
    "coordenadaY" : "6.34634716",
    "nomenclaturaSui" : "D 53 13 44 IN 103",
    "datetime" : datetime.now()
    },
    {
    "nomenclatura" : "CL 11 A SUR CR 53 CC -16",
    "codInstalacion": "041511103330160000",
    "coordenadaX" : "-75.59236111",
    "coordenadaY" : "6.19960863",
    "nomenclaturaSui" : "C 11 A S 53 CC 16",
    "datetime" : datetime.now()
    }
]


# Sample Data1
def getReplacedItem(id):
    return {
        'id': 'id{0}'.format(id),
        'partitionKey': id,
        'message': 'Hello World CosmosDB!',
        'addition': 'test replace {0}'.format(id),
    }
# Sample Data2
def getItem(id):
    return {
        'id': 'id{0}'.format(id),
        'partitionKey': id,
        'message': 'Hello World CosmosDB!',
    }
