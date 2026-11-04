# CLAUDE.md — Resonance 養成手帳

Final Fantasy Resonance 逐章養成攻略網。用家（jokeryung）用廣東話溝通，請用廣東話回覆。

## 網站
- 公開網址（GitHub Pages，serve `docs/`）：https://jokeryung.github.io/ffr-guide/
- 私人 Artifact 版本：https://claude.ai/artifact/K9F5HnyTNZSBQ8bWiPiqGH（由 `site/index.html` + `site/assets/` 發佈；只可以喺用家部 Mac 嘅 Claude app 更新）

## 工作室分工
呢個項目用「三人工作室」模式做：
- **統籌**（主 session）：定規格、派工、核對資料、整合、向用家匯報。
- **資料專家**（subagent）：上網搵遊戲資料，只改 `research/data.json`，來源同不確定事項寫入 `research/REPORT.md`。
- **UX/UI 設計**（subagent）：只改 `design/prototype.html` 同 `design/DESIGN.md`。

兩個 subagent 之間嘅合約係 `SCHEMA.md`（而家係 v0.4）。要改資料格式，由統籌改 `SCHEMA.md`，再通知兩邊。詳細要求見 `BRIEF.md`。

## 點樣 update
1. 改資料：`research/data.json`；改設計：`design/prototype.html`。唔好直接改 `docs/` 或者 `site/`，嗰兩個係生成出嚟嘅。
2. 重新生成網站：
   ```bash
   python3 -I build.py
   ```
3. 驗證：
   - `research/data.json` 係有效 JSON；每條 build 嘅 characterId / phantomId / chapterId 都要對得上。
   - `targetAwakening` 唔可以超過嗰章材料容許嘅上限：第 1–3 章 ≤ ★1，第 4–6 章 ≤ ★2，第 7–8 章 ≤ ★3。
   - 同一章唔應該有兩個角色嘅**主力**（`purpose: "main"`）用同一隻幻兵；`skill` 可以輪住練。角色離隊嘅章節用 `absentChapterIds` 標明。
   - MR 每個角色＋幻兵分開計；★ 全隊共用，同一隻幻兵嘅星數唔可以隨章節下跌。
   - 有條件嘅話，喺瀏覽器開 `docs/index.html` 睇吓。
4. Commit 之後 push 去 `main`，GitHub Pages 大約一分鐘就會更新。

## 規則
- **資料要誠實**：唔好作資料。搵唔到嘅填 `null`；推斷出嚟嘅要寫明「推斷」，並且設 `confidence: "low"`。
- **Commit email**：一定要用 `337920974+jokeryung@users.noreply.github.com`，唔好用用家嘅真 email。
- 角色同幻兵圖 © SQUARE ENIX，repo 已經係公開，用家知道並接受呢個風險。
- 唔好改寫已經 push 咗嘅 git 歷史。
