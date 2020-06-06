
'''
File Name:                 Shaik.Shabana.Assignment-10.py
Name:	                   Shabana Shaik
Date: 	   				   06/05/2020 	      
Course:                    Python Programming ICT – 4370

Description: Reading the Stock Info from a JSON file and plot the graph 
based on certain time period and the closing price using matplotlib.
Additioinally, plotting a histogram using the same stock information. 
'''

#Importing json and matplotlib

import json
import matplotlib.pyplot as plt

#Empty dictionary to store the data
stocks = {} 

#Extracting Input from the json file
file = "AllStocks.json"

with open(file) as f:
    stocks = json.load(f) #loaded data into the stocks dictionary
    
#print(stocks)

#Creating the dates and closing prices list for each type of stock

#AIG
aig_dates = []
aig_prices = []
for i in stocks:
    if i['Symbol']=='AIG':
        aig_dates.append(i['Date'])
        aig_prices.append(i['Close'])

#Rearranging the dates from oldest to newest:        
aig_dates = aig_dates[::-1]      
aig_prices = aig_prices[::-1]
        
#F        
F_dates = []
F_prices = []
for i in stocks:
    if i['Symbol']=='F':
        F_dates.append(i['Date'])
        F_prices.append(i['Close'])  
        
F_dates = F_dates[::-1]      
F_prices = F_prices[::-1]


#FB        
FB_dates = []
FB_prices = []
for i in stocks:
    if i['Symbol']=='FB':
        FB_dates.append(i['Date'])
        FB_prices.append(i['Close'])
        
FB_dates = FB_dates[::-1]      
FB_prices = FB_prices[::-1]

#GOOG
GOOG_dates = []
GOOG_prices = []
for i in stocks:
    if i['Symbol']=='GOOG':
        GOOG_dates.append(i['Date'])
        GOOG_prices.append(i['Close'])
        
GOOG_dates = GOOG_dates[::-1]      
GOOG_prices = GOOG_prices[::-1]

#IBM      
IBM_dates = []
IBM_prices = []
for i in stocks:
    if i['Symbol']=='IBM':
        IBM_dates.append(i['Date'])
        IBM_prices.append(i['Close'])
        
IBM_dates = IBM_dates[::-1]      
IBM_prices = IBM_prices[::-1]

#M
M_dates = []
M_prices = []
for i in stocks:
    if i['Symbol']=='M':
        M_dates.append(i['Date'])
        M_prices.append(i['Close'])
        
M_dates = M_dates[::-1]      
M_prices = M_prices[::-1]

#MSFT        
MSFT_dates = []
MSFT_prices = []
for i in stocks:
    if i['Symbol']=='MSFT':
        MSFT_dates.append(i['Date'])
        MSFT_prices.append(i['Close'])
        
MSFT_dates = MSFT_dates[::-1]      
MSFT_prices = MSFT_prices[::-1]

#RDSA        
RDSA_dates = []
RDSA_prices = []
for i in stocks:
    if i['Symbol']=='RDS-A':
        RDSA_dates.append(i['Date'])
        RDSA_prices.append(i['Close'])
        
RDSA_dates = RDSA_dates[::-1]      
RDSA_prices = RDSA_prices[::-1]

#print(len(GOOG_dates)) #507

#Just creating dates to show in the Figure
 #taking only few dates
dates = [GOOG_dates[0], GOOG_dates[50], GOOG_dates[100], GOOG_dates[150],
GOOG_dates[200], GOOG_dates[250], GOOG_dates[300], GOOG_dates[350],
GOOG_dates[400],GOOG_dates[450],GOOG_dates[-1]]

#Set the size of the rc parameters
plt.rcParams["figure.figsize"] = (10,3)

#set chart title and label axes

plt.title("Historical Stock Data")

plt.xlabel('Stock Valuation Dates')

plt.ylabel('Stock Closing Prices in Dollars')

plt.plot(aig_dates, aig_prices, label="AIG")

plt.plot(F_dates, F_prices, label="F")

plt.plot(FB_dates, FB_prices, label="FB")

plt.plot(GOOG_dates, GOOG_prices,label="GOOG")

plt.plot(IBM_dates, IBM_prices,label="IBM")

plt.plot(M_dates, M_prices,label="M")

plt.plot(MSFT_dates, MSFT_prices,label="MSFT")

plt.plot(RDSA_dates, RDSA_prices, label="RDSA")

#Styling the tick parameters
plt.xticks(dates, rotation=45) 

#To display individual labels
plt.legend()

#Displays the plot
#plt.show()

#To save the plt to a file
plt.savefig('Shaik.Shabana.Assignment-8.png', bbox_inches = 'tight')



#######################################################################
#Here starts the additional(Assignment-10 work) added code to create the 
#Stocks histogram for the data taken from the JSON file

# taking all the dates and closing prices:
data =[]
for i in stocks:
    data.append([i['Date'], i['Close']])  
data = data[::-1]

#taking only dates:
date = []
for i in data:
    date.append(i[0])

#for every unique date creating an empty list to sotre the prices
dc=[]
for i in date:
    for j in data:
        if i == j[0]:
            dc.append([i,[]])

#adding the price values to respective dates
for i in dc:
    for j in data:
        if i[0]== j[0]:
            i[1].append(j[1])
            
#taking only unique dates
final_list = []
for i in dc:
    if i not in final_list:
        final_list.append(i)

#separating dates and costs to lists:
final_dates = []
final_costs = []
for i in final_list:
    final_dates.append(i[0])
    final_costs.append(int(sum(i[1])))

#Histogram of Portfolio by Date and total value

#Set the size of the parameters

fig = plt.figure(figsize=(10, 6))

#ax is the Axes instance to plot
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

#set chart title and label axes

plt.title("Histogram of Date vs Total Value")

plt.xlabel('Dates')

plt.ylabel('Total value in Dollars')

#plotting histogram
plt.hist(final_costs)

#Styling the tick parameters
ax.set_xticklabels(dates, rotation=45)

plt.show()
#plt.savefig('Shaik.Shabana.Assignment-10.png')

