from create_templates import * 

def test_user_field():
    user_field1= {
    'UID':67,
    'date':date.today(),
    'descriptions':[
            { 'desc':"job1 description", 'quantity':1, 'unit_price':10,},
            { 'desc':"job2 description", 'quantity':2, 'unit_price':20,},
            { 'desc':"job3 description", 'quantity':3, 'unit_price':30,},
        ],
    'tax_rate':0.67,
    'dest_lang':'eng'
    }

    user_field2= {
    'UID':41,
    'date':date.today(),
    'descriptions':[
            { 'desc':"job1 description", 'quantity':1, 'unit_price':10,},
            { 'desc':"job2 description", 'quantity':2, 'unit_price':20,},
            { 'desc':"job3 description", 'quantity':3, 'unit_price':30,},
        ],
    'tax_rate':0.1,
    'dest_lang':'eng'
    }

def doc_creation_tests(document_fields : dict , company_fields : dict, FILE_DIR : str):
    
    
    
    create_invoice(document_fields , company_fields  , FILE_DIR)

    pass

company_info1={
        'name':'John Pork Co',
        'address':'John Pork Co Street',
        'phone':'903-670-1738',
        'email':'john_pork_inc@hotmail.com'
},

doc_info= {
    'UID':41,
    'date':date.today(),
    'estimate_number':6,
    'descriptions':[
            { 'desc':"job1 description", 'quantity':1, 'unit_price':10,},
            { 'desc':"job2 description", 'quantity':2, 'unit_price':20,},
            { 'desc':"job3 description", 'quantity':3, 'unit_price':30,},
        ],
    
    'client_info':{
        'name':'John Pork',
        'address':'John Pork 67 Street',
        'phone':'401-670-4167',
        'email':'john_pork@aol.com'
        },
    
    
    'tax_rate':0.1,
    'dest_lang':'eng'
}

FILE_DIR_1 : str = "created_test_docs/testdoc1.md"
FILE_DIR_2 : str = "created_test_docs/testdoc2.md"

#translate for doc part test
#get_translated_document(user_field1)
#get_translated_document(user_field2)

doc_creation_tests(doc_info,company_info1,FILE_DIR_1)