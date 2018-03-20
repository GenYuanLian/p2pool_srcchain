find . -name "*.pyc" | xargs rm 
rm -rf ./data/*
git add -A
git commit -m "$1"
git push origin master
#python run_p2pool.py --bitcoind-config-path=/data/genyuanlianchengxu/linux/data/srcchain.conf 
