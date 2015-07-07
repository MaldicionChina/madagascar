sfofd2_25 = rsf.doc.rsfprog('sfofd2_25','user/songxl/Mofd2_25.c','''2-D Fourth-order Optimized Finite-difference wave extrapolation ''')
sfofd2_25.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfofd2_25.par('G',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfofd2_25.par('s1',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfofd2_25.par('s2',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfofd2_25.par('dt',rsf.doc.rsfpar('float','','',''''''))
sfofd2_25.par('nt',rsf.doc.rsfpar('int','','',''''''))
sfofd2_25.par('isx',rsf.doc.rsfpar('int','','',''''''))
sfofd2_25.par('isz',rsf.doc.rsfpar('int','','',''''''))
sfofd2_25.version('1.7')
sfofd2_25.synopsis('''sfofd2_25 > out.rsf vel=vel.rsf < source.rsf G=G.rsf s1=files1.rsf s2=files2.rsf dt= nt= isx= isz=''','''''')
rsf.doc.progs['sfofd2_25']=sfofd2_25

