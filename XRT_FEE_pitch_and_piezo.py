import scipy
import numpy as np
import re
import pandas as pd
df = pd.read_csv('/Users/Daniel/desktop/XRT_FEE/XRT_FEE_M1_M2_M3pitch and piezo.csv',
	engine='python',
	skipfooter = 2, 
	header = None, 
	skiprows = 21, 
	names = ['HOMS1.rActVoltage', 'HOMS1.rSetVoltage', 'M1_P.ActPos', 'HOMS2.rActVoltage', 'HOMS2.rSetVoltage', 'M2_P.ActPos', 'HOMS3.rActVoltage', 'HOMS3.rSetVoltage', 'M3_P.ActPos'], 
	usecols=[1, 3, 5, 7, 9, 11, 13, 15, 17], 
	delimiter = '\\t')

a = {}
b = {}
c = {}
d = {}
e = {}
f = {}
g = {}
h = {}
i = {}

df1 = pd.read_csv('/Users/Daniel/desktop/XRT_FEE/XRT_FEE_M1_M2_M3pitch and piezo.csv',
	engine='python',
	header = None,
	skiprows = 6,
	nrows = 14,
	delimiter = '\\t',
)
print(df.head(5))

import re
head = 'Data-Type	REAL32	Data-Type	REAL32	Data-Type	REAL64	Data-Type	REAL32	Data-Type	REAL32	Data-Type	REAL64'

DataType = re.findall(r'\w{4}\-\w{4}\s\w{4}\d{2}', head)
print(DataType[5])

NetId = re.findall(r'\w{5}\s\d\.(\d*\.*)*', head)
Name = re.findall(r'\w{4}\s\w*\.\w*\.\w*', head)
Port = re.findall(r'\w{4}\s\d{3}', head)
SampleTime = re.findall(r'\w{10}\[\w*\]\s\d*', head)
SymbolBased = re.findall(r'\w{11}\s\w[Fa,Tr]', head)
IndexGroup = re.findall(r'\w{10}\s\d*', head)
IndexOffset = re.findall(r'\w{11}\s\d{5,6}', head)
VariableSize = re.findall(r'\w{12}\s\d', head)
Offset = re.findall(r'\w{6}\s\d*', head)
ScaleFactor = re.findall(r'\w{11}\s\d', head)
BitMask = re.findall(r'\w{7}\s\w{18}', head)