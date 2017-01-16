import os
from datetime import datetime
import pandas as pd
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
GRW_GRAZ_2012_1_FILE = 'results/grw_graz_2012_1.csv'

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

# convert results of gemeinderatswahl graz 2012
def convert_grwgraz12():
	data = {}
	party_names = []
	cols_read = ['sprengel','ptname', 'gesamt', 'unguel', 'gueltig', 'stimmen']
	csv_file = INPUT_FOLDER+GRW_GRAZ_2012_1_FILE
	seperator = ';'
	encoding = 'latin1'
	
	df = pd.read_csv(csv_file, sep=seperator, encoding=encoding)
	
	df = df[cols_read]
	df.ix[df['ptname'].isnull(), 'ptname'] = 'ekw'
	df.ix[df['ptname'] == 'GRÜNE', 'ptname'] = 'gruene'
	df.ix[df['ptname'] == 'CP-G', 'ptname'] = 'cpg'
	df.ix[df['ptname'] == 'SPÖ', 'ptname'] = 'spoe'
	df.ix[df['ptname'] == 'ÖVP', 'ptname'] = 'oevp'
	df.ix[df['ptname'] == 'FPÖ', 'ptname'] = 'fpoe'
	df.ix[df['ptname'] == 'KPÖ', 'ptname'] = 'kpoe'
	df.ix[df['ptname'] == 'BZÖ', 'ptname'] = 'bzoe'
	df.ix[df['ptname'] == 'BBB', 'ptname'] = 'wir'
	df.ix[df['ptname'] == 'WIR', 'ptname'] = 'bbb'
	df.ix[df['ptname'] == 'PIRAT', 'ptname'] = 'piraten'
	party_names = list(df['ptname'].unique())
	
	for i, row in df.iterrows():
	    sprengel = row['sprengel']
	    if sprengel not in data.keys():
	        data[sprengel] = {}
	        data[sprengel]['spatial_id'] = sprengel
	    data[sprengel][row['ptname']] = row['stimmen']
	    data[sprengel]['votes'] = row['gesamt']
	    data[sprengel]['invalid'] = row['unguel']
	    data[sprengel]['valid'] = row['gueltig']

	df = pd.DataFrame(data).T

	cols_write = ['spatial_id', 'votes', 'invalid', 'valid']
	cols_write.extend(party_names)
	write_csv(df, OUTPUT_FOLDER+GRW_GRAZ_2012_1_FILE, cols_write)
	

###    MAIN   ###

if __name__ == "__main__":
	setup_environment()
	convert_grwgraz12()






