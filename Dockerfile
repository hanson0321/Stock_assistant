# 使用官方 Python 映像作為基礎
FROM python:3.9-slim

# 設定工作目錄
WORKDIR /app

# 複製依賴性定義檔案到容器中
# 我們稍後會在 app 資料夾內建立一個 requirements.txt 檔案
COPY ./app/requirements.txt /app/requirements.txt

# 安裝 Python 依賴性
# --no-cache-dir：不安裝快取，減少映像大小
# --trusted-host pypi.python.org：在某些網路環境下可能需要，確保可以從 PyPI 下載
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

# 複製應用程式的其餘部分到容器中
COPY ./app /app

# 設定容器啟動時執行的命令
# 使用 gunicorn 作為 WSGI 伺服器來執行 Flask 應用程式是生產環境的好選擇
# 這裡我們先用 Flask內建的開發伺服器，方便測試
# EXPOSE 5000 # 告知 Docker 容器將會監聽的連接埠 (可選，docker-compose.yml 中已處理)
CMD ["python", "main.py"]