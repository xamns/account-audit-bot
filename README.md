# Account Audit Bot (帳號清單自動整理與統計教學專案)

## 專案緣起
日常資訊管理與維運，經常需要檢查主機的帳號清單與數量。如果逐台手動登入，既花時間又容易遺漏。  
本專案以「自動化思維教學」為出發點，利用 Python 自動產生假主機帳號清單圖片與帳號數量統計概念，幫助需要這方面的人，可以熟悉資訊自動化的流程與報告產出。

## 特色
- **全程假資料**：本程式不連任何實體主機，純產生隨機帳號清單與統計，資安零風險，以概念的方式呈現。
- **圖文自動產出**：每台主機自動產出帳號清單圖檔，並生成帳號統計文字報告。
- **可用於教學/入門/課堂自動化實驗**。
- **MIT License 授權，歡迎自由複製/修改/分享。**

---

## 快速開始

在命令提示字元(cmd)依下列步驟執行：

```bash
# 1. 從 GitHub 下載專案原始碼
git clone https://github.com/xamns/account-audit-bot.git
cd account-audit-bot

# 2. 安裝依賴套件
pip install -r requirements.txt

# 3. 執行主程式
python account_audit.py

程式會在 output_accounts/ 目錄下產生帳號圖檔（如 server01_accounts.png）與帳號統計報告（account_summary.txt）。
✅ 圖片已產生: ./output_accounts\server01_accounts.png
✅ 圖片已產生: ./output_accounts\server02_accounts.png
✅ 圖片已產生: ./output_accounts\server03_accounts.png

✅ 帳號總結: ./output_accounts\account_summary.txt

注意事項
本專案僅供教學與自動化概念演示，無任何真實主機帳號、密碼資訊。

歡迎任意 clone、fork、學習、分享，或於課堂與自學時參考！

授權 License
本專案採用 MIT License，詳見 LICENSE。
