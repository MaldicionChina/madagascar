sfclip = rsf.doc.rsfprog('sfclip','system/generic/Mclip.c','''Clip the data.''')
sfclip.par('clip',rsf.doc.rsfpar('float','','','''clip value '''))
sfclip.par('value',rsf.doc.rsfpar('float','clip','','''replacement value '''))
sfclip.version('1.7')
sfclip.synopsis('''sfclip < in.rsf > out.rsf clip= value=clip''','''
The output is 
 clip if input > clip
-clip if input < -clip
input if |input| < clip 

See also sfclip2.

September 2011 program of the month:
http://ahay.org/rsflog/index.php?/archives/269-Program-of-the-month-sfclip.html
''')
rsf.doc.progs['sfclip']=sfclip

