# Research Report — Final Fantasy Resonance (2026-11-02)

## 1. 遊戲身份
- Final Fantasy Resonance（ファイナルファンタジー レゾナンス，FFRS）。Square Enix 發行，Lancarse 協力開發，系列首部 HD-2D 作品。
- **單機買斷制，冇抽卡**。係 FFBE 第一季嘅重製版。
- 平台：PS5 / XSX|S / Switch / Switch 2 / PC。2026-10-22 發售（Steam 10-23）。Demo 包含完整第1章，存檔可承接。
- 伺服器：冇分區。版本：1.0。
- 官方繁中標題／繁中介面：未確認。資料內嘅中文名係系列慣用譯名或自行翻譯，**非官方**。

## 2. 術語
- 幻兵 = ビジョン / Vision：歷代 FF 角色化身，作用類似「職業」，每隻角色裝一隻。OSLink 繁中攻略都用「幻兵」。另有幻獣（Esper，9 隻），本次未收錄。
- stage = MR（マスタリーランク）1–9，上限 9（體驗版上限 5）。升 MR 會學技能，技能轉幻兵後仍可用；部份加成係「永続」。
- 覺醒 ★0→★3：喺 Grandport 搵光のモーグリ。材料依次為魔石の欠片、魔石、魔石の結晶。★3 上限由材料表推斷。
- 本資料用 MR 做 `stage`（`maxStage: 9`），覺醒寫喺 `reason`。

## 3. 數量
- 8 章、8 角色、26 幻兵、48 builds（high 12 / medium 26 / low 10）。
- 圖片 34/34 全部下載成功：幻兵係像素 sprite，角色係插畫頭像（300×300）。

## 4. 缺口
1. 推薦等級全部係 null（只知道第2章頭目 Lv18）。
2. 角色屬性大多係 null。只填咗：拉斯維爾＝冰、菲娜＝光、魔人菲娜＝闇；尼可＝水係由「水神の加護」推斷。稀有度不存在。
3. 菲娜（第5→6章）同拉斯維爾（第6章）嘅離隊時段未確認。第5章 build 假設菲娜唔喺隊。
4. 常闇のヴェリアス 冇證據可以操作，所以未收錄。
5. Leah / Tronn / Camille / Aileen / Archwitch Fina 等英文名取自 gmtreks 同 keengamer，未經官方核實。
6. 來源分歧：綾香俾尼可（kamigame）定菲娜（keengamer）；拉斯維爾用克勞德→賽菲羅斯定弗利昂；魔人菲娜用雅·修特拉定維多利亞；夏洛特評價 A 定 ★5。全部已列做 recommended／optional。
7. 第5–8章 MR 目標（7→9）屬推斷。
8. 章名、取得地點係自行翻譯。

## 5. SCHEMA 建議（未改 SCHEMA.md）
- builds 加 `targetAwakening`（0–3），phantoms 加 `maxAwakening`。
- `meta.terms` 加 awakening 同 esper。
- characters 加 `leaveChapterId`。
- phantoms 加 `tier`（SS/S/A）同 `category`（物理/魔法/輔助）。
- `rarity` 長期係 null，Design 唔好用嚟 sort/filter。
- `nameOriginal`（現為「日文 / English」）可拆做 `nameJa` + `nameEn`。
- 可選：加 `espers[]`。

## 6. 來源
- kamigame（主要來源）：https://kamigame.jp/ffrs/index.html，包括 ビジョン一覧、キャラ一覧、ストーリーチャート、最強パーティ、序盤おすすめ、ビジョンTier、キャラランキング、覚醒優先度、MR上げ（全部 URL 已列喺 data.json 嘅 `meta.sources`）。
- KeenGamer Best Visions: https://www.keengamer.com/articles/guides/final-fantasy-resonance-best-visions-for-every-character/
- OSLink 繁中: https://www.oslink.io/tw/blog/news/final-fantasy-resonance-beginner-guide.html
- RPG Site: https://www.rpgsite.net/news/20619-final-fantasy-resonance-a-new-hd-2d-ff-game-launches-october-22
- Nova Crystallis preview: https://novacrystallis.com/2026/09/final-fantasy-resonance-preview/
- 官方網站：https://www.jp.square-enix.com/FFRS/
- 圖片來自 kamigame（lh3.googleusercontent.com），© SQUARE ENIX，只限私人用途。

## 7. 未收錄
幻獸（Esper）、裝備、支線、鬥技場、十二武具之間。
