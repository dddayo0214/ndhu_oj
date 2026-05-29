import html
import os
import re
import subprocess
import requests

# ================= 配置設定 =================
HACKMD_API_TOKEN = ""
# 填入你從 F12 複製下來的 API 實際網址
OJ_API_URL = "http://134.208.3.66/api/problem?problem_id=PR114-2-"
# 本地程式碼路徑
MY_CODE_FILE = ""
OUTPUT_DIR = "solutions"
# ============================================


def clean_html(html_text):
    """將 JSON 裡的 HTML 標籤（如 <p>, <b>）乾淨地轉為 Markdown 格式"""
    if not html_text:
        return ""
    # 處理常見的 HTML 實體字元（如 &lt; 轉為 <）
    text = html.unescape(html_text)
    # 將 <b> 補丁轉為 Markdown 的粗體 **
    text = re.sub(r"</?b>", "**", text)
    # 將 <br />, <br> 換成換行
    text = re.sub(r"</p>", "\n", text)
    text = re.sub(r"<br\s*/?>", "\n", text)
    # 移除其餘的 HTML 標籤（如 <p>, </p>, <div>）
    text = re.sub(r"<[^>]+>", "", text)
    return text.strip()

def combind_md(prob_id, title, desc, input_desc, output_desc, samples_md, code):
    markdown_content = f"""# {prob_id}: {title}

## 題目敘述
{desc}

## 輸入說明
{input_desc}

## 輸出說明
{output_desc}

---

## 範例測試
{samples_md}
---

## 我的程式碼 (C++)
```cpp
{code}
```
"""
    return markdown_content

def get_problem_data_from_api(url):
    """直接呼叫 OJ API 取得題目 JSON 資料"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    res_json = response.json()
    # 根據圖片結構，資料藏在 data 欄位裡
    data = res_json.get("data", {})

    # 解析各個欄位
    problem_id = data.get("_id", "Unknown")
    title = data.get("title", "Untitled")
    display_title = f"{problem_id}: {title}"

    description = clean_html(data.get("description", ""))
    input_desc = clean_html(data.get("input_description", ""))
    output_desc = clean_html(data.get("output_description", ""))

    # 處理多組範例測資
    samples = data.get("samples", [])
    sample_blocks = ""
    for i, sample in enumerate(samples, 1):
        # 圖片中顯示換行符號為 ↵，實體資料通常是 \n，這邊做個保險清潔
        s_input = sample.get("input", "").replace("↵", "\n")
        s_output = sample.get("output", "").replace("↵", "\n")
        sample_blocks += f"### 範例輸入 {i}\n```text\n{s_input}\n```\n"
        sample_blocks += f"### 範例輸出 {i}\n```text\n{s_output}\n```\n\n"

    return display_title, description, input_desc, output_desc, sample_blocks

def get_problem_data(url):
    """呼叫 OJ API 取得題目資料"""
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    data = response.json().get("data", {})
    problem_id = data.get("_id", "Unknown")
    title = data.get("title", "Untitled")

    desc = clean_html(data.get("description", ""))
    input_desc = clean_html(data.get("input_description", ""))
    output_desc = clean_html(data.get("output_description", ""))

    # 處理範例測資
    samples = data.get("samples", [])
    sample_blocks = ""
    for i, sample in enumerate(samples, 1):
        s_input = sample.get("input", "").replace("↵", "\n")
        s_output = sample.get("output", "").replace("↵", "\n")
        sample_blocks += f"### 範例輸入 {i}\n```text\n{s_input}\n```\n"
        sample_blocks += f"### 範例輸出 {i}\n```text\n{s_output}\n```\n\n"

    return problem_id, title, desc, input_desc, output_desc, sample_blocks

def git_push_to_github(file_path, commit_message):
    """利用 subprocess 執行 Git 指令自動上傳"""
    try:
        print("📁 正在將檔案加入 Git 暫存區...")
        subprocess.run(["git", "add", file_path], check=True)

        print(f"💬 正在建立 Commit: {commit_message}")
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        print("🚀 正在 PUSH 到 GitHub...")
        # 假設你的分支是 main，如果是 master 請改為 master
        subprocess.run(["git", "push", "origin", "main"], check=True)

        print("🎉 成功上傳到 GitHub！")
    except subprocess.CalledProcessError as e:
        print(f"❌ Git 操作失敗: {e}")

def create_hackmd_note(title, content):
    """發送請求至 HackMD 建立筆記"""
    url = "https://api.hackmd.io/v1/notes"
    headers = {
        "Authorization": f"Bearer {HACKMD_API_TOKEN}",
        "Content-Type": "application/json",
    }
    payload = {
        "title": title,
        "content": content,
        "readPermission": "owner",
        "writePermission": "owner",
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 201:
        print(f"🎉 成功建立 HackMD 筆記！")
        print(f"連結: {response.json().get('publishLink')}")
    else:
        print(f"上傳 HackMD 失敗: {response.text}")

def hackmd_main():
    for i in range(1, 63):
        now_URL = ""
        code_URL = ""
        if i < 10:
            now_URL = OJ_API_URL + "0" + str(i)
        else:
            now_URL = OJ_API_URL + str(i)
        code_URL = MY_CODE_FILE + str(i) + ".cpp"
        print("1. 正在從 OJ API 擷取題目資料...")
        try:
            title, desc, input_desc, output_desc, samples_markdown = (
                get_problem_data_from_api(now_URL)
            )
        except Exception as e:
            print(f"擷取 API 失敗: {e}")
            return

        print("2. 正在讀取本地程式碼...")
        code = "// 尚未撰寫程式碼或找不到檔案"
        if os.path.exists(code_URL):
            with open(code_URL, "r", encoding="utf-8") as f:
                code = f.read()

        # 3. 組合 Markdown 內文
        markdown_content = f"""# {title}

## 題目敘述
{desc}

## 輸入說明
{input_desc}

## 輸出說明
{output_desc}

---

## 範例測試
{samples_markdown}
---

## 我的程式碼 (C++)
```cpp
{code}
```
"""

        print("4. 正在打包上傳至 HackMD...")
        create_hackmd_note(title, markdown_content)

def github_main():
    for i in range(1, 63):
        # 1. 抓取題目資料
        now_URL = ""
        code_URL = ""
        if i < 10:
            now_URL = OJ_API_URL + "0" + str(i)
        else:
            now_URL = OJ_API_URL + str(i)
        code_URL = MY_CODE_FILE + str(i) + ".cpp"
        print("1. 正在從 OJ 擷取題目資料...")
        try:
            prob_id, title, desc, input_desc, output_desc, samples_md = (
                get_problem_data(now_URL)
            )
        except Exception as e:
            print(f"擷取失敗: {e}")
            return

        # 2. 讀取程式碼
        print("2. 正在讀取本地程式碼...")
        code = "// 尚未撰寫程式碼"
        if os.path.exists(code_URL):
            with open(code_URL, "r", encoding="utf-8") as f:
                code = f.read()

        # 3. 組裝 Markdown 內容
        markdown_content = combind_md(prob_id, title, desc, input_desc, output_desc, samples_md, code)

        # 4. 儲存成本地 .md 檔案
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

        # 檔名範例: solutions/PR114-2-01_Question_1_The_Student_Name_Card.md
        # 清除檔名中不合法的字元
        safe_title = re.sub(r'[\\/*?:"<>| ]', "_", title)
        filename = f"{prob_id}_{safe_title}.md"
        file_path = os.path.join(OUTPUT_DIR, filename)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(markdown_content)
        print(f"💾 已在本機建立檔案: {file_path}")

        # 5. 自動推送到 GitHub
        # commit_msg = f"Solve {prob_id}: {title}"
        # git_push_to_github(file_path, commit_msg)

github_main()