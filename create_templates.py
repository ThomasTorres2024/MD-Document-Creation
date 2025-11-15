from datetime import date 




#Incoming JSON String Format 
#Document Type - invoice, 
# UID : int 
# Invoice specific fields - dict of str 
#   date - Date of Issue 
#   descriptions - list[dict[str]] work description - 
#       desc - desc 
#       quantity - quantity
#       unit price - unity price
#       total - total
# subtotal - subtotal  
# tax - tax 
# total 
# destination language - 'dest_lang' 
#
#optional fields 
#expiration/validation date 
#expected start date
#expected completion date
#terms conditionsa and exclusions 
#notes/additional details 
#work auth signature 

#for the first part im just going to focus ong etting the eky stuff in 

# get company info from given UID obtain as fields await 
# translate relevant translateable fields, await this also 
# while we are waiting, make a new .md doc with the info, we want to save it as an editable pdf 

#when done render it nicely as a pdf at the end 

def create_doc():
    pass 

def get_translated_document(fields : dict):
    
    
    #get default info from user ID 
    UID : int = fields['UID']
    print(UID)
    #initialize all fields for readability 
    
    #generate doc number for company 
    
    provided_date =fields['date']
    print(provided_date)
    
    #translate all translateable fields 
    #list of different descriptions for different asks
    descriptions : list[dict:[str]]=fields['descriptions']
    tax_rate = float(fields['tax_rate'])
    destination_language  = fields['dest_lang']
    
    
    #await translations 
    
    print(descriptions)
    print(tax_rate)
    print(destination_language)
    
    #add to md doc
    
    #
    
    #if creation of the document was succesful, update internal fields of firebase 
    


field1= {
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

field2= {
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

get_translated_document(field1)