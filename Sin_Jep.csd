<CsoundSynthesizer>; START O F A CSOUND FILE
<CsOptions> ; CSO UND CO NFIG URATIO N
;-odac ; Aquest sona en directe
-o So.wav ; Ho grava en un fitxer.
</CsOptions>
<CsInstruments> ; INSTRUMENT DEFINITIONS GO HERE
; Set the audio sample rate to 44100 Hz
sr = 44100
instr 1
; a 440 Hz Sine Wave
aSin oscils 0dbfs/4, 440, 0
     out aSin
endin
instr 2
; a 240 Hz Sine Wave
aSin oscils 0dbfs/4, 640, 0
     out aSin
endin
</CsInstruments>
<CsScore> ; SCORE EVENTS GO HERE
i 1 0 2
i 2 1 3
</CsScore>
</CsoundSynthesizer> ; END OF THE CSOUND FILE
; Anything after is ignored by Csound

