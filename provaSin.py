Python 3.3.5 (default, Mar 27 2014, 17:16:46) [GCC] on linux
Type "copyright", "credits" or "license()" for more information.
>>> import matplotlib.pylab as plt
>>> import numpy as np
>>> from pylab import plot, show, title, xlabel, ylabel, subplot
>>> from scipy import fft, arange
>>> Fs = 44100
>>> ff = 1000
>>> t=arange(0,1,Ts)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    t=arange(0,1,Ts)
NameError: name 'Ts' is not defined
>>> Ts=1/Fs
>>> t=arange(0,1,Ts)
>>> y=np.sin(2*np.pi*ff*t)
>>> # Vull fer un filtre que deixi passar fins al 500 hz i que ens atenui el senyal original
>>> Fpass=500
>>> Fstop = 1e3
>>> Wp = Fpass/Fs
>>> wp
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    wp
NameError: name 'wp' is not defined
>>> Wp
0.011337868480725623
>>> Ws = Fstop/Fs
>>> Rp=1 # passband ripple db
>>> As = 42 # stopband attenuation dB
>>> import scipy.signal as signal
>>> b,a = signal.iir
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    b,a = signal.iir
AttributeError: 'module' object has no attribute 'iir'
>>> b,a = signal.iirdesign( Wp, Ws, Rp, As, ftype='ellip')
>>> b
array([ 0.00785187, -0.03124143,  0.04677963, -0.03124143,  0.00785187])
>>> a
array([ 1.        , -3.96515832,  5.8974087 , -3.89930589,  0.96705606])
>>> yf = signal.filtfilt(b,a,y)
>>> plot( y,t)
[<matplotlib.lines.Line2D object at 0x7fdd0d261c10>]
>>> show()
>>> plot( y,t,'r')
[<matplotlib.lines.Line2D object at 0x7fdd08d25210>]
>>> show()
>>> plot( t,y )
[<matplotlib.lines.Line2D object at 0x7fdd0d1fe690>]
>>> show()
>>> show()
>>> plot( t,y )
[<matplotlib.lines.Line2D object at 0x7fdd08d25250>]
>>> show()
>>> plot( t,yf )
[<matplotlib.lines.Line2D object at 0x7fdd0d20b5d0>]
>>> show()
>>> plot( t,yf )
[<matplotlib.lines.Line2D object at 0x7fdd08d1a890>]
>>> plot( t,y,'r')
[<matplotlib.lines.Line2D object at 0x7fdd08bdb950>]
>>> show()
>>> # No se perque a http://dsp.stackexchange.com/questions/2864... tornen a dividir per 2.
# Per veure el gràfic.
def mfreqz(b,a=1):
    w,h = signal.freqz(b,a)
    h_dB = 20 * log10 (abs(h))
    subplot(211)
    plot(w/max(w),h_dB)
    ylim(-150, 5)
    ylabel('Magnitude (db)')
    xlabel(r'Normalized Frequency (x$\pi$rad/sample)')
    title(r'Frequency response')
    subplot(212)
    h_Phase = unwrap(arctan2(imag(h),real(h)))
    plot(w/max(w),h_Phase)
    ylabel('Phase (radians)')
    xlabel(r'Normalized Frequency (x$\pi$rad/sample)')
    title(r'Phase response')
    subplots_adjust(hspace=0.5)
    show()
