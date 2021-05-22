import pandas as pd
import io
import requests

directory = "C:/Users/Peter/Downloads/"
month = "05"
days = [
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31",
]
year = "21"
url = "https://sendersupport.olc.protection.outlook.com/snds/data.aspx?key=6b66979a-418f-bd6d-d6dc-1616e9a532e7"
fields = [
    "m_MailerIp",
    "m_LogDate",
    "end_time",
    "rcpt",
    "window_count",
    "message",
    "snds_filter",
    "complaint",
    "trap_start",
    "trap_finish",
    "snds_count",
    "helo",
    "mail_from",
    "comments",
]
dfall = pd.DataFrame(columns=fields)
datecols = ["m_LogDate", "end_time", "trap_start", "trap_finish"]

for day in days:
    request = url + "&date=" + month + day + year
    s = requests.get(request).content
    df = pd.read_csv(io.StringIO(s.decode("utf-8")), names=fields, parse_dates=datecols)
    dfall = dfall.append(df)

dfall.drop(
    columns=["rcpt", "message", "complaint", "helo", "mail_from", "comments"],
    inplace=True,
)
dfall["complaint_rate"] = 0.001
print(dfall.shape)
print(dfall.dtypes)
dfall.to_csv(directory + "sndsmay2021.csv", index=False)

