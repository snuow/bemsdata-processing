"""
BEMSから出力されたデータを共通形式に変換するツールに通すための
データ前処理用のツールである。
"""
import Tools.tools_common as tool
import Tools.ui_common as ui
import sys

if __name__ == '__main__':
    try:
        if sys.argv[1] == 'GUI':
            Mode = 1
        else:
            Mode = 0

    except IndexError:
        Mode = 0
        pass

    version = 'v1.0'
    message = 'データ前処理ツール　GUI'

    welcome_message = message + ' ' + version
    print(welcome_message)

    if Mode == 0:
        tool_list = ui.disp_tool()
        select_tools = input().split(',')

        for no, func in enumerate(select_tools):
            if func == '0':
                tool.tool_vertical_and_horizontal_conversion()
            elif func == '1':
                tool.tool_give_timestamp()
            elif func == '2':
                tool.tool_delete_error_string()
            elif func == '3':
                tool.tool_concat_dataframe()
            elif func == 'a':
                tool.tool_all()
            else:
                raise ValueError('Tool選択が間違っています。')

        print('All Completed!')
        print('Enterキーで終了します。')
        input()

    else:
        ui.main(welcome_message)

