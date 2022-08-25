Assignment done by Anuj Shrivastava - 21111013 - anujs21@iitk.ac.in, anujsh@cse.iitk.ac.in

For executing the whole Assignment, I have created a Script Filename "assign2.sh".

In this Scripts Directory, the list of Scripts are as follows

1.sh percent-india.sh


2.sh gender-india.sh


3.sh geography-india.sh


4.sh 3-to-2-ratio.sh


5.sh 2-to-1-ratio.sh


6.sh age-india.sh


7.sh literacy-india.sh


8.sh region-india.sh


9.sh age-gender.sh


10.sh literacy-gender.sh

Run assign2.sh after making working directory to folder - '21111013-assign2' 

To run the entire assignment by command -> sh assign2.sh



The following dependencies are used in my Assignment

1) Jupyter Notebook (.ipynb)
2) Python (v3.7.6) and its packages




Python packages required are :



- pandas : for dataset handling


- numpy : support for calculations


- scipy : For p-value calculation in Q2 and Q3


- warnings : to ignore unnecessary warnings




Some important information regarding assumptions and input files for some questions :



Question 1 :

Input for question 1 is'DDW_PCA0000_2011_Indiastatedist.xlsx' file which was used at time of assignment 1 

for getting total population and 'DDW-C18-0000.xlsx' file for getting information about monolingualism, bilingualism and trilingualism. One thing to note here is that in 'DDW-C18-0000.xlsx' file data given is cumulative so we subtracted total population data from bilingualism data to get number of monolingual people and similarly subtracted bilingualism data from trilingualism data to get number of bilingual people.




Question 2 and Question 3 :

For calculating p-value I used scipy.stats.ttest_1samp() function from scipy library



Question 4 :

Since in question 4 two different script/program were mentioned to generate results therefore I created 2 separate .py files for corresponding part of question 4.


Question 5 :

In this question for getting age-group wise population data I used 'DDW-0000C-13.xls' file, it is having population data for each age so from that I added and made age-group wise population data according to our requirement.



Question 6 :

In this we want literacy group wise population data that in each literacy group how many peoples are there so we used data from 'DDW-0000C-08.xlsx' file and then pre-processed it to find required data.

One thing to note here is that for getting population data for 'Litreate below primary' group I used 'below primary' coloumn from mentioned file and for 'Matric/Secondary but below graduate' group, I added data of 'Matric/Secondary', 'Higher secondary/Intermediate', 'Non-technical diploma' and 'Technical diploma or certificate' coloumn from mentioned file. This I have done in order to avoid getting false percentage values which I was getting before doing all this.

Question 7 :

Since this question involves lots of input files so to make everything well arranged I made a folder named 'Q7_Dataset' and in this folder I further made folders for every region and then kept corresponding file in its corresponding region foder. Also to make soloution shorter I used loops for every region, so because of which I renamed all the files accoring to my need for working smoothly with my code. You can see that in code why I have done that.







































