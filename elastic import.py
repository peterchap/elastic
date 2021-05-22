import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

# Import LabelEncoder
from sklearn import preprocessing

# Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics


def blocker(row):
    if row["m_Status"] == "DELIVERED":
        return "Delivered"
    elif row["m_Status"] == "FILTERED":
        return "Filtered"
    elif row["m_Status"] == "EXPIRED":
        return "Expired"
    if row["Group"] == "Other":
        if ("cyren") in str(row["m_LogEntry"]).lower():
            return "Cyren"
        elif ("symantec") in str(row["m_LogEntry"]).lower():
            return "Symantec"
        elif ("proofpoint") in str(row["m_LogEntry"]).lower():
            return "Proofpoint"
        elif ("barracuda") in str(row["m_LogEntry"]).lower():
            return "Barracuda"
        elif ("trend") in str(row["m_LogEntry"]).lower():
            return "Trend Micro"
        elif ("mimecast") in str(row["m_LogEntry"]).lower():
            return "Mimecast"
        elif ("cloudmark") in str(row["m_LogEntry"]).lower():
            return "Cloudmark"
        elif ("spamhaus/invaluement/returnpath") in str(row["m_LogEntry"]).lower():
            return "Spamhaus/Invaluement/ReturnPath"
        elif ("spamhaus") in str(row["m_LogEntry"]).lower():
            return "Spamhaus"
        elif ("invaluement") in str(row["m_LogEntry"]).lower():
            return "Invaluement"
        elif ("return path") in str(row["m_LogEntry"]).lower():
            return "Return Path"
        elif ("returnpath") in str(row["m_LogEntry"]).lower():
            return "Return Path"
        elif ("ers-rbl") in str(row["m_LogEntry"]).lower():
            return "Trend Micro"
        elif ("spamcop") in str(row["m_LogEntry"]).lower():
            return "SpamCop"
        elif ("sophos") in str(row["m_LogEntry"]).lower():
            return "Sophos"
        elif ("outlook") in str(row["m_LogEntry"]).lower():
            return "Microsoft Block"
        elif ("kundserver") in str(row["m_LogEntry"]).lower():
            return "1&1 Block"
        elif ("spam") in str(row["m_LogEntry"]).lower():
            return "Other Spam Block"
        elif ("cox") in str(row["m_LogEntry"]).lower():
            return "Other Spam Block"
        elif ("too many recipients") in str(row["m_LogEntry"]).lower():
            return "Other Spam Block"
        elif ("5.4.2") in str(row["m_StatusCode"]):
            return "Cloudmark"
        elif ("filtered") in str(row["m_LogEntry"]).lower():
            return "Other Spam Block"
        elif ("greylist") in str(row["m_LogEntry"]).lower():
            return "Other Spam Block"
        elif ("connection error") in str(row["m_LogEntry"]).lower():
            return "Other Spam Block"
        elif ("refused") in str(row["m_LogEntry"]).lower():
            return "Other Spam Block"
        elif ("blocked") in row["m_LogEntry"]:
            return "Other Spam Block"
        elif ("envelope") in row["m_LogEntry"]:
            return "Other Spam Block"
        elif ("message content rejected") in row["m_LogEntry"]:
            return "Other Spam Block"
        elif "spam" in str(row["m_LogEntry"]).lower():
            return "Other Spam Block"
        elif "message rejected" in str(row["m_LogEntry"]).lower():
            return "Other Spam Block"
        elif "prohibit" in str(row["m_LogEntry"]).lower():
            return "Other Spam Block"
        elif "policy" in str(row["m_LogEntry"]).lower():
            return "Other Spam Block"
        elif "content filter" in str(row["m_LogEntry"]).lower():
            return "Other Spam Block"
        elif "comcast" in str(row["m_LogEntry"]).lower():
            return "Comcast Throttle"
        elif "excite" in str(row["m_LogEntry"]).lower():
            return "Excite block"
        elif "blocked" in str(row["m_LogEntry"]).lower():
            return "Other Spam Block"
        elif "reject" in str(row["m_LogEntry"]).lower():
            return "Other Spam Block"
        elif "too many" in str(row["m_LogEntry"]).lower():
            return "Other Spam Block"
        elif ".7.1" in str(row["m_LogEntry"]).lower():
            return "Other Spam Block"
        elif "reputation" in str(row["m_LogEntry"]).lower():
            return "Other Spam Block"
        return "Other Unknown"
    elif row["Group"] == "1&1":
        if row["m_StatusCode"] == "4.0.0":
            return "1&1 Throttled"
        elif row["m_StatusCode"] == "4.2.1":
            return "1&1 Throttled"
        elif row["m_StatusCode"] == "4.5.0":
            return "1&1 Throttled"
        elif row["m_StatusCode"] == "4.5.1":
            return "1&1 Throttled"
        elif row["m_StatusCode"] == "5.5.0":
            return "1&1 Undeliverable email"
        elif row["m_StatusCode"] == "5.5.4":
            return "1&1 Reputation Block"
        elif "6.0" in row["m_StatusCode"]:
            return "1&1 Reputation Block"
        else:
            return "1&1 Unknown"
    elif row["Group"] == "Apple":
        if "4.0.0" in row["m_StatusCode"]:
            return "Apple Throttled"
        elif "4.2.1" in row["m_StatusCode"]:
            return "Apple Throttled"
        elif "4.5.1" in row["m_StatusCode"]:
            return "Apple Throttled"
        elif "5.5.0" in row["m_StatusCode"]:
            return "Apple Reputation Block"
        elif "5.5.4" in row["m_StatusCode"]:
            return "Apple Reputation Block"
        elif "6.0" in row["m_StatusCode"]:
            return "Apple Reputation Block"
        elif ("proofpoint") in str(row["m_LogEntry"]).lower():
            return "Proofpoint"
        else:
            return "Apple Unknown"
    elif row["Group"] == "BT":
        if "4.0.0" in row["m_StatusCode"]:
            return "BT Throttled"
        elif "4.2.1" in row["m_StatusCode"]:
            return "BT Spam Throttle"
        elif row["m_StatusCode"] == "5.2.2":
            return "BT SPR block"
        elif "5.5.0" in row["m_StatusCode"]:
            return "BT Reputation Block"
        elif "6.0" in row["m_StatusCode"]:
            return "BT Reputation Block"
        elif row["m_StatusCode"] == "5.5.4":
            return "BT Spam block"
        else:
            return "BT Unknown"
    elif row["Group"] == "Google":
        if "4.0.0" in row["m_StatusCode"]:
            return "Google Spam Block"
        elif "4.2.1" in row["m_StatusCode"]:
            return "Google Spam Throttle"
        elif "4.5.0" in row["m_StatusCode"]:
            return "Google Spam Throttle"
        elif "4.5.1" in row["m_StatusCode"]:
            return "Google Spam Throttle"
        elif "5.5.0" in row["m_StatusCode"]:
            return "Google Reputation Block"
        elif "6.0" in row["m_StatusCode"]:
            return "Google Reputation Block"
        else:
            return "Google Unknown"
    elif row["Group"] == "GMail":
        if "4.0.0" in row["m_StatusCode"]:
            return "GMail Spam Block"
        elif "4.2.1" in row["m_StatusCode"]:
            return "GMail Spam Throttle"
        elif "4.5.0" in row["m_StatusCode"]:
            if "trend micro" in row["m_LogEntry"].lower():
                return "Gmail Trend Micro Block"
            elif "ers-qil" in row["m_LogEntry"].lower():
                return "Gmail Trend Micro Block"
            else:
                return "Google Spam Throttle"
        elif "4.5.1" in row["m_StatusCode"]:
            return "GMail Mimecast Block"
        elif "5.5.0" in row["m_StatusCode"]:
            return "GMail Reputation Block"
        elif "5.5.4" in row["m_StatusCode"]:
            return "GMail Mimecast Spam Block"
        elif "6.0" in row["m_StatusCode"]:
            return "GMail Reputation Block"
        else:
            return "GMail Unknown"
    elif row["Group"] == "Kcom":
        if "reputation" in row["m_StatusCode"]:
            return "Microsoft Reputation Block"
    elif row["Group"] == "Microsoft":
        if "4.0.0" in row["m_StatusCode"]:
            return "Microsoft Throttled"
        elif "4.5.1" in row["m_StatusCode"]:
            return "Microsoft Throttled"
        elif "5.5.0" in row["m_StatusCode"]:
            return "Microsoft Reputation Block"
        elif "6.0" in row["m_StatusCode"]:
            return "Microsoft Reputation Block"
        else:
            return "Microsoft Unknown"
    elif row["Group"] == "Office365":
        if "4.0.0" in row["m_StatusCode"]:
            return "Office365 Throttled"
        elif "4.5.1" in row["m_StatusCode"]:
            return "Office365 Throttled"
        elif "5.5.0" in row["m_StatusCode"]:
            return "Office365 Reputation Block"
        elif "5.5.4" in row["m_StatusCode"]:
            return "Office365 Reputation Block"
        elif "5.5.6" in row["m_StatusCode"]:
            return "Office365 No MX"
        elif "6.0" in row["m_StatusCode"]:
            return "Office365 Reputation Block"
        else:
            return "Office365 Unknown"
    elif row["Group"] == "Talk Talk":
        if "4.0.0" in row["m_StatusCode"]:
            return "Talk Talk Throttled"
        elif "4.5.3" in row["m_StatusCode"]:
            return "Spam Throttle"
        elif ("content rejected") in str(row["m_LogEntry"]).lower():
            return "Talk Talk Spam Block"
        elif "6.0" in row["m_StatusCode"]:
            return "Talk Talk Reputation Block"
        else:
            return "Talk Talk Unknown"
    elif row["Group"] == "Verizon":
        if "4.0.0" in row["m_StatusCode"]:
            return "Verizon Throttled"
        elif row["m_StatusCode"] == "4.2.1":
            return "Verizon Reputation Block"
        elif row["m_StatusCode"] == "4.5.0":
            return "Verizon Reputation Throttle"
        elif row["m_StatusCode"] == "4.5.1":
            return "Verizon Reputation Block"
        elif "6.0" in row["m_StatusCode"]:
            return "Verizon Reputation Block"
        elif ("content rejected") in str(row["m_LogEntry"]).lower():
            return "Verizon Spam Block"
        else:
            return "Verizon Unknown"
    elif row["Group"] == "Virgin":
        if "4.0.0" in row["m_StatusCode"]:
            return "Virgin Throttled"
        elif row["m_StatusCode"] == "4.5.1":
            return "Mimecast Reputation Block"
        elif row["m_StatusCode"] == "4.5.2":
            return "Virgin Reputation Block"
        elif row["m_StatusCode"] == "4.2.1":
            return "Virgin Reputation Block"
        elif row["m_StatusCode"] == "5.5.4":
            return "Spam Throttle"
        elif "6.0" in row["m_StatusCode"]:
            return "Virgin Reputation Block"
        else:
            return "Virgin Unknown"
    return "Unknown"


def deademail(row):
    if row["m_Status"] == "DELIVERED":
        return "Delivered"
    elif row["m_Status"] == "FILTERED":
        return "Filtered"
    elif row["m_Status"] == "EXPIRED":
        return "Expired"
    if row["Group"] == "Other":
        if ("invalid mailbox") in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif ("invalid recipient") in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif ("invalid address") in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif ("no mx") in str(row["m_LogEntry"]).lower():
            return "No MX"
        elif ("unknown") in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif ("mail box") in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif ("not exist") in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif ("address rejected") in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif ("account locked") in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif ("mailbox") in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif ("user not known") in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif ("recipient undeliverable") in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif ("recipient") in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif ("no such") in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif ("could not be found") in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif ("not found") in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif ("No user") in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif ("deleted") in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif ("disabled") in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif ("permanent") in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif ("relay") in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif ("route") in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif ("unroutable") in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif ("verify") in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif ("is not") in str(row["m_LogEntry"]).lower() and row[
            "m_Status"
        ] == "BOUNCED":
            return "Undeliverable email"
        elif ("quota") in str(row["m_LogEntry"]).lower():
            return "Over Quota"
        elif "no mx" in str(row["m_LogEntry"]).lower():
            return "No MX"
        elif "unknown" in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif "not exist" in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif "recipient address rejected" in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif "recipient undeliverable" in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif "recipientnotfound" in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif "no such" in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif "could not be found" in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif "not found" in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif "No user" in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif "deleted" in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif "disabled" in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif "permanent" in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif "relay" in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif "route" in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif "unroutable" in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif "verify" in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        elif (
            "is not" in str(row["m_LogEntry"]).lower() and row["m_Status"] == "BOUNCED"
        ):
            return "Undeliverable email"
        elif "quota" in str(row["m_LogEntry"]).lower():
            return "Over Quota"
        return "Other Unknown"
    elif row["Group"] == "1&1":
        if row["m_StatusCode"] == "5.5.0":
            return "Undeliverable email"
        else:
            return "1&1 Unknown"
    elif row["Group"] == "Apple":
        if row["m_StatusCode"] == "4.5.0":
            return "Over Quota"
        elif "5.5.2" in row["m_StatusCode"]:
            return "Over Quota"
        else:
            return "Apple Unknown"
    elif row["Group"] == "BT":
        if "4.5.0" in row["m_StatusCode"]:
            return "Undeliverable email"
        elif "4.5.1" in row["m_StatusCode"]:
            return "Undeliverable email"
        else:
            return "BT Unknown"
    elif row["Group"] == "Google":
        if "4.5.2" in row["m_StatusCode"]:
            return "Over Quota"
        elif "5.0.1" in row["m_StatusCode"]:
            return "Undeliverable email"
        elif "5.5.2" in row["m_StatusCode"]:
            return "Over Quota"
        else:
            return "Google Unknown"
    elif row["Group"] == "GMail":
        if "4.5.2" in row["m_StatusCode"]:
            return "Over Quota"
        elif "5.0.1" in row["m_StatusCode"]:
            return "Undeliverable email"
        elif "5.5.2" in row["m_StatusCode"]:
            return "Over Quota"
        else:
            return "GMail Unknown"
    elif row["Group"] == "Kcom":
        return "Kcom Unknown"
    elif row["Group"] == "Microsoft":
        if "5.0.1" in row["m_StatusCode"]:
            return "Undeliverable email"
        else:
            return "Microsoft Unknown"
    elif row["Group"] == "Office365":
        if "5.0.1" in row["m_StatusCode"]:
            return "Office365 Undeliverable email"
        else:
            return "Office365 Unknown"
    elif row["Group"] == "Talk Talk":
        if row["m_StatusCode"] == "5.5.0":
            return "Undeliverable email"
        else:
            return "Talk Talk Unknown"
    elif row["Group"] == "Verizon":
        if row["m_StatusCode"] == "5.5.4":
            return "Undeliverable email"
        elif ("mailbox not found") in str(row["m_LogEntry"]).lower():
            return "Undeliverable email"
        else:
            return "Verizon Unknown"
    elif row["Group"] == "Virgin":
        if row["m_StatusCode"] == "5.5.0":
            return "Undeliverable email"
        else:
            return "Virgin Unknown"
    return "Unknown"


# Model Creation
model = pd.read_csv("C:\\new bounce model data.csv")

print(model.shape)

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(
    model["Desc1"], model["Bounce"], test_size=0.3, random_state=109
)  # 70% training and 30% test

# Creating labelEncoder
le = preprocessing.LabelEncoder()

# Converting string labels into numbers.
bounce_encoded = le.fit_transform(y_train)

# Creating Model
vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(X_train)

classifier = MultinomialNB()
classifier.fit(counts, bounce_encoded)

counts_test = vectorizer.transform(X_test)
y_pred = classifier.predict(counts_test)


# Model Accuracy, how often is the classifier correct?
y_test_encoded = le.fit_transform(y_test)
print("Accuracy:", metrics.accuracy_score(y_test_encoded, y_pred))


directory = "C:/Users/Peter/Downloads/"
file1 = "rs3MTA_queryDELIVERED120521.csv"
file2 = "rs3MTA_queryBOUNCED120521.csv"
file3 = "rs3MTA_queryDEFERED120521.csv"
file4 = "rs3MTA_queryEXPIRED120521.csv"
# file5 = "rs3MTApt3DELIVERED120521.csv"
# file6 = "rs3MTApt3EXPIRED120521.csv"
file7 = "cross-business-export_13_05_2021 15_12_22.csv"

lookupcols = [
    "Campaign id",
    "Offer name",
    "List name",
    "Master filter",
    "Brand",
    "List owner",
]

directory1 = "C:/Users/Peter/OneDrive - Email Switchboard Ltd/Data Cleaning Project/"
statusfile = "domain_status.csv"
statuscols = ["name", "owner", "status", "segment"]

directory2 = "C:/Users/Peter/OneDrive - Email Switchboard Ltd/"
isp = "ISP Group domains.csv"
ispcols = ["Domain", "Group"]

colstouse = [
    "m_LogDate",
    "m_SubmissionDate",
    "m_CampaignId",
    "m_MessageId",
    "m_LogEntry",
    "m_StatusCode",
    "m_SendingDomain",
    "m_RecipientDomain",
    "m_From",
    "m_To",
    "m_Status",
    "m_MailerIp",
]

df1 = pd.read_csv(directory + file1, encoding="utf-8", usecols=colstouse)
df2 = pd.read_csv(directory + file2, encoding="utf-8", usecols=colstouse)
df3 = pd.read_csv(directory + file3, encoding="utf-8", usecols=colstouse)
df4 = pd.read_csv(directory + file4, encoding="utf-8", usecols=colstouse)
# df11 = pd.read_csv(directory + file5, encoding="utf-8", usecols=colstouse)
# df41 = pd.read_csv(directory + file6, encoding="utf-8", usecols=colstouse)

examples = df2["m_LogEntry"].values.astype("U")
examples2 = df3["m_LogEntry"].values.astype("U")

bounce_counts = vectorizer.transform(examples)
df2["bounce"] = classifier.predict(bounce_counts)
df2["bounce"] = df2["bounce"].replace([0, 1], ["HARD", "SOFT"])

bounce_counts2 = vectorizer.transform(examples2)
df3["bounce"] = classifier.predict(bounce_counts2)
df3["bounce"] = df3["bounce"].replace([0, 1], ["HARD", "SOFT"])

df1["bounce"] = ""
df4["bounce"] = ""
# df11["bounce"] = ""
# df41["bounce"] = ""


df = pd.concat([df1, df2, df3, df4], ignore_index=True)

df5 = pd.read_csv(directory1 + statusfile, encoding="utf-8", usecols=statuscols)
df6 = pd.read_csv(directory2 + isp, encoding="utf-8", usecols=ispcols)
df7 = pd.read_csv(directory + file7, encoding="utf-8", usecols=lookupcols)

df = df.merge(df5, left_on="m_RecipientDomain", right_on="name", how="left")
df = df.merge(df6, left_on="m_RecipientDomain", right_on="Domain", how="left")
df = df.merge(df7, left_on="m_CampaignId", right_on="Campaign id", how="left")
df.drop(columns=["name", "Domain"], inplace=True)
df.loc[(df["owner"] == "Microsoft") & (df["segment"] == "B"), "Group"] = "Office365"
df.loc[(df["owner"] == "Google") & (df["segment"] == "B"), "Group"] = "GMail"
df["Group"].fillna("Other", inplace=True)
df["owner"].fillna("Other", inplace=True)
df["blocker"] = df.apply(lambda row: blocker(row), axis=1)
df["dead"] = df.apply(lambda row: deademail(row), axis=1)
df.loc[df["dead"] == "Undeliverable email", "status"] = "Undeliverable email"
df.loc[df["dead"] == "Over Quota", "status"] = "Over Quota"
df.loc[((df["dead"] == "No MX") & (df["status"] == "OK")), "status"] = "No MX"
df.drop(columns=["Campaign id",], inplace=True)

print(df.columns)
print(df.shape)

print(df["status"].value_counts(dropna=False))
print(df["bounce"].value_counts())
print(df["Group"].value_counts())
print(df["blocker"].value_counts())

unknown = df[df["blocker"].str.contains("Unknown")].copy()
unknown.drop_duplicates(subset=["m_To"], keep="last", inplace=True)
nomx = df[df["status"] == "No MX"]
nostatus = df[df["status"].isnull()]
unknown.to_csv(directory + "unknownrs2.csv", index=False)
nomx.to_csv(directory + "nomxrs2.csv", index=False)
df.to_csv(directory + "elastictestrs2.csv", index=False)
nostatus.to_csv(directory + "nostatus2.csv", index=False)
