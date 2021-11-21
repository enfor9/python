from genericpath import exists
import os
import sys
from tkinter import *
from tkinter import ttk 
import os.path

#ドライブレター一覧
driveLetterList = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#使用可能なドライブレター一覧を返す
def getExistsDriveLettrList():
  #使用可能なドライブレターを格納する変数
  existsDriveLetter = []
  #ループしてAからZまで使用可能なドライブレターを探索
  for drive in driveLetterList:
    #存在確認
    if os.path.exists(drive + ':'):
      existsDriveLetter.append(drive + ':')
  #使用可能なドライブレターを返却する
  return existsDriveLetter

#メイン関数
def main():
  #ルートウィンドウ
  root = Tk() 
  #ルートウィンドウのサイズ
  root.geometry('300x500')
  #ドライブレター一覧を取得
  existsDriveLetter = getExistsDriveLettrList()
  #ドライブの一覧用コンボボックス
  driveCombobox = ttk.Combobox(root,height=len(existsDriveLetter),width=2,values=existsDriveLetter,state='readonly')
  #ドライブの一覧用コンボボックスの初期選択値を設定する
  driveCombobox.set(existsDriveLetter[0])
  #ドライブ一覧をルートウィンドウに表示する
  driveCombobox.pack()
  #ルートウィンドウを表示し続ける
  root.mainloop()

#
if __name__ == '__main__':
  sys.exit(main())