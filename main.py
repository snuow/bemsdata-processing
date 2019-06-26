"""
BEMSから出力されたデータを共通形式に変換するツールに通すための
データ前処理用のツールである。
"""
import Tools.tools_common as tool
import Tools.ui_common as ui
import os

if __name__ == '__main__':
    tool_list = ui.disp_tool()
    select_tools = input().split(',')

    for no, func in enumerate(select_tools):
        if func == '0':
            tool.tool_vertical_and_horizontal_conversion()
        elif func == '1':
            tool.tool_give_timestamp()
        elif func == '2':
            tool.tool_delete_error_string()
        elif func == 'a':
            tool.tool_vertical_and_horizontal_conversion()
            tool.tool_give_timestamp()
            tool.tool_delete_error_string()
        else:
            raise ValueError('Tool選択が間違っています。')

    print('All Completed!')
