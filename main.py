"""
BEMSから出力されたデータを共通形式に変換するツールに通すための
データ前処理用のツールである。
"""
import Tools.tools_common as tool
import ui_common
import os

if __name__ == '__main__':

    tool.tool_vertical_and_horizontal_conversion()
    tool.tool_give_timestamp()
    tool.tool_delete_error_string()
    print('All Completed!')
