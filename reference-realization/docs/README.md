# ProjectName 文檔庫 / Docs Index

> **文檔維護原則：一個文檔只回答一個問題。透過相對索引串聯，不靠無限合併。**

開發薄入口：[DEVELOPMENT.md](../DEVELOPMENT.md)  
結構契約：[ownership/doc_structure_contract.md](ownership/doc_structure_contract.md)  
格式 / WIP / fact-owner：[DOC_MAINTENANCE.md](DOC_MAINTENANCE.md)

---

## 📂 核心目錄架構

| 路徑 | 角色 |
|:--|:--|
| [modules/](modules/) | 模組卡 + 模組研究（copy from [`_template/`](modules/_template/)） |
| [research/](research/) | 跨模組實驗、evidence ledger、threads |
| [research/threads/](research/threads/) | 連續任務**導航**母線（非證據家） |
| [reference/](reference/) | 共享基準、runbooks、[NO-GO 總表](reference/no_go_registry.md) |
| [ownership/](ownership/) | O-series：WIP、結構契約、routing |
| [archive/](archive/) | 歷史 one-shot / 廢棄設計 |
| [../report_data/](../report_data/) | 可重建 paper 表/圖（與 decision narrative 互指） |

---

## ✍️ 開發者寫作導覽（我去哪裡寫？）

```text
我做了什麼？                          →  去哪個目錄？                    →  寫什麼 / 必做
──────────────────────────────────────────────────────────────────────────────────────────────
1. 單模組實驗 / ablation              →  modules/<m>/research/          →  全文 + 父 README 索引一行
2. 全局 / 跨模組實驗                  →  research/<area>/               →  子目錄或 research/README 索引
3. 多步 / 跨家連續任務                →  research/threads/              →  導航卡 only + threads README 索引
4. 可引用 baseline / 決策數字         →  research/evidence_ledger.md    →  加列 + 連 source
5. 論文 claim / 可重建表圖            →  report_data/                   →  source_map 或 README 回連
6. 負結果 / default-off 結案          →  reference/no_go_registry.md    →  短列 + evidence link
7. 結案 one-shot / 廢棄設計           →  archive/                       →  活躍索引移除或標 historical
8. 重大技術選型                       →  decisions/（可選）             →  下一號 ADR
9. 任務 WIP 鎖                        →  modules/<m>/TODO.md            →  sole active 一句；長文不塞 TODO
──────────────────────────────────────────────────────────────────────────────────────────────
※ 日常 Bug fix、純重構 (API 外部行為未變) → 無需新增/更新文檔。
※ 完整契約：ownership/doc_structure_contract.md
```

---

## 🔗 文檔寫作規範

請遵守 **[DOC_MAINTENANCE.md](DOC_MAINTENANCE.md)**：

- 相對路徑連結
- WIP=1
- fact-owner 不複製第二真相
- PR checklist
