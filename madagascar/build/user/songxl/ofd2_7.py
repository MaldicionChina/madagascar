sfofd2_7 = rsf.doc.rsfprog('sfofd2_7','user/songxl/Mofd2_7.c','''2-D Fourth-order Optimized Finite-difference wave extrapolation ''')
sfofd2_7.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfofd2_7.par('G',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfofd2_7.par('dt',rsf.doc.rsfpar('float','','',''''''))
sfofd2_7.par('nt',rsf.doc.rsfpar('int','','',''''''))
sfofd2_7.par('isx',rsf.doc.rsfpar('int','','',''''''))
sfofd2_7.par('isz',rsf.doc.rsfpar('int','','',''''''))
sfofd2_7.version('1.7')
sfofd2_7.synopsis('''sfofd2_7 > out.rsf vel=vel.rsf < source.rsf G=G.rsf dt= nt= isx= isz=''','''''')
rsf.doc.progs['sfofd2_7']=sfofd2_7

