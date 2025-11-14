<?php


/* -- 以下、基本の設定 ------------------------------------------------------------------------------------------------------------------------------------------------- */


//【必須】 自分のメールアドレスの設定 -- 複数のメールアドレスに送信したい場合は、以下の行をコピーして増やしていけばOKです。行頭の//を消せば有効となります。いくつでも追加可能。 --
$rm_send_address[] = 'business@oterastay.com';
//$rm_send_address[] = 'test@gmail.com';


//【必須】 サンクスページのURL -- index.htmlからの相対パス、またはhttp://からの絶対パス --
$rm_thanks_page_url = 'thanks.html';



/* -- 以下、自分＆相手に届くメールの設定 ------------------------------------------------------------------------------------------------------------------------------------- */


//【任意】 自分(サイト管理者)や相手(フォーム入力者)に届くメールの送信元アドレス -- 複数設定は不可 --

// ( 補足説明 )
// 通常これは記入する必要はありません。以下の初期状態のように空欄のままにしておけばOK。
// なりすまし判定を受けてメールが受信できない場合にのみ、以下のページを参考にして設定すると良いでしょう。
// https://www.1-firststep.com/archives/15075
$rm_from_address = 'business@oterastay.com';




/* -- 以下、自分に届くメールの設定 ------------------------------------------------------------------------------------------------------------------------------------- */


//【任意】 自分に届くメールの題名
$rm_send_subject = 'お寺ヨガ（英語ページ）の紹介資料ダウンロードがありました。';


//【任意】 自分に届くメールの本文 -- EOMからEOM;までの間の文章を自由に変更してください。 --
$rm_send_body = <<<EOM

メールフォームからお寺ヨガ（英語ページ）の紹介資料ダウンロードがありました。
お問い合わせの内容は以下の通りです。

EOM;




/* -- 以下、相手への自動返信メールの設定 ------------------------------------------------------------------------------------------------------------------------------- */


//【任意】 相手に自動返信メールを送るかどうか -- 送らない場合は0、送る場合は1にしてください。 --
$rm_reply_mail = 1;


//【だいたい必須】 メールの差出人名に表示される自分の名前 -- 相手への自動返信メールに使用されます --
$rm_send_name = 'OTERA STAY';


//【任意】 相手に届く自動返信メールの題名
$rm_thanks_subject = 'Download temple yoga introduction materials';


//【任意】 相手に届く自動返信メールの本文 -- EOMからEOM;までの間の文章を自由に変更してください。 --
$rm_thanks_body  = <<<EOM

Thank you for downloading the "Temple Yoga Introduction Material" from our website.

You can access the requested document via the following URL:
Please check the content at your convenience.

If you have any questions or require further assistance, please feel free to contact us.

Document Name: Temple Yoga Introduction Material
https://drive.google.com/file/d/1k46THxuajOrU5PzzXy-l1aQlXhBDvyHR/view

Additionally, if you have provided any inquiries in the optional contact form, our representative will reach out to you separately.

We appreciate your continued support.

EOM;



//【だいたい必須】 相手に届く自動返信メールの最後に付加される署名 -- EOMからEOM;までの間の文章を自由に変更してください。 --
$rm_thanks_body_signature = <<<EOM

○●───────────────────────────────────●○

Share Wing Co., Ltd.
Corporate Sales Department
〒150-0031
Sakuragaoka Front II Building, 3rd Floor
16-13 Sakuragaoka-cho, Shibuya-ku, Tokyo
Email: business@oterastay.com
Website: https://oterastay.com/

○●───────────────────────────────────●○

EOM;