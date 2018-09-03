
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


#diffrent ways to create a series
   
        #creating array by using scalar values 
    
series = pd.Series([89,234,567,888],[1,2,3,4])

print("\n values in series with their index number : \n",series)


        #creating series by using numppy array

array = np.arange(200,220,5)

index = [100,101,102,103]

series = pd.Series(array,index) #series will be created with numpy array passed as data into series to create it.
                                # index is a list which is passed as index for series

print("\n values in series with their index number : \n",series)

        #creating series by using dictionary


dictionary = {"john":450,"smith":200,"bob":400,"david":460}

series = pd.Series(dictionary)

print("\n values in series with their index number : \n",series)

print("\n value in series who's index is 'smith' = ",series["smith"])

print("\n value at 3 location in series : ",series[2]) #location begins at 0

print("\n last two elements in series : \n",series[-2:])


# In[3]:


#diffrent ways to create a data frame
       
        #simple way to create a data frame 
    
dframe = pd.DataFrame([['joe root',890],['ian bell',706],['sam billings',540],['josh buttler',600]],[1,2,3,4],['name','marks'])

print("\n elements in data frame : \n",dframe)  #name and marks are column name
         
        #creating data frame by using list 

data = [['steve smith',587],['david warner',894],['michel johnson',468],['mitchel stark',569]]

index = [10,11,12,13]

columns = ['Student Name','marks']

dframe = pd.DataFrame(data,index,columns)

print("\n elements in data frame : \n",dframe)


       #creating data frame by using dictionary
    
datadict = {'name of students':['chris woakes','jack ball','greame smith'],'marks of students':[581,862,785]}

index = [110,112,114]

dframe = pd.DataFrame(datadict,index)

print("\n elements in data frame : \n",dframe)

        #creating data frame by using dictionary of series
    
series_one = pd.Series([90,43,54],[100,101,102])
series_two = pd.Series([56,54,23,65],[100,101,102,103])
    
datadict = {"column_one":series_one,"column_two":series_two}

dframe = pd.DataFrame(datadict)

print("\n elements in data frame : \n",dframe)

print("\n elements at column_one : \n",dframe['column_one'])

print("\n value at column_two who's index number is 101 : ",dframe['column_two'][101])

        #adding new column in data frame 
    
series_three = pd.Series([64,79,28,45,24],[100,101,102,104,105])    
    
dframe['column_three'] = series_three

print("\n new column 'column_three' is added at data frame : \n",dframe)

dframe['column_four'] = dframe['column_one']*dframe['column_two']

print("\n new column 'column_four' is added at data frame : \n",dframe)


        #delete column from data frame
    
del dframe['column_four'] 

print("\n data frame after deletion of 'column_four' : \n",dframe)

dframe.pop('column_three') #pop() can also delete column from data frame

print("\n data frame after deletion of 'column_three' by using pop() : \n",dframe)

    #diffrent ways to access row of data frame
    
print("\n elements at row = 102 in data frame : \n",dframe.loc[102]) #loc() is used to get row from data frame

print("\n elemets at second row in data frame : \n",dframe.iloc[1]) #Row selected by passing integer location to an iloc()

print("\n rows from second to last in data frame : \n",dframe[1:]) #multiple rows selection

print("\n rows from first to third in data frame : \n",dframe[0:2])

    #adding a new row in data frame

data= [[45,56],[67,78]]
index = [104,105]

new_row = pd.DataFrame(data,index,columns=['column_one','column_two'])

dframe = dframe.append(new_row)

print("\n data frame after adding two new rows : \n",dframe)

    #delete row from data frame
    
dframe = dframe.drop(105)

print("\n data frame after deletion of row who's index is 105 : \n",dframe)


# In[4]:


#Series basic functionlities
        #axes

series = pd.Series(data=[93,34,44,64],index=[100,200,300,400])

print("\n elements in series : \n",series)

print("\n Index numbers of each row of series : \n",series.axes) 

        #empty
    
print("\n Series is empty ? ",series.empty) #returns true if series is empty and false if not empty

        #dtype

print("\n data type : ",series.dtype) #returns data type of series

        #size

print("\n size of series : ",series.size) #returns the total number of elements in series as size of series

        #values
    
print("\n all values in series : \n",series.values) #this will return all the values of series

        #head
    
print("\n first two rows in series : \n",series.head(2)) 

        #tail

print("\n last two rows in series : \n",series.tail(2))

        #


# In[5]:


#data frame basic functionalities

data = [["joe root",799],["steve smith",892],["greame swan",630],["Ian bell",893]]
    
index = [11,12,13,14]

columns = ['student_name','student_marks']

dframe = pd.DataFrame(data,index,columns)

print("\n Data Frame : \n",dframe)

                #axes
    
print("\n axes of data frame  : \n ",dframe.axes)

                #transpose (T)

print("\n Transpose of data frame : \n",dframe.T)

                #shape
    
print("\n shape of data frame : ",dframe.shape)

                #size

print("\n size of data frame : ",dframe.size) 

                #values

print("\n vlaues in data frame : \n",dframe.values)

                #head
    
print("\n first two rows in data frame : \n",dframe.head(2))

                #tail

print("\n last two rows in data frame : \n",dframe.tail(2))


# In[6]:


#Descriptive Statistics
    
datadict = {'name':['john','ajit','ajay','shahid','virat','amir','sachin','imran','irfan','yusuf'],
           'salary':[2000,4500,8000,4520,5550,4000,5780,8880,5000,2030],
           'age':[21,43,42,25,27,19,20,21,26,27]}

dframe = pd.DataFrame(datadict)

print(dframe)
                #sum()
    
print("\n sum at axis = 0 : \n\n",dframe.sum()) #by default axis is 0

print("\n sum at axis = 1 : \n\n",dframe.sum(1))

                #max() and min()
    
print("\n minimum values in each columns of data frame : \n",dframe.min())

print("\n maximum values in each columns of data frame : \n",dframe.max())

                #describe()

print("\n description of complete data frame : \n\n",dframe.describe(include='all'))

print("\n description of string columns of data frame : \n\n",dframe.describe(include=['object']))

print("\n description of numericle columns of data frame : \n\n",dframe.describe(include=['number']))


# In[7]:


print("\n data frame : \n\n",dframe)               
    
                #std()

print("\n standard deviation of numericle columns : \n",dframe.std())

                #mean()
    
print("\n mean of numericle columns of our data frame : \n",dframe.mean())

                #median()
    
print("\n median of numericle columns of our data frame : \n",dframe.median())

                #mode()

print("\n product of numericle columns of our data frame : \n",dframe.prod())

                #cumsum()
    
print("\n cumulative sum of our data frame : \n",dframe.cumsum())


# In[8]:


#reindexing

datadict= {'name':['ms dhoni','virat kohli','rahul dravid','anil kumble'],'marks':[899,567,861,379]}

dframe = pd.DataFrame(datadict)

print("data frame :\n",dframe)

dframe= dframe.reindex(index=[2,1,3,0])

print("\n data frame after reindexing index numbers : \n",dframe)

dframe = dframe.reindex(index=[0,1,2,3],columns=['marks','name'])

print("\n data frame after reindexing index numbers and column names : \n",dframe)

dframe = dframe.reindex(columns=['name','marks','result'])

print("\n data frame after adding new column 'result' and reindexing index numbers again : \n",dframe)

datadict = {'name':['sachin tendulkar','sourav ganguly'],'marks':[689,369],'result':['paas','fail']}

new_dframe = pd.DataFrame(datadict)

print("\n new data frame : \n",new_dframe)


print("\n data frame after reindexing it according to the indices of new data frame : \n",dframe.reindex_like(new_dframe))
                                #it will print index 0 and 1 
                                #because index 0 and 1 are matching in both data frames
    
    
                              #methods used with reindex_like()

print("\n our first data frame : \n",dframe)

print("\n our second data frame : \n",new_dframe)

print("\n\n",new_dframe.reindex_like(dframe))

print("\n reindexing second data frame like first data frame by using method = 'ffill' : \n",new_dframe.reindex_like(dframe,method='ffill')) #method='pad' works same

print("\n reindexing second data frame like first data frame by using method = 'ffill' : and limit = 1 \n",new_dframe.reindex_like(dframe,method='ffill',limit=1))

print("\nreindexing second data frame like first data frame by using method = 'backfill' : \n",new_dframe.reindex_like(dframe,method='backfill')) #method = 'bfill' works same

print("\nreindexing second data frame like first data frame by using method = 'nearest' : \n",new_dframe.reindex_like(dframe,method='nearest'))

                            #renaming column names

print("\n data frame after renaming column 'name' to 'student_name' and 'marks' to 'total_marks' : \n",dframe.rename(columns={'name':'student_name','marks':'total_marks'}))


# In[9]:


#Iteration

datadict={'name':['rickey ponting','steve smith','steve waugh','alen border'],
         'salary':[4500,3000,4900,5000]}

dframe = pd.DataFrame(datadict)

series = pd.Series(data=[4500,3000,4900,5000])    

print("\n our data frame is : \n",dframe)

print("\n our series is : \n",series)

print("\n")

for x in dframe :  #if it's data frame then column names will be iterated
    print("column name in our data frame : ",x)
    
print("\n")

for x in series : #if it's series then values will be iterated
    print("values in our data frame : ",x)

                #iteritems()

for keys,values in dframe.iteritems() :          #itereate on series
    print("\nkey in our data frame : ",keys)
    print("values at ",keys," in our data frame : \n",values)
    
for keys,values in series.iteritems() :          #itereate on series
    print("\nkey in our series : ",keys)
    print("values at ",keys," in our series : \n",values)

                #iterrows()
    
for row_index,row in dframe.iterrows() :          #itereate on data frame
    print("\n row_index in our series : ",row_index)
    print("row at ",row_index," in our series : \n",row)
    
                #itertuples()

print("\n\n")        
        
for row in dframe.itertuples() :
    print(row)
                


# In[10]:


#sorting()

datadict = {'name':['steve smith','steve waugh','ian chappel','bob willis'],'marks':[456,412,300,538]}

dframe = pd.DataFrame(datadict,index=[3,4,1,2])

print("\n our data frame is : \n",dframe)

                    #sorting index numbers

print("\n data frame after sorting index numbers : \n",dframe.sort_index()) #by default it will sort in ascending order

print("\n data frame after sorting index numbers in descending order : \n",dframe.sort_index(ascending=False))
                                        
                    #sorting columns
        
print("\n data frame sort along axis = 1 : \n",dframe.sort_index(axis=1)) #by default axis = 0

                    #sorting values
    
print("\n sorting data frame by column 'marks' : \n",dframe.sort_values(by='marks'))

print("\n sorting data frame in descending order by column 'marks' : \n",dframe.sort_values(by='marks',ascending=False))

print("\n sorting data frame by column 'name' : \n",dframe.sort_values(by='name'))

print("\n sorting data frame in descending order by column 'name' : \n",dframe.sort_values(by='name',ascending=False))
    
print("\n sorting data frame by column 'marks' by using 'mergesort' : \n",dframe.sort_values(by='marks',kind='mergesort'))

print("\n sorting data frame by column 'marks' by using 'heapsort' : \n",dframe.sort_values(by='marks',kind='heapsort'))

print("\n sorting data frame by column 'marks' by using 'quicksort' : \n",dframe.sort_values(by='marks',kind='quicksort'))


# In[11]:


#string functions
    
series = pd.Series(['MS Dhoni','Virat Kohli','Ravi Ashwin','Yuvraj Singh'])

print("our series is : \n",series)

                    #lower()

print("\n all string values of series in lower case : \n",series.str.lower())

                    #upper
    
print("\n all string values of series in lower case : \n",series.str.upper())

                    #len()
    
print("\n length of each string in series : \n",series.str.len())

                    #cat(sep=)
    
print("\n string of series sepreted by ',' : ",series.str.cat(sep=','))
print("\n string of series sepreted by '_' : ",series.str.cat(sep='_'))
print("\n string of series sepreted by '*' : ",series.str.cat(sep='*'))

                    #get_dummies()

print("\n",series.str.get_dummies())  #returns a data frame with dummy values
    
                    #replace()
        
print("\n in each string 'i' is replaced with Q : \n",series.str.replace('i','Q'))
    
                    #repeat()

print("\n each string is repeated 4 times : \n",series.str.repeat(4))
    
                    #count()
        
print("\n number of times 'i' appeared in strings : \n",series.str.count('i'))
                    
                    #startswith()

print("\n true if string starts with 'v' : \n",series.str.startswith('V'))
    
                    #endswith()

print("\n true if string ends with 'i' :\n",series.str.endswith('i'))
    
                    #find()
        
print("\n first possition of the occurrence of 'a' in string : \n",series.str.find('a'))
                # -1 if specifies character not occured
                    
                   #findall()
        
print("\n all occurrences of 'a' in string : \n",series.str.findall('a')) 
                # -1 if specifies character not occured
                        
    
                    #swapcase()
        
print("\n all lower case has changed into upper case and upper case has changed into lower case : \n",series.str.swapcase())        
    

                    #contains(pattern)
        
series = pd.Series(['MS_Dhoni','Virat_Kohli','Ravi Ashwin','Yuvraj Singh'])        

print("\n",series.str.contains('_')) #returns true if string contains specified pattern
     #in our case pattern is '_'
    
                    


# In[12]:


#options and customization
    
print("\n default maximum rows : ",pd.get_option('display.max_rows')) #60 is default value

pd.set_option('display.max_rows',100) #this will change default maximum rows value to 100

print("\n maximum rows after changing : ",pd.get_option('display.max_rows'))

pd.reset_option('display.max_rows') #now maximum rows value is change back to default value which is 60

print("\n maximum rows after reset : ",pd.get_option('display.max_rows'))


print("\n default maximum columns : ",pd.get_option('display.max_columns')) #default maximum column is 60

pd.get_option('display.max_columns',35) 

print("\n maximum columns after changing : ",pd.get_option('display.max_columns',35))

pd.reset_option('display.max_columns')

print("\n maximum columns after reset : ",pd.get_option('display.max_columns'))

print("\n\n\n",pd.describe_option('display.max_rows'))

print("\n\n\n",pd.describe_option('display.max_columns'))


# In[13]:


#Indexing and Selecting Data
    
                #loc() #used for lable based indexing

datadict = {"name":['john smith','stephen hawkins','joe root','shahid afridi','ms dhoni']
           ,"salary":[13000,56000,32000,58000,20400]
           ,"department":['sales','marketing','marketing','sales','testing']}

index = [100,102,104,105,106]

dframe = pd.DataFrame(datadict,index)

print("\n our data frame : \n",dframe)

print("\n selecting all rows of column 'salary' : \n",dframe.loc[:,'salary'])

print("\n selecting all rows of coumn 'name' and 'department' : \n",dframe.loc[:,['name','department']])

#print("\n selecting rows from index 102 to index 105 of column 'name' : \n",dframe.loc[[102,103,104,105],['name']])
                        #this will generate warning
    
print("\n selecting rows from index 102 to index 105 of all coulmns : \n",dframe.loc[102:105]) 


                #iloc() #used for integer based indexing
    
print("\n second element in data frame(index begins with 0) : \n",dframe.iloc[1])

print("\n last two elements in data frame : \n",dframe.iloc[-2:])

print("\n first three elements in data frame : \n",dframe.iloc[:3])

print("\n elements from second to fourth in data frame(index begins with 0) : \n",dframe.iloc[1:4])

            #ix() #can be used for both label based and integer based indexing

#print("\n elements in column 'name' : \n",dframe.ix[:,'name']) #this wiil generate a warning which say
                        #.ix is deprecated. Please use
                        #.loc for label based indexing or
                        #.iloc for positional indexing

          #other ways to access data frame
        
print("\n all values in column 'salary' :\n",dframe['salary'])

print("\n all values in columns 'salary' and 'name' : \n",dframe[['salary','name']])

print("\n all values in column 'salary' : \n",dframe.salary)


# In[14]:


#Statistical Functions
    

        
                                    #pct_change() percentage change
    
series = pd.Series([10,20,30,80])

print("\n our series : \n",series)

print("\n precentage change in series : \n",series.pct_change()) # (20-10 = 10/10=1) (30-20=10/20=0.5) (80-30=50/30=1.666667)

datadict = {"salary":[3000,5000,6000,2000],"bonus":[500,1000,200,7000]}

dframe = pd.DataFrame(datadict)

print("\n our data frame : \n",dframe)

print("\n percentage change column wist (at axis = 0) in data frame : \n",dframe.pct_change()) 
#('salary' : (5000-3000=2000/3000=0.666667)(6000-5000=1000/5000=0.200000) (2000-6000= -4000/6000=-0.666667))
#('bonus': (1000-500=500/500=1.0) (200-1000= -800/1000= -0.8) (7000-200= 6800/200= 34.0))
    
print("\n percantage change row wise (at axis = 1) in data frame : \n",dframe.pct_change(axis=1))

#(500-3000= -2500/3000 = -0.833333) (1000-5000= -4000/5000 = -0.800000) (200-6000= -5800/6000= -0.966667)
#(7000-2000 = 5000/2000 = 2.500000)


#cov() covariance
        
series_one = pd.Series([60,500,400,700])
series_two = pd.Series([300,320,456])

print("\n seires_one : \n",series_one)
print("\n series_two : \n",series_two)

print("\n covariance of series_one and series_two : ",series_one.cov(series_two))

print("\n covarince in data frame : \n",dframe.cov())

#corr() correlation
    
print("\n correlance in series :\n",series_one.corr(series_two))

print("\n correlance in data frame :\n",dframe.corr())


#rank() data rank
        
print("\n data rank in series one : \n",series_one.rank())

print("\n data rank in data frame : \n",dframe.rank())
        


# In[15]:


#handling missing values

datadict = {'name':['john smith','joe root','shaun michel','rickey ponting'],
           'salary':[4500,6000,3050,5040],
           'bounus':[200,500,700,200]}

index = [1,3,5,7]

dframe = pd.DataFrame(datadict,index)

print("\n our data frame without missing values : \n",dframe)

dframe = dframe.reindex([1,2,3,4,5,6,7])  #creating missing values by reindexing

print("\n our data frame with some missing values in it : \n",dframe) #all 'Nan' are missing values


#check for missing values

print("\n checking missing values by 'isnull' function : \n",dframe.isnull()) #returns true where there is missing value

print("\n checking missing values by 'notnull' function : \n",dframe.notnull()) #returns false where there is missing value

#filling missing values 

        #filling missing values with scalar values    
        
print("\n data frame after filling missing values with 1 : \n",dframe.fillna(1)) #all missing values will be replaced with 1

        #filling missing values by using 'ffill/pad' or 'backfill/bfill' methods

print("\n data frame after filling missing values with 'ffill' method : \n",dframe.fillna(method='ffill')) 

print("\n data frame after filling missing values with 'backfill' method : \n",dframe.fillna(method='backfill'))


#drop missing values

print("\n data frame after droping missing values  \n",dframe.dropna())


# In[16]:


#replacing values of data frame

datadict = {'name':['john smith','joe root','shaun michel','rickey ponting'],
           'salary':[4500,6000,3050,5040],
           'bounus':[200,500,700,200]}

dframe = pd.DataFrame(datadict)

print("\n our data frame : \n",dframe)

print("\n data frame after replacing salary '6000' with '1500' : \n",dframe.replace({6000:1500}))

print("\n data frame after replacing 'shaun michel' with 'undertaker' : \n",dframe.replace({'shaun michel':'undertaker'}))

print("\n data frame after replacing some values : \n",dframe.replace({'rickey ponting':'ms dhoni','joe root':'virat kohli'}))


# In[17]:


#group by ()
    
datadict = {'player name':['ms dhoni','virat kohli','sachin tendulkar','sourav ganguly','ms dhoni','sachin tendulkar','virat kohli','virat kohli','sourav ganguly','ms dhoni'],
           'rank':[2,1,3,1,1,3,2,4,5,6],
           'year':[2001,2002,2000,2002,2002,2002,2001,2001,2000,2000],
           'runs':[7000,4000,6000,12300,85400,34500,5632,32100,6300,5490]}

dframe = pd.DataFrame(datadict)

print("\n our data frame : \n",dframe)

group = dframe.groupby('year').groups

print("\n group of years : \n\n",group)

group = dframe.groupby(['player name','rank']).groups

print("\n group of 'palyer name' and 'rank' : \n\n",group)

group = dframe.groupby(['player name','runs','year']).groups

print("\n group of 'player name' , 'runs' and 'year' : \n\n",group)

                                           
  #Iterating through Groups
        
group = dframe.groupby('player name')

for player,record in group :
    print("\n\n player name = ",player)
    print(record)
    
print("\n record of 'scahin tendulkar' : \n",group.get_group('sachin tendulkar'))


# In[18]:


#Aggregations
    

print("\n our data frame : \n",dframe)

group = dframe.groupby('year').agg(min)

print("\n minimum values in each year : \n",group)

group = dframe.groupby('year').agg(sum)

print("\n sum of all values of each column in each year :\n",group) 

                    #something very important

group = dframe.groupby('year')

print("\n total runs scored in each year : \n",group['runs'].agg(sum))

print("\n minimum run scored in each year : \n",group['runs'].agg(min))

print("\n maximum run scored in each year : \n",group['runs'].agg(max))
 
                        
                    #applying multiple Aggregation functions at once
            
group = dframe.groupby('player name')

print("\n total runs , minimum runs and maximum runs scored by each player : \n",group['runs'].agg([sum,min,max])) 

                    #filter

print("\n\n",dframe.groupby('player name').filter(lambda x : len(x)>2)) 

#will print record of 'm dhoni' and 'virat kohli' because their record comes three times which is greater then 2


# In[19]:


#merging/joining
    
data_one = {'name':['joe root','Ian bell','stuart broad','Ian botham','alan border','denis lilly','mark taylor','steve waugh','mark henry','kevin peterson','greame swan'],
        'department':['sales','marketing','strategy','marketing','strategy','testing','strategy','sales','sales','marketing','strategy'],
         'shift':['day','night','night','night','day','day','day','day','night','day','day'],
           'id':[1012,96,91,95,92,93,99,94,1051,98,1000]}

first_dframe = pd.DataFrame(data_one)

print("our first data frame : \n",first_dframe)

data_two = {'name':['Ms Dhoni','Sachin Tendulkar','Virat Kohli','Kapil Dev','Sunil Gavaskar','Sourav Ganguly','Rahul Dravid','Mohammed Shami','Irfan Pathan','Yusuf Pathan','Zaheer Khan'],
        'department':['marketing','strategy','testing','development','quality assurance','quality assurance','sales','sales','marketing','sales','testing'],
         'shift':['night','night','night','day','day','day','day','day','night','night','day'],
           'id':[92,91,93,94,95,96,94,99,98,1011,1012]}

index = [21,22,23,24,25,26,27,28,29,30,31]

second_dframe = pd.DataFrame(data_two,index)

print("\n our second data frame : \n",second_dframe)

print("\n merge both data frames on 'department' : \n",pd.merge(first_dframe,second_dframe,on='id'))

print("\n merge both data frames on 'department' and 'id' : \n",pd.merge(first_dframe,second_dframe,on=['department','id']))

print("\n merge both data frames on 'department' , 'id' and 'shift' : \n",pd.merge(first_dframe,second_dframe,on=['department','id','shift']))


# In[20]:


#types of Joines
    

datadict = {'id':[12,32,43,64,75],
            'Name': ['Ms Dhoni', 'Virat Kohli', 'Sunil Gavaskar', 'Irfan Pathan', 'Yusuf Pathan'],
            'subject':['DBMS','OS','ANDROID','JAVA','IOS']}

first_dframe = pd.DataFrame(datadict)

datadict_two = {'id':[65,77,99,46,53],
         'Name': ['Alan Border', 'Mark Taylor', 'Steve Waugh', 'Rickey Ponting', 'David Warner'],
         'subject':['OS','ANDROID','AI','JAVA','IOS']}

second_dframe = pd.DataFrame(datadict_two)

print("\n our first data frame : \n",first_dframe)

print("\n our second data frame : \n",second_dframe)

                    #left Join

print("\n both data frame are joined on 'subject' by using 'left join' : \n",pd.merge(first_dframe,second_dframe,on='subject',how='left'))

                    #right Join

print("\n both data frame are joined on 'subject' by using 'right join' : \n",pd.merge(first_dframe,second_dframe,on='subject',how='right'))

                    #outer Join

print("\n both data frame are joined on 'subject' by using 'outer join' : \n",pd.merge(first_dframe,second_dframe,on='subject',how='outer'))

                    #inner Join

print("\n both data frame are joined on 'subject' by using 'inner join' : \n",pd.merge(first_dframe,second_dframe,on='subject',how='inner'))


# In[21]:


#Concatenation
    
print("\n our first data frame : \n",first_dframe)

print("\n our second data frame : \n",second_dframe)

print("\n concatenat both data frames : \n",pd.concat([first_dframe,second_dframe]))

print("\n concatenat both data frames and place keys on each on : \n",pd.concat([first_dframe,second_dframe],keys=['first','second']))

#that's how you can diffrentiate data frames after concat

print("\n concatenat both data frames : \n",pd.concat([first_dframe,second_dframe],ignore_index=True)) 

print("\n concat both data frames along axis = 0 : \n",pd.concat([first_dframe,second_dframe],axis=0))

print("\n concat both data frames along axis = 1 : \n",pd.concat([first_dframe,second_dframe],axis=1))


# In[22]:


#date
    
    # date_range function can take three perameters start, end, periods, and freq
    
print("\n date from 12/25/2018 to 10 days : \n",pd.date_range("12/25/2018",periods=10)) 

#print dates from 25 dec 2018 to 3 jan 2019 because periods is 10 

print("\n date from 11/20/2018 to 12/03/2018 : \n",pd.date_range(start = '11/20/2018', end = '12/03/2018'))

print("\n buisness dates from 11/20/2018 to to 8 days (weekends will be excluded): \n",pd.bdate_range('11/20/2018',periods=8))

# 24 and 25 nov will not be printed because saturday and sunday

print("\n  print dates excluding weekends : \n",pd.date_range("03/15/2018",periods=10,freq='B'))

print("\n print business quarter dates : \n",pd.date_range("01/01/2018",periods=5,freq='BQS')) 

print("\n print annual(Year) end frequency : \n",pd.date_range('2018',periods=3,freq='A'))
print("\n print weekly frequency : \n",pd.date_range('09/01/2018',periods=5,freq='W')) 

print("\n print business year end frequency : \n",pd.date_range('2018',periods=4,freq='BA')) 

print("\n  print month end frequency : \n",pd.date_range('2018',periods=4,freq='M')) 

print("\n print business year start frequency : \n",pd.date_range('2018',periods=4,freq='BAS')) 

print("\n print semi-month end frequency : \n",pd.date_range('2018',periods=4,freq='SM'))

print("\n  print business hour frequency : \n",pd.date_range('01/23/2018','01/25/2018',freq='BH')) 

print("\n  print business month end frequency : \n",pd.date_range('2018','2020',freq='BM')) 

print("\n print hourly frequency : \n",pd.date_range('04/25/2018','04/26/2018',freq='H')) 

print("\n print month start frequency : \n",pd.date_range('03/2018','05/2018',freq='MS')) 

print("\n print minutely frequency ('min can also be used') : \n",pd.date_range('03/23/2018','03/25/2018',freq='T')) 

print("\n  print semi month start frequency : \n",pd.date_range('03/23/2018','05/25/2018',freq='sms'))


# In[23]:


print("\n  print secondly frequency : \n",pd.date_range('03/23/2018','03/25/2018',freq='S'))

print("\n  print business month start frequency : \n",pd.date_range('2018','2019',freq='BMS'))

print("\n  print milliseconds frequency : \n",pd.date_range('12/04/2018','12/05/2018',freq='ms'))

print("\n  print quarter end frequency : \n",pd.date_range('2018','2019',freq='Q'))

print("\n  print business quarter end frequency : \n",pd.date_range('2018','2019',freq='BQ'))

print("\n  print quarter start frequency : \n",pd.date_range('2018','2019',freq='QS'))


# In[24]:


#Timedelta
    
print(pd.Timedelta(' 5 days 10 hours 45 minutes 50 seconds 800 milliseconds'))

print("\n",pd.Timedelta(3, unit = 'h'))

print("\n",pd.Timedelta(3, unit = 'm'))

print("\n",pd.Timedelta(3, unit = 's'))

print("\n",pd.Timedelta(3, unit = 'ms'))

print("\n",pd.Timedelta(days = 10))

print("\n",pd.Timedelta(days = 10, hours = 9 ,minutes = 23 ,seconds = 45 , milliseconds = 790)) 


    
mylist = ['23:20:45','7:56:23','15:26:29','08:19:09']

time = pd.to_timedelta(mylist)

print("\n",time)

print("\n",time[2])

print("\n",time[0])

print("\n",time[1:3])

for x in time :
    print("\n",x)
    
myseries = []


# In[82]:


#working with csv file

dframe = pd.read_csv("emp_records.csv") #reading csv file and creating a new dtat frame 

print(dframe)

print("\n first 5 records from csv file : \n",dframe.head())

print("\n last 5 records from csv file : \n",dframe.tail())

            #nrows() to print n number of rows

dframe = pd.read_csv("emp_records.csv",nrows = 7)    
    
print("\n first 7 rows from csv file : \n",dframe)


            #specify data type of columns of csv file

dframe = pd.read_csv("emp_records.csv",dtype={'salary':float})
 
print("\n data in csv file after changing data type of column 'salary' to 'float' : \n",dframe.head())

                  
                        #fetching only specific columns from csv file

dframe = pd.read_csv("emp_records.csv", usecols=['emp_name','salary'])

print("\n fetched only two columns 'emp_name' and 'salary' from csv file : \n",dframe.head())

print("\n adding 100 to each value in cloumns 'series' : \n",(dframe['salary']+100).head())

                                #changing column name
    
dframe = pd.read_csv("emp_records.csv",names=['index_num','name_emp','salary_emp','dept_emp'],header=0)

print("\n changing column names of csv file : \n",dframe.head())

                                #saving data frame in csv file

dframe.to_csv("new_records.csv",index=False) #saving data frame into .csv file

dframe = pd.read_csv("new_records.csv")
                     
    
print("\n records in 'new_records.csv' : \n",dframe.head())

