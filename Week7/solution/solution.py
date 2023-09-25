import pandas as pd
#1.Add 12 records
data=[]
for i in range(1,13):
    Prod_No=i
    Prod_Name=input("Enter product name for product{}:".format(i))
    month_sell=[]
    for j in range(1,7):
        sell=int(input("Enter sell of product {} in month{}:".format(i,j)))
        month_sell.append(sell)
    data.append([Prod_No,Prod_Name]+month_sell)
#2.Create DataFrame
df=pd.DataFrame(data,columns=["Prod_No","Prod_Name","Jan","Feb","Mar","Apr","May","Jun"])
#3.Change Column Name Product No,Product Name,January,Febuary,March,April,May,June.
df.columns=["Product No","Product Name","January","Febuary","Mrach","April","May","June"]
#4.Add column "Total Sell" to count total of all month and "Average Sell"
df["Total Sell"]=df[["January","Febuary","Mrach","April","May","June"]].sum(axis=1)
df["Average Sell"]=df["Total Sell"]/6
#5.Add 2 row at the end.
df.loc[12]=[13,"Groundnuts",29,30,37,28,28,29,181,30.166666]
df.loc[13]=[14,"Mushroom",33,37,38,31,30,38,207,34.500000]
#6.Add 2 row after 3rd row.
#7.Print first 5 row.
df.head()
#8.Print last 5 row.
df.tail()
#9.Print row 6 to 10.
df.loc[6:10]
#10.Print only product name
df["Product Name"]
#11.Print sell of January month with product id and  product name.
df[["Product No","Product Name","January"]]
#12.Print only those product id,product name where january sell is >5000 and Febuary sell is >8000
df[(df["January"]>5000) and (df["Febuary"]>8000)][["Product No","Product Name"]]
#13.Print record in sorting order of Product name.
df.sort_values(by="Product Name")
#14.Display only odd index number column record.
df.iloc[:,1::2]
#15.Display alternate row.
df.iloc[0::2,:]
