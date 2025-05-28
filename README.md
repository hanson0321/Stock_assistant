# 本地 AI 財經助理 (Local AI Financial Assistant)

[![zh-TW](https://img.shields.io/badge/lang-zh--TW-blue.svg)](README.md) 一個使用 LocalAI 驅動的本地化財經助理應用程式，旨在提供新聞摘要、多模態分析（文字與圖片結合）以及實驗性的圖像生成功能。使用者可以輸入公司名稱，上傳相關圖片，系統將利用本地運行的 AI 模型進行分析並呈現結果。

##  功能

* **財經新聞摘要**：輸入公司名稱，獲取（目前為模擬的）相關新聞摘要。
* **多模態分析 (LLaVA)**：結合上傳的圖片與文字資訊，由 LLaVA 模型進行綜合分析與解讀。
* **AI 概念圖像生成 (Stable Diffusion )**：根據新聞摘要或圖片分析結果，自動生成相關的概念性圖像。
* **本地化 AI 模型**：所有 AI 推論均透過 LocalAI 在本地運行，確保資料隱私與客製化彈性。
* **網頁介面**：使用 Flask 和 Bootstrap 搭建的簡單易用網頁介面。
* **個性化前端**：包含開發者頭像和名稱，以及可自訂的股票相關圖示。

##  技術

* **後端**：
    * Python 3.9+
    * Flask (網頁框架)
    * Requests (HTTP 請求函式庫)
* **前端**：
    * HTML5
    * CSS3 (包含內嵌樣式與 Bootstrap 5)
    * Bootstrap 5.3.0 (CSS 框架)
* **AI 模型服務**：
    * LocalAI (本地 AI 推論平台，相容 OpenAI API 格式)
    * Docker & Docker Compose (容器化與服務編排)
* **AI 模型 **：
    * **文字/多模態分析**：LLaVA 
    * **圖像生成**：Stable Diffusion 

## 安裝與啟動教學

### 先決條件

1.  **Docker Desktop**：請先安裝 Docker Desktop (或適用於您作業系統的 Docker 版本) 並確保其正在運行。
2.  **Git**：用於複製此儲存庫。
3.  **AI 模型檔案**：您需要自行下載所需的 AI 模型檔案，並放置到正確的位置。
    * **LLaVA 模型**：
        * 下載 LLaVA 的 GGUF 格式主模型檔案 (例如 `llava-v1.5-7b-Q4_K_M.gguf`)。
        * 下載對應的多模態投影器 (mmproj) 檔案 (例如 `llava-v1.5-7b-mmproj-model-f16.gguf`)。
    * **Stable Diffusion 模型**：
        * 下載 Stable Diffusion 的 `.safetensors` 檔案 (例如 `v1-5-pruned-emaonly.safetensors`)。
    * 上述模型檔案均需放置在專案根目錄下的 `models/` 資料夾中。

### 安裝步驟

1.  **複製儲存庫**：
    ```bash
    git clone [https://github.com/YourUsername/Local-AI-Financial-Assistant.git](https://github.com/YourUsername/Local-AI-Financial-Assistant.git) # 請替換成您的儲存庫 URL
    cd Local-AI-Financial-Assistant
    ```

2.  **準備模型檔案**：
    * 在專案根目錄下建立一個名為 `models` 的資料夾。
    * 將您下載好的 LLaVA 主模型檔案、LLaVA mmproj 檔案以及 Stable Diffusion `.safetensors` 檔案**全部複製**到這個 `models/` 資料夾中。



3.  **啟動應用程式**：
    * 在專案根目錄 (包含 `docker-compose.yml` 檔案的目錄)，打開終端機並執行：
        ```bash
        docker-compose up --build
        ```
    * 首次啟動時，LocalAI 可能需要一些時間來下載基礎映像檔和安裝 `build_env` 中指定的 Python 依賴 (特別是針對 Stable Diffusion)。請耐心等待。
    * 留意終端機日誌，確保 `localai` 服務和 `app` 服務都已成功啟動，並且沒有明顯的錯誤訊息。

### 如何使用

1.  **訪問網頁介面**：
    * 當 Docker Compose 服務成功啟動後，打開您的網頁瀏覽器，輸入以下網址：
        `http://localhost:5000`
2.  **進行分析**：
    * 在「輸入公司名稱或股票代碼」欄位中輸入您想分析的公司名稱。
    * (可選) 點擊「選擇檔案」按鈕，上傳一張與該公司或主題相關的圖片，以供 LLaVA 模型進行多模態分析。
    * 點擊「分析」按鈕。
3.  **查看結果**：
    * 頁面將會顯示（目前為模擬的）爬取原始資料。
    * 接著會顯示由 LLaVA 模型生成的「AI 摘要與趨勢解讀」。
    * 如果 Stable Diffusion 模型設定正確且成功運作，下方還會顯示一張由 AI 根據摘要生成的概念圖像。



 📄 授權 (可選)

本專案採用 [MIT License](LICENSE) 授權。


