# main.py

while True:
    print("数値を入力してください")
    input_num = int(input()) # 入力コマンド

    if input_num == 0:
        print('プログラムを終了します')
        break
    # -- ここに処理を追加してみよう --
    elif input_num > 1 and input_num <= 9:
        print('一桁の数字です')
    elif input_num >= 10 and input_num <=99:
        print('二桁の数字です')
    else:
        print('該当するコマンドがありません')
