import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

customer_address = pd.read_csv(r'/Users/moosmacm1/Data_science/Code/GITHUB/GITHUB/Vitual_Intern/KPMG/Data/Raw/C_Customer_adress.csv', encoding='windows-1252')
customer_demographic = pd.read_csv(r'/Users/moosmacm1/Data_science/Code/GITHUB/GITHUB/Vitual_Intern/KPMG/Data/Raw/C_Customer_demographic.csv', encoding='windows-1252')
new_customer_list = pd.read_csv(r'/Users/moosmacm1/Data_science/Code/GITHUB/GITHUB/Vitual_Intern/KPMG/Data/Raw/C_New_customer_list.csv', encoding='windows-1252')
transaction = pd.read_csv(r'/Users/moosmacm1/Data_science/Code/GITHUB/GITHUB/Vitual_Intern/KPMG/Data/Raw/C_Transaction.csv', encoding='windows-1252')

data_list = [customer_address, customer_demographic, new_customer_list, transaction]
def basic_properties(data):
    print('head')
    for i in data:
        print('================== head of ======================================================')
        print(i.head())
        print('==================== end =====================================================')
    print('shape')
    for i in data:
        print(i.shape)


#** Customer address
customer_address_column = ['state', 'country', 'property_valuation']
def customer_address_count_plot(data):
    for i in data:
        sns.countplot(data=customer_address, x=i)
        plt.title(i)
        plt.show()
'''
There have some same data but use differences key words, which Victoria is VIC and New South Wales is NSW. These mistake have to be changed
'''
customer_address['state'] = customer_address['state'].replace({'New South Wales':'NSW', 'Victoria':'VIC'})      #OK
