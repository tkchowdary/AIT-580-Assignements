###################
#Data set Exploration



import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

f=pd.read_csv("/Users/tharun/Atlantic.csv",sep=',') #read dataset
print(f) 



###########################################
print (f['year'].describe()) #summary of year

f['year'].plot(kind='hist',bins=50) #visualisation of year


##############################################
print (f['cyclone_of_the_year'].describe()) #Summary of cyclone of year


f['cyclone_of_the_year'].plot(kind='hist',bins=50)




##################################################################

##############################################
print (f['date'].describe())  #summary of date

f['date'].plot(kind='hist',bins=50)#visualisation of date




############################################
print (f['time'].describe())  #summary of time
plt.boxplot(f['time'])#visualisation of time 
plt.show()



#####################################################
x = Counter(list(f['status_of_system'])).items()

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = tuple([_[0] for _ in x])
y_pos = np.arange(len(objects))
performance = [_[1] for _ in x]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('count')
plt.title('status of the system')

plt.show()



##################################################
print (f['longitude'].describe()) #summary of longitude





###############################################
print (f['latitude'].describe())
                                    #summary of latitude.
                                    
                                    
                                    
                                    

#################################################

print (f['max_sustained_wind'].describe()) #Summary of max_sustained_wind

f['max_sustained_wind'].plot(kind='hist',bins=20)
 #visualisation of max_sustained_wind



##################################################
print (f['central_pressure'].describe()) #Summary of central pressure

f['central_pressure'].plot(kind='hist',bins=50) #visulisation of pressure.



#################################################







###############################################################################
#b)

#Correlation between central pressure and max_sustained_wind

f['central_pressure'].corr(f['max_sustained_wind'])
pd.DataFrame(f['year']).plot(kind='kde',title="Year")

#correlation between status of system and max sustained wind

plt.scatter(f['central_pressure'],f['max_sustained_wind'])




############################################################################
#c)

#c)
 #Explain how you accounted for any missing data, and how that may have affected your results
#to find missing data in a column


import pandas as pd
f=pd.read_csv("/Users/tharun/Atlantic.csv",sep=',') #read dataset
f['central_pressure'].isnull()
f.isnull().sum().sum()
f['central_pressure']
mean=f['central_pressure'].mean()
f['central_pressure'].fillna(mean,inplace=True)

#visulisation
f['central_pressure'].plot(kind='hist',bins=50)


##############################################################################
#create a csv dataset
#encoding='utf8'

import requests
import pandas as pd
from bs4 import BeautifulSoup #import BeautifulSoup

import sys
reload(sys)
sys.setdefaultencoding('utf8')

page1_url = ["https://top500.org/list/2019/06/?page=1", "https://top500.org/list/2019/06/?page=2",
             "https://top500.org/list/2019/06/?page=3", "https://top500.org/list/2019/06/?page=4",
             "https://top500.org/list/2019/06/?page=5"]

data = []
for i in range(5):
    page = []

    req = requests.get(page1_url[i])
    soup = BeautifulSoup(req.content, 'html.parser')
    for row in soup.table.contents:
        pg = []
        if type(row).__name__ == 'Tag':
            for cell in row:
                if type(cell).__name__ == 'Tag':
                    pg.append(cell.get_text())
            page.append(pg)
    page.pop(0)
    data.extend(page)
df = pd.DataFrame(data)
df.to_csv("./Top500.csv", index=False)


########################################################################
#Clean & explore the dataset, producing summary statistics
   #and visualizations for Cores, RMax, RPeak, and Power.

import numpy as np
import matplotlib.pyplot as plt
import re
import pandas as pd



def main():
    # ['Rank', 'Site', 'System', 'Cores', 'Rmax', 'Rpeak', 'Power']
    df = pd.read_csv('./Top500.csv')
    print()

    df['3'] = df['3'].apply(lambda x: int(re.sub('[\n, ]', '', x)))
    df['4'] = df['4'].apply(lambda x: float(re.sub('[\n, ]', '', x)))
    df['5'] = df['5'].apply(lambda x: float(re.sub('[\n, ]', '', x)))
    df['6'] = df['6'].apply(lambda x: x if type(x).__name__ == 'float' else int(re.sub('[\n, ]', '', x)))
    line1, = plt.plot(df['3'])
    line2, = plt.plot(df['4'])
    line3, = plt.plot(df['5'])
    line4, = plt.plot(df['6'])
    plt.legend([line1, line2, line3, line4], ['3', '4', '5', '6'])

    plt.show()


if __name__ == "__main__":
    main()


##########################################################################################
#Display and explain the relationship between Cores and RPeak,
   #and Cores and Power. Consider transforming the data to reduce 
   #the range of the data values.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re


def main():
    df = pd.read_csv('./Top500.csv')
    df['3'] = df['3'].apply(lambda x: int(re.sub('[\n, ]', '', x)))
    df['4'] = df['4'].apply(lambda x: float(re.sub('[\n, ]', '', x)))
    df['5'] = df['5'].apply(lambda x: float(re.sub('[\n, ]', '', x)))
    df['6'] = df['6'].apply(lambda x: x if type(x).__name__ == 'float' else int(re.sub('[\n, ]', '', x)))

    df.sort_values(by='5')
    plt.plot(df['5'], df['3'])

    df.sort_values(by='6')
    plt.plot(df['6'], df['3'])

    plt.show()


if __name__ == "__main__":
    main()

