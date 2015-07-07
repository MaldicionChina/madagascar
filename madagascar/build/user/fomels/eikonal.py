sfeikonal = rsf.doc.rsfprog('sfeikonal','user/fomels/Meikonal.c','''Fast marching eikonal solver (3-D). ''')
sfeikonal.par('shotfile',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfeikonal.par('vel',rsf.doc.rsfpar('bool','y','','''if y, the input is velocity; n, slowness squared '''))
sfeikonal.par('order',rsf.doc.rsfpar('int','2','[1,2]','''Accuracy order '''))
sfeikonal.par('sweep',rsf.doc.rsfpar('bool','n','','''if y, use fast sweeping instead of fast marching '''))
sfeikonal.par('br1',rsf.doc.rsfpar('float','d1','',''''''))
sfeikonal.par('br2',rsf.doc.rsfpar('float','d2','',''''''))
sfeikonal.par('br3',rsf.doc.rsfpar('float','d3','','''Constant-velocity box around the source (in physical dimensions) '''))
sfeikonal.par('plane1',rsf.doc.rsfpar('bool','n','',''''''))
sfeikonal.par('plane2',rsf.doc.rsfpar('bool','n','',''''''))
sfeikonal.par('plane3',rsf.doc.rsfpar('bool','n','','''plane-wave source '''))
sfeikonal.par('b1',rsf.doc.rsfpar('int','plane[2]? n1: (int) (br1/d1+0.5)','',''''''))
sfeikonal.par('b2',rsf.doc.rsfpar('int','plane[1]? n2: (int) (br2/d2+0.5)','',''''''))
sfeikonal.par('b3',rsf.doc.rsfpar('int','plane[0]? n3: (int) (br3/d3+0.5)','','''Constant-velocity box around the source (in samples) '''))
sfeikonal.par('zshot',rsf.doc.rsfpar('float','0.','','''Shot location (used if no shotfile) '''))
sfeikonal.par('yshot',rsf.doc.rsfpar('float','o2 + 0.5*(n2-1)*d2','',''''''))
sfeikonal.par('xshot',rsf.doc.rsfpar('float','o3 + 0.5*(n3-1)*d3','',''''''))
sfeikonal.par('shotfile',rsf.doc.rsfpar('string ',desc='''File with shot locations (n2=number of shots, n1=3) (auxiliary input file name)'''))
sfeikonal.version('1.7 Meikonal.c 12827 2014-06-12 04:04:58Z sfomel')
sfeikonal.synopsis('''sfeikonal < vel.rsf > time.rsf shotfile=shots.rsf vel=y order=2 sweep=n br1=d1 br2=d2 br3=d3 plane1=n plane2=n plane3=n b1=plane[2]? n1: (int) (br1/d1+0.5) b2=plane[1]? n2: (int) (br2/d2+0.5) b3=plane[0]? n3: (int) (br3/d3+0.5) zshot=0. yshot=o2 + 0.5*(n2-1)*d2 xshot=o3 + 0.5*(n3-1)*d3''','''
June 2014 program of the month:
http://ahay.org/rsflog/index.php?/archives/392-Program-of-the-month-sfeikonal.html
''')
rsf.doc.progs['sfeikonal']=sfeikonal

