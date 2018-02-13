find . -name "*.pyc" | xargs rm 
rm -rf ./data/*
git add -A
git commit -m "$1"
git push origin master
