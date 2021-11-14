import glob
#Cドライブ配下のファイルを検索する処理

#検索対象のファイル名を入力させる。
print("Please input search word.")
target = 'C:\**\\' + input()

# Cドライブ配下の検索処理を実施する。再帰検索有効。
for name in glob.glob(target,recursive=True):
  print(name)