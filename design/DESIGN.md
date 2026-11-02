# Design notes — Resonance 養成手帳 (prototype.html)

## Visual system
- **World**: classic FF blue menu windows on a night-sky ground. Deliberately single-theme (dark); `color-scheme: dark` on `:root`, every colour is a token, `body` has an explicit background. No light mode by choice.
- **Tokens** (`:root`): `--ink` page, `--ink-2` recessed wells, `--win-top/--win-bot` window gradient, `--frame/--frame-dim` borders, `--gold` cursor/pips/selection, `--gold-dim` "already trained" pips, `--core/--rec/--opt` priority, `--hi/--mid/--lo` confidence, `--rar-ssr/sr/r/n` rarity frames. Element colours live in JS `ELEMENT_COLOR` (火冰水雷風土光闇; unknown elements get a hashed hue).
- **Fonts** (Google Fonts): `DotGothic16` for all CJK/Latin UI text; `Press Start 2P` only for numbers, chapter pins and small caps labels (it has no CJK). Fallback stacks declared.
- **Components**: `.win` (3px white frame + dark outer ring + inner bevel + hard drop shadow), `.cur` (pixel hand cursor, generated at runtime from a 14x9 pixel map into `--hand`, shown on hover/focus/selected), `.node` (world-map chapter pin), `.card` (character window), `.equip` (phantom slot), `.pips` (stage meter), `.conf` (3-bar signal), `.prio` badge, `.chg` blinking NEW/SWAP/UP tag, `.ph-card`, `dialog.win` detail.
- **Motion** (all `steps()`, all disabled by `prefers-reduced-motion`): character idle bob (2 steps) with shadow squash, phantom float (4 steps), hop on card hover/focus, hand cursor nudge, selected chapter pin pulse, new-stage pips blink, stepped scanline wipe on chapter change, dialog opens with a stepped clip.

## Pixel sprites
`mountSprites()` turns `<span class="spr" data-kind data-id data-res>` slots into a small canvas (48px chars, 32px phantom minis, 56px in the dialog), drawing the image with `imageSmoothingEnabled=false` (square crop; tall character art is cropped from the top to keep the head). CSS scales it up with `image-rendering: pixelated`. Pixels are never read back, so cross-origin images are fine. If an image fails, `drawPlaceholder()` draws a deterministic mirrored invader sprite (12x12 chars, 14x14 phantoms) in the element colour, seeded by id.

## Interaction decisions
- **Chapter select** = horizontal world map (radiogroup; arrow keys / Home / End). Each pin shows a red badge with the number of characters that need new training in that chapter. Choice persists in `localStorage` key `ffr-guide:v1` (also tab and sort), all wrapped in try/catch.
- **Effective build carry-forward**: if a character has no build row for the selected chapter, the latest earlier chapter's build is shown, labelled "沿用第 N 章". Research does not need to repeat unchanged rows.
- **Change detection** (for the "只睇今章有變" filter, NEW/SWAP/UP tags and the map badges): only exact rows count. NEW = no earlier build; SWAP = different phantom from previous effective build; UP = same phantom, higher targetStage. On UP, pips already trained show dim gold and the new pips blink, so the user sees exactly what to train now.
- Multiple builds for the same chapter+character are allowed: the card shows the highest-priority one; the detail timeline lists all.
- Locked characters (unlock chapter later than selected) show as black silhouettes with "第 N 章先加入"; toggle hides them. Locked items are always sorted last.
- Sort: 優先度 / 名稱 (zh-Hant collation) / 目標 stage (desc) / 稀有度 (UR>SSR>SR>R>N). Filter: 職業, 屬性, priority chips (at least one stays on), changes-only, show-locked.
- **幻兵 tab**: per phantom, users at the selected chapter (effective builds) and the highest stage needed so far; sorted by need. Element filter applies; clicking a user chip opens that character.
- Character detail: modal `<dialog>` (Esc closes, focus returns), full route table across chapters, sources, image credit.
- Labels for "幻兵" and "stage" come from `meta.terms.phantom` / `meta.terms.stage`.

## 覺醒 axis (schema v0.2)
- **Card**: under the MR pips, a `目標 覺醒` row of pixel stars. The star shapes are two CSS masks (`--star-fill`, `--star-line`) generated at runtime from one 9x9 pixel map, the same way the hand cursor is made. Filled gold stars go up to `targetAwakening`; outline stars go up to `maxAwakening`. If `maxAwakening` is null, only the target count shows, with "n/?".
  - `targetAwakening: null`: the row is hidden.
  - `0`: dimmed outline stars plus 「唔使覺醒」.
  - `awakeningNote`, when present, shows as a small ※ line under the row.
  - The label comes from `meta.terms.awakening` (default 覺醒).
- **Change detection**: `upsOf(build, prevBuild)` compares stage and awakening against the previous effective build when the phantom is the same. A null previous awakening counts as 0. Either one going up makes it an UP change. That feeds the 「只睇今章有變」 filter, the map badges and the chapter stats. The tag text says which one went up (「MR 提升」/「覺醒 提升」). Stars already done last chapter show dim; the new stars blink like the new pips.
- **幻兵 tab**: a second meter shows 「最高要覺醒」, the highest `targetAwakening` among that phantom's users at the selected chapter. It is hidden if every user has null. User chips show ★n when n > 0. Phantoms sort by MR need, then awakening need.
- **Detail modal**: a new 覺醒 column with small stars, "—" for null, 「唔使」 for 0, and the note underneath.
- **Sort**: 「目標 覺醒」 sorts descending, with null last and MR as the tie-break. The option hides itself when no build has awakening data.
- Dummy data now uses `terms.stage = "MR"` and includes null, 0, 1, 2 and 3 values. Odin has `maxAwakening: null`. Barret in ch5 is an awakening-only UP.

## Integration (Coordinator)
1. **Data**: replace the contents of `<script id="guide-data" type="application/json">…</script>` with `research/data.json` verbatim. No other code changes. Do not include a literal `</script>` inside the JSON.
2. **Images**: all paths go through one function near the top of the main script:
   ```js
   var ASSET_BASE = "";
   function resolveImage(image) { … return ASSET_BASE + image.local; }
   ```
   Data paths are studio-root relative (`research/assets/characters/cloud.png`). For `studio/site/`, either set `ASSET_BASE = "../"` (local preview) or, for the published artifact, copy assets into `site/assets/...` and rewrite inside `resolveImage` (e.g. `p.replace(/^research\//, "")`), then publish them via the Artifact `files` map. Remote `image.url` is intentionally not used: the artifact CSP blocks external images. `data:` URIs also work if you inline images.
3. Missing values: `null` element/rarity/maxStage/recommendedLevel/howToGet are all handled (unknown maxStage shows "?").
4. JS syntax checked (JXA `new Function` parse); JSON validated. Visual render was not checked in a browser from this session.
