#!/bin/bash
git clone https://github.com/Jakub-Nnoli/HangmanProject.git
sudo chmod -R 777 HangmanProject
cd HangmanProject
rm installWindows.bat
rm HangmanApp.bat
rm installLinux.sh
rm README.md
git remote remove origin
rm -rf .git
rm -rf __pycache__
pip install -r requirements.txt
./HangmanApp.sh