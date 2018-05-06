find . -name "*.pyc" | xargs rm 
rm -rf ./data/*
git add -A
git commit -m "$1"
git push origin master
#python run_p2pool.py --srcchaind-config-path=/data/genyuanlianchengxu/linux/data/srcchain.conf --reserve-address=1R2Y45QymfK3Bg4shM26kuQKWYjQ4iQA8 --reserve-percentage=5
#python run_p2pool.py --srcchaind-config-path=/data/genyuanlianchengxu/linux/data/srcchain_test.conf --testnet 
