from tkinter import *
from tkinter import ttk
import Tools.tools_common as tool
import sys

def disp_tool():
    tool_list = [ 'tool_vertical_and_horizontal_conversion' ,
                  'tool_give_timestamp' ,
                  'tool_delete_error_string' ,
                  'tool_concat_dataframe',
                  ]

    print('---'*20)
    print('a All')
    for no, tool in enumerate(tool_list):
        print(no,tool)

    print('---'*20)
    return tool_list


class App(ttk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.parent = master
        self.InitUI()
        self.create_widgets()

    def create_widgets(self):
        """ウィジェットの作成."""
        # 計算結果の表示ラベル
        dispay_label = ttk.Label(
            self, text='データ前処理ツール'
        )
        dispay_label.grid(
            column=0, row=0 ,rowspan=4, sticky=(N, S, E, W)
        )

        # ALLコマンドボタン
        button = ttk.Button(self,text='ALL',command=tool.tool_all)
        button.grid(column=0,row=1,sticky=(N,S,E,W))

        # 縦横変換ボタン
        button = ttk.Button(self , text='縦横変換' , command=tool.tool_vertical_and_horizontal_conversion)
        button.grid(column=0 , row=2 , sticky=(N , S , E , W))

        # タイムスタンプ付与ボタン
        button = ttk.Button(self , text='タイムスタンプ付与' , command=tool.tool_give_timestamp)
        button.grid(column=0 , row=3 , sticky=(N , S , E , W))

        # エラー文字削除ボタン
        button = ttk.Button(self , text='エラー文字削除' , command=tool.tool_delete_error_string)
        button.grid(column=0 , row=4 , sticky=(N , S , E , W))

        # データ結合
        button = ttk.Button(self , text='データ結合' , command=tool.tool_concat_dataframe)
        button.grid(column=0 , row=5 , sticky=(N , S , E , W))

        self.grid(column=0 , row=0 , sticky=(N , S , E , W))

        # # ProgressBar
        # button = ttk.Button(self , text='ProgressBar' , command=self.generate_subwindow)
        # button.grid(column=0 , row=6 , sticky=(N , S , E , W))


        # 横の引き伸ばし設定
        self.columnconfigure(0, weight=4,uniform='group1')
        self.columnconfigure(1, weight=1,uniform='group1')
        # self.columnconfigure(2, weight=1)
        # self.columnconfigure(3, weight=1)


        # 縦の引き伸ばし設定。0番目の結果表示欄だけ、元の大きさのまま
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5 , weight=1)

        # ウィンドウ自体の引き伸ばし設定
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

    def InitUI(self):
        self.text_box = Text(self.parent , wrap='word' , height=11 , width=50)
        self.text_box.grid(column=1 , row=0 , columnspan=2 , sticky='NSWE' , padx=5 , pady=5)
        sys.stdout = StdoutRedirector(self.text_box)


class StdoutRedirector(object):
    def __init__(self , text_widget):
        self.text_space = text_widget

    def write(self , string):
        self.text_space.insert('end' , string)
        self.text_space.see('end')


def main(message):
    root = Tk()
    root.title('DataProcessingApplication')
    root.geometry('540x300')
    App(root)
    print(message)
    root.mainloop()


if __name__ == '__main__':
    main()