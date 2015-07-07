sftinterp = rsf.doc.rsfprog('sftinterp','user/llisiw/Mtinterp.c','''Traveltime interpolation by cubic Hermite spline ''')
sftinterp.par('deriv',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftinterp.par('pattern',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftinterp.par('type',rsf.doc.rsfpar('string ',desc='''type of interpolation (default Hermit) '''))
sftinterp.par('deriv',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sftinterp.par('pattern',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sftinterp.version('1.7')
sftinterp.synopsis('''sftinterp < in.rsf > out.rsf deriv=deriv.rsf pattern=pattern.rsf type=''','''''')
rsf.doc.progs['sftinterp']=sftinterp

