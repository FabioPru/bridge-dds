python3 genNS.py "$1" > dealsNS.txt
./dds-master/examples/CalcAllTablesPBN < dealsNS.txt >> dNS.txt

# roughly   200 deals/min (x10)
#         12000 deals/hr  (x10)