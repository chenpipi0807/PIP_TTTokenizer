@echo off
chcp 65001 >nul
cd /d %~dp0

cd..
cd..
cd..
cd python_embeded

echo 正在安装 spacy...
.\python.exe -m pip install spacy
IF %ERRORLEVEL% EQU 0 (
    echo "spacy 安装成功"
) ELSE (
    echo "spacy 安装失败"
    exit /b %ERRORLEVEL%
)

echo 正在下载 en_core_web_sm...
.\python.exe -m spacy download en_core_web_sm
IF %ERRORLEVEL% EQU 0 (
    echo "en_core_web_sm 下载成功"
) ELSE (
    echo "en_core_web_sm 下载失败"
    exit /b %ERRORLEVEL%
)

pause