python3 genDeals.py "$1" > deals.txt
./dds-master/examples/CalcAllTablesPBN < deals.txt >> d.txt
rm deals.txt
