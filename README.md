# Installation

Go through the README file of each folder to install the required dependencies. Java has to be installed for neuralcoref. Refer [this](http://www.cs.cmu.edu/~mdenkows/cdec-realtime.html) link to install `cdec` for jamr generator. Refer [this](https://github.com/pygraphviz/pygraphviz/issues/61#issuecomment-207830568) if you face any problem while installing AMRICA.

Notice: installing a different version of `gcc` (for jamr) might result in NVIDIA drivers behaving weirdly. 

This repository was stored at my workstation at `/home/ritwik/ATS` and that is why in many places you might see absolute paths to it. You'll have change them by yourself.

Download the non-anonymized dataset of CNN/Daily mail from [here](https://cs.nyu.edu/~kcho/DMQA/), click on stories. Move the archive files to `/dataset` folder and extract there.

Make a file named `files.txt` and store names of all the news articles present in `/dataset/cnn/stories`. Similarly make a file named `files2.txt` for `/dataset/dailymail/stories`. 

`/test/t5.py` by default picks news articles from `/dataset/dailymail/stories` on the basis of `files2.txt`.
Replace `dailymail`  with `cnn` and use `files.txt` if you wish to pick sentences from there. In that case don't forget to change the results path in `/jamr/writeRslts.py` from `/dataset/results` to `/dataset/results2` (if you wish to keep the results from both datasets at different place, otherwise no problem) 

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

# Sample
Article
___
(CNN) -- The 54 men and 14 boys rescued after being found chained this week at an Islamic religious school in Pakistan have been reunited with their families or placed in shelters, authorities said.

The group was discovered in an underground room with heavy chains linking them together.

The school, Al-Arabiya Aloom Jamia Masjid Zikirya, which also was a drug rehab clinic, is in Sohrab Goth, a suburb of Gadap in Karachi.

All 14 boys were returned to their families, senior police official Ahsanullah Marwat told CNN.

Of the adults, 47 had been released to their families, and seven were handed over to a shelter for the homeless, he said.

Three people who worked at the facility were arrested, but the four men who ran the place were still at large, Marwat said.

Officials said the facility was part madrassa and part drug-rehab facility, and the captives were chained at night apparently to prevent their escape.

"The operation was successful, and we plan on continuing our work to ensure that places like this are shut down," Marwat said.

Many of the captives told police their families sent them there because they were recovering drug addicts. During the day, they worked and did religious studies.

But the future of the rescued children was unclear.

One woman told a local television station that she was willing to pay the police to keep her troublesome child. She said she would rather have the facility remain open, regardless of how it treated the children.

Many others, however, said they were in shock and disbelief over the allegations.

One man complained he was deep in debt after paying the school a large amount of money to board his son.
___

Output
___
authorities said that there will be 54 this week , the chain was found after rescue from islamic religious school in pakistan men and 14 boy reunite with families or placed in shelters
group was discovered in the underground room for the heavy chain link together
drug rehab also aloom jamia masjid zikirya gadap suburbs in karachi 's sohrab goth , anti - school
cnn told the 14 all of the boy 's return to the 14 all boy family senior ahsanullah marwat police official to the police with official senior ahsanullah marwat , said that the release of 14 of all the boy family 47 adults and 47 will be handed over to the shelter for the homeless to 7
marwat said that run these four men were arrested with large still work at the facility three but
officials said the apparently prevent the person captured the escape in the night , and the madrassas and facility facilities
marwat said the operation was successful and we continue to work with our plan to ensure that the place to be this resemblance to shut
told that many captured the police family sent the police there because the police are recovering drug addicts , police have been working at the time of the day and do the religious study
but it is unclear in the rescue of the child 's future
one woman told a local television station that one woman is willing to pay the police , said that one woman had the facilities remain open regardless of a woman 's troublesome one child to keep the children to be treated in the facility
many of the other many other said be-destined-for with shock and disbelief the allegations
one man complained that one man after paying a large amount of the money for a son board a school deep in debt
___
