Author: Prakhar Dogra
G Number: G01009586
CS 657 Assignment 1

The following README gives details about the dataset and the files contained in this folder:

1. Dataset
	The dataset was downloaded from the State of Union Addresses website using the following link : http://stateoftheunion.onetwothree.net/texts/stateoftheunion1790-2017.txt.zip
	Alternatively, a python script was also written to download and parse HTML files.

2. SourceCode
	This folder contains the Source Code of all the Mappers and Reducers used to complete the tasks of the assignment. It also contains a python script that was used to download and parse HTML data of the State of Union Addresses website.
	Task #1 to run the initial version of WordCount using streaming was done using the following Mappers and Reducers:
		- wcmapper.py
		- wcreducer.py
	Task #2 to write a hadoop program to compute 
		- average use of every word per year
		- maximum and minimum times a word apprears in all addresses
	was done using the following Mappers and Reducers:
		- wcmapperMinMaxAvg.py
		- wcreducerMinMaxAvg.py
	Task #3 to compute the average and standard deviation of times a word appears in a window of four years was done using the following Mappers and Reducers:
		- wcmapperAvgStd.py
		- wcreducerAvgStd.py
	Task #4 to output the words that appear in the year following the four year window with a frequrency that exceeds the average plus two standard deviations was done using the following Mappers and Reducers:
		- wcmapperHighFreq.py
		- wcreducerHighFreq.py

3. PseudoCode
	This folder contains the Pseudo Codes for all the Mappers and Reducers mentioned above:
	Following are the Pseudo Codes associated with their respective tasks:
	Task #1		MapReduceBase.pdf
	Task #2		MapReduceMinMaxAvg.pdf
	Task #3		MapReduceAvgStd.pdf
	Task #4		MapReduceHighFreq.pdf

4. Output
	This folder contains the Output Folders of each respective task:
	Following are the sub folders and format of the output associated with their respective tasks:
	Task #1		MapReduceBase
		- Each line of the output file is a Word tab separated with it's respective count.
	Task #2		MapReduceMinMaxAvg
		- Each line of the output file is in the following form:
		Word, Minimum, Maximum, Average
		Where each of them are tab separated
	Task #3		MapReduceAvgStd
		- Each output file in this folder correspond to the four year window (for example, 1985-1988) for which the average and standard deviation were calculated for:
		- Each line of the output file is in the following form:
		Word, Average, Standard_Deviation
		Where each of them are tab separated
	Task #4		MapReduceHighFreq
		- Each output subfolder(containing the output) in this folder corresponds to the year that is followed by a four year window (for example, 1989 is followed by 1985-1988) for which the words, with frequency that exceed the average plus two standard deviations, were found:
		- Each line of the output file is in the following form:
		Word, Frequency_in_current_year, Average_plus_2_times_Standard_Deviation_of_previous_four_year_window
		Where each of them are tab separated
5. Graph
	This folder contains the graph that was plotted for Task #1.
	The graph plotted is the time taken by the map-reduce job versus the amount of the data set.
	The graph was plotted for 20%, 40%, 60%, 80% and 100% data sizes.
	We can see that there is little increase in time for User Time and System Time. But there is kind of a linear increase in time for Real Time with respect to the dataset size.
	
6. General Information
	When doing Task #3, the MapReduce program was run multiple times, everytime with a different command line arguement to the Mapper.
	When doing Task #4, the MapReduce program was run multiple times, everytime with a different command line arguement to the Reducer.
	For example to calculate the average and standard deviation in task #3 for the 4 year window 1985-1988, command line arguement '1985' was given. 
	And to find the words in 1989, with frequency that exceed the average frequency of words in 1985-1988 plus two times the standard deviation, command line arguement '1985-1988' was given (file that contains the result from previous four-year window).
	