@echo
mkdir %2
cd %2
echo "# CMD-automation" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin %1
git push -u origin main



