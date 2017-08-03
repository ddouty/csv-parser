import scipy
import numpy as np
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

df1=df1.replace('"','',regex=True).astype(str)

a[df1.iloc[0,0]] = df1.iloc[0,1]
a[df1.iloc[1,0]] = df1.iloc[1,1]
a[df1.iloc[2,0]] = df1.iloc[2,1]
a[df1.iloc[3,0]] = df1.iloc[3,1]
a[df1.iloc[4,0]] = df1.iloc[4,1]
a[df1.iloc[5,0]] = df1.iloc[5,1]
a[df1.iloc[6,0]] = df1.iloc[6,1]
a[df1.iloc[7,0]] = df1.iloc[7,1]
a[df1.iloc[8,0]] = df1.iloc[8,1]
a[df1.iloc[9,0]] = df1.iloc[9,1]
a[df1.iloc[10,0]] = df1.iloc[10,1]
a[df1.iloc[11,0]] = df1.iloc[11,1]
a[df1.iloc[12,0]] = df1.iloc[12,1]
a[df1.iloc[13,0]] = df1.iloc[13,1]

b[df1.iloc[0,2]] = df1.iloc[0,3]
b[df1.iloc[1,2]] = df1.iloc[1,3]
b[df1.iloc[2,2]] = df1.iloc[2,3]
b[df1.iloc[3,2]] = df1.iloc[3,3]
b[df1.iloc[4,2]] = df1.iloc[4,3]
b[df1.iloc[5,2]] = df1.iloc[5,3]
b[df1.iloc[6,2]] = df1.iloc[6,3]
b[df1.iloc[7,2]] = df1.iloc[7,3]
b[df1.iloc[8,2]] = df1.iloc[8,3]
b[df1.iloc[9,2]] = df1.iloc[9,3]
b[df1.iloc[10,2]] = df1.iloc[10,3]
b[df1.iloc[11,2]] = df1.iloc[11,3]
b[df1.iloc[12,2]] = df1.iloc[12,3]
b[df1.iloc[13,2]] = df1.iloc[13,3]

c[df1.iloc[0,4]] = df1.iloc[0,5]
c[df1.iloc[1,4]] = df1.iloc[1,5]
c[df1.iloc[2,4]] = df1.iloc[2,5]
c[df1.iloc[3,4]] = df1.iloc[3,5]
c[df1.iloc[4,4]] = df1.iloc[4,5]
c[df1.iloc[5,4]] = df1.iloc[5,5]
c[df1.iloc[6,4]] = df1.iloc[6,5]
c[df1.iloc[7,4]] = df1.iloc[7,5]
c[df1.iloc[8,4]] = df1.iloc[8,5]
c[df1.iloc[9,4]] = df1.iloc[9,5]
c[df1.iloc[10,4]] = df1.iloc[10,5]
c[df1.iloc[11,4]] = df1.iloc[11,5]
c[df1.iloc[12,4]] = df1.iloc[12,5]
c[df1.iloc[13,4]] = df1.iloc[13,5]

d[df1.iloc[0,6]] = df1.iloc[0,7]
d[df1.iloc[1,6]] = df1.iloc[1,7]
d[df1.iloc[2,6]] = df1.iloc[2,7]
d[df1.iloc[3,6]] = df1.iloc[3,7]
d[df1.iloc[4,6]] = df1.iloc[4,7]
d[df1.iloc[5,6]] = df1.iloc[5,7]
d[df1.iloc[6,6]] = df1.iloc[6,7]
d[df1.iloc[7,6]] = df1.iloc[7,7]
d[df1.iloc[8,6]] = df1.iloc[8,7]
d[df1.iloc[9,6]] = df1.iloc[9,7]
d[df1.iloc[10,6]] = df1.iloc[10,7]
d[df1.iloc[11,6]] = df1.iloc[11,7]
d[df1.iloc[12,6]] = df1.iloc[12,7]
d[df1.iloc[13,6]] = df1.iloc[13,7]

e[df1.iloc[0,8]] = df1.iloc[0,9]
e[df1.iloc[1,8]] = df1.iloc[1,9]
e[df1.iloc[2,8]] = df1.iloc[2,9]
e[df1.iloc[3,8]] = df1.iloc[3,9]
e[df1.iloc[4,8]] = df1.iloc[4,9]
e[df1.iloc[5,8]] = df1.iloc[5,9]
e[df1.iloc[6,8]] = df1.iloc[6,9]
e[df1.iloc[7,8]] = df1.iloc[7,9]
e[df1.iloc[8,8]] = df1.iloc[8,9]
e[df1.iloc[9,8]] = df1.iloc[9,9]
e[df1.iloc[10,8]] = df1.iloc[10,9]
e[df1.iloc[11,8]] = df1.iloc[11,9]
e[df1.iloc[12,8]] = df1.iloc[12,9]
e[df1.iloc[13,8]] = df1.iloc[13,9]

f[df1.iloc[0,10]] = df1.iloc[0,11]
f[df1.iloc[1,10]] = df1.iloc[1,11]
f[df1.iloc[2,10]] = df1.iloc[2,11]
f[df1.iloc[3,10]] = df1.iloc[3,11]
f[df1.iloc[4,10]] = df1.iloc[4,11]
f[df1.iloc[5,10]] = df1.iloc[5,11]
f[df1.iloc[6,10]] = df1.iloc[6,11]
f[df1.iloc[7,10]] = df1.iloc[7,11]
f[df1.iloc[8,10]] = df1.iloc[8,11]
f[df1.iloc[9,10]] = df1.iloc[9,11]
f[df1.iloc[10,10]] = df1.iloc[10,11]
f[df1.iloc[11,10]] = df1.iloc[11,11]
f[df1.iloc[12,10]] = df1.iloc[12,11]
f[df1.iloc[13,10]] = df1.iloc[13,11]

g[df1.iloc[0,12]] = df1.iloc[0,13]
g[df1.iloc[1,12]] = df1.iloc[1,13]
g[df1.iloc[2,12]] = df1.iloc[2,13]
g[df1.iloc[3,12]] = df1.iloc[3,13]
g[df1.iloc[4,12]] = df1.iloc[4,13]
g[df1.iloc[5,12]] = df1.iloc[5,13]
g[df1.iloc[6,12]] = df1.iloc[6,13]
g[df1.iloc[7,12]] = df1.iloc[7,13]
g[df1.iloc[8,12]] = df1.iloc[8,13]
g[df1.iloc[9,12]] = df1.iloc[9,13]
g[df1.iloc[10,12]] = df1.iloc[10,13]
g[df1.iloc[11,12]] = df1.iloc[11,13]
g[df1.iloc[12,12]] = df1.iloc[12,13]
g[df1.iloc[13,12]] = df1.iloc[13,13]

h[df1.iloc[0,14]] = df1.iloc[0,15]
h[df1.iloc[1,14]] = df1.iloc[1,15]
h[df1.iloc[2,14]] = df1.iloc[2,15]
h[df1.iloc[3,14]] = df1.iloc[3,15]
h[df1.iloc[4,14]] = df1.iloc[4,15]
h[df1.iloc[5,14]] = df1.iloc[5,15]
h[df1.iloc[6,14]] = df1.iloc[6,15]
h[df1.iloc[7,14]] = df1.iloc[7,15]
h[df1.iloc[8,14]] = df1.iloc[8,15]
h[df1.iloc[9,14]] = df1.iloc[9,15]
h[df1.iloc[10,14]] = df1.iloc[10,15]
h[df1.iloc[11,14]] = df1.iloc[11,15]
h[df1.iloc[12,14]] = df1.iloc[12,15]
h[df1.iloc[13,14]] = df1.iloc[13,15]

i[df1.iloc[0,16]] = df1.iloc[0,17]
i[df1.iloc[1,16]] = df1.iloc[1,17]
i[df1.iloc[2,16]] = df1.iloc[2,17]
i[df1.iloc[3,16]] = df1.iloc[3,17]
i[df1.iloc[4,16]] = df1.iloc[4,17]
i[df1.iloc[5,16]] = df1.iloc[5,17]
i[df1.iloc[6,16]] = df1.iloc[6,17]
i[df1.iloc[7,16]] = df1.iloc[7,17]
i[df1.iloc[8,16]] = df1.iloc[8,17]
i[df1.iloc[9,16]] = df1.iloc[9,17]
i[df1.iloc[10,16]] = df1.iloc[10,17]
i[df1.iloc[11,16]] = df1.iloc[11,17]
i[df1.iloc[12,16]] = df1.iloc[12,17]
i[df1.iloc[13,16]] = df1.iloc[13,17]