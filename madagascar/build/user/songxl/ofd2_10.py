sfofd2_10 = rsf.doc.rsfprog('sfofd2_10','user/songxl/Mofd2_10.c','''2-D Fourth-order Optimized Finite-difference wave extrapolation ''')
sfofd2_10.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfofd2_10.par('G',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfofd2_10.par('dt',rsf.doc.rsfpar('float','','',''''''))
sfofd2_10.par('nt',rsf.doc.rsfpar('int','','',''''''))
sfofd2_10.par('isx',rsf.doc.rsfpar('int','','',''''''))
sfofd2_10.par('isz',rsf.doc.rsfpar('int','','',''''''))
sfofd2_10.version('1.7')
sfofd2_10.synopsis('''sfofd2_10 > out.rsf vel=vel.rsf < source.rsf G=G.rsf dt= nt= isx= isz=''','''''')
rsf.doc.progs['sfofd2_10']=sfofd2_10

