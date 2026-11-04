# Data Schema v0.3（v0.2：覺醒星數；v0.3：每個角色多隻幻兵、連戰攻略） (`research/data.json`)

一個 JSON 檔，頂層結構：

```jsonc
{
  "meta": {
    "game": "Final Fantasy Resonance",
    "server": "Global / JP / TW / CN ...",
    "gameVersion": "x.y",
    "lastUpdated": "2026-11-02",
    "terms": {                       // 遊戲內術語對照，Design 用嚟做 label
      "phantom": "幻兵",
      "stage": "stage",              // 例如「突破」「覺醒」「星級」— 按遊戲實際叫法
      "awakening": "覺醒"            // v0.2：第二條養成軸（★）
    },
    "sources": [{ "title": "", "url": "" }]
  },

  "chapters": [
    {
      "id": "ch1",
      "order": 1,
      "name": "第一章 ……",
      "nameOriginal": "Chapter 1 ……",
      "recommendedLevel": "1-20",    // 可選
      "notes": "呢章重點/難點"
    }
  ],

  "characters": [
    {
      "id": "cloud",
      "name": "克勞德",
      "nameOriginal": "Cloud",
      "role": "攻擊 / 坦克 / 治療 / 支援 ...",
      "element": "火 / 冰 / ...",   // 冇就 null
      "rarity": "SSR",               // 冇就 null
      "howToGet": "第一章劇情",
      "unlockChapterId": "ch1",      // 幾時開始用得到
      "absentChapterIds": [],        // v0.2：劇情離隊嘅章節（嗰章唔沿用舊配搭）
      "absentNote": "",              // v0.2：可選，離隊說明
      "image": { "local": "research/assets/characters/cloud.png", "url": "原圖網址", "credit": "來源" },
      "notes": ""
    }
  ],

  "phantoms": [
    {
      "id": "ifrit",
      "name": "伊弗利特",
      "nameOriginal": "Ifrit",
      "type": "攻擊 / 防禦 / ...",
      "element": "火",
      "rarity": "SR",
      "maxStage": 5,                 // 最高可以練到幾多
      "maxAwakening": 3,             // v0.2：覺醒最高幾多粒星；唔知填 null
      "howToGet": "",
      "unlockChapterId": "ch2",
      "image": { "local": "research/assets/phantoms/ifrit.png", "url": "", "credit": "" },
      "notes": ""
    }
  ],

  // v0.3：同一個角色同一章可以有多條 builds（每隻幻兵一條）。
  // 某隻幻兵喺某章冇新一條，就沿用佢最近一章嘅目標。
  "builds": [
    {
      "chapterId": "ch2",
      "characterId": "cloud",
      "phantomId": "ifrit",
      "purpose": "main",             // v0.3：main 呢章主力裝備 / skill 練嚟學技能或者永續加成 / alt 可選替代
      "learnSkills": [],             // v0.3：可選，練呢隻要學到嘅技能或者加成名
      "targetStage": 3,              // 喺呢章應該練到幾多
      "targetAwakening": 1,          // v0.2：喺呢章應該覺醒到幾多粒星（0 = 唔使覺醒）；冇資料填 null
      "awakeningNote": "",           // v0.2：可選，點解要覺醒 / 材料提示（一句）
      "priority": "core",            // core 必練 / recommended 推薦 / optional 可選
      "reason": "點解咁配（一兩句）",
      "confidence": "high",          // high 多個來源一致 / medium 單一可靠來源 / low 推斷或有爭議
      "sources": ["url"]
    }
  ],

  // v0.3：打法／挑戰內容攻略（例如 16 連打配技）
  "challenges": [
    {
      "id": "combo-16",
      "name": "16 連打",
      "nameOriginal": "遊戲內原名",
      "unlock": "幾時／點樣開放",
      "description": "規則、限制（例如中途可唔可以回復、換隊）",
      "recommendedLevel": null,
      "tips": ["通用打法重點"],
      "party": [                     // 推薦配置
        {
          "characterId": "rain",
          "phantomId": "warrior-of-light", // 可以係 null
          "targetStage": 9,
          "targetAwakening": 3,
          "skills": [],              // 要帶嘅技能、配置
          "equipment": [],           // 片或者來源有講先填
          "notes": ""
        }
      ],
      "battles": [                   // 逐場；搵唔到就空陣列
        { "order": 1, "enemy": "", "notes": "" }
      ],
      "confidence": "medium",
      "sources": ["url"]
    }
  ]
}
```

規則：
- 所有 `id` 用細楷英文 kebab-case。
- `builds` 每條都要有 `confidence` 同至少一個 `sources`（confidence = low 可以冇來源，但要喺 reason 講明係推斷）。
- 搵唔到嘅欄位填 `null`，唔好作。

- v0.2：`targetAwakening` 嘅可信度跟同一條 build 嘅 `confidence`；如果覺醒建議係推斷而 MR 建議有來源，喺 `awakeningNote` 寫明「推斷」。
- v0.3：影片資料要標明出處同時間點；睇唔到或者聽唔清楚嘅內容填 `null`，唔好估。
- v0.3：MR 係每個角色＋幻兵分開計；★ 係全隊共用，所以同一隻幻兵嘅 `targetAwakening` 只可以跟章節上升。
