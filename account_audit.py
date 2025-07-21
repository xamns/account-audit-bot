import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import random

# 模擬假主機資料
hosts = [
    {"name": "server01", "hostname": "192.168.1.101"},
    {"name": "server02", "hostname": "192.168.1.102"},
    {"name": "server03", "hostname": "192.168.1.103"},
]
output_dir = "./output_accounts"
os.makedirs(output_dir, exist_ok=True)

def fake_passwd_lines():
    """產生假帳號資料"""
    base_users = ["root", "admin", "user", "test", "backup"]
    users = base_users + [f"user{str(i)}" for i in range(random.randint(2, 10))]
    return "\n".join([f"{u}:x:100{idx}:1000:Fake User:/home/{u}:/bin/bash" for idx, u in enumerate(users)])

def generate_image(host, text):
    """產生黑底白字帳號圖檔"""
    try:
        font = ImageFont.load_default()
        lines = text.split('\n')
        width = max(font.getsize(line)[0] for line in lines) + 40
        height = len(lines) * 18 + 40
        img = Image.new('RGB', (width, height), (0, 0, 0))
        draw = ImageDraw.Draw(img)
        for i, line in enumerate(lines):
            draw.text((20, 20 + i * 18), line, font=font, fill=(255, 255, 255))
        path = os.path.join(output_dir, f"{host['name']}_accounts.png")
        img.save(path)
        print(f"✅ 圖片已產生: {path}")
    except Exception as e:
        print(f"❌ 產生圖片失敗: {e}")

def main():
    total_accounts = 0
    summary_lines = []
    for host in hosts:
        passwd_data = fake_passwd_lines()
        account_count = passwd_data.count('\n') + 1
        now = datetime.now().strftime('%Y-%m-%d')
        text = (f"Host: {host['name']} ({host['hostname']})\n"
                f"Account List:\n{passwd_data}\n\n"
                f"Account Total: {account_count}\nCheck Date: {now}")
        generate_image(host, text)
        summary_lines.append(f"{host['name']}: Account Total: {account_count}")
        total_accounts += account_count
    # 輸出統計
    summary_path = os.path.join(output_dir, "account_summary.txt")
    with open(summary_path, 'w') as f:
        f.write("\n".join(summary_lines))
        f.write(f"\nTotal Accounts: {total_accounts}")
    print(f"\n✅ 帳號總結: {summary_path}")

if __name__ == "__main__":
    main()