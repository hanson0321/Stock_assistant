import os
import requests
import json

# 從環境變數讀取 LocalAI API 的基礎路徑
# 這個環境變數是在 docker-compose.yml 中設定給 app 服務的
LOCALAI_API_BASE = os.getenv("LOCALAI_API_BASE", "http://localhost:8080/v1") # 提供一個本地預設值以防萬一
LOCALAI_CHAT_API_URL = LOCALAI_API_BASE + "/chat/completions"

MODEL_NAME = os.getenv("LOCALAI_MODEL_NAME", "llava-financier")

def get_summary_and_trends(text_to_summarize: str) -> str:
    """
    將文本傳送給 LocalAI 進行摘要和趨勢分析。

    Args:
        text_to_summarize (str): 從爬蟲獲取的文本資料。

    Returns:
        str: AI 生成的摘要與趨勢分析，或錯誤訊息。
    """
    print(f"[Summarizer] 接收到文本，準備傳送給 LocalAI (模型: {MODEL_NAME})...")
    print(f"[Summarizer] LocalAI API URL: {LOCALAI_CHAT_API_URL}")
    print(f"[Summarizer] 待摘要文本 (前100字): {text_to_summarize[:100]}...")

    # 為 AI 模型設計的提示 (Prompt Engineering)
    # 您可以調整這個提示來獲得更符合您期望的結果
    prompt = f"""
    你是一位專業的財經分析師。請根據以下提供的財經新聞內容，執行以下任務：
    1. 生成一個簡潔明瞭的摘要，捕捉最重要的資訊。
    2. 根據新聞內容，分析並指出任何明顯的市場趨勢、潛在機會或風險。
    請將摘要和趨勢分析清楚地分開呈現。

    新聞內容如下：
    ---
    {text_to_summarize}
    ---

    你的分析結果：
    """

    headers = {
        "Content-Type": "application/json"
    }

    # LocalAI 的 /v1/chat/completions API 通常需要 OpenAI 相容的格式
    payload = {
        "model": MODEL_NAME, # 指定要使用的模型
        "messages": [
            {"role": "system", "content": "你是一位專業的財經分析師。"},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7, # 控制輸出的隨機性，0.7 是一個常用的值
        # "max_tokens": 500, # 可以設定最大生成字數，依需求調整
    }

    try:
        response = requests.post(LOCALAI_CHAT_API_URL, headers=headers, data=json.dumps(payload), timeout=300) # 設定超時時間為120秒
        response.raise_for_status()  # 如果請求返回錯誤狀態碼 (4xx or 5xx)，則拋出 HTTPError

        response_data = response.json()
        
        # 從回應中提取 AI 生成的內容
        # 這部分可能需要根據您使用的 LocalAI 模型和其回應格式進行調整
        if response_data.get("choices") and len(response_data["choices"]) > 0:
            ai_content = response_data["choices"][0].get("message", {}).get("content", "")
            if ai_content:
                print(f"[Summarizer] LocalAI 回應成功接收。")
                return ai_content.strip()
            else:
                print("[Summarizer] LocalAI 回應中未找到有效的內容。")
                return "AI未能生成有效的摘要內容。"
        else:
            print(f"[Summarizer] LocalAI 回應格式不符預期: {response_data}")
            return "從AI獲取摘要時發生錯誤：回應格式不符預期。"

    except requests.exceptions.RequestException as e:
        print(f"[Summarizer] 連線到 LocalAI 時發生錯誤: {e}")
        return f"無法連線到 AI 服務進行摘要分析：{e}"
    except Exception as e:
        print(f"[Summarizer] 處理 LocalAI 回應時發生未知錯誤: {e}")
        return f"處理 AI 回應時發生未知錯誤：{e}"

if __name__ == '__main__':
    # 這部分是為了單獨測試 summarizer.py 是否正常運作
    # 您需要確保 LocalAI 服務正在運行，並且模型已正確設定
    
    # 從 crawler 模組獲取模擬資料來測試
    # 為了讓這個獨立測試能運作，請確保 crawler.py 在同一個 app 資料夾中
    try:
        from crawler import fetch_financial_news
        test_company = "台積電" # 或其他在您 MOCK_NEWS_DATABASE 中的公司
        mock_data = fetch_financial_news(test_company)
        
        if "無法找到" not in mock_data: # 確保獲取到有效的新聞
            print(f"\n--- 測試摘要功能，公司: {test_company} ---")
            summary = get_summary_and_trends(mock_data)
            print("\n--- AI 分析結果 ---")
            print(summary)
        else:
            print(f"無法獲取 {test_company} 的模擬新聞資料進行測試。")

    except ImportError:
        print("無法匯入 crawler 模組。請確保 crawler.py 在同一個資料夾中，且 LocalAI 服務正在運作以便測試。")
    except Exception as e:
        print(f"執行獨立測試時發生錯誤: {e}")