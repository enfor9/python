#requestsとmastodon.pyとtqdmライブラリをインストールしてね
#同階層にアクセストークンとクライアントキーを書いたtxtファイルをそれぞれ配置してね

from mastodon import Mastodon
from time import sleep
from tqdm import tqdm
import traceback


#インスタンスURLをユーザーが手動で設定してください(例：https://mstdn.jp/)
instance_url= ''

#ログイン
def login():
    mstdn = Mastodon(
        #同階層にクライアントキー記載のtxtファイルをユーザが手動で配置すること
        client_id='cid_file.txt',
        #同階層にアクセストークン記載のtxtファイルをユーザが手動で配置すること
        access_token='access_token.txt',
        #インスタンスURL
        api_base_url=instance_url
    )
    return mstdn


#待機と進捗表示
def waitAndProgress(prm):

    if prm == 'get':
      print('最新の1件のtootを取得中...')
    else:
      print('取得した最新のtootを削除中...')

    #Too Many Requests対策でAPIアクセス後30秒間待機
    for _ in tqdm(range(30)):
      sleep(1)

#プログラム開始
def main():
    #ログイン
    mstdn = login()

    try:  
      #削除行数
      i = 0
      while True:
        waitAndProgress('get')
        #toot削除対象アカウント取得
        myAccount = mstdn.account_verify_credentials()
        #最新toot取得(1件)
        recentToot = mstdn.account_statuses(myAccount, limit=1)

        #取得したtoot情報のIDを取得
        tootId = recentToot[0]['id']
        waitAndProgress('delete')
        #toot削除
        mstdn.status_delete(tootId)
        #削除行数可視化
        i = i + 1
        print(str(i) + '件目のtoot削除！')
    except:
      traceback.print_exc()


#エントリーポイント
if __name__ == "__main__":
    main()