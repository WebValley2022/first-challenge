from datetime import date, timedelta
import os, stat

start_date = date(2012,1,1)
end_date = date(2022, 7, 1)
file_path = "download-data.sh"

with open(file_path, "w") as f:
    f.write("#!/bin/env bash\n")
    current_date = start_date
    while current_date < end_date:
        date2 = current_date + timedelta(days=60)
        f.write(f'curl https://bollettino.appa.tn.it/aria/opendata/csv/{current_date},{date2}/ -o data_{current_date}-{date2}.csv\n')
        current_date += timedelta(days=60)

os.chmod(file_path, stat.S_IEXEC|stat.S_IREAD|stat.S_IWRITE)
