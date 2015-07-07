sffindmax = rsf.doc.rsfprog('sffindmax','user/psava/Mfindmax.py','''''')
sffindmax.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag'''))
sffindmax.version('1.7')
sffindmax.synopsis('''sffindmax < Fin.rsf > Fou.rsf verb=n''','''find max value in a file
''')
rsf.doc.progs['sffindmax']=sffindmax

