import configparser as cp
import pandas as pd
import os
import glob
from tqdm import tqdm
from datetime import datetime as dt


def read_config() -> object:
    config = cp.ConfigParser()
    config.read(r'../config.ini', encoding='UTF-8')
    return config


def tool_vertical_and_horizontal_conversion():
    # configファイル読み込み
    config = read_config()

    # csvファイルリスト作成
    csv_list = [os.path.basename(r) for r in glob.glob(r'../add_rawdata/*.csv')]

    for csv in tqdm(csv_list):
        # csv_list内のcsvを読み込み
        raw_df = pd.read_csv(r'../add_rawdata/' + csv,
                             keep_default_na=False,
                             header=[0],
                             index_col=[_ for _ in range(int(config['FILESETTING']['HeaderArrayNumber']) + 1)],
                             encoding='shift-jis',
                             engine='python'
                             )
        # 縦横変換
        raw_dfT = raw_df.T
        # TODO 転置時にcolumnsにnanが含まれる問題の解消

        # 縦横変換後のデータフレームをcsv出力
        raw_dfT.to_csv(r'../output_processingdata/' + csv, encoding='shift-jis')

    print('\n')
    print('--' * 20)
    print('tool_vertical_and_horizontal_conversion Completed!')
    print('--' * 20)


def tool_give_timestamp():
    # configファイル読み込み
    config = read_config()

    # csvファイルリスト作成
    csv_list = [os.path.basename(r) for r in glob.glob('../output_processingdata/*.csv')]

    for csv in tqdm(csv_list):
        # csv_list内のcsvを読み込み
        raw_df = pd.read_csv(r'../output_processingdata/' + csv,
                             keep_default_na=False,
                             header=[_ for _ in range(int(config['FILESETTING']['HeaderArrayNumber']) + 1)],
                             index_col=[0],
                             encoding='shift-jis',
                             engine='python'
                             )
        # TODO Unnamedと表示されるカラム名をどう処理するか。Unnamedはread_csvでヘッダに入る。

        
        # 日付データ生成
        # TODO 24hデータ以外が来た時の判断はどうする？
        # TODO DateTImeFormatのパターンの柔軟さを考える
        raw_df.index = pd.date_range(dt.strptime(csv, config['FILESETTING']['DateTimeFormat']),
                                     periods=24,
                                     freq='60T')

        # Timestamp加工済みdfをcsv出力
        add_ts_raw_df = raw_df
        add_ts_raw_df.to_csv(r'../output_processingdata/' + csv, encoding='shift-jis')

    print('\n')
    print('--' * 20)
    print('tool_give_timestamp Completed!')
    print('--' * 20)


def tool_delete_error_string():
    # configファイル読み込み
    config = read_config()

    # csvファイルリスト作成
    csv_list = [os.path.basename(r) for r in glob.glob(r'../output_processingdata/*.csv')]

    concat_df = pd.DataFrame()
    for no, csv in enumerate(csv_list):
        if no == 0:
            concat_df = pd.read_csv(r'../output_processingdata/' + csv,
                                    keep_default_na=False,
                                    header=[_ for _ in range(int(config['FILESETTING']['HeaderArrayNumber']) + 1)],
                                    index_col=[0],
                                    parse_dates=[0],
                                    encoding='shift-jis',
                                    engine='python')
        else:
            add_df = pd.read_csv(r'../output_processingdata/' + csv,
                                 keep_default_na=False,
                                 header=[_ for _ in range(int(config['FILESETTING']['HeaderArrayNumber']) + 1)],
                                 index_col=[0],
                                 parse_dates=[0],
                                 encoding='shift-jis',
                                 engine='python')
            concat_df = pd.concat([concat_df, add_df], axis=0, join='outer', sort=False)

    # 不要な文字列の削除（文字列の定義はconfig.iniで定義）
    for delete_string in config['FILESETTING']['ExcludeStringList']:
        concat_df = concat_df.replace(delete_string, '')

    # データ出力
    concat_df.to_csv(r'../output_{}.csv'.format(dt.strftime(dt.now(), '%Y%m%d%H%M')), encoding='shift-jis')

    print('\n')
    print('--' * 20)
    print('tool_delete_error_string Completed!')
    print('--' * 20)


if __name__ == '__main__':
    tool_vertical_and_horizontal_conversion()
    tool_give_timestamp()
    tool_delete_error_string()
    print('All Completed!')
