import os
from datetime import datetime
import pandas as pd
import json
import csv
from config import *

__author__ = "Stefan Kasberger"
__copyright__ = "Copyright 2017"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Stefan Kasberger"
__email__ = "mail@stefankasberger.at"
__status__ = "Production" # 'Development', 'Production' or 'Prototype'


###    FUNCTIONS   ###

def setup_environment():
	"""Sets up the folder structure and working environment.
	"""
	if not os.path.exists(OUTPUT_FOLDER):
		os.makedirs(OUTPUT_FOLDER)
	if not os.path.exists(OUTPUT_FOLDER+'ergebnisse/'):
		os.makedirs(OUTPUT_FOLDER+'ergebnisse/')
	if not os.path.exists(OUTPUT_FOLDER+'geo/'):
		os.makedirs(OUTPUT_FOLDER+'geo/')

# read in csv file into dataframe



# read in xls file into dataframe



# read in xlsx file into dataframe



# write out into csv file
def write_csv(df, filename, col_list):
	seperator = ';'
	encoding = 'utf-8'
	date_format = '' # Format string for datetime objects
	index=False
	df.to_csv(path_or_buf=filename, sep=seperator, columns=col_list, date_format=date_format, encoding=encoding, index=index)

# convert 
def convert_grwgraz12():
	data = {}
	party_names = []
	cols_read = ['sprengel','ptname', 'gesamt', 'unguel', 'gueltig', 'stimmen']
	csv_file = INPUT_FOLDER+'ergebnisse/grw_graz_2012_01.csv'
	seperator = ';'
	encoding = 'latin1'
	
	df = pd.read_csv(csv_file, sep=seperator, encoding=encoding)
	
	df = df[cols_read]
	df.ix[df['ptname'].isnull(), 'ptname'] = 'EKW'
	df.ix[df['ptname'] == 'GRÜNE', 'ptname'] = 'Grüne'
	df.ix[df['ptname'] == 'CP-G', 'ptname'] = 'CPG'
	df.ix[df['ptname'] == 'PIRAT', 'ptname'] = 'Piraten'
	party_names = list(df['ptname'].unique())
	
	for i, row in df.iterrows():
	    sprengel = row['sprengel']
	    if sprengel not in data.keys():
	        data[sprengel] = {}
	        data[sprengel]['sprengel'] = sprengel
	    data[sprengel][row['ptname']] = row['stimmen']
	    data[sprengel]['wahlberechtigt'] = row['gesamt']
	    data[sprengel]['ungueltig'] = row['unguel']
	    data[sprengel]['gueltig'] = row['gueltig']

	df = pd.DataFrame(data).T

	cols_write = ['sprengel', 'wahlberechtigt', 'ungueltig', 'gueltig']
	cols_write.extend(party_names)
	write_csv(df, OUTPUT_FOLDER+'ergebnisse/grw_graz_2012_01.csv', cols_write)
	

###    MAIN   ###

if __name__ == "__main__":
	print('Started...')
	setup_environment()
	convert_grwgraz12()






