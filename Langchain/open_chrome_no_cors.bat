@echo off
echo 正在启动禁用 CORS 的 Chrome 浏览器...
start chrome --disable-web-security --user-data-dir="%TEMP%\chrome_temp" --allow-file-access-from-files http://127.0.0.1:2024/docs
echo.
echo 浏览器已启动！
echo 现在可以访问: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
echo.
pause
