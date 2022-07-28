import os
import pandas as pd

save_path = "C:/Users/thoma/Desktop/DS1/first-challenge/"
data_folder_path = "C:/Users/thoma/Desktop/DS1/first-challenge/"

# 2. creates list with files to merge based on name convention
file_list = [
    data_folder_path + f for f in os.listdir(data_folder_path)
    if f.startswith('data')
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

# remove rows with not defined value
csv_merged = csv_merged[csv_merged.Valore != "n.d."]


# sorts the pandas DF by station, pollutant, date and hour
csv_merged = csv_merged.sort_values(
    by=["Stazione", "Inquinante", "Data", "Ora"])

csv_merged["Data"] = csv_merged["Data"] + "-" + csv_merged["Ora"].astype(str)


# 6. Single DF is saved to the path in CSV format, without index column
csv_merged.to_csv(save_path + 'APPA data merged.csv',
                  index=False,
                  columns=[
                      "Stazione", "Inquinante", "Data", "Valore",
                      "Unità di misura"
                  ]
)
