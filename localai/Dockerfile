# 使用官方 LocalAI 映像作為基礎
# 這個 Dockerfile 僅在您想要通過 docker-compose 的 build 指令
# (例如 build: ./localai) 而非直接使用 image: 指令來建置 LocalAI 服務時使用。
# 當 docker-compose.yml 中 localai 服務使用 "image: quay.io/go-skynet/local-ai:latest" 時，
# 這個 Dockerfile 實際上不會被 docker-compose up 使用來建置該服務。

FROM quay.io/go-skynet/local-ai:latest

# 您可以在這裡添加客製化的指令，例如：
# ENV NEW_VARIABLE=new_value
# RUN apt-get update && apt-get install -y some-tool

# 預設情況下，LocalAI 映像已經有自己的 ENTRYPOINT 和 CMD。
# 如果您不需要修改它們，就不用在這裡重新指定。