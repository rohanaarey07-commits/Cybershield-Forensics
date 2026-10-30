from pathlib import Path
import pandas as pd
import numpy as np
# ADVANCED CDR ANALYZER 
FILE=Path("sample_cdr.csv")
print("cybershield forensics")
print("CDR-ANALYZER - version 1.0")
if not FILE.exists():
    print("CSV file not found")
    exit()
if FILE.stat().st_size == 0:
    print("CSV file is empty")
    exit()
df = pd.read_csv(FILE)
if df.empty:
    print("CSV has no records")
    exit()
print("\nfirst 5 records")
print(df.head())
print(len(df))
# OVERALL CALL REPORT
print("Total duration:",df["duration"].sum())
print("Average duration:",df["duration"].mean())
print("Longest call:",df["duration"].max())
print("Shortest call:",df["duration"].min())
# TOTAL CALL DURATION IN HOURS
print("Total call duration in hours",df["duration"].sum()/3600)
# TOTAL CALL DURATION IN MINUTES
print("Total call duration in minutes",df["duration"].sum()/60)
# CALLERS
print("Total calls:",len(df))
print("Calls per caller:",df["caller"].value_counts())
print("Unique callers:",df["caller"].nunique())
# RECEIVERS
print("Total call records:",len(df))
print("Calls received per number:",df["receiver"].value_counts())
print("Unique receivers:",df["receiver"].nunique())
# CALL DURATION ANALYSIS
print("Calls more than 2 minutes:",(df["duration"]>120).sum())
print("Calls less than 2 minutes:",(df["duration"]<120).sum())
print("Calls exactly 2 minutes:",(df["duration"]==120).sum())
print("Calls exactly or more than 5 minutes:",(df["duration"]>=300).sum())
print("Calls with zero duration:",(df["duration"]==0).sum())
# TOP 5 CALLERS ANALYSIS
print("Top 5 callers",df["caller"].value_counts().head(5))
# TOP 5 RECEIVERS ANALYSIS
print("Top 5 receivers",df["receiver"].value_counts().head(5))
# TOTAL CALL DURATION PER CALLER:
call_duration=df.groupby("caller")["duration"].sum()
print(call_duration)
# AVERAGE CALL DURATION PER CALLER
avg_call_duration=df.groupby("caller")["duration"].mean()
print("Average call duration per caller:")
print(avg_call_duration)
print("Duration shown in seconds")
# TOTAL CALL DURATION PER RECEIVER:
call_receiver=df.groupby("receiver")["duration"].sum()
print(call_receiver)
# AVERAGE CALL DURATION PER RECEIVER
avg_receiver_duration=df.groupby("receiver")["duration"].mean()
print("Average call duration per receiver:")
print(avg_receiver_duration)
print("Duration shown in seconds")
# MISSING VALUE ANALYSIS
missing_values=df.isnull().sum()
print("Missing values in each column:")
print(missing_values)
print("Total missing values:",missing_values.sum())
# CHECK NEGATIVE CALL DURATIONS:
negative_calls=df[df["duration"]<0]
print("Negative call records:")
print(negative_calls)
print("Total negative calls:",len(negative_calls))
# DUPLICATE RECORDS:
duplicates=df[df.duplicated()]
print(duplicates)
print("Total duplicates are:",len(duplicates))
# SELF CALL CHECK:
self_calls=df[df["caller"]==df["receiver"]]
print("Self call records:")
print(self_calls)
print("Total self calls:",len(self_calls))
# MOST FREQUENT CALL PAIR:
call_pairs=df.groupby(["caller","receiver"]).size()
top_pair=call_pairs.idxmax()
print("Most frequent call pair:")
print(top_pair)
print("Total calls:",call_pairs.max())
