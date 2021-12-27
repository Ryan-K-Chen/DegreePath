@echo off
    echo NOTICE: Make sure to update Chrome version to 88.0.4324.96

cd /d %~dp0/webscraping
call install_dependencies.bat
python gatechscrape.py
python courses_tree.py
pause

