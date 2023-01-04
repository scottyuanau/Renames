from os.path import isfile, join
import os
import shutil

path = os.path.expanduser("~/OneDrive/Scott and Coco Pty Ltd/Invoices")
filename = os.path.basename(path).split(".")[0].title()

#basic configuration
first_month = input('What is the first month?e.g. 04\n')  # first month of the last quarter, e.g. July is 07.
second_month = input('What is the second month?e.g. 05\n')   # second month of the last quarter
third_month = input('What is the third month?e.g. 06\n')   # third month of the last quarter
currentYear = input('What is the year?e.g. 2022\n') # year


credit_card_suppliers = ['Algo Expert','iCare','Bunnings','Gazman','NSW Transport', 'Station', 'Godaddy', 'Seafood', 'Seed', 'QBE', 'Rego','Udacity','Typo','Uniqlo', 'Opera House', 'Mecca', 'JB Hifi', 'Eastwood Seafood', 'Chop', 'Baby Harbour', 'Apple', 'Parking', 'Chemist warehouse', 'Officeworks', 'Google Ads', 'Ikea', 'Amazon', 'Meat Emporium', 'butchery','DFI','coles','fuel','feeder','web ninja','kmall09','super','seek business','food packaging','google','coursera','fedder', 'when i work','wws','nike', 'cardless','kennards', 'telstra','petrol', 'lululemon', 'Zip', 'Costco', 'Bob', 'Woolworth', 'Tongli', 'post', 'Bombora', 'Food Dairy', 'Shopify', 'Adobe', 'Ikea', 'FYI']  # paid via credit card
ba_suppliers = ['KP Lawyers','Food Safety Inspection', 'sinosmart','legal','HW Accounting','daiwa','de toni','pomona', 'Madhouse', 'Tulip', 'MF', 'Fresh', 'YCC', 'Munja']  # paid via business account
hl_suppliers = ['igeno', 'nova', 'rent']  # paid by home loan
the_month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

invoices = [f for f in os.listdir(path) if isfile(join(path, f))]  # read invoices path



def move_file():
    #check if folder exists, if not, create the folder
    folder1 = f"/Users/scott/Library/CloudStorage/OneDrive-Personal/Scott and Coco Pty Ltd/Invoices/{the_month[int(first_month) - 1]} {currentYear}/Westpac Credit Card 0631/"
    folder2 = f"/Users/scott/Library/CloudStorage/OneDrive-Personal/Scott and Coco Pty Ltd/Invoices/{the_month[int(second_month) - 1]} {currentYear}/Westpac Credit Card 0631/"
    folder3 = f"/Users/scott/Library/CloudStorage/OneDrive-Personal/Scott and Coco Pty Ltd/Invoices/{the_month[int(third_month) - 1]} {currentYear}/Westpac Credit Card 0631/"
    folder4 = f"/Users/scott/Library/CloudStorage/OneDrive-Personal/Scott and Coco Pty Ltd/Invoices/{the_month[int(first_month) - 1]} {currentYear}/CBA Business Account 5433/"
    folder5 = f"/Users/scott/Library/CloudStorage/OneDrive-Personal/Scott and Coco Pty Ltd/Invoices/{the_month[int(second_month) - 1]} {currentYear}/CBA Business Account 5433/"
    folder6 = f"/Users/scott/Library/CloudStorage/OneDrive-Personal/Scott and Coco Pty Ltd/Invoices/{the_month[int(third_month) - 1]} {currentYear}/CBA Business Account 5433/"
    folder7 = f"/Users/scott/Library/CloudStorage/OneDrive-Personal/Scott and Coco Pty Ltd/Invoices/{the_month[int(first_month) - 1]} {currentYear}/Westpac Home Loan 800269/"
    folder8 = f"/Users/scott/Library/CloudStorage/OneDrive-Personal/Scott and Coco Pty Ltd/Invoices/{the_month[int(second_month) - 1]} {currentYear}/Westpac Home Loan 800269/"
    folder9 = f"/Users/scott/Library/CloudStorage/OneDrive-Personal/Scott and Coco Pty Ltd/Invoices/{the_month[int(third_month) - 1]} {currentYear}/Westpac Home Loan 800269/"
    folders = [folder1, folder2, folder3, folder4, folder5, folder6, folder7, folder8, folder9]
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder) #make folder recursively
    print('Folder checked & created.')

    #move files
    for invoice in invoices:
        for credit_card_supplier in credit_card_suppliers:
            if invoice.lower().find(credit_card_supplier.lower()) >= 0 and invoice.split()[-1].split('.')[0][2:4] == first_month:
                shutil.move(path+"/"+invoice, os.path.expanduser(f"/Users/scott/Library/CloudStorage/OneDrive-Personal/Scott and Coco Pty Ltd/Invoices/{the_month[int(first_month)-1]} {currentYear}/Westpac Credit Card 0631/")+invoice)
            elif invoice.lower().find(credit_card_supplier.lower()) >= 0 and invoice.split()[-1].split('.')[0][2:4] == second_month:
                shutil.move(path+"/"+invoice, os.path.expanduser(f"/Users/scott/Library/CloudStorage/OneDrive-Personal/Scott and Coco Pty Ltd/Invoices/{the_month[int(second_month)-1]} {currentYear}/Westpac Credit Card 0631/")+invoice)
            elif invoice.lower().find(credit_card_supplier.lower()) >= 0 and invoice.split()[-1].split('.')[0][2:4] == third_month:
                shutil.move(path + "/" + invoice, os.path.expanduser(f"/Users/scott/Library/CloudStorage/OneDrive-Personal/Scott and Coco Pty Ltd/Invoices/{the_month[int(third_month)-1]} {currentYear}/Westpac Credit Card 0631/") + invoice)

    # paid by business bank account
    for invoice in invoices:
        for ba_supplier in ba_suppliers:
            if invoice.lower().find(ba_supplier.lower()) >= 0 and invoice.split()[-1].split('.')[0][2:4] == first_month:
                shutil.move(path+"/"+invoice, os.path.expanduser(f"/Users/scott/Library/CloudStorage/OneDrive-Personal/Scott and Coco Pty Ltd/Invoices/{the_month[int(first_month)-1]} {currentYear}/CBA Business Account 5433/")+invoice)
            elif invoice.lower().find(ba_supplier.lower()) >= 0 and invoice.split()[-1].split('.')[0][2:4] == second_month:
                shutil.move(path+"/"+invoice, os.path.expanduser(f"/Users/scott/Library/CloudStorage/OneDrive-Personal/Scott and Coco Pty Ltd/Invoices/{the_month[int(second_month)-1]} {currentYear}/CBA Business Account 5433/")+invoice)
            elif invoice.lower().find(ba_supplier.lower()) >= 0 and invoice.split()[-1].split('.')[0][2:4] == third_month:
                shutil.move(path + "/" + invoice, os.path.expanduser(f"/Users/scott/Library/CloudStorage/OneDrive-Personal/Scott and Coco Pty Ltd/Invoices/{the_month[int(third_month)-1]} {currentYear}/CBA Business Account 5433/")+invoice)

    # paid by home loan account
    for invoice in invoices:
        for hl_supplier in hl_suppliers:
            if invoice.lower().find(hl_supplier.lower()) >= 0 and invoice.split()[-1].split('.')[0][2:4] == first_month:
                shutil.move(path+"/"+invoice, os.path.expanduser(f"/Users/scott/Library/CloudStorage/OneDrive-Personal/Scott and Coco Pty Ltd/Invoices/{the_month[int(first_month)-1]} {currentYear}/Westpac Home Loan 800269/")+invoice)
            elif invoice.lower().find(hl_supplier.lower()) >= 0 and invoice.split()[-1].split('.')[0][2:4] == second_month:
                shutil.move(path+"/"+invoice, os.path.expanduser(f"/Users/scott/Library/CloudStorage/OneDrive-Personal/Scott and Coco Pty Ltd/Invoices/{the_month[int(second_month)-1]} {currentYear}/Westpac Home Loan 800269/")+invoice)
            elif invoice.lower().find(hl_supplier.lower()) >= 0 and invoice.split()[-1].split('.')[0][2:4] == third_month:
                shutil.move(path + "/" + invoice, os.path.expanduser(f"/Users/scott/Library/CloudStorage/OneDrive-Personal/Scott and Coco Pty Ltd/Invoices/{the_month[int(third_month)-1]} {currentYear}/Westpac Home Loan 800269/")+invoice)
    print('Files moved to the folders.')


move_file()
