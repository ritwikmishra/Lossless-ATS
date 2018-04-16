#!/bin/bash
for number in {1..1500}
do
echo -e "\n\n\n\t\t################################"
echo -e "\t\t################################"
echo -e "\t\t\tTest case $number "
echo -e "\t\t################################"
echo -e "\t\t################################"
cd test
python t5.py
cd ..
time ./myrun.bash article.txt
sleep 2
done
date
exit 0