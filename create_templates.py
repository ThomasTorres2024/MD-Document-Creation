from datetime import date #for getting currnet date str
from markdown_pdf import MarkdownPdf, Section #for converting .MD files to pdf 

"""
Takes in inputs and converts them into an invoice an example PDF file.
The functions are essentially identitcal, I have 2 versions because they
are easier to work with on the front end.
"""

#### EXPECTED SYNTAX FOR INPUT DOC_INFO JSON ####

#Incoming JSON String Format 

#FIELDS WE ARE EXPECTING TO GET PASSED TO THE INVOICE/EXAMPLE CREATORS
#Document Type - invoice, 
# UID : int 
# date - Date of Issue 
# tax - tax rate
#
# descriptions - list[dict[str]] work description - 
#   desc - desc 
#   quantity - quantity
#   unit price - unity price
#   total - total
#
# client info
#   -name 
#   -title 
#   -address 
#   -email 
#Company Fields 
#   company name - str : address
#   company email - str : email 
#   company phone number - str : phone
#
#(Not worried about this at the moment, will add later)
#optional fields 
#expiration/validation date 
#expected start date
#expected completion date
#terms conditionsa and exclusions 
#notes/additional details 
#work auth signature 

#when done render it nicely as a pdf at the end 

#Company Fields 
#   company name - str : address
#   company email - str : email 
#   company phone number - str : phones

"""Saves existing markdown file to PDF
Yes, there are more efficient ways to do this, I'm just doing this temporarily
"""
def save_md_example_to_pdf(INPUT_DIR : str, OUTPUT_DIR : str):
  
  with open(INPUT_DIR, "r") as f:
      md_file_content = f.read()
      
  pdf_from_file = MarkdownPdf()
  pdf_from_file.add_section(Section(md_file_content))
  pdf_from_file.save(OUTPUT_DIR)

"""
Creates invoice document according to my_sample_invoice.md (doesn't clear yet) and turns it into a PDF 
document_fields - a dict containing all fields relevant to the document (for more info look at top of document)
company_fields - fields reused that pertain to each company (for more info look at top of document)
FILE_DIR - a valid directory where the file can be saved to without overwriting existing data
"""
def create_invoice(document_fields : dict , company_fields : dict, FILE_DIR : str):

    client_fields=document_fields['client_info']
    
    #initializing fields here for readability 
    COMPANY_NAME = company_fields['name']
    COMPANY_ADDRESS = company_fields['address']
    COMPANY_PHONE_NUM = company_fields['phone']
    COMPANY_EMAIL = company_fields['email']
    
    #initializing fields here for readability 
    CLIENT_NAME = client_fields['name']
    CLIENT_TITLE = client_fields['title']
    CLIENT_ADDRESS = client_fields['address']
    CLIENT_EMAIL = client_fields['email']
    
    #DOCUMENT_FIELDS 
    INVOICE_NUMBER = document_fields['invoice_number']
    INVOICE_DATE = document_fields['date']
    INVOICE_DUE_DATE = document_fields['due_date']
    
    INVOICE_PAYMENT_INSTRUCTIONS = document_fields['instructions']
    TAX_RATE = document_fields['tax']
    
    #save to dir and modify 
    with open(FILE_DIR,'w') as file:
      
        #top most part 
        file.write(f"# {COMPANY_NAME} - Invoice\n\n")
        file.write(f"## Description  \n\n")

        #company info 
        
        file.write(f"**From**: {COMPANY_NAME}  \n")
        file.write(f"{COMPANY_ADDRESS}   \n")
        file.write(f"{COMPANY_EMAIL}  \n")
        file.write(f"{COMPANY_PHONE_NUM}  \n")
        
        file.write(f"\n\n")
        
        #client info
        file.write(f"**To**: {CLIENT_TITLE}  \n")
        file.write(f"{CLIENT_NAME}   \n")
        file.write(f"{CLIENT_ADDRESS}  \n")
        file.write(f"{CLIENT_EMAIL}  \n")
        
        file.write(f"\n\n")
        
        #date/number info 
        file.write(f"**Invoice Number**  \n")
        file.write(f"{INVOICE_NUMBER}  \n")
        file.write(f"**Invoice Date**  \n")
        file.write(f"{INVOICE_DATE}  \n")
        file.write(f"**Due Date**  \n")
        file.write(f"{INVOICE_DUE_DATE}  \n")
        
        file.write(f"\n\n")
        
        #table info
        file.write("| Description | Quantity | Unit Price | Total |  \n")
        file.write("| :----------- | :------------: | ------------: | ------------:|  \n")
        
        #write each element from doc fields 
        descriptions : list[dict:[str]]=document_fields['descriptions']
        subtotal=0
        total_with_tax=0
        tax_amount=0
        for description in descriptions:
              
              desc=description['desc']
              quantity=description['quantity']
              unit_price=description['unit_price']
              
              total=quantity*unit_price
              subtotal+=total
              
              file.write(f"| {desc} | {quantity} | \\$ {unit_price} | \\$ {total} | \n")
        
        #do calculations
        tax_amount=TAX_RATE*subtotal
        total_with_tax=tax_amount+subtotal
        
        #add part for the 
        
        file.write(f"|  |  | **Subtotal** | \\$ {subtotal} | \n")
        file.write(f"|  |  | **Sales Tax** ({TAX_RATE*100}\\% )  | \\$ {tax_amount} | \n")
        file.write(f"|  |  | **Total** | \\$ {total_with_tax} | \n")
        
        file.write("\n  \n")
        
        file.write(f"**Payment Instructions**:  {INVOICE_PAYMENT_INSTRUCTIONS}  ") 
    
    #finally get as pdf 
    save_md_example_to_pdf(FILE_DIR,"create_pdf_test/example_invoice.pdf")


"""
Creates invoice document according to my_sample_estimate.md
document_fields - a dict containing all fields relevant to the document (for more info look at top of document)
company_fields - fields reused that pertain to each company (for more info look at top of document)
FILE_DIR - a valid directory where the file can be saved to without overwriting existing data
"""
def create_estimate(document_fields : dict , company_fields : dict, FILE_DIR : str):

    client_fields=document_fields['client_info']
    
    #initializing fields here for readability 
    COMPANY_NAME = company_fields['name']
    COMPANY_ADDRESS = company_fields['address']
    COMPANY_PHONE_NUM = company_fields['phone']
    COMPANY_EMAIL = company_fields['email']
    
    #initializing fields here for readability 
    CLIENT_NAME = client_fields['name']
    CLIENT_TITLE = client_fields['title']
    CLIENT_ADDRESS = client_fields['address']
    CLIENT_EMAIL = client_fields['email']
    
    #DOCUMENT_FIELDS 
    ESTIMATE_NUMBER = document_fields['estimate_number']
    ESTIMATE_DATE = document_fields['date']
    ESTIMATE_NOTE = document_fields['document_note']
    TAX_RATE = document_fields['tax']
    
    #save to dir and modify 
    with open(FILE_DIR,'w') as file:
      
        #top most part 
        file.write(f"# {COMPANY_NAME} - Estimate\n\n")
        file.write(f"## Description  \n\n")

        #company info 
        
        file.write(f"**bold** From : {COMPANY_NAME}  \n")
        file.write(f"{COMPANY_ADDRESS}   \n")
        file.write(f"{COMPANY_EMAIL}  \n")
        file.write(f"{COMPANY_PHONE_NUM}  \n")
        
        file.write(f"\n\n")
        
        #client info
        file.write(f"**To**: {CLIENT_TITLE}  \n")
        file.write(f"{CLIENT_NAME}   \n")
        file.write(f"{CLIENT_ADDRESS}  \n")
        file.write(f"{CLIENT_EMAIL}  \n")
        
        file.write(f"\n\n")
        
        #date/number info 
        file.write(f"**Estimate Number**  \n")
        file.write(f"{ESTIMATE_NUMBER}  \n")
        file.write(f"**Estimate Date**  \n")
        file.write(f"{ESTIMATE_DATE}  \n")
        
        file.write(f"\n\n")
        
        #table info
        file.write("| Description | Quantity | Unit Price | Total |  \n")
        file.write("| :----------- | :------------: | ------------: | ------------:|  \n")
        
        #write each element from doc fields 
        descriptions : list[dict:[str]]=document_fields['descriptions']
        subtotal=0
        total_with_tax=0
        tax_amount=0
        for description in descriptions:
              
              desc=description['desc']
              quantity=description['quantity']
              unit_price=description['unit_price']
              
              total=quantity*unit_price
              subtotal+=total
              
              file.write(f"| {desc} | {quantity} | \\$ {unit_price} | \\$ {total} | \n")
        
        #do calculations
        tax_amount=TAX_RATE*subtotal
        total_with_tax=tax_amount+subtotal
        
        #add part for the 
        
        file.write(f"|  |  | **Subtotal** | \\$ {subtotal} | \n")
        file.write(f"|  |  | **Sales Tax** ({TAX_RATE*100}\\% )  | \\$ {tax_amount} | \n")
        file.write(f"|  |  | **Total** | \\$ {total_with_tax} | \n")
        
        #Estimate Number and Date 
        file.write("\n  \n")
        
        file.write(f"**Estimate Notes**:  {ESTIMATE_NOTE}  ") 
    
    #finally get as pdf
    save_md_example_to_pdf(FILE_DIR,"create_pdf_test/example_estimate.pdf")
        
""""Work in progress on this function, i only touched this at 4am trying to give notes on it
Meant to be an async function that queries data for company and do call to webhook """
def get_translated_document(docment_fields : dict):

    #get default info from user ID 
    UID : int = docment_fields['UID']

    #we are supposed to get company info from some kind of query here, not sure yet how this will work
    
    #initialize all fields for readability 
    
    #generate doc number for company     
    provided_date =docment_fields['date']
    
    #translations, webhook expected here   
    
    #await translations 
    
    
    #now that we have the company info that has been queried we can do everything here
  
    
    #if creation of the document was succesful, update internal fields of firebase 
