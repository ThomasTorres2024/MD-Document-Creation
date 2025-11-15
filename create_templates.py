from datetime import date 

import os 


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
#
#   client info
#     -name 
#     -address 
#     -email 
#
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

#Company Fields 
#   company name - str : address
#   company email - str : email 
#   company phone number - str : phone

def get_translation(invoice : str, table_info_to_translate : dict):
        pass 

def create_invoice(document_fields : dict , company_fields : dict, FILE_DIR : str,):

    client_fields=document_fields['client_info']
    
    #initializing fields here for readability 
    COMPANY_NAME = company_fields['name']
    COMPANY_ADDRESS = company_fields['address']
    COMPANY_PHONE_NUM = company_fields['phone']
    COMPANY_EMAIL = company_fields['email']

    #initializing fields here for readability 
    CLIENT_NAME = client_fields['name']
    CLIENT_ADDRESS = client_fields['address']
    CLIENT_PHONE_NUM = client_fields['phone']
    CLIENT_EMAIL = company_fields['email']
    
    #DOCUMENT_FIELDS 
    ESTIMATE_NUMBER = document_fields['estimate_number']
    ESTIMATE_NUMBER = document_fields['date']

    with open(FILE_DIR,'w') as file:
      
        #top most part 
        file.write(f"# {COMPANY_NAME} - Estimate\n\n")
        file.write(f"### Description  \n")

        #company info 
        file.write(f"### Description  \n")    
        
        file.write(f"$\textbf{{From}}$: {COMPANY_NAME}  \n")
        file.write(f"{COMPANY_ADDRESS}   \n")
        file.write(f"{CLIENT_ADDRESS}  \n")
        file.write(f"{COMPANY_EMAIL}  \n")
        file.write(f"{COMPANY_PHONE_NUM}  \n")
    
def create_estimate(document_fields : dict , company_fields : dict, user_fields :dict, FILE_DIR : str,):
    pass 

def create_doc(document_fields : dict , company_fields : dict, user_fields :dict, FILE_DIR : str, doc_type : str) -> bool: 

    doc_created : bool =False 

    if(doc_type=="invoice"):
      doc_created=output_dir=create_invoice()
    elif(doc_type=="estimate"):
      doc_created=output_dir=create_estimate()

    return doc_created

def get_translated_document(docment_fields : dict):
    

    #get default info from user ID 
    UID : int = docment_fields['UID']
    print(UID)
    #initialize all fields for readability 
    
    #generate doc number for company 
    
    provided_date =docment_fields['date']
    print(provided_date)
    
    #translate all translateable fields 
    #list of different descriptions for different asks
    descriptions : list[dict:[str]]=docment_fields['descriptions']
    tax_rate = float(docment_fields['tax_rate'])
    destination_language  = docment_fields['dest_lang']
    
    
    #await translations 
    
    print(descriptions)
    print(tax_rate)
    print(destination_language)
    
    #add to md doc
    
    #
    
    #if creation of the document was succesful, update internal fields of firebase 
    



#translate for doc part test
#get_translated_document(user_field1)

#create_doc()