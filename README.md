# Installation

Go through the README file of each folder to install the required dependencies. Java has to be installed for neuralcoref. Refer [this](http://www.cs.cmu.edu/~mdenkows/cdec-realtime.html) link to install `cdec` for jamr generator. Refer [this](https://github.com/pygraphviz/pygraphviz/issues/61#issuecomment-207830568) if you face any problem while installing AMRICA.

Notice: installing a different version of `gcc` (for jamr) might result in NVIDIA drivers behaving weirdly. 

This repository was stored at my workstation at `/home/ritwik/ATS` and that is why in many places you might see absolute paths to it. You'll have change them by yourself.

Download the non-anonymized dataset of CNN/Daily mail from [here](https://cs.nyu.edu/~kcho/DMQA/), click on stories. Move the archive files to `/dataset` folder and extract there.

`/test/t5.py` by default picks news articles from `/dataset/dailymail/stories`.
Replace `dailymail`  with `cnn` if you wish to pick sentences from there. In that case don't forget to change the results path in `/jamr/writeRslts.py` from `/dataset/results` to `/dataset/results` (if you wish to keep the results from both datasets at different place, otherwise not problem) 

# Usage

Once everything is installed, with the above directory structure and absolute paths resolved. Simply run

```
mkdir /dataset/results
mkdir /dataset/results2
mkdir /dataset/results/AMRs
mkdir /dataset/results2/AMRs
chmod +x myrun.bash
chmod +x m2yrun.bash
./m2yrun.bash
```

Final results will be stored in `/dataset/results` and `/dataset/results2`
