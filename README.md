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
