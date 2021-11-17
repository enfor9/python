import glob
#Cドライブ配下のファイルを検索する処理

#検索対象ディレクトリ
searchDir = ''
#検索ワード
searchWord = ''
#検索条件
searchCondition = ''

#検索対象ディレクトリ

while searchDir == '':
  print("Please enter a directory to search. > ")
  searchDir = input()

#検索対象ディレクトリの末尾が「\」でない場合はtargetの末尾に「\」を追加する
if searchDir[-1] != '\\':
  searchDir = searchDir + '\\'

#検索ワードを入力させる
while searchWord == '':
  print("Please enter search word. > ")
  searchWord = input()
  searchCondition = searchDir + '**\\' + searchWord

# Cドライブ配下の検索処理を実施する。再帰検索有効。
for name in glob.glob(searchCondition,recursive=True):
  print(name)