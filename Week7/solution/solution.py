{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3901b86f-82ba-400f-9f15-26f96828cc9a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bedcb68c-b3cb-4d8f-a17a-c1020af5f660",
   "metadata": {},
   "outputs": [],
   "source": [
    "#1.Add 12 records\n",
    "data=[]\n",
    "for i in range(1,13):\n",
    "    Prod_No=i\n",
    "    Prod_Name=input(\"Enter product name for product{}:\".format(i))\n",
    "    month_sell=[]\n",
    "    for j in range(1,7):\n",
    "        sell=int(input(\"Enter sell of product {} in month{}:\".format(i,j)))\n",
    "        month_sell.append(sell)\n",
    "    data.append([Prod_No,Prod_Name]+month_sell)\n",
    "#2.Create DataFrame\n",
    "df=pd.DataFrame(data,columns=[\"Prod_No\",\"Prod_Name\",\"Jan\",\"Feb\",\"Mar\",\"Apr\",\"May\",\"Jun\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c6c6d499-91e5-45c7-bce8-0995a21e6b40",
   "metadata": {},
   "outputs": [],
   "source": [
    "#3.Change Column Name Product No,Product Name,January,Febuary,March,April,May,June.\n",
    "df.columns=[\"Product No\",\"Product Name\",\"January\",\"Febuary\",\"Mrach\",\"April\",\"May\",\"June\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "269409a5-86d5-4c0f-9444-f69aea02f6f2",
   "metadata": {},
   "outputs": [],
   "source": [
    "#4.Add column \"Total Sell\" to count total of all month and \"Average Sell\"\n",
    "df[\"Total Sell\"]=df[[\"January\",\"Febuary\",\"Mrach\",\"April\",\"May\",\"June\"]].sum(axis=1)\n",
    "df[\"Average Sell\"]=df[\"Total Sell\"]/6"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d12c2d90-2b3a-4b31-a8d9-7102259aa44c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#5.Add 2 row at the end.\n",
    "df.loc[12]=[13,\"Groundnuts\",29,30,37,28,28,29,181,30.166666]\n",
    "df.loc[13]=[14,\"Mushroom\",33,37,38,31,30,38,207,34.500000]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0ce5974b-bf92-4ff5-8fa3-c898a3fa2ce0",
   "metadata": {},
   "outputs": [],
   "source": [
    "#6.Add 2 row after 3rd row."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7f855b7f-1870-4d90-8b93-53bdca571030",
   "metadata": {},
   "outputs": [],
   "source": [
    "#7.Print first 5 row.\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6110dfcd-25e6-44a8-82ec-c50b7bdddb0b",
   "metadata": {},
   "outputs": [],
   "source": [
    "#8.Print last 5 row.\n",
    "df.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "86665d30-1bea-47e0-9496-16eae9f9cab1",
   "metadata": {},
   "outputs": [],
   "source": [
    "#9.Print row 6 to 10.\n",
    "df.loc[6:10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5ebba1f0-8ba4-47fd-b7a8-d456409a6ef4",
   "metadata": {},
   "outputs": [],
   "source": [
    "#10.Print only product name\n",
    "df[\"Product Name\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "376b2899-d388-4b19-a394-8305faa11ef8",
   "metadata": {},
   "outputs": [],
   "source": [
    "#11.Print sell of January month with product id and  product name.\n",
    "df[[\"Product No\",\"Product Name\",\"January\"]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b127438f-b03a-440a-b360-4fe3022cfa78",
   "metadata": {},
   "outputs": [],
   "source": [
    "#12.Print only those product id,product name where january sell is >5000 and Febuary sell is >8000\n",
    "df[(df[\"January\"]>5000) and (df[\"Febuary\"]>8000)][[\"Product No\",\"Product Name\"]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aa84979e-cf5e-43df-8c03-1d9993fdeb27",
   "metadata": {},
   "outputs": [],
   "source": [
    "#13.Print record in sorting order of Product name.\n",
    "df.sort_values(by=\"Product Name\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7c5585d2-4f5c-4336-b730-cec85ec50859",
   "metadata": {},
   "outputs": [],
   "source": [
    "#14.Display only odd index number column record.\n",
    "df.iloc[:,1::2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f31e1dd0-3deb-48ff-a81b-ef57f48bf770",
   "metadata": {},
   "outputs": [],
   "source": [
    "#15.Display alternate row.\n",
    "df.iloc[0::2,:]"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}