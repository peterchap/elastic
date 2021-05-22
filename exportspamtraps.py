import pandas as pd

directory = "C:/Users/Peter/Downloads/"

file1 = "baddata.csv"
file2 = "baddata1.csv"
file3 = "baddata2.csv"
file4 = "baddata3.csv"
file5 = "baddata4.csv"
file6 = "baddata5.csv"

directory1 = "C:/Users/Peter/OneDrive - Email Switchboard Ltd/Data Cleaning Project/"
statusfile = "domain_status.csv"
statuscols = ["name", "owner", "status", "segment"]

df1 = pd.read_csv(directory + file1, encoding="utf-8")
df2 = pd.read_csv(directory + file2, encoding="utf-8")
df3 = pd.read_csv(directory + file3, encoding="utf-8")
df4 = pd.read_csv(directory + file4, encoding="utf-8")
df5 = pd.read_csv(directory + file4, encoding="utf-8")
df6 = pd.read_csv(directory + file4, encoding="utf-8")

df = pd.concat([df1, df2, df3, df4, df5, df6], ignore_index=True)
print(df.shape)
df.drop_duplicates(subset=["m_To"], keep="last", inplace=True)

df = df[df["m_Status"].notnull()]
print(df.shape)

df7 = pd.read_csv(directory1 + statusfile, encoding="utf-8", usecols=statuscols)

final = df.merge(df7, left_on="m_RecipientDomain", right_on="name", how="left")

final.to_csv(directory + "rs3mta_bad_data.csv", index=False)
