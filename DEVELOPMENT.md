# ProjectName 開發指南 / Development Guide

**角色：** 開發者**薄入口**——先對齊**需求層級**，再取**文檔組合**；細節留在各自的家，本檔不百科化。

```text
進入 → 選層級 → 打開文檔組合 → 改 code / 寫 note → 對層級做驗證
```

長文契約與寫作路由：

- 文件家 / research 索引 / 數字升格 → [docs/ownership/doc_structure_contract.md](docs/ownership/doc_structure_contract.md)（**O1.5**）
- 跨子類連續研究任務 → [docs/research/threads/](docs/research/threads/) 建 navigation-only thread；不放長表、不取代 evidence_ledger / module research。
- 接續任務 → [docs/research/threads/README.md](docs/research/threads/README.md)（先看 Active threads，再進單卡）
- **TODO = WIP 鎖**（sole active 一句 + link）；**不是**任務敘事 / 上下文恢復 → [DOC_MAINTENANCE § WIP](docs/DOC_MAINTENANCE.md) · [契約 C7](docs/ownership/doc_structure_contract.md)
- 格式、WIP=1、fact-owner → [docs/DOC_MAINTENANCE.md](docs/DOC_MAINTENANCE.md)
- 「我去哪寫」決策樹 → [docs/README.md](docs/README.md)
- 模組目標隔離 → [docs/ownership/README.md](docs/ownership/README.md)

---

## 1. 需求層級（先選這個）

層級愈高，**必讀 + 必寫 + 必驗**愈重。可只升不降：不確定時往上一級。

| 層級 | 何時用 | 意圖 |
|:--|:--|:--|
| **D0** | Bug fix / 純重構 / API 與預設行為不變 | 低摩擦合入 |
| **D1** | 單模組實驗、ablation、default-off probe、文檔-only | RESEARCH 線；不翻 production default |
| **D2** | 跨模組實驗、可被 PR/README **引用**的數字、NO-GO 結案 | 要有 evidence 家 |
| **D3** | 動到 eval 預設路徑、headline preset、inject/contract、hot path | 行為 / 合約敏感 |
| **D4** | 架構選型、ADR、paper claim、對外敘事 | 決策或出版物級 |

**與 O-series 對照（不互相取代）：**

| 治理 | 管什麼 |
|:--|:--|
| **O0 WIP=1** | 每模組同時最多一個 sole active |
| **O1 objective** | 這次 PR 的 primary 是 RUNTIME / RESEARCH / … |
| **O1.5 結構** | 檔案家、README 索引、promotion |
| **本表 D0–D4** | 這次工作要帶哪一包文檔與驗證 |

---

## 2. 各層文檔組合（讀 / 寫 / 驗）

「組合」= 該層**最低限度**應打開的檔。細節仍以各檔為準。

### D0 — 修復 / 重構

| | 文檔組合 |
|:--|:--|
| **讀** | 相關模組 `docs/modules/<m>/README.md`（I/O 一眼）；熱路徑見下方 §5 |
| **寫** | 通常**不寫**新 docs（見 [DOC_MAINTENANCE](docs/DOC_MAINTENANCE.md)「不需要寫文檔」） |
| **驗** | 單元 / 既有測試；你的 pre-push / CI 腳本 |

### D1 — 單模組研究 / default-off

| | 文檔組合 |
|:--|:--|
| **讀** | 模組 README + TODO；[doc_structure_contract](docs/ownership/doc_structure_contract.md) C1/C4；相關 [no_go_registry](docs/reference/no_go_registry.md) |
| **寫** | `docs/modules/<m>/research/<note>.md`（或跨模組則 `docs/research/<area>/`）+ **owning README 索引一行** + 文首 `doc-status` / `doc-promotion`；TODO 只更新 sole active **one-liner + link**；跨多步 → [threads/](docs/research/threads/) |
| **驗** | 實驗協議自洽即可；**不**要求改 headline |
| **禁** | 同 PR 翻 production default（RESEARCH + default → 拆 PR，見 [change_routing_matrix](docs/ownership/change_routing_matrix.md)） |

### D2 — 可引用結果 / 跨模組結論

| | 文檔組合 |
|:--|:--|
| **讀** | D1 組合 + [evidence_ledger](docs/research/evidence_ledger.md) 協議列；必要時 [report_data/README](report_data/README.md) |
| **寫** | D1 正文與索引；**若數字要被引用** → ledger 一列 和/或 no_go 一條 和/或 report_data 表（[契約 C5](docs/ownership/doc_structure_contract.md)）；模組 README GO/NO-GO **一行** |
| **驗** | 標註 commit/preset/host；noise 意識（自訂你的 Δ-metric 噪聲地板） |

### D3 — 生產路徑 / 合約

| | 文檔組合 |
|:--|:--|
| **讀** | 管線 / 預設合約文檔；相關 [decision-log](docs/research/)（closed 只讀）；[change_routing_matrix](docs/ownership/change_routing_matrix.md) |
| **寫** | 行為變更說明；必要時 ADR；合約 / preset 與 [module TODO](docs/modules/) / [docs/TODO.md](docs/TODO.md) 對齊；**新**決策線不得 silent reopen closed line |
| **驗** | smoke 至少一條 canonical 序列 / 用例；identity/default → 全套；headline 合約腳本（若有） |

### D4 — 架構 / 論文 / 對外敘事

| | 文檔組合 |
|:--|:--|
| **讀** | 架構入口；決策敘事 + ledger；method assets → [report_data](report_data/README.md)（**兩線互指、不互相覆寫**） |
| **寫** | ADR（`docs/decisions/`，按需建立）；paper 素材進 report_data 或 outline；claim 必須能指回 ledger / tables |
| **驗** | 無「只存在 chat 的數字」；必要時重建 paper assets |

---

## 3. 場景速查（靈活微調組合）

| 我要… | 建議層級 | 文檔組合（在層級底稿上加減） |
|:--|:--|:--|
| 修 crash / flake，行為不變 | **D0** | 測試 + pre-push |
| 單模組 ablation，default-off | **D1** | module research + README 索引 + TODO 連結 |
| 數據驅動 gate / signal 深度分析 | **D1** | [signal_analysis_ledger](docs/research/eval/signal_analysis_ledger.md)（一訊號一列；數字在 `out/`） |
| 可引用 e2e / 決策數字 | **D2** | evidence_ledger 一列 + source note |
| 改 `<baseline-preset>` 預設旋鈕 | **D3** | default-config + routing matrix + ledger（若報數字） |
| 寫 arXiv / tech report 段落 | **D4** | paper outline **或** report_data（先選線）+ source_map |
| 只更新文檔結構 / 索引 | **D1** | O1.5 契約 + DOC_MAINTENANCE checklist |

寫作目錄細節（檔放哪）：[docs/README 決策樹](docs/README.md)。

---

## 4. 現況快照

### Baseline

**生產 baseline preset = `<baseline-preset>`**（填入你的預設）。

<!-- fact-owner: current-baseline = docs/TODO.md -->

**數字唯一來源：** [docs/TODO.md](docs/TODO.md)「當前 Baseline」——本檔不嵌指標表。

```bash
# example — replace with your eval entrypoint
# python scripts/eval/run.py --preset <baseline-preset>
```

### 模組現狀總覽

> **Dashboard fact-owner：本節。** 只鏡射各 `docs/modules/<m>/TODO.md` 的 **sole active one-liner**（WIP 鎖），**不**鏡射細節、**不**另立第二待辦清單。  
> **任務敘事 / 接續** → [docs/research/threads/](docs/research/threads/README.md)；**事實** → module research / ledger。  
> **O0 / WIP=1：** 每模組 🔄 最多一個 active。規則：[DOC_MAINTENANCE § WIP](docs/DOC_MAINTENANCE.md)。

| 模組 | 狀態 | sole active（WIP 鎖） | TODO |
|------|------|---------------------|------|
| module-a | 📋 待辦 | — | [↗](docs/modules/module-a/TODO.md) |
| module-b | 📋 待辦 | — | [↗](docs/modules/module-b/TODO.md) |
| module-c | 📋 待辦 | — | [↗](docs/modules/module-c/TODO.md) |

全局矩陣 / 跨模組待辦：[docs/TODO.md](docs/TODO.md)。

---

## 5. 熱路徑與高頻命令

### 主線常改檔（填你的路徑）

| 意圖 | 起點 |
|:--|:--|
| Core runtime | `src/...` |
| Policy / association / scoring | `src/...` |
| Eval 編排 | `scripts/eval/...` |
| Preset / knobs | `configs/presets/` |

### 推送前

```bash
# replace with your hooks
# bash scripts/pre_push.sh
```

### 依層級加驗證

```bash
# D0/D1
# pytest tests/

# D3 常見
# python scripts/eval/run.py --preset <baseline-preset> --smoke
```

實驗分層（避免只看最終 headline metric）：module-local signal → 再 e2e；`local↑ + downstream↓` = regression。

### 分支（摘要）

- `main` only 合入目標；工作分支 `feat/*` `fix/*` `perf/*` `docs/*` `research/*`
- 不直接 push `main`；PR + CI
- 開分支前：工作項對齊 **module TODO sole active**（WIP 鎖）或全局 [docs/TODO.md](docs/TODO.md)；連續任務先讀 [threads/](docs/research/threads/README.md)

---

## 6. 衝突時誰說了算

1. **主路徑程式碼**（你的 runtime / eval 入口）
2. **合約 / 預設**（headline YAML、contract checkers、accepted ADR）
3. **事實家**（baseline → `docs/TODO.md`；決策數字 → `evidence_ledger`；模組 sole active → 本檔 dashboard 鏡射 module TODO）
4. **入口敘事**（本檔、pipeline、showcase）— 只鏡射，不另造數字

本檔**不是**語意百科，也**不是** paper 第二真相。

---

## 7. 入口地圖（其餘家）

| 需求 | 去 |
|:--|:--|
| 寫 docs / research 路由 | [docs/README.md](docs/README.md) · [O1.5 契約](docs/ownership/doc_structure_contract.md) |
| 格式 · WIP · fact-owner | [DOC_MAINTENANCE.md](docs/DOC_MAINTENANCE.md) |
| 目標隔離 · PR 檢查矩陣 | [docs/ownership/](docs/ownership/README.md) |
| NO-GO 總表 | [docs/reference/no_go_registry.md](docs/reference/no_go_registry.md) |
| 全局 research 入口 | [docs/research/README.md](docs/research/README.md) |
| 連續任務母線 | [docs/research/threads/](docs/research/threads/README.md) |
| Paper / publication assets | [report_data/README.md](report_data/README.md) |

---

## 原則（三條）

- 架構與合約決定什麼值得做；TODO sole active = WIP 鎖；threads = 怎麼接續。
- 單一原始碼檔原則上不超過你的專案上限（建議 **1000** 行）。
- **每個事實一個家**；入口只組合連結，不複製長表。
