import requests
from bs4 import BeautifulSoup

# 模擬的財經新聞資料庫 (之後可以替換成真正的網路爬蟲邏輯)
MOCK_NEWS_DATABASE = {
    "台積電": [
        "台積電第一季度財報超出預期，營收達到新高。",
        "分析師看好台積電，預計其股價將持續上漲。",
        "台積電宣布將在美國擴大投資，建設新的晶圓廠。"
    ],
    "聯發科": [
        "聯發科發布最新款手機晶片，性能大幅提升。",
        "市場對聯發科的展望樂觀，認為其在5G市場將有更大作為。",
        "聯發科與多家汽車製造商合作，進入車用晶片市場。"
    ],
    "鴻海": [
        "鴻海集團積極佈局電動車產業，投資多家相關企業。",
        "鴻海法說會釋出樂觀訊息，看好下半年營運表現。",
        "蘋果新款 iPhone 訂單加持，鴻海營運看旺。"
    ]
}

def fetch_financial_news(company_name: str) -> str:
    """
    根據公司名稱爬取財經新聞。
    目前這是一個模擬版本，它會從 MOCK_NEWS_DATABASE 中查找新聞。
    未來可以擴展此函式以執行真正的網路爬蟲。

    Args:
        company_name (str): 使用者輸入的公司名稱。

    Returns:
        str: 合併後的新聞文本字串，如果找不到則回傳提示訊息。
    """
    print(f"[Crawler] 接收到查詢公司: {company_name}")

    if company_name in MOCK_NEWS_DATABASE:
        news_list = MOCK_NEWS_DATABASE[company_name]
        combined_news = "\n".join(news_list)
        print(f"[Crawler] 找到新聞: {combined_news[:100]}...") # 印出前100字預覽
        return combined_news
    else:
        # 如果找不到公司，可以回傳一個預設的或空的訊息
        # 這裡我們回傳一些模擬的通用新聞，或者提示找不到
        print(f"[Crawler] 在模擬資料庫中找不到 {company_name} 的特定新聞，回傳通用訊息。")
        return f"目前無法找到關於「{company_name}」的特定財經新聞。請嘗試其他公司，或稍後我們將加入更廣泛的爬蟲功能。"

if __name__ == '__main__':
    # 這部分是為了單獨測試 crawler.py 是否正常運作
    test_companies = ["台積電", "聯發科", "阿里巴巴"]
    for company in test_companies:
        print(f"\n--- 測試爬取 {company} ---")
        news = fetch_financial_news(company)
        print(news)