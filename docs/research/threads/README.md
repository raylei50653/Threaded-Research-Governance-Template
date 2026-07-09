# Research threads（navigation-only）

**定位：** 跨子類連續任務的**導航卡 / 母線**，不是新的事實家。

```text
TODO.md              = WIP lock / active pointer（sole active 一句）
threads/             = 連續任務母線（狀態 · 邊界 · 下一步）
module research      = 事實與分析
ledger/report_data/no_go = 升格後的正式事實
conversation hook    = 短期接力（應收進 thread）
```

**不做：**

- 不放長表、完整分析、可引用數字正文
- 不取代 `evidence_ledger` / `signal_analysis_ledger` / module research / `report_data`
- **不**取代 module TODO 的 WIP=1 鎖（thread 可多張；sole active 仍以 TODO 為準）

**結構契約：** [../../ownership/doc_structure_contract.md](../../ownership/doc_structure_contract.md)（O1.5）  
**薄入口：** [../../../DEVELOPMENT.md](../../../DEVELOPMENT.md)  
**模板：** [thread_template.md](thread_template.md)

---

## When to create a thread

```text
跨 2 個以上文檔家 / 子類
或連續 3 步以上
或會產生可引用數字 / policy / hook / audit
→ 建 thread
```

**不建：** 單次 bug fix、單次 ablation、一步能在 module research 結案的工作。

---

## Active threads

| Thread | Status (one-line) | Owner |
|:--|:--|:--|
| — | no active threads yet | — |

---

## File shape

Copy [thread_template.md](thread_template.md) → `<topic>_<YYYYMMDD>.md`.

**命名：** `<topic>_<YYYYMMDD>.md`（母線主題，不是每步一個檔）。  
**Same-PR：** 新增 thread → 本 README Active 表加一行。

---

## Role split

| 層 | 負責 |
|:--|:--|
| [DEVELOPMENT.md](../../../DEVELOPMENT.md) | 分層路由 D0–D4 · dashboard 只鏡射 sole active one-liner |
| module `TODO.md` | **WIP 鎖**（sole active + links）；非任務敘事 |
| module / research README | 局部入口與檔案索引 |
| **threads/** | 連續任務母線（狀態 · 邊界 · 下一步） |
| ledger / report_data / out/ | 事實與數字升格 |
