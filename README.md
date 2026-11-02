# Resonance 養成手帳

Final Fantasy Resonance 逐章養成攻略：每一章邊個角色配邊隻幻兵（Vision）、MR 要練到幾多、覺醒要幾多粒星。像素風、識郁、可以按章節 sort / filter。

> 私人用途。角色同幻兵圖片 © SQUARE ENIX，來源見 `research/REPORT.md`。

## 點樣睇

- 直接用瀏覽器開 `docs/index.html`
- 或者開 claude.ai 上面嘅私人 Artifact 版本

## 資料夾

| 路徑 | 內容 | 由邊個負責 |
|---|---|---|
| `BRIEF.md` | 項目要求同分工 | 統籌 |
| `SCHEMA.md` | 資料格式（研究同設計之間嘅合約） | 統籌 |
| `research/data.json` | 章節、角色、幻兵、每章配搭 | 資料專家 |
| `research/REPORT.md` | 資料來源、可信度、未確認事項 | 資料專家 |
| `research/assets/` | 角色同幻兵圖 | 資料專家 |
| `design/prototype.html` | 網站設計（用假資料） | UX/UI 設計 |
| `design/DESIGN.md` | 設計說明 | UX/UI 設計 |
| `build.py` | 將真資料放入設計 | 統籌 |
| `docs/` | 生成出嚟嘅網站（GitHub Pages 用） | `build.py` 生成 |

`site/` 都係 `build.py` 生成，專俾 claude.ai Artifact 用，所以冇放入 git。

## 點樣 update

1. 改 `research/data.json`（資料）或者 `design/prototype.html`（設計）
2. 重新生成網站：
   ```bash
   python3 -I build.py
   ```
3. 喺 GitHub Desktop commit 同 Push origin
