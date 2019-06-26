# 概要
- BEMSの生データをとある共通形式に変換するためのデータフォーマットに変換するデータ前処理ツール群


# 機能
-[ ] 縦横変換ツール  
    - 行方向に流れるデータを、列方向に流れるデータに変更する  
    - ヘッダの行数はユーザーが自由に変更できるように設定ファイル(config.ini)を設ける  
    
-[ ] タイムスタンプ付与ツール  
    - ファイル名に付与された年月日をパースし、ファイル内のタイムスタンプとして利用する  
    - タイムスタンプ書式はユーザーが自由に変更できるように設定ファイル(config.ini)を設ける  
    
-[ ] 文字列削除ツール  
    - 「エラー」等の文字列をレコードから削除する  
    

# option
- 入力データに対して差分値をアウトプットする。