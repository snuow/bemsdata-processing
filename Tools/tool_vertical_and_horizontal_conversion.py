import pandas as pd
import os
import sys
import glob
import Tools.tools_common as tc

config = tc.read_config()
csv_list = [os.path.basename(r) for r in glob.glob('../add_rawdata/*')]

for csv in csv_list:
    raw_df = pd.read_csv(r'../add_rawdata/' + csv,
                         header=[_ for _ in range(int(config['FILESETTING']['HeaderArrayNumber']))],
                         encoding='shift-jis',
                         engine='python'
                         )

# output_data処理
print('Completed')