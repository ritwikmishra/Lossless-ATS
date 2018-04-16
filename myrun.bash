#/ATS
cat $1> neuralcoref/article.txt
cd neuralcoref
python 2mysample.py
cat sents_article.txt> ../camr/input_file
cd ..

cd camr
echo '## script: Doing preprocessing'

python amr_parsing.py -m preprocess input_file
echo '## script: Generating AMR Trees'
python amr_parsing.py -m parse --model models/amr-anno-1.0/amr-anno-1.0.train.basic-abt-brown-verb.m input_file 2>errors.log
python amr_parsing.py -m preprocess --amrfmt amr input_file.all.basic-abt-brown-verb.parsed
python mysampleCamr.py
# cat input_file.all.basic-abt-brown-verb.parsed.amr.tok > ../AMRICA/sample.amr
cat input_file.all.basic-abt-brown-verb.parsed.amr.tok > /home/ritwik/ATS/test/art.txt
rm input_file.*
cd ..
cd test
python t2.py
cat summ.txt > ../AMRICA/sample.amr
cat summ.txt > ../jamr/input_file
# cat input_file.all.basic-abt-brown-verb.parsed.amr.tok > ../jamr/input_file
cd ..

cd AMRICA
echo 'IN AMRICA'
./disagree.py -i sample.amr -o sample_out_dir/
echo 'Graphs generated'
cd ..

echo 'Generating Text'
cd jamr
. scripts/config_LDC2014T12-NAACL2016-generator.sh
scripts/GENERATE.sh input_file
python writeRslts.py
echo -e 'Done\n'