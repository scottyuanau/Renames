from os.path import isfile, join
import os
import shutil
import pandas as pd


def move_file():
    path = "/Users/scott/OneDrive/Scott and Coco Pty Ltd/Invoices/"
    supplier_file = 'Supplier-Payment-Method.xlsx'


    # basic configuration
    quarter = input('What is the quarter? e.g. q1, q2, q3, q4\n')
    match quarter.lower():
        case 'q1':
            first_month = '01'
            second_month = '02'
            third_month = '03'
        case 'q2':
            first_month = '04'
            second_month = '05'
            third_month = '06'
        case 'q3':
            first_month = '07'
            second_month = '08'
            third_month = '09'
        case 'q4':
            first_month = '10'
            second_month = '11'
            third_month = '12'

    current_year = input('What is the year?e.g. 2023\n')  # year
    #inital setup for supplier payment methods
    if not os.path.exists(supplier_file):
        print('Please create "Supplier-Payment-Method.xlsx" and put inside the folder.')
    df = pd.read_excel(supplier_file)

    credit_card_suppliers = df.loc[df['Payment Method'] == 'Credit Card Account']['Suppliers'].to_numpy().tolist()
    ba_suppliers = df.loc[df['Payment Method'] == 'Business Account']['Suppliers'].to_numpy().tolist()
    hl_suppliers = df.loc[df['Payment Method'] == 'Home Loan Account']['Suppliers'].to_numpy().tolist()
    all_suppliers = [*credit_card_suppliers, *ba_suppliers, *hl_suppliers]
    the_month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    invoices = [f for f in os.listdir(path) if isfile(join(path, f))]  # read invoices path
    #check if folder exists, if not, create the folder
    folder_path = "/Users/scott/Library/CloudStorage/OneDrive-Personal/Scott and Coco Pty Ltd/Invoices"
    folder1 = f"{folder_path}/{the_month[int(first_month) - 1]} {current_year}/Westpac Credit Card 0631/"
    folder2 = f"{folder_path}/{the_month[int(second_month) - 1]} {current_year}/Westpac Credit Card 0631/"
    folder3 = f"{folder_path}/{the_month[int(third_month) - 1]} {current_year}/Westpac Credit Card 0631/"
    folder4 = f"{folder_path}/{the_month[int(first_month) - 1]} {current_year}/CBA Business Account 5433/"
    folder5 = f"{folder_path}/{the_month[int(second_month) - 1]} {current_year}/CBA Business Account 5433/"
    folder6 = f"{folder_path}/{the_month[int(third_month) - 1]} {current_year}/CBA Business Account 5433/"
    folder7 = f"{folder_path}/{the_month[int(first_month) - 1]} {current_year}/Westpac Home Loan 800269/"
    folder8 = f"{folder_path}/{the_month[int(second_month) - 1]} {current_year}/Westpac Home Loan 800269/"
    folder9 = f"{folder_path}/{the_month[int(third_month) - 1]} {current_year}/Westpac Home Loan 800269/"
    folders = [folder1, folder2, folder3, folder4, folder5, folder6, folder7, folder8, folder9]
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder) #make folder recursively
            print(f'Created Folder: {folder}')

    #move files
    missing_suppliers = []
    for invoice in invoices:
        for credit_card_supplier in credit_card_suppliers:
            if (invoice.lower().find(credit_card_supplier.lower()) >= 0 and invoice.split()[-1].split('.')[0][2:4]) or (invoice.lower().find(credit_card_supplier.lower()) >= 0 and invoice.split()[-2][2:4]) == first_month:
                shutil.move(path+"/"+invoice, os.path.expanduser(f"{folder_path}/{the_month[int(first_month)-1]} {current_year}/Westpac Credit Card 0631/")+invoice)
            elif (invoice.lower().find(credit_card_supplier.lower()) >= 0 and invoice.split()[-1].split('.')[0][2:4]) or (invoice.lower().find(credit_card_supplier.lower()) >= 0 and invoice.split()[-2][2:4]) == second_month:
                shutil.move(path+"/"+invoice, os.path.expanduser(f"{folder_path}/{the_month[int(second_month)-1]} {current_year}/Westpac Credit Card 0631/")+invoice)
            elif (invoice.lower().find(credit_card_supplier.lower()) >= 0 and invoice.split()[-1].split('.')[0][2:4]) or (invoice.lower().find(credit_card_supplier.lower()) >= 0 and invoice.split()[-2][2:4]) == third_month:
                shutil.move(path + "/" + invoice, os.path.expanduser(f"{folder_path}/{the_month[int(third_month)-1]} {current_year}/Westpac Credit Card 0631/") + invoice)

    # paid by business bank account
        for ba_supplier in ba_suppliers:
            if (invoice.lower().find(ba_supplier.lower()) >= 0 and invoice.split()[-1].split('.')[0][2:4]) or (invoice.lower().find(ba_supplier.lower()) >= 0 and invoice.split()[-2][2:4]) == first_month:
                shutil.move(path+"/"+invoice, os.path.expanduser(f"{folder_path}/{the_month[int(first_month)-1]} {current_year}/CBA Business Account 5433/")+invoice)
            elif (invoice.lower().find(ba_supplier.lower()) >= 0 and invoice.split()[-1].split('.')[0][2:4]) or (invoice.lower().find(ba_supplier.lower()) >= 0 and invoice.split()[-2][2:4]) == second_month:
                shutil.move(path+"/"+invoice, os.path.expanduser(f"{folder_path}/{the_month[int(second_month)-1]} {current_year}/CBA Business Account 5433/")+invoice)
            elif (invoice.lower().find(ba_supplier.lower()) >= 0 and invoice.split()[-1].split('.')[0][2:4]) or (invoice.lower().find(ba_supplier.lower()) >= 0 and invoice.split()[-2][2:4]) == third_month:
                shutil.move(path + "/" + invoice, os.path.expanduser(f"{folder_path}/{the_month[int(third_month)-1]} {current_year}/CBA Business Account 5433/")+invoice)

    # paid by home loan account
        for hl_supplier in hl_suppliers:
            if (invoice.lower().find(hl_supplier.lower()) >= 0 and invoice.split()[-1].split('.')[0][2:4]) or (invoice.lower().find(hl_supplier.lower()) >= 0 and invoice.split()[-2][2:4]) == first_month:
                shutil.move(path+"/"+invoice, os.path.expanduser(f"{folder_path}/{the_month[int(first_month)-1]} {current_year}/Westpac Home Loan 800269/")+invoice)
            elif (invoice.lower().find(hl_supplier.lower()) >= 0 and invoice.split()[-1].split('.')[0][2:4]) or (invoice.lower().find(hl_supplier.lower()) >= 0 and invoice.split()[-2][2:4]) == second_month:
                shutil.move(path+"/"+invoice, os.path.expanduser(f"{folder_path}/{the_month[int(second_month)-1]} {current_year}/Westpac Home Loan 800269/")+invoice)
            elif (invoice.lower().find(hl_supplier.lower()) >= 0 and invoice.split()[-1].split('.')[0][2:4]) or (invoice.lower().find(hl_supplier.lower()) >= 0 and invoice.split()[-2][2:4]) == third_month:
                shutil.move(path + "/" + invoice, os.path.expanduser(f"{folder_path}/{the_month[int(third_month)-1]} {current_year}/Westpac Home Loan 800269/")+invoice)

    #check if all suppliers have been indicated
        for supplier in all_suppliers:
            if invoice.lower().find(supplier.lower()) == -1 and invoice.split()[0] not in missing_suppliers and invoice != '.DS_Store':
                missing_suppliers.append(invoice.split()[0])
                print(f'"{invoice.split()[0]}" has not been specified, please modify in {supplier_file}.')
    print('Files moved to the folders.')



if __name__ == '__main__':
    move_file()
