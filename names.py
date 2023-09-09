import csv

import numpy as np
import pandas as pd
import re
from IPython.display import display

dataset = pd.read_csv('genshin.csv')
#
name = dataset['character_name'].to_string()

re_name = re.sub(r'^\d+\s+', '', name, flags=re.MULTILINE)
# final_name = re_name.strip().split('\n')
final_name = re_name.strip()
# print(final_name)
name_file_csv = 'new_name.csv'

with open(name_file_csv, mode='w') as file:
    file.write(re_name)
print(f"Data has been written to {name_file_csv}")

