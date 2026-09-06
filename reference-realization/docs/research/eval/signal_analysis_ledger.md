# Signal Analysis Ledger（深度訊號分析總帳）

<!-- doc-status: active -->
<!-- doc-promotion: none -->
<!-- doc-date: YYYY-MM-DD -->
<!-- fact-owner: signal-depth-analysis = this file (index) + out/<study_id>/ (numbers) -->

**Purpose:** **一次一個 gate / 一個連續訊號** 做深度分析時，**只在這裡掛一列**。  
這是「分析過哪些訊號、結論 pointer、下一步」的**統一入口**；不是 e2e metrics 百科，也不是 production GO 表。

| 誰管什麼 | 家 |
|:--|:--|
| **本檔** | 深度分析**索引**（一訊號一列；狀態；一句 verdict；連 note + study） |
| **數字 master** | `out/<study_id>/`（json/csv；禁止把大表嵌死 markdown） |
| **可引用 e2e / 決策數字** | [../evidence_ledger.md](../evidence_ledger.md)（升格後才抄一行） |
| **NO-GO 結案** | [../../reference/no_go_registry.md](../../reference/no_go_registry.md) |
| **長 note 正文** | 通常 `docs/modules/<m>/research/` 或本目錄 eval note |

**協議（強制）：**

1. **一次一個 gate / 一個 score 欄**（可同 note 裡對照 hard pool，但不要一次掃十個 rule 當「深度分析」）。  
2. 新分析 → **本表加一列** + study_dir + 短 note；重測 → **新 `study_id`**，改 pointer，不改舊 study。  
3. 結論分層標清：coverage vs ranking vs online（自訂 layer 命名即可）。  
4. 本檔**不**嵌 master 表；orient 數字 as-of 一句即可，裁決以 study 為準。

開發入口：[DEVELOPMENT.md](../../../DEVELOPMENT.md) §3。

---

## 0. 狀態圖例

| Status | 含義 |
|:--|:--|
| `🔄 analyzing` | 正在挖；note 可 WIP |
| `✅ depth-done` | 單訊號深度讀完；有 study + note；**未**主張上線 |
| `⏸ parked` | 有意暫停；理由在 notes |
| `⬆ promoted` | 已進 ledger / no_go / preset 討論 |
| `∅ not-started` | 排隊；尚無 study |

---

## 1. 總表（唯一索引）

> 新列插在表**頂**（最新在上）。`signal_id` 穩定、可 grep。

| signal_id | 物理量 / gate | Layer | Status | Study (master) | Note | One-line verdict (as-of) |
|:--|:--|:--|:--|:--|:--|:--|
| `example.signal` | placeholder | L0 | `∅ not-started` | — | — | replace or delete |

---

## How to add

```text
1. Pick one signal_id.
2. Run study → write out/<study_id>/ (or project study dir).
3. Write short note under modules/<m>/research/ or research/eval/.
4. Add row here; index from module README if module-owned.
5. Promote to evidence_ledger / no_go only when cited outside the note.
```
