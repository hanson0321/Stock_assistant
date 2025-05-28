from flask import Flask, render_template, request
import os
# import requests # 我們暫時不在 main.py 直接呼叫 LocalAI

# 從我們建立的 crawler 模組中匯入 fetch_financial_news 函式
from crawler import fetch_financial_news
# 從 summarizer 模組匯入函式
from summarizer import get_summary_and_trends # <--- 已取消註解

# 初始化 Flask 應用程式
app = Flask(__name__)

# ... (其餘程式碼不變) ...

@app.route('/', methods=['GET', 'POST'])
def index():
    company_name_display = None # 用於在頁面上顯示分析目標
    crawled_text_display = None # 用於顯示爬取到的文本
    summary_display = None      # 用於顯示摘要結果

    if request.method == 'POST':
        company_input = request.form.get('company_name')
        company_name_display = company_input # 更新顯示的公司名稱

        if company_input:
            # 1. 呼叫 crawler.py 爬取新聞/財報
            print(f"[MainApp] 接收到查詢: {company_input}, 準備呼叫爬蟲...")
            crawled_text_data = fetch_financial_news(company_input) # 呼叫爬蟲函式
            crawled_text_display = crawled_text_data # 將爬蟲結果用於顯示

            # 2. 呼叫 summarizer.py 進行摘要與趨勢解讀
            if crawled_text_data and "無法找到" not in crawled_text_data: # 確保有實際資料且不是錯誤訊息
                print(f"[MainApp] 爬蟲回傳資料，準備呼叫摘要器 (summarizer)...")
                try:
                    summary_display = get_summary_and_trends(crawled_text_data)
                    print(f"[MainApp] 摘要器回傳: {summary_display[:200]}...") # 印出摘要前200字
                except Exception as e:
                    print(f"[MainApp] 呼叫摘要器時發生錯誤: {e}")
                    summary_display = f"無法從 AI 服務獲取摘要 ({e})。請檢查 LocalAI 服務是否正常運行以及模型設定是否正確。"
            elif crawled_text_data and "無法找到" in crawled_text_data:
                # 如果爬蟲回傳的是找不到資料的訊息，直接顯示該訊息，不進行摘要
                print(f"[MainApp] 爬蟲回傳找不到資料，不進行摘要。")
                summary_display = crawled_text_data # crawled_text_data 此時是提示訊息
            else:
                print(f"[MainApp] 沒有從爬蟲獲取到有效資料，無法進行摘要。")
                summary_display = "沒有從爬蟲獲取到有效資料，因此無法進行摘要。"

        # 將結果傳遞給模板
        return render_template('index.html',
                               company_name=company_name_display,
                               crawled_data=crawled_text_display,
                               summary=summary_display)

    # GET 請求時，只傳遞 None 或預設值
    return render_template('index.html',
                           company_name=company_name_display,
                           crawled_data=crawled_text_display,
                           summary=summary_display)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)