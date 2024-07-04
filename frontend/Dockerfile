FROM node:14

# 앱 디렉토리 생성
WORKDIR /app

# # GitHub에서 소스 코드 복사
# RUN apt-get update && apt-get install -y git
# ARG CACHEBUST=1
# RUN git clone https://github.com/sudo-G41/kitri_semi_fe .


# 종속성 설치
COPY package*.json ./
RUN npm install

# 앱 소스 코드 복사
COPY . .

# 앱 빌드
RUN npm run build

# 포트 노출
EXPOSE 8
# NGINX 설치 및 설정
FROM nginx:alpine
WORKDIR /app
COPY --from=0 /app .
RUN ["rm", "-r", "/usr/share/nginx/html"]
RUN ["mv", "build/", "/usr/share/nginx/html"]
RUN ["mv", "nginx/nginx.conf", "/etc/nginx/conf.d"]
RUN ["rm", "/etc/nginx/conf.d/default.conf"]
# COPY --from=0 /app/build /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]
