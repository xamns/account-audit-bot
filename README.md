# Account Audit Bot (帳號清單自動整理與統計教學專案)

## 快速開始

### Windows 11 命令提示字元 (cmd)

```cmd
# 1. 從 GitHub 下載專案原始碼
git clone https://github.com/xamns/account-audit-bot.git
cd account-audit-bot

# 2. 建立虛擬環境
python -m venv venv

# 3. 啟動虛擬環境
venv\Scripts\activate

# 4. 安裝依賴套件
pip install -r requirements.txt

# 5. 執行主程式
python account_audit.py

# 6. 使用完畢後，停用虛擬環境
deactivate
```

### Linux/macOS 終端機

```bash
# 1. 從 GitHub 下載專案原始碼
git clone https://github.com/xamns/account-audit-bot.git
cd account-audit-bot

# 2. 建立虛擬環境
python3 -m venv venv

# 3. 啟動虛擬環境
source venv/bin/activate

# 4. 安裝依賴套件
pip install -r requirements.txt

# 5. 執行主程式
python account_audit.py

# 6. 使用完畢後，停用虛擬環境
deactivate
```

### 執行結果

程式會在 `output_accounts/` 目錄下產生帳號圖檔（如 `server01_accounts.png`）與帳號統計報告（`account_summary.txt`）。

```
✅ 圖片已產生: ./output_accounts\server01_accounts.png
✅ 圖片已產生: ./output_accounts\server02_accounts.png
✅ 圖片已產生: ./output_accounts\server03_accounts.png

✅ 帳號總結: ./output_accounts\account_summary.txt
```

## 虛擬環境管理

### 為什麼使用虛擬環境？
- **隔離性**：避免套件版本衝突，不影響系統 Python 環境
- **可移植性**：確保在不同機器上有一致的執行環境
- **易於清理**：專案結束後可直接刪除整個 `venv` 資料夾

### 常用指令
```bash
# 檢查虛擬環境是否啟動（提示符會顯示 (venv)）
# Windows: (venv) C:\path\to\project>
# Linux:   (venv) user@host:~/project$

# 查看已安裝的套件
pip list

# 更新 requirements.txt
pip freeze > requirements.txt

# 完全移除專案（包含虛擬環境）
# 先退出虛擬環境
deactivate
# 然後刪除整個專案資料夾
# Windows: rmdir /s account-audit-bot
# Linux:   rm -rf account-audit-bot
```

## 專案緣起

日常資訊管理與維運，經常需要檢查主機的帳號清單與數量。如果逐台手動登入，既花時間又容易遺漏。  
本專案以「自動化思維教學」為出發點，利用 Python 自動產生假主機帳號清單圖片與帳號數量統計概念，幫助需要這方面的人，可以熟悉資訊自動化的流程與報告產出。

## 特色

- **全程假資料**：本程式不連任何實體主機，純產生隨機帳號清單與統計，資安零風險，以概念的方式呈現。
- **圖文自動產出**：每台主機自動產出帳號清單圖檔，並生成帳號統計文字報告。
- **跨平台支援**：Windows 11、Linux、macOS 均可執行。
- **虛擬環境隔離**：不影響系統 Python 環境，易於管理和清理。
- **可用於教學/入門/課堂自動化實驗**。
- **MIT License 授權**，歡迎自由複製/修改/分享。

## 系統需求

- Python 3.7 或以上版本
- Git（用於下載專案）
- 支援的作業系統：Windows 11、Linux、macOS

## 疑難排解

### Windows 常見問題
```cmd
# 如果遇到執行政策問題
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# 如果 python 指令不存在，嘗試
py -m venv venv
py account_audit.py
```

### Linux 常見問題
```bash
# 如果 python3-venv 未安裝（Ubuntu/Debian）
sudo apt update
sudo apt install python3-venv

# 如果 pip 未安裝
sudo apt install python3-pip
```

## 注意事項

本專案僅供教學與自動化概念演示，無任何真實主機帳號、密碼資訊。

歡迎任意 clone、fork、學習、分享，或於課堂與自學時參考！

## 授權 License

本專案採用 MIT License，詳見 LICENSE。
