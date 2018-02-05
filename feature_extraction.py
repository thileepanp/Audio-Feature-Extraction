""" 
This code extracts features from a single audio file
using YAAFE in python. 

Yaafe installation is exteremely simple with anaconda
using this command 'conda install -c conda-forge yaafe'

other ways to install yaafe is given here
'https://github.com/Yaafe/Yaafe' 

YAAFE user manual http://yaafe.sourceforge.net/manual.html 

This code extracts 28 features. some of the features 
themselves have about 500 columns/dimensions. Yet, yaafe is 
extremely fast. It takes about 30 seconds to calculate all the
features for a 10 minute .flac file. 

All the output files will be written in the directory
mentioned in the 'outDir' parameter in the afp.setOutputFormat
command.

Output files can be either in HdF5 or in csv format. 
HdF5 is better because it gives only one file for every audio
file that is being analysed. Whereas csv format creates one csv
file for every feature that is being extracted. 

Size of the Hdf5 file is smaller than all the csv files created 
for a single audio file. 

Analysis time is also lower when Hdf5 output is used. 

Only disadvantage with Hdf5 is that it doesn't allow us to see
how many columns/dimensions each features have. Therefore, I think
it is good to first extract features as csv, then understand the 
output dimensions and then use hdf5 to extract all other features. 
"""

from yaafelib import * #import all the features from yaafe library

fp = FeaturePlan(sample_rate=25600, resample=True) #the sample_rate could be changed
									#also resampling can be enabled,
									# by default it is disabled

fp.loadFeaturePlan('featureplan') #loads the feature plan from 
								  # text file called 'featureplan'

#The following 2 steps are optional
df=fp.getDataFlow() #creates the dataflow for extracting feautures
df.display()# displays the created dataflow

engine=Engine() #loads the feature generation engine
engine.load(fp.getDataFlow()) #loads the dataflow into the engine
afp=AudioFileProcessor() #initiates the audio file processor to 
						#process audio directly from file

afp.setOutputFormat(format='csv', 
	outDir='/home/thileepan/Dropbox/PhD/2018 work/amselected',
	 params={'feats.keys()':'feats.values()'}) #to get .csv output

afp.setOutputFormat(format='h5',
	outDir='/home/thileepan/Dropbox/PhD/2018 work/amselected',
	 params={'feats.keys()':'feats.values()'}) #to get hdf5 output


#line 18 sets the format in which we need the o/p.
			#o/p file can be in HdF5/csv format


afp.processFile(engine, 'AM_B1_D3.1_2017-03-21T171000.flac')
