<CsoundSynthesizer>; START O F A CSOUND FILE
<CsOptions> ; CSO UND CO NFIG URATIO N
-odac ; Aquest sona en directe
-o So.wav ; Ho grava en un fitxer.
</CsOptions>
<CsInstruments> ; INSTRUM ENT DEFINITIO NS G O HERE
; Set the audio sample rate to 44100 Hz
sr = 44100
instr 1
; a 440 Hz Sine Wave
aSin oscils 0dbfs/4, 440, 0
     out aSin
endin
</CsInstruments>
<CsScore> ; SCO RE EVENTS GO HERE
i 1 0 1
</CsScore>
</CsoundSynthesizer> ; END O F THE CSO UND FILE
; Anything after is ignored by Csound
