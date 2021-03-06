
Notes = [16.35, 17.32, 18.35, 19.45, 20.60, 21.83, 23.12, 24.50, 25.96, 27.50, 29.14, 30.87, 32.70, 34.65, 36.71, 38.89, 41.20, 43.65, 46.25, 49.00, 51.91, 55.00, 58.27, 61.74, 65.41, 69.30, 73.42, 77.78, 82.41, 87.31, 92.50, 98.00, 103.83, 110.00, 116.54, 123.47, 130.81, 138.59, 146.83, 155.56, 164.81, 174.61, 185.00, 196.00, 207.65, 220.00, 233.08, 246.94, 261.63, 277.18, 293.66, 311.13, 329.63, 349.23, 369.99, 392.00, 415.30, 440.00, 466.16, 493.88, 523.25, 554.37, 587.33, 622.25, 659.25, 698.46, 739.99, 783.99, 830.61, 880.00, 932.33, 987.77, 1046.50, 1108.73, 1174.66, 1244.51, 1318.51, 1396.91, 1479.98, 1567.98, 1661.22, 1760.00, 1864.66, 1975.53, 2093.00, 2217.46, 2349.32, 2489.02, 2637.02, 2793.83, 2959.96, 3135.96, 3322.44, 3520.00, 3729.31, 3951.07, 4186.01, 4434.92, 4698.63, 4978.03, 5274.04, 5587.65, 5919.91, 6271.93, 6644.88, 7040.00, 7458.62, 7902.13]

import numpy as np
import scipy.signal as signal

FreqTall = np.zeros( len(Notes*2) )

FreqTall[0] = 10
for k in range( len(Notes)-1 ):
    FreqTall[ 2*k+1 ] = ( Notes[k] + Notes[k+1] ) / 2.0
    FreqTall[ 2*k+2 ] = FreqTall[ 2*k+1 ] 
FreqTall[ len(2*Notes)-1] = Notes[ -1 ] * 1.1

FreqPas = np.zeros( len(Notes*2) )
for k in range( len(Notes) ):
    FreqPas[ 2*k ] = ( Notes[k] + FreqTall[2*k] ) /2 
    FreqPas[ 2*k+1 ] = ( Notes[k] + FreqTall[2*k+1] ) /2 


FreqTall = [   10.   ,    16.835,    16.835,    17.835,    17.835,    18.9  ,    18.9  ,    20.025,    20.025,    21.215,    21.215,    22.475,    22.475,    23.81 ,    23.81 ,    25.23 ,    25.23 ,    26.73 ,    26.73 ,    28.32 ,    28.32 ,    30.005,    30.005,    31.785,    31.785,    33.675,    33.675,    35.68 ,    35.68 ,    37.8  ,    37.8  ,    40.045,    40.045,    42.425,    42.425,    44.95 ,    44.95 ,    47.625,    47.625,    50.455,    50.455,    53.455,    53.455,    56.635,    56.635,    60.005,    60.005,    63.575,    63.575,    67.355,    67.355,    71.36 ,    71.36 ,    75.6  ,    75.6  ,    80.095,    80.095,    84.86 ,    84.86 ,    89.905,    89.905,    95.25 ,    95.25 ,   100.915,   100.915,   106.915,   106.915,   113.27 ,   113.27 ,   120.005,   120.005,   127.14 ,   127.14 ,   134.7  ,   134.7  ,   142.71 ,   142.71 ,   151.195,   151.195,   160.185,   160.185,   169.71 ,   169.71 ,   179.805,   179.805,   190.5  ,   190.5  ,   201.825,   201.825,   213.825,   213.825,   226.54 ,   226.54 ,   240.01 ,   240.01 ,   254.285,   254.285,   269.405,   269.405,   285.42 ,   285.42 ,   302.395,   302.395,   320.38 ,   320.38 ,   339.43 ,   339.43 ,   359.61 ,   359.61 ,   380.995,   380.995,   403.65 ,   403.65 ,   427.65 ,   427.65 ,   453.08 ,   453.08 ,   480.02 ,   480.02 ,   508.565,   508.565,   538.81 ,   538.81 ,   570.85 ,   570.85 ,   604.79 ,   604.79 ,   640.75 ,   640.75 ,   678.855,   678.855,   719.225,   719.225,   761.99 ,   761.99 ,   807.3  ,   807.3  ,   855.305,   855.305,   906.165,   906.165,   960.05 ,   960.05 ,  1017.135,  1017.135,  1077.615,  1077.615,  1141.695,  1141.695,  1209.585,  1209.585,  1281.51 ,  1281.51 ,  1357.71 ,  1357.71 ,  1438.445,  1438.445,  1523.98 ,  1523.98 ,  1614.6  ,  1614.6  ,  1710.61 ,  1710.61 ,  1812.33 ,  1812.33 ,  1920.095,  1920.095,  2034.265,  2034.265,  2155.23 ,  2155.23 ,  2283.39 ,  2283.39 ,  2419.17 ,  2419.17 ,  2563.02 ,  2563.02 ,  2715.425,  2715.425,  2876.895,  2876.895,  3047.96 ,  3047.96 ,  3229.2  ,  3229.2  ,  3421.22 ,  3421.22 ,  3624.655,  3624.655,  3840.19 ,  3840.19 ,  4068.54 ,  4068.54 ,  4310.465,  4310.465,  4566.775,  4566.775,  4838.33 ,  4838.33 ,  5126.035,  5126.035,  5430.845,  5430.845,  5753.78 ,  5753.78 ,  6095.92 ,  6095.92 ,  6458.405,  6458.405,  6842.44 ,  6842.44 ,  7249.31 ,  7249.31 ,  7680.375,  7680.375,  8692.343]

FreqPas = [   13.175 ,    16.5925,    17.0775,    17.5775,    18.0925,18.625 ,    19.175 ,    19.7375,    20.3125,    20.9075,21.5225,    22.1525,    22.7975,    23.465 ,    24.155 ,24.865 ,    25.595 ,    26.345 ,    27.115 ,    27.91  ,28.73  ,    29.5725,    30.4375,    31.3275,    32.2425,33.1875,    34.1625,    35.165 ,    36.195 ,    37.255 ,38.345 ,    39.4675,    40.6225,    41.8125,    43.0375,44.3   ,    45.6   ,    46.9375,    48.3125,    49.7275,51.1825,    52.6825,    54.2275,    55.8175,    57.4525,59.1375,    60.8725,    62.6575,    64.4925,    66.3825,68.3275,    70.33  ,    72.39  ,    74.51  ,    76.69  ,78.9375,    81.2525,    83.635 ,    86.085 ,    88.6075,91.2025,    93.875 ,    96.625 ,    99.4575,   102.3725, 105.3725,   108.4575,   111.635 ,   114.905 ,   118.2725, 121.7375,   125.305 ,   128.975 ,   132.755 ,   136.645 , 140.65  ,   144.77  ,   149.0125,   153.3775,   157.8725, 162.4975,   167.26  ,   172.16  ,   177.2075,   182.4025, 187.75  ,   193.25  ,   198.9125,   204.7375,   210.7375, 216.9125,   223.27  ,   229.81  ,   236.545 ,   243.475 , 250.6125,   257.9575,   265.5175,   273.2925,   281.3   , 289.54  ,   298.0275,   306.7625,   315.755 ,   325.005 , 334.53  ,   344.33  ,   354.42  ,   364.8   ,   375.4925, 386.4975,   397.825 ,   409.475 ,   421.475 ,   433.825 , 446.54  ,   459.62  ,   473.09  ,   486.95  ,   501.2225, 515.9075,   531.03  ,   546.59  ,   562.61  ,   579.09  , 596.06  ,   613.52  ,   631.5   ,   650.    ,   669.0525, 688.6575,   708.8425,   729.6075,   750.99  ,   772.99  , 795.645 ,   818.955 ,   842.9575,   867.6525,   893.0825, 919.2475,   946.19  ,   973.91  ,  1002.4525,  1031.8175,1062.0575,  1093.1725,  1125.2125,  1158.1775,  1192.1225,1227.0475,  1263.01  ,  1300.01  ,  1338.11  ,  1377.31  ,1417.6775,  1459.2125,  1501.98  ,  1545.98  ,  1591.29  ,1637.91  ,  1685.915 ,  1735.305 ,  1786.165 ,  1838.495 ,1892.3775,  1947.8125,  2004.8975,  2063.6325,  2124.115 ,2186.345 ,  2250.425 ,  2316.355 ,  2384.245 ,  2454.095 ,2526.02  ,  2600.02  ,  2676.2225,  2754.6275,  2835.3625,2918.4275,  3003.96  ,  3091.96  ,  3182.58  ,  3275.82  ,3371.83  ,  3470.61  ,  3572.3275,  3676.9825,  3784.75  ,3895.63  ,  4009.805 ,  4127.275 ,  4248.2375,  4372.6925,4500.8475,  4632.7025,  4768.48  ,  4908.18  ,  5052.0325,5200.0375,  5352.4425,  5509.2475,  5670.715 ,  5836.845 ,6007.915 ,  6183.925 ,  6365.1675,  6551.6425,  6743.66  ,6941.22  ,  7144.655 ,  7353.965 ,  7569.4975,  7791.2525,8297.2365]

a_array = []
b_array = []
Fs_array = []
Rp = 1
As = 42
for k in range( len(Notes)-1 ):
    if Notes[k] < 200:
        Fs = 441
    elif Notes[k] < 2000:
        Fs = 4410
    else:
        Fs = 44100
    Wp = [ FreqPas[2*k] / (Fs/2), FreqPas[2*k+1] / (Fs/2) ]
    Ws = [ FreqTall[2*k] / (Fs/2), FreqTall[2*k+1] / (Fs/2) ]
    b,a = signal.iirdesign( Wp, Ws, Rp, As, ftype='ellip')
    a_array.append(a)
    b_array.append(b)
    Fs_array.append(Fs)

from pylab import plot, show, title, xlabel, ylabel, subplot
from scipy import fft, arange

Fs = 441
Wp = [FreqPas[0]/(Fs/2), FreqPas[1]/(Fs/2)]
Ws = [FreqTall[0]/(Fs/2), FreqTall[1]/(Fs/2)]
Rp = 1
As = 42
b,a = signal.iirdesign( Wp, Ws, Rp, As, ftype='ellip')
Ts=1.0/Fs
t=arange(0,1,Ts)
y=np.sin(2*np.pi*10*t)
yf = signal.filtfilt(b,a,y)

# Comprovar que si faig un senyal de 10 Hz de 44100 Fs. Si el sotamostrejo el recupero igual
Fs = 44100
Wp = [FreqPas[0]/(Fs/2), FreqPas[1]/(Fs/2)]
Ws = [FreqTall[0]/(Fs/2), FreqTall[1]/(Fs/2)]
Rp = 1
As = 42
b,a = signal.iirdesign( Wp, Ws, Rp, As, ftype='ellip')
Ts = 1.0/Fs
t=arange(0,1,Ts)
y=np.sin(2*np.pi*10*t)

# Fem el filtre pas baix del decimate
b,a = signal.cheby1(8,0.05,0.8/100)
ydeci = signal.filtfilt(b,a,y)
yd = ydeci[::100]
yf = signal.filtfilt(b,a,y)
# No es recupera igual, s'ha de fer un filtre pas baix i després reduir el senyal. Un exemple és la funció decimate.m d'octave. Fa un filtre cheby1(8,0.05,0.8/q) a on q és el factor a reduir.
# No veig que hagi de generar aliasing, ho he d'investigar més.
# Ja hi ha el decimate en el signal del python
# S'ha de fer el decimate amb el filtre fir sí que ha anat bé. Ara bé, teòricament no veig perquè agafar mostres de més tard, delmar, ha de crear aliasing. Si el senyal original l'hagués agafat amb el nou període, tindria els mateixos valors.
# Sí que s'ha de fer el decimate perquè posi les freqúències en sintonia, en el lloc que toqui. Altrament només hi ha freqüències molt altes.

# He de comprovar que tot el que he creat, tots els filtres, es comporten bé pels senyals que vull.
import numpy as np; import scipy.signal as signal;from pylab import plot, show, title, xlabel, ylabel, subplot;from scipy import fft, arange
Fs = 441
NotaProvar = 1
Wp = [FreqPas[2*NotaProvar]/(Fs/2) , FreqPas[2*NotaProvar+1]/(Fs/2)]
Ws = [FreqTall[2*NotaProvar]/(Fs/2), FreqTall[2*NotaProvar+1]/(Fs/2)]
Rp = 1
As = 42
b,a = signal.iirdesign( Wp, Ws, Rp, As, ftype='ellip')
Fs = Fs*100
Ts=1.0/Fs
t=arange(0,1,Ts)
y=np.sin(2*np.pi*Notes[ NotaProvar ]*t)
ydec = signal.filtfilt(b,a,y)
plot(ydec);show()
# !!!! El que retorna de senyal el firwin és el numerador, no té numerador i denominador com el iirdesign, així per filtrar-la ha de ser filtfilt(b,1 ó vector d'1s, senyal)
# Un cop comprovats he de crear les constants dels arrays a i b dels filtres. # Crec que l'hauré de crear com a classe perquè quan calculi el valor dels paràmetres del filtre me'ls retorni. No cal que sigui classe, ho puc fer com a funció.

# Mirar nota per nota el màxim que tenen i el màxim de la sinusoide a les freqüències de tall. Després mostrar el rati.