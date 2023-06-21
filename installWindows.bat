git clone https://github.com/Jakub-Nnoli/HangmanProject.git
cd HangmanProject
del install.bat
del README.md
git remote remove origin
rmdir /s /q .git
pip install -r requirements.txt
python main.py