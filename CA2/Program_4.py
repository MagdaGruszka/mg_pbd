cust_address = raw_input('enter customer file:') or 'C:\Python27\CustomerAddresses.csv'
customer_details = open(cust_address, 'r')
print customer_details  # reads and saves in memory the file for customers details

output_invoice = raw_input('enter invoice file:' ) or 'C:\Python27\InvoiceDetails.csv'
invoice_file = open(output_invoice, 'r')
print invoice_file  # reads the invoice file
invoices = invoice_file.readlines()
invoice_file.close()
print invoices

#insert_invoice = raw_input('enter invoice file:' )
#if len(insert_invoice)== 0:
   # insert_invoice = 'C:\Python27\InvoiceOutput.csv'
#else:
    #print ' Start entering data'

#insert_invoice = open(cust_invoice, 'w')
#print insert_invoice  # reads the invoice file

#in csv file we will have a list in defoult
#turn the list into a dictionary
#with key being the customer number and the values into the key

customer_list = customer_details.readlines()
customer_dict = {}

for customer in customer_list[1:]:
    customer_details = customer.strip().split(',')
    customer_dict[customer_details[0]] = customer_details



def create_invoice(customer_details, invoice_number, today, po_number):
    value = 'The Academic Supply Academy LTD' + 22*' ' + 'I N V O I C E' '\n' + \
            'Castle House' + 41*' ' + 'Invoice number: ' + str(invoice_number) + '\n' + \
            'Georges Street' + 39*' ' + str(today) + '\n' + \
            'Dublin 2' + 35*' ' + str(po_number) + '\n' + \
            'TO:' + 50*' ' + '\n' + \
            customer_details[1] + ' ' + customer_details[2] + ' ' + customer_details[3] + '\n' + \
            customer_details[4] + '\n' + \
            customer_details[5] + '\n' + \
            customer_details[6] + '\n'
    return value

print customer_dict
print customer_dict['1']
print customer_dict['1'][2] + ' ' + customer_dict['1'][3]



invoice_number = 5555

import datetime
today = datetime.date.today()


output_handler = open('Invoices.txt', 'w')

for invoice in invoices[1:]:
    invoice_details = invoice.strip().split(',')
    output_handler.write(create_invoice(customer_dict[invoice_details[0]], invoice_number, today, invoice_details[1]))
    invoice_number += 1
output_handler.close()









