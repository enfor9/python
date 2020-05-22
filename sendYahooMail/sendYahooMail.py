import smtplib
import traceback

from email.mime.text import MIMEText

# SMTPサーバ
smtp_server = 'smtp.mail.yahoo.co.jp'
# SMTPのPORT番号
smtp_port_no = '465'
# ヤフードメイン

#実行前にサーバ側でSMTP利用を許可してください
def main(from_addr, passwd, to_addr, subject, message):
    try: 

        # 本文、件名、送信元、送信先を設定
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = from_addr
        msg['To'] = to_addr

        # SMTPサーバ指定
        smtp = smtplib.SMTP_SSL(smtp_server, smtp_port_no)
        # ログイン
        smtp.login(from_addr, passwd)
        # メール送信
        smtp.sendmail(from_addr, to_addr, msg.as_string())
        # 終了
        smtp.quit()
    except:
        traceback.print_exc()

if __name__ == "__main__":
    # それぞれ値を設定してください
    main("メールアドレスを設定","パスワードを設定","送信先アドレスを設定","件名を設定","本文を設定")