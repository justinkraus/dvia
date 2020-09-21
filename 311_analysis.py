import pandas as pd
from pandas_profiling import ProfileReport

# PART 1 - only need to do once
##reading original datadump and saving as profile
df = pd.read_csv('311_Service_Requests_from_2010_to_Present.csv')

profile = ProfileReport(df, title="311 Service Requests: 2010 - Present", minimal=True)

profile.to_file("311_SR.html")

print(df.info(verbose=True, null_counts=True))


##PART 2 - only need to do once
#selected columns from original dataset as 311_SR_SELECT
#Unique Key, Created Date, Complaint Type, Descriptor
#Read the select column dataset
df = pd.read_csv('311_SR_Select.csv')

print(df.info(verbose=True, null_counts=True))

#convert to a new datetime column
df['Datetime'] = pd.to_datetime(df['Created Date'])
#get the numbered week of the year it is, add to new column
##converted this to weeks on second edit (previously did this .dt.dayofyear)
# df['Week'] = df['Datetime'].dt.week
#converted this to  dt.month to get monthly values
df['Month'] = df['Datetime'].dt.month
#get the year 
df['Year'] = df['Datetime'].dt.year

df.to_csv('311_SR_SELECT_Months.csv', mode='a')
print("done!")



# ##PART 3 - groupings for graphing
df = pd.read_csv('311_SR_SELECT_Months.csv')

print("done reading!")

# df2 = (df.groupby(['Year', 'DOY','Complaint Type']).size())
df2 = df.groupby(['Year', 'Month','Complaint Type']).size().to_frame(name='SR_count').reset_index()

print("done grouping!")

print(df2.info(verbose=True, null_counts=True))

print("writing to csv!")

df2.to_csv('311_grouped_months.csv', mode='a')

print("done!")