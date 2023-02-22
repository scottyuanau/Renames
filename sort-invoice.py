from os.path import isfile, join
import os
import shutil
import pandas as pd


def move_file():
    """
    This function automatically reads Supplier-Payment-Method.xlsx from the same folder, and move
    all invoices in the specified path to the correct sub folders.

    Supplier-Payment-Method.xlsx has 2 columns, 1 is "Suppliers", another is "Payment Method". The
    current payment method is determined to "Credit Card Account", "Business Account"
    or "Home Loan Account".

    Add new lines if the supplier is not already pre-defined.

    Each reporting quarter are determined as: 1st Quarter: Jan - Mar, 2nd Quarter: Apr - Jun,
    3rd Quarter: Jul - Sep, 4th Quarter: Oct - Dec.
    """


    # function setup
    path = "/Users/scott/Library/CloudStorage/OneDrive-Personal/Scott and Coco Pty Ltd/Invoices/"
    supplier_file = 'Supplier-Payment-Method.xlsx'
    account_folders = ['Westpac Credit Card 0631',
                       'CBA Business Account 5433',
                       'Westpac Home Loan 800269']

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
    # initial setup for supplier payment methods
    default_df = pd.DataFrame(data=None, columns=['Suppliers', 'Payment Method'])

    if not os.path.exists(supplier_file):
        default_df.to_excel(supplier_file, index=False)
        print(f'Created {supplier_file}. Add entries to start.')

    df = pd.read_excel(supplier_file)

    credit_card_suppliers = df.loc[df['Payment Method'] == 'Credit Card Account']['Suppliers'].to_numpy().tolist()
    ba_suppliers = df.loc[df['Payment Method'] == 'Business Account']['Suppliers'].to_numpy().tolist()
    hl_suppliers = df.loc[df['Payment Method'] == 'Home Loan Account']['Suppliers'].to_numpy().tolist()
    all_suppliers = [*credit_card_suppliers, *ba_suppliers, *hl_suppliers]
    the_month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    invoices = [f for f in os.listdir(path) if isfile(join(path, f))]  # read invoices path
    # check if folder exists, if not, create the folder


    months = [first_month, second_month, third_month]
    folders = []
    for folder in account_folders:
        for month in months:
            folders.append(f"{path}{the_month[int(month) - 1]} {current_year}/{folder}/")

    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder) #make folder recursively
            print(f'Created Folder: {folder}')

    # move files
    for invoice in invoices:
        for credit_card_supplier in credit_card_suppliers:
            if ((invoice.lower().find(credit_card_supplier.lower()) >= 0 and invoice.split()[-1].split('.')[0][2:4]) == first_month) or ((invoice.lower().find(credit_card_supplier.lower()) >= 0 and invoice.split()[-2][2:4]) == first_month):
                shutil.move(path+"/"+invoice, os.path.expanduser(f"{path}{the_month[int(first_month)-1]} {current_year}/{account_folders[0]}/")+invoice)
            elif ((invoice.lower().find(credit_card_supplier.lower()) >= 0 and invoice.split()[-1].split('.')[0][2:4]) == second_month) or ((invoice.lower().find(credit_card_supplier.lower()) >= 0 and invoice.split()[-2][2:4]) == second_month):
                shutil.move(path+"/"+invoice, os.path.expanduser(f"{path}{the_month[int(second_month)-1]} {current_year}/{account_folders[0]}/")+invoice)
            elif ((invoice.lower().find(credit_card_supplier.lower()) >= 0 and invoice.split()[-1].split('.')[0][2:4]) == third_month) or ((invoice.lower().find(credit_card_supplier.lower()) >= 0 and invoice.split()[-2][2:4]) == third_month):
                shutil.move(path + "/" + invoice, os.path.expanduser(f"{path}{the_month[int(third_month)-1]} {current_year}/{account_folders[0]}/") + invoice)

    # paid by business bank account
        for ba_supplier in ba_suppliers:
            if ((invoice.lower().find(ba_supplier.lower()) >= 0 and invoice.split()[-1].split('.')[0][2:4]) == first_month) or ((invoice.lower().find(ba_supplier.lower()) >= 0 and invoice.split()[-2][2:4]) == first_month):
                shutil.move(path+"/"+invoice, os.path.expanduser(f"{path}{the_month[int(first_month)-1]} {current_year}/{account_folders[1]}/")+invoice)
            elif ((invoice.lower().find(ba_supplier.lower()) >= 0 and invoice.split()[-1].split('.')[0][2:4]) == second_month) or ((invoice.lower().find(ba_supplier.lower()) >= 0 and invoice.split()[-2][2:4]) == second_month):
                shutil.move(path+"/"+invoice, os.path.expanduser(f"{path}{the_month[int(second_month)-1]} {current_year}/{account_folders[1]}/")+invoice)
            elif ((invoice.lower().find(ba_supplier.lower()) >= 0 and invoice.split()[-1].split('.')[0][2:4]) == third_month) or ((invoice.lower().find(ba_supplier.lower()) >= 0 and invoice.split()[-2][2:4]) == third_month):
                shutil.move(path + "/" + invoice, os.path.expanduser(f"{path}{the_month[int(third_month)-1]} {current_year}/{account_folders[1]}/")+invoice)

    # paid by home loan account
        for hl_supplier in hl_suppliers:
            if ((invoice.lower().find(hl_supplier.lower()) >= 0 and invoice.split()[-1].split('.')[0][2:4]) == first_month) or ((invoice.lower().find(hl_supplier.lower()) >= 0 and invoice.split()[-2][2:4]) == first_month):
                shutil.move(path+"/"+invoice, os.path.expanduser(f"{path}{the_month[int(first_month)-1]} {current_year}/{account_folders[2]}/")+invoice)
            elif ((invoice.lower().find(hl_supplier.lower()) >= 0 and invoice.split()[-1].split('.')[0][2:4]) == second_month) or ((invoice.lower().find(hl_supplier.lower()) >= 0 and invoice.split()[-2][2:4]) == second_month):
                shutil.move(path+"/"+invoice, os.path.expanduser(f"{path}{the_month[int(second_month)-1]} {current_year}/{account_folders[2]}/")+invoice)
            elif ((invoice.lower().find(hl_supplier.lower()) >= 0 and invoice.split()[-1].split('.')[0][2:4]) == third_month) or ((invoice.lower().find(hl_supplier.lower()) >= 0 and invoice.split()[-2][2:4]) == third_month):
                shutil.move(path + "/" + invoice, os.path.expanduser(f"{path}{the_month[int(third_month)-1]} {current_year}/{account_folders[2]}/")+invoice)

    print('Files moved to the folders.')

    # check if there are any files not being moved to the folder
    invoices = [f for f in os.listdir(path) if isfile(join(path, f))]
    for invoice in invoices:
        if invoice.split()[0] not in all_suppliers and invoice.split()[0] != '.DS_Store':
            print(f'\033[93m"{invoice.split()[0]}" Not Found. Please specify in {supplier_file}.\033[93m')


if __name__ == '__main__':
    move_file()
