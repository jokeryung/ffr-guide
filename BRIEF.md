# Studio Brief — Final Fantasy Resonance 養成攻略網

## 團隊
- **統籌 (Coordinator)**：主對話。定規格、派工、核對、整合、向用家匯報。
- **資料專家 (Research)**：上網搵遊戲資料，輸出 `research/data.json` + `research/REPORT.md`。
- **UX/UI 設計 (Design)**：設計網站，輸出 `design/prototype.html` + `design/DESIGN.md`。

## 用家要求
- 遊戲：Final Fantasy Resonance（伺服器待研究確認）
- 用途：自己用（私人）
- 核心功能：按「章節」揀進度 → 顯示嗰個章節每隻角色應該配邊隻幻兵、幻兵要練到咩 stage
- 必須有角色同幻兵圖
- 互動：揀章節、sort、filter
- 風格：**唔要 AI 感**，要有打機 style；人物同幻兵用**像素風格**，而且**識郁**（idle 動畫）
- 語言：繁體中文（廣東話用語可以），遊戲專有名詞附英文/日文原名

## 資料合約
`SCHEMA.md` 係 Research 同 Design 之間嘅合約。Design 用假資料都要跟呢個格式，咁統籌先可以直接替換做真資料。
如果 Research 發現遊戲機制同 schema 唔夾（例如「幻兵」其實冇 stage 而係用星級），喺 REPORT.md 提出修改建議，**唔好自己改 SCHEMA.md**。

## 資料夾
```
ffr-guide/
  BRIEF.md       ← 呢份
  SCHEMA.md      ← 資料格式
  build.py       ← 統籌：將真資料放入設計
  research/      ← Research 輸出 (data.json, REPORT.md, assets/)
  design/        ← Design 輸出 (prototype.html, DESIGN.md)
  docs/          ← 生成嘅網站（GitHub Pages：https://jokeryung.github.io/ffr-guide/）
  site/          ← 生成嘅網站（claude.ai Artifact 用，唔入 git）
```
