Python 3.3.5 (default, Mar 27 2014, 17:16:46) [GCC] on linux
Type "copyright", "credits" or "license()" for more information.
>>> from pylab import plot, show, title, xlabel, ylabel, subplot
>>> from scipy import fft, arange
>>> Fs = 44100
>>> ff = 1000
>>> import scipy.signal as signal
>>> Fpass = [15 17]/Fs
SyntaxError: invalid syntax
>>> Fpass = [15/Fs 17/Fs]
SyntaxError: invalid syntax
>>> Fpass = [15, 17]/Fs
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    Fpass = [15, 17]/Fs
TypeError: unsupported operand type(s) for /: 'list' and 'int'
>>> Fpass = [15/Fs, 17/Fs]
>>> Wp = Fpass
>>> Ws = [10/Fs, 18/Fs]
>>> Rp=1
>>> As = 42
>>> b,a = signal.iirdesign( Wp, Ws, Rp, As, ftype='ellip')
>>> b
array([ 0.00794446, -0.06355564,  0.22244464, -0.44488915,  0.55611139,
       -0.44488915,  0.22244464, -0.06355564,  0.00794446])
>>> w,h = signal.freqz(b,a)
>>> h_dB = 20 * log10 (abs(h))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    h_dB = 20 * log10 (abs(h))
NameError: name 'log10' is not defined
>>> from numpy
SyntaxError: invalid syntax
>>> from numpy import * 
>>> h_dB = 20 * log10 (abs(h))
>>> plot(w/max(w),h_dB)
[<matplotlib.lines.Line2D object at 0x7f6770b23510>]
>>> show()
>>> Ts=1/Fs
>>> t=arange(0,1,Ts)
>>> y=sin(2*pi*10*t)+sin(2*pi*100*t)+sin(2*pi*16*t)
>>> plot(t,y)
[<matplotlib.lines.Line2D object at 0x7f676c581b50>]
>>> show()
>>> yf = signal.filtfilt(b,a,y)
>>> plot(t,yf)
[<matplotlib.lines.Line2D object at 0x7f6770afb910>]
>>> show()
>>> t
array([  0.00000000e+00,   2.26757370e-05,   4.53514739e-05, ...,
         9.99931973e-01,   9.99954649e-01,   9.99977324e-01])
>>> yf
array([              nan,               nan,               nan, ...,
        -2.85157790e+274,  -2.86748252e+274,  -2.88362853e+274])
>>> y=sin(2*pi*16*t)
>>> plot(t,y)
[<matplotlib.lines.Line2D object at 0x7f676c86d210>]
>>> show()
>>> yf = signal.filtfilt(b,a,y)
>>> plot(t,yf)
[<matplotlib.lines.Line2D object at 0x7f676c872750>]
>>> show
<function show at 0x7f6783a7e4d0>
>>> show()
>>> Fpass = [400/Fs, 600/Fs]
>>> Wpass = [400/Fs, 600/Fs]
>>> Ws = [200/Fs, 700/Fs]
>>> b,a = signal.iirdesign( Wp, Ws, Rp, As, ftype='ellip')
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    b,a = signal.iirdesign( Wp, Ws, Rp, As, ftype='ellip')
  File "/usr/lib64/python3.3/site-packages/scipy/signal/filter_design.py", line 655, in iirdesign
    N, Wn = ordfunc(wp, ws, gpass, gstop, analog=analog)
  File "/usr/lib64/python3.3/site-packages/scipy/signal/filter_design.py", line 2135, in ellipord
    disp=0)
  File "/usr/lib64/python3.3/site-packages/scipy/optimize/optimize.py", line 1535, in fminbound
    res = _minimize_scalar_bounded(func, (x1, x2), args, **options)
  File "/usr/lib64/python3.3/site-packages/scipy/optimize/optimize.py", line 1556, in _minimize_scalar_bounded
    raise ValueError("The lower bound exceeds the upper bound.")
ValueError: The lower bound exceeds the upper bound.
>>> b,a = signal.iirdesign( Wpass, Ws, Rp, As, ftype='ellip')
>>> b
array([ 0.00789821, -0.06312045,  0.22075857, -0.44132165,  0.55157063,
       -0.44132165,  0.22075857, -0.06312045,  0.00789821])
>>> y=sin(2*pi*500*t)
>>> yf = signal.filtfilt(b,a,y)
>>> plot(t,yf)
[<matplotlib.lines.Line2D object at 0x7f676c840950>]
>>> show()
>>> Wpass = [400/Fs/2, 600/Fs/2]
>>> Ws = [200/Fs/2, 700/Fs/2]
>>> b,a = signal.iirdesign( Wp, Ws, Rp, As, ftype='ellip')
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    b,a = signal.iirdesign( Wp, Ws, Rp, As, ftype='ellip')
  File "/usr/lib64/python3.3/site-packages/scipy/signal/filter_design.py", line 655, in iirdesign
    N, Wn = ordfunc(wp, ws, gpass, gstop, analog=analog)
  File "/usr/lib64/python3.3/site-packages/scipy/signal/filter_design.py", line 2135, in ellipord
    disp=0)
  File "/usr/lib64/python3.3/site-packages/scipy/optimize/optimize.py", line 1535, in fminbound
    res = _minimize_scalar_bounded(func, (x1, x2), args, **options)
  File "/usr/lib64/python3.3/site-packages/scipy/optimize/optimize.py", line 1556, in _minimize_scalar_bounded
    raise ValueError("The lower bound exceeds the upper bound.")
ValueError: The lower bound exceeds the upper bound.
>>> b,a = signal.iirdesign( Wpass, Ws, Rp, As, ftype='ellip')
>>> b
array([ 0.00792   , -0.0633436 ,  0.22166168, -0.44327428,  0.5540724 ,
       -0.44327428,  0.22166168, -0.0633436 ,  0.00792   ])
>>> a
array([  1.        ,  -7.9920293 ,  27.94550538, -55.84040932,
        69.7404921 , -55.74695723,  27.8520469 ,  -7.95197111,   0.99332257])
>>> yf = signal.filtfilt(b,a,y)
>>> plot(t,yf)
[<matplotlib.lines.Line2D object at 0x7f676c595ad0>]
>>> show()
>>> >>> Ts=1.0/Fs
>>> Ts
2.2675736961451248e-05
>>> t=arange(0,1,Ts)
>>> y=sin(2*pi*500*t)

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    y=sin(2*pi*500*t)
NameError: name 'sin' is not defined
>>> from numpy import *
>>> y=sin(2*pi*500*t)
>>> Wpass = [400/Fs, 600/Fs]
>>> Wpass
[0, 0]
>>> Wpass = [400.0/Fs, 600.0/Fs]
>>> Ws = [200.0/Fs, 700.0/Fs]
>>> Rp=1
>>> As = 42
>>> b,a = signal.iirdesign( Wpass, Ws, Rp, As, ftype='ellip')
>>> yf = signal.filtfilt(b,a,y)
plot(t,yf)
[<matplotlib.lines.Line2D object at 0x7f676c84
 
[<matplotlib.lines.Line2D object at 0x268b710>]
show()
