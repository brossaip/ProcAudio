from pylab import plot, show, title, xlabel, ylabel, subplot
from scipy import fft, arange
FsLf = 44100.0/100 # Freqüència de mostreig per freqüències baixes fins 200 Hz.
FsMf = 44100.0/50 # Freqüència de mostreig per freqüències mitges, fins 400 Hz
FsHf = 44100.0 # Freqüència de mostreig per freqüències altes.

# Creem les bandes de pas i de tall dels diferents filtres
# Farem un array de totes les freqüències perquè es vagin agafant en un bucle al crear-se.
Wpass
