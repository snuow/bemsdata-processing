import pandas as pd
import os
import glob
import Tools.tools_common as tc
from tqdm import tqdm

# configファイル読み込み
config = tc.read_config()

# csvファイルリスト作成
csv_list = [os.path.basename(r) for r in glob.glob('../add_rawdata/*')]

for csv in tqdm(csv_list):
    # csvlist内のcsvを読み込み
    raw_df = pd.read_csv(r'../add_rawdata/' + csv,
                         header=[0],
                         index_col=[_ for _ in range(int(config['FILESETTING']['HeaderArrayNumber']) + 1)],
                         encoding='shift-jis',
                         engine='python'
                         )
    # 縦横変換
    raw_dfT = raw_df.T
    # 縦横変換後のデータフレームをcsv出力
    raw_dfT.to_csv(r'../output_processingdata/' + csv,encoding='shift-jis')

# output_data処理
print('Completed')