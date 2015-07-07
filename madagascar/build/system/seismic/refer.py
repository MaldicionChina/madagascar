sfrefer = rsf.doc.rsfprog('sfrefer','system/seismic/Mrefer.c','''Subtract a reference from a grid. ''')
sfrefer.par('ref',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfrefer.version('1.7')
sfrefer.synopsis('''sfrefer < in.rsf > out.rsf ref=ref.rsf''','''''')
rsf.doc.progs['sfrefer']=sfrefer

