from genericpath import exists
import os
import sys
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
import os.path
import tkinter
import glob

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

#検索処理
def file_Search():
  #検索対象ディレクトリ
  searchDir = ''
  #検索ワード
  searchWord = ''
  #検索条件
  searchCondition = ''

  #検索対象ディレクトリを入力させる。
  while searchDir == '':
    print("Please enter a directory to search. > ")
    searchDir = input()

  #検索対象ディレクトリの末尾が「\」でない場合はtargetの末尾に「\」を追加する。
  if searchDir[-1] != '\\':
    searchDir = searchDir + '\\'

#検索ワードを入力させる。
  while searchWord == '':
    print("Please enter search word. > ")
    searchWord = input()
    searchCondition = searchDir + '**\\' + searchWord

  # Cドライブ配下の検索処理を実施する。再帰検索有効。
  for name in glob.glob(searchCondition,recursive=True):
    print(name)
  return


#メイン関数
def main():
  #ルートウィンドウ
  root = Tk()
  #ルートウィンドウのサイズ
  root.geometry('300x530')
  #ドライブレター一覧を取得
  existsDriveLetter = getExistsDriveLettrList()
  driveCombobox = ttk.Combobox(height=len(existsDriveLetter),width=2,values=existsDriveLetter,state='readonly')
  #ドライブの一覧用コンボボックスの初期選択値を設定する
  driveCombobox.set(existsDriveLetter[0])
  #ドライブ一覧をルートウィンドウに表示する
  driveCombobox.place(x=20,y=30)
  #検索用テキストボックス
  searchEntry = tkinter.Entry(width=25)
  #検索用テキストボックスをルートウィンドウに表示する
  searchEntry.place(x=60,y=30)
  #検索ボタン
  searchButton = tkinter.Button(text='search',command=file_Search)
  #検索ボタンをルートウィンドウに表示する
  searchButton.place(x=220,y=30)
  #結果一覧
  treeview = ttk.Treeview(show='headings',columns=1,height=20)
  #treeview
  treeview.column(1,width=250)
  treeview.heading(1,text='result')
  treeview.place(x=20,y=75)


  #ルートウィンドウを表示し続ける
  root.mainloop()

#
if __name__ == '__main__':
  sys.exit(main())