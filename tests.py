"""
@author Thomas Torres
@date 11/14/25 
Connectro Invocie/Estimate Test Script for CSC 305 Connectro
    - for now if you run it it just shows that we can get an example invoice and 
    estimate .md file 
    - export .md to pdf, i don't delete md files at the moment but will in the future when this is actually
    implemented 
    
"""
from datetime import date,timedelta #for getting currnet date str
from create_templates import * 


def main():
    
    #example syntax for company info
    #should be the same for invoice/estimate 
    #also i envision this to be part of the database and called 
    company_info={
            'name':'Example Name Co',
            'address':'Example Name Co Street',
            'phone':'903-120-1738',
            'email':'john_pork_inc@hotmail.com'
    }

    #estimates have 'notes' instead of 'payment instructions'
    #no due date 
    estimate_doc_info_example= {
        'UID':41,
        'document_note':'Here is an example note.',
        'date':date.today(),
        'estimate_number':"Example Company - 1",
        'descriptions':[
                { 'desc':"job1 description", 'quantity':1, 'unit_price':10,},
                { 'desc':"job2 description", 'quantity':2, 'unit_price':20,},
                { 'desc':"job3 description", 'quantity':3, 'unit_price':30,},
            ],
        
        'client_info':{
            'name':'Example Name',
            'title':'Client Title',
            'address':'Example Name 12 Street',
            'phone':'401-120-4112',
            'email':'john_pork@aol.com'
            },
        
        
        'tax':0.1,
        'dest_lang':'eng'
    }
    
    
    #invoices have 'payment instructions' instead of 'notes'
    #due date given 
    invoice_doc_info_example= {
        'UID':41,
        'instructions':'Payment Instructions.',
        'date':date.today(),
        'due_date':date.today() + timedelta(days=5),
        'invoice_number':"Example Company - 1",
        'descriptions':[
                { 'desc':"job1 description", 'quantity':1, 'unit_price':10,},
                { 'desc':"job2 description", 'quantity':2, 'unit_price':20,},
                { 'desc':"job3 description", 'quantity':3, 'unit_price':30,},
            ],
        
        'client_info':{
            'name':'Example Name',
            'title':'Client Title',
            'address':'Example Name 12 Street',
            'phone':'401-120-4112',
            'email':'john_pork@aol.com'
            },
        
        
        'tax':0.1,
        'dest_lang':'eng'
    }

    ESTIMATE_DIR : str = "created_test_docs/estimate_test.md"
    INVOICE_DIR : str = "created_test_docs/invoice_test.md"
    
    #create estimate and invocie for the user
    create_estimate(estimate_doc_info_example,company_info,ESTIMATE_DIR)
    create_invoice(invoice_doc_info_example,company_info,INVOICE_DIR)


main()

#i will formalize this for unit tests this week and parse the doc maybe
#not sure how i will do this atm
def doc_creation_tests(document_fields : dict , company_fields : dict, FILE_DIR : str):
    
    
    
    create_invoice(document_fields , company_fields  , FILE_DIR)
    pass

