sfinvalid = rsf.doc.rsfprog('sfinvalid','user/ivlad/Minvalid.py','''Finds RSF files with missing or incomplete binaries or headers.''')
sfinvalid.par('verb',rsf.doc.rsfpar('bool','n','','''Display what is wrong with the dataset'''))
sfinvalid.par('dir',rsf.doc.rsfpar('string','.','','''Directory with files'''))
sfinvalid.par('rec',rsf.doc.rsfpar('bool','n','','''Whether to go down recursively'''))
sfinvalid.par('chk4nan',rsf.doc.rsfpar('bool','n','','''Check for NaN values. Expensive!!'''))
sfinvalid.version('1.7')
sfinvalid.synopsis('''sfinvalid verb=n dir=. rec=n chk4nan=n''','''Delete them all with shell constructs like: rm -f `sfinvalid dir=.`''')
rsf.doc.progs['sfinvalid']=sfinvalid

