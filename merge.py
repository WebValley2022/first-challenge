import os
import pandas as pd
from datetime import datetime, timedelta

save_path = "C:/Users/thoma/Desktop/DS1/first-challenge/"
data_folder_path = "C:/Users/thoma/Desktop/DS1/first-challenge/"

# 2. creates list with files to merge based on name convention
file_list = [
    data_folder_path + f for f in os.listdir(data_folder_path)
    if f.startswith('data_20')
]

# 3. creates empty list to include the content of each file converted to pandas DF
csv_list = []

ind = 0
# 4. reads each (sorted) file in file_list, converts it to pandas DF and appends it to the csv_list
for file in sorted(file_list):
    print(ind)
    ind += 1
    csv_list.append(
        pd.read_csv(
            file, encoding="cp1252").assign(File_Name=os.path.basename(file)))

# 5. merges single pandas DFs into a single DF, index is refreshed
csv_merged = pd.concat(csv_list, ignore_index=True)


newDates = []
for date, hour in zip(csv_merged["Data"], csv_merged["Ora"]):
    newDate = datetime(int(date[:4]), int(date[5:7]), int(date[8:10]))
    newDate = newDate + timedelta(hours=int(hour))
    newDates.append(newDate)
csv_merged["Data"] = newDates

# remove rows with not defined value
csv_merged = csv_merged[csv_merged.Valore != "n.d."]


# sorts the pandas DF by station, pollutant, date and hour
csv_merged = csv_merged.sort_values(
    by=["Stazione", "Inquinante", "Data", "Ora"])


# 6. Single DF is saved to the path in CSV format, without index column
csv_merged.to_csv(save_path + 'APPA_data_merged.csv',
                  index=False,
                  columns=[
                      "Stazione", "Inquinante", "Data", "Valore",
                      "Unità di misura"
                  ]
)

import zipfile
zipfile.ZipFile("APPA_data_merged.zip", mode="w", compression=zipfile.ZIP_DEFLATED).write("APPA_data_merged.csv")
print("fatto")