class ErrorChecker():
    def __init__(self,df):
        self.df = df

    def missing_values_check(self):
        if list(self.df[self.df.isnull().all(axis=1)].index) == []:
            print('欠損はおそらくありません。')
        else:
            for _ in list(self.df[self.df.isnull().all(axis=1)].index):
                print(_)
            print('欠損値の可能性があります。確認してください。')


if __name__ == '__main__':
    pass