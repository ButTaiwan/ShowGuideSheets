# Show Guide Sheets | 稿紙

Glyphs.app plug-in for displaying guide sheets for the glyph you are editing. This can be helpful especially for CJK glyphs editing.
You can create different guide sheets for different scripts. Each master may have different ones.
After installation, turn it on or off by choosing *View > Show Guide Sheets* (zh-Hant: 稿紙, ja: 原稿用紙)

這是一個 Glyphs 外掛程式，可在字符編輯畫面中顯示背景的稿紙，非常適合 CJK 文字編輯時定義字身框、字面框，以及各種編輯參考用框線。
每個主板的稿紙是分開的，即使是多主板編輯時，也能輕易管理不同的框線設定。
另外，不同語系的稿紙也可以分開定義。這表示漢字、假名、注音符號、韓文都可以各自有不同的稿紙背景。
在安裝外掛程式後，別忘記點選 顯示 > 顯示稿紙 (en: *Show Guide Sheets*) 打開它。

これは Glyphs のプラグインで、グリフの編集ビューの背景に原稿用紙（自由にデザインできるのであえて方眼紙と呼ばない）を表示することができます。
和文など CJK の文字デザインでは仮想ボディや字面など、デザインに必要なガイドが多岐にあるため、役に立つと思います。
マスターごとに違うデザインにすることもできるし、文字体系ごとに違う原稿用紙を用意することも可能。
インストールして、メニューの 表示 > 原稿用紙を表示 でオンにしてください。

![ShowGuideSheets](ShowGuideSheets.png)



## How to use | 使用方式 | 使い方

### English
1. Create a new glyph to make your own guide sheet. The glyph name should be `_guide.XXX`, where *XXX* is the script name of character. e.g. *_guide.han*, *_guide.kana*, *_guide.bopomofo*, *_guide.hangul* ... (or `_guide.any` for any script.)
2. Add text notes by annotation tool if you need.
3. Now you can see the guide in the background when you edit glyphs. (It will not display anything if the zoom of the current tab is below 250px.)
4. Nodes which on the paths of guides will be highlighted. (It works when the zoom more than 400px)


### 繁體中文
1. 建立新字符來設計你的稿紙。字符名稱必須是 `_guide.XXX`，其中 *XXX* 表示文字語系，例如 *_guide.han* (漢字), *_guide.kana* (假名), *_guide.bopomofo* (注音), *_guide.hangul* (韓文)...，或是也可建立 `_guide.any` 適用於所有文字（但應該沒什麼用）。
2. 若需要加上文字說明，可以用「註記」工具在適當位置加註文字。
3. 這樣在編輯文字時，就會看到背景出現稿紙了。（注意編輯面板必須大於 250px 時才會顯示。）
4. 當控制點接觸稿紙上的線條，會被凸顯顯示。（注意編輯面板必須大於 400px 時才會顯示。)


### 日本語　
1. まずは原稿用紙のグリフを作成してください。グリフ名は `_guide.XXX` で、*XXX* は文字体系を指定してください。たとえば *_guide.han* (漢字), *_guide.kana* (仮名), *_guide.hangul* (ハングル)…。また、 `_guide.any` はあらゆる文字に適用します（逆に使えないけど）。
2. メモ記述を入れたい場合は、注釈ツールでテキストをつけてください。
3. 編集ビューで該当文字体系のグリフを編集する場合、背景に原稿用紙が表示されます。（ズームが 250 以下だと表示されません。）
4. ガイドのパスの上に乗せたポイントはハイライトされます。（ズームが 400 以下だと表示されません。）



## Custom Parameter | 自訂參數 | カスタムパラメータ

You can change the color of guide lines. Just set the font custom parameter `Guide Color` in Hex color code, e.g. FF0000 meanst red lines. 

想要更改稿紙線條顏色，可以在字型資訊視窗中設定字型的自訂參數。名稱為 `Guide Color` ，請設定 6 位數的十六進位色碼。例如 FF0000 表示紅色。

ガイドの色は変更できます。フォントパラメータ `Guide Color` を作って、6 桁の十六進数のカラーコードを指定してください。たとえば FF0000 は赤です。



## Requirements

The plug-in works both in Glyphs 2 and Glyphs 3. I can only test it in latest app, and perhaps it crashs on earlier versions.

此外掛程式適用於 Glyphs 2 與 Glyphs 3，但只在目前最新版本測試過。

このプラグインは Glyphs 2 と Glyphs 3 に対応しています。ただし最新バージョンでしかテストしていません。



## License

Copyright 2021 But Ko (@buttaiwan).
Based on sample code by Georg Seifert (@schriftgestalt).

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

See the License file included in this repository for further details.
