# 文檔撰寫規範 (Doc Writing Conventions)

> **去哪寫？** → 見 [docs/README.md](README.md) 的決策樹。  
> 本文件定義的是**格式細節**（ADR 編號、WIP、fact-owner、連結寫法）。

---

## 路徑連結規範

所有文檔內連結使用**相對於目前文件所在位置的相對路徑**。不要使用
`/docs/...`、`/src/...` 這類 repo-root 絕對 Markdown links。

```text
# good (from docs/modules/module-a/README.md)
../../ownership/doc_structure_contract.md
../../../DEVELOPMENT.md
```

不對：

```text
/docs/ownership/doc_structure_contract.md   ← repo-root 絕對路徑
```

---

## 不需要寫文檔

- 日常 bug fix、純重構，且 **API 與預設行為不變**
- 測試修 flake、註解修正、typo
- 已在 PR 描述說清楚、且不會被後續引用的一次性操作說明

需要寫時，寧可**一短 note + 索引一行**，也不要塞進 TODO。

---

## ADR 編寫規範（可選目錄 `docs/decisions/`）

### 何時新增

- 技術選型變更（換模型、換框架、換儲存）
- 核心算法調整
- 設計原則變更

### 狀態流轉

```text
Proposed → Accepted → (必要時) Superseded by ADR XXX
```

### 編號規則

- 序號連續。若範圍擴大，新增下一號，不修改舊的。
- 不回頭改已 Accepted 的內容（另開新 ADR 標 Superseded）。

---

## Doc Structure Contract（研究 / 模組家與索引）

**This is O1.5 of O-series**（docs-only）：檔案家、入口可發現性、evidence promotion。  
全文：[ownership/doc_structure_contract.md](ownership/doc_structure_contract.md)。

### 原則（詳見契約 C0–C9）

- **四家：** `docs/research/`（跨模組）· `docs/modules/<m>/`（模組）· `report_data/`（可重建 paper 資產）· `docs/archive/`（歷史）
- **數字 master：** 決策 / baseline → [research/evidence_ledger.md](research/evidence_ledger.md)；負結果 → [reference/no_go_registry.md](reference/no_go_registry.md)
- **入口 = 目錄：** 新增 research 檔的同一 PR **必須**更新對應 README 索引行
- **禁止幽靈路徑：** README 不得鏈到不存在的子目錄
- **新 research 文首標記**（HTML comment）：

```html
<!-- doc-status: active | parked | closed | archived -->
<!-- doc-promotion: none | ledger | report_data | archive | no_go -->
<!-- doc-date: YYYY-MM-DD -->
```

- **TODO = WIP 鎖，不是任務管理：** sole active 一句 + 連 thread 和/或 `research/`；無 active 時寫 `⏸️`。長文 / 結果 / 推理 → research 或 [threads/](research/threads/)（見契約 C7）

### 相關 checker

- 結構檢查：**phase 2**（見 [scripts/tools/README.md](../scripts/tools/README.md)）

---

## Workstream WIP（一模主一目標）

**This is O0 of O-series: Ownership / Objective Isolation**。

WIP=1 是 **ownership governance 的 process seal**（docs-only）：每個模組負責人至多一個 concurrent active 目標。

### 規則

```text
WIP = 1 per module owner  (O0 seal)
- DEVELOPMENT.md「模組現狀總覽」每個 🔄 列只寫「一個」active 目標 one-liner
- 各 docs/modules/<m>/TODO.md = WIP register：
    sole active 一句 + link(s) 到 thread / research
    無 active → 明確 ⏸️ / 無 active
    不寫長文、結果表、推理流水帳
- 跨多步 / 跨家任務 → docs/research/threads/ 導航卡
- 要開第二目標：同一變更內先收合或 park 第一個
- 已結案決策線僅在新證據下以「具名新線」重開
- 寫 paper 與改 production 行為是不同線；同一負責人不同時並進
```

### Dashboard

模組現狀一覽：[DEVELOPMENT.md 模組現狀總覽](../DEVELOPMENT.md)（**只**鏡射 module TODO 的 sole active one-liner）。

### 不在此規則內

- 跨模組 **依賴**不算第二目標，但 dashboard 應標註依賴關係。
- Parked one-liners 可列多項；只有 **sole active** 受 WIP=1 約束。
- Research threads 可多張並存（navigation）；**不得**被當成第二個 sole active 來源。

---

## 事實所有權與新鮮度 (Fact Ownership & Freshness)

核心原則見 [DEVELOPMENT.md §6](../DEVELOPMENT.md)：**每個事實只有一個家，其餘只鏡射並回連，不複製成獨立事實。**

### fact-owner marker

```html
<!-- fact-owner: <fact-id> = <repo-root-relative path> -->
```

- 路徑一律用 **repo-root 相對路徑**（如 `docs/TODO.md`）。
- 標記路徑 **等於所在檔案本身** → 該檔是這項事實的 **owner**。
- 標記路徑 **指向別的檔案** → 該段只是 **mirror**，必須附「唯一來源在 X」並回連。

目前建議定義的 fact-id：

| fact-id | owner |
|---------|-------|
| `current-baseline` | `docs/TODO.md`「當前 Baseline」節 |

---

## PR checklist（文檔）

```text
□ 新 research 檔有 doc-status / doc-promotion / doc-date
□ owning README 已加索引行（same PR）
□ 可引用數字已升格到 ledger / no_go / report_data（或明確 doc-promotion: none）
□ 無幽靈連結
□ module TODO 仍符合 WIP=1（sole active 一句或 ⏸️）
□ RESEARCH PR 未順便翻 production default
```
