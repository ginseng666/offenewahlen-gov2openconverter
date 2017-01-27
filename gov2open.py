import os
from datetime import datetime
import pandas as pd
import numpy as np
import json
import csv

__author__ = "Stefan Kasberger"
__copyright__ = "Copyright 2017"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Stefan Kasberger"
__email__ = "mail@stefankasberger.at"
__status__ = "Production" # 'Development', 'Production' or 'Prototype'

###    GLOBALS   ###

basedir = os.path.abspath(os.path.dirname(__file__))

INPUT_FOLDER = basedir+'/data/input/'
OUTPUT_FOLDER = basedir+'/data/output/'
CONVERSION_FILE = basedir+'/data/conversion.csv'
PARTY_NAMES = ['bbb', 'bzoe', 'cpg', 'cpoe', 'ekw', 'eustop', 'fpoe', 'gruene', 'kpoe', 'm', 'neos', 'oevp', 'spoe', 'stronach', 'slp', 'wandl', 'wir']

###    FUNCTIONS   ###

def setup_environment():
	"""Sets up the folder structure and working environment.
	"""
	if not os.path.exists(OUTPUT_FOLDER):
		os.makedirs(OUTPUT_FOLDER)
	if not os.path.exists(OUTPUT_FOLDER+'results/'):
		os.makedirs(OUTPUT_FOLDER+'results/')
	if not os.path.exists(OUTPUT_FOLDER+'geo/'):
		os.makedirs(OUTPUT_FOLDER+'geo/')


def open_spreadsheet(filename, file_type, sep, encoding):
	if file_type == 'csv':
		df = pd.read_csv(filename, sep=sep, encoding=encoding)
		
	# if file_type == 'xlsx':
	# if file_type == 'xls':
	# if file_type == 'txt':

	return df


def write_csv(df, filename, cols_out, sep, encoding):
	date_format = '' # Format string for datetime objects
	sep = ';'
	encoding= 'utf-8'
	index=False
	df.to_csv(path_or_buf=filename, sep=sep, columns=cols_out, date_format=date_format, encoding=encoding, index=index)
		

# convert results of gemeinderatswahl graz 2012
def convert_data(filename, file_type, cols_in, cols_out, sep, encoding):

	# open spreadsheet
	df = open_spreadsheet(INPUT_FOLDER+'results/'+filename+'.'+file_type, file_type, sep, encoding)
	
	# reshape data
	if filename == 'grw_graz_2012_1':
		df, cols_in = reshape_grw_graz_2012_1(df, cols_in)

	if filename == 'nrw_2013_1':
		# print('NRW')
		df = reshape_nrw_2013_1(df)

	# select columns
	df = df[cols_in]
	df.columns = cols_out
	# for col in df:
	# 	# print(col)
	# 	if col in PARTY_NAMES:
	# 		# print(df[col])
	# 		df[col] = df[col].apply(np.int64)

	# write columns
	write_csv(df, OUTPUT_FOLDER+'results/'+filename+'.'+file_type, cols_out, sep, encoding)


def reshape_grw_graz_2012_1(df, cols_in):
	data = {}
	df.ix[df['ptname'].isnull(), 'ptname'] = 'ekw'
	party_names = list(df['ptname'].unique())
	
	for i, row in df.iterrows():
	    sprengel = row['sprengel']
	    if sprengel not in data.keys():
	        data[sprengel] = {}
	        data[sprengel]['sprengel'] = sprengel
	    data[sprengel][row['ptname']] = row['stimmen']
	    data[sprengel]['gesamt'] = row['gesamt']
	    data[sprengel]['unguel'] = row['unguel']
	    data[sprengel]['gueltig'] = row['gueltig']

	df = pd.DataFrame(data).T
	if 'stimmen' in cols_in: cols_in.remove('stimmen')
	if 'ptname' in cols_in: cols_in.remove('ptname')

	return df, cols_in


def reshape_nrw_2013_1(df):
	return df

###    MAIN   ###

if __name__ == "__main__":
	setup_environment()

	df = pd.read_csv(CONVERSION_FILE, sep=';', encoding='utf-8')

	for i, row in df.iterrows():
		cols_in = [col.strip() for col in row['cols_in'].split(',')]
		cols_out = [col.strip() for col in row['cols_out'].split(',')]
		convert_data(row['filename'], row['filetype'], cols_in, cols_out, row['sep'], row['encoding'])






