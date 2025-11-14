  window.initMap = () => {

    let map;

    const area = document.getElementById("map"); // マップHTMLの箱
    // マップの中心位置
    const center = {
      lat: 35.3926918,
      lng: 136.9493077
    };

    const styles = [
      //地図グレー、saturation(彩度)-100
      {
        stylers: [{
          saturation: -90
        }]
      }
    ];

    //マップ作成
    map = new google.maps.Map(area, {
      center,
      zoom: 7,
      styles: styles
    });

    //マーカー表示データ
    const markerData = [{
        "name": "宿坊 善光寺",
        "type": "zenkoji",
        "lat": 36.1387244,
        "lng": 137.2544694,
        "address": "岐阜県高山市天満町4-3",
        "url": "https://oterastay.com/zenkoji/"
      },
      {
        "name": "正伝寺",
        "type": "shodenji",
        "lat": 35.6503605,
        "lng": 139.7546265,
        "address": "東京都港区芝1丁目12-12",
        "url": "https://oterastay.com/shodenji/"
      },
      {
        "name": "宿坊 端場坊",
        "type": "habanobo",
        "lat": 35.381331,
        "lng": 138.429895,
        "address": "山梨県南巨摩郡身延町身延３４９３",
        "url": "https://www.habanobo.org/"
      },
      {
        "name": "大泰寺",
        "type": "daitaiji",
        "lat": 33.5894383,
        "lng": 135.8937043,
        "address": "和歌山県東牟婁郡那智勝浦町下和田775",
        "url": "https://oterastay.com/daitaiji/"
      },
      {
        "name": "宿坊 志摩房",
        "type": "shimabou",
        "lat": 35.37825,
        "lng": 138.426001,
        "address": "山梨県南巨摩郡身延町身延３５４３",
        "url": "https://oterastay.airhost.co/ja/houses/266330"
      },
      {
        "name": "宿坊 武井坊",
        "type": "takeibou",
        "lat": 35.381372,
        "lng": 138.422543,
        "address": "山梨県南巨摩郡身延町身延３５８３",
        "url": "https://oterastay.airhost.co/ja/houses/130996"
      },
      {
    "name": "正暦寺",
        "type": "shourekiji",
        "lat": 35.2911138,
        "lng": 135.2608284,
        "address": "京都府綾部市寺町堂ノ前４５",
        "url": "https://oterastay.com/shourekiji/"
      },
      {
        "name": "宿坊 志摩房",
        "type": "shimabou",
        "lat": 35.37825,
        "lng": 138.426001,
        "address": "山梨県南巨摩郡身延町身延３５４３",
        "url": "https://oterastay.airhost.co/ja/houses/266330"
      },
      {
        "name": "南アルプス法源寺",
        "type": "hougen-ji",
        "lat": 35.6148256,
        "lng": 138.4815008,
        "address": "山梨県南アルプス市十五所218番1",
        "url": "https://oterastay.com/hougen-ji/"
      },
      {
        "name": "観音院",
        "type": "kannon-in",
        "lat": 36.4115324,
        "lng": 139.3474893,
        "address": "群馬県桐生市東２丁目１３−１８",
        "url": "https://oterastay.com/kannon-in/"
      },
      {
        "name": "宿坊 岸之坊",
        "type": "kishinobo",
        "lat": 35.38198576826927,
        "lng": 138.42183684289165,
        "address": "山梨県南巨摩郡身延町身延３５９１",
        "url": "https://kishinobo.jp/"
      },
      {
        "name": "宿坊 松井坊",
        "type": "matsui-bo",
        "lat": 35.378628,
        "lng": 138.424601,
        "address": "山梨県南巨摩郡身延町身延３５６６",
        "url": "https://oterastay.com/matsui-bo/"
      },
    ];

    //マーカーを格納する配列
    const marker = [];

    //吹き出し（情報ウィンドウ）を格納する配列
    const infoWindow = [];

    // マーカーをクリックしたときのイベント登録
    const markerEvent = (i) => {
      marker[i].addListener('click', () => {
        for (const j in marker) {
          //マーカーをクリックしたときに他の情報ウィンドウを閉じる
          infoWindow[j].close(map, marker[j]);
        }

        //クリックされたマーカーの吹き出し（情報ウィンドウ）を表示
        infoWindow[i].open(map, marker[i]);
      });
    }

    // マーカー毎の処理
    for (let i = 0; i < markerData.length; i++) {

      //マーカー作成
      // 緯度経度のデータ作成
      const markerLatLng = new google.maps.LatLng({
        lat: markerData[i]['lat'],
        lng: markerData[i]['lng']
      });

      //マーカーオプション設定
      const markerOption = {
        position: markerLatLng, // マーカーを立てる位置を指定
        map: map, // マーカーを立てる地図を指定
        //icon: {
//          url: '/img/marker.png'
//        }
      }

      //原宿だったときのマーカー画像を設定
//      if (markerData[i]['type'] === 'harazyuku') {
//        markerOption.icon = '/img/marker04.png'
//      }
      //新宿だったときのマーカー画像を設定
     // if (markerData[i]['type'] === 'shinzyuku') {
//        markerOption.icon = '/img/maker05.png'
//      }


      //各データごとにマーカーを作成
      marker[i] = new google.maps.Marker(markerOption);

      // 各データごとに吹き出し（情報ウィンドウ）を作成
      infoWindow[i] = new google.maps.InfoWindow({
        content: `<div class="custom-info">
                <div class="custom-info-item name">
                ${markerData[i]['name']}
                </div>
                <div class="custom-info-item address">
                ${markerData[i]['address']}
                </div>
                <div class="custom-info-item google-map">
                <a href="${markerData[i]['url']}" target="_blank">URL</a>
                </div>
            </div>` // 吹き出しに表示する内容
      });

      // 各マーカーにクリックイベントを追加
      markerEvent(i);
    }

  }