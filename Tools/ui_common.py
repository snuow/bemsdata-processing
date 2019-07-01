from tkinter import *
from tkinter import ttk
import Tools.tools_common as tool

LAYOUT =['ALL','縦横変換','タイムスタンプ付与','エラー文字列削除','']


class App(ttk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        """ウィジェットの作成."""
        # 計算結果の表示ラベル
        dispay_label = ttk.Label(
            self, text='データ処理ツール'
        )
        dispay_label.grid(
            column=0, row=0 ,rowspan=1, sticky=(N, S, E, W)
        )

        # レイアウトの作成
        # for no, tool_name in enumerate(LAYOUT):
        #     button = ttk.Button(self, text=tool_name, command=self.say_hi)
        #     button.grid(column=0, row=no, sticky=(N, S, E, W))
        # self.grid(column=0, row=0, sticky=(N, S, E, W))

        # ALLコマンドボタン
        button = ttk.Button(self,text='ALL',command=tool.tool_all)
        button.grid(column=0,row=1,sticky=(N,S,E,W))

        # 縦横変換ボタン
        button = ttk.Button(self , text='縦横変換' , command=tool.tool_vertical_and_horizontal_conversion)
        button.grid(column=0 , row=2 , sticky=(N , S , E , W))

        # タイムスタンプ付与ボタン
        button = ttk.Button(self , text='タイムスタンプ付与' , command=tool.tool_give_timestamp)
        button.grid(column=0 , row=3 , sticky=(N , S , E , W))

        # タイムスタンプ付与ボタン
        button = ttk.Button(self , text='エラー文字削除' , command=tool.tool_delete_error_string)
        button.grid(column=0 , row=4 , sticky=(N , S , E , W))

        self.grid(column=0 , row=0 , sticky=(N , S , E , W))

        # ProgressBar
        button = ttk.Button(self , text='ProgressBar' , command=self.generate_subwindow)
        button.grid(column=0 , row=5 , sticky=(N , S , E , W))


        # 横の引き伸ばし設定
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        # 縦の引き伸ばし設定。0番目の結果表示欄だけ、元の大きさのまま
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)

        # ウィンドウ自体の引き伸ばし設定
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

    def say_hi(self):
            print('hello world')

    def generate_subwindow(self):
        sub_win =Toplevel()
        sub_win.title('ProgressBar')
        sub_win.geometry('300x300')

def main():
    root = Tk()
    root.title('DataProcessingApplication')
    root.geometry('500x300')
    App(root)
    root.mainloop()


if __name__ == '__main__':
    main()