sftouch = rsf.doc.rsfprog('sftouch','user/ivlad/Mtouch.py','''Applies the Unix command touch to binaries of RSF datasets in a directory.''')
sftouch.par('verb',rsf.doc.rsfpar('bool','n','','''Display what is wrong with the dataset'''))
sftouch.par('dir',rsf.doc.rsfpar('string','.','','''Directory with files'''))
sftouch.par('rec',rsf.doc.rsfpar('bool','n','','''Whether to go down recursively'''))
sftouch.par('chk4nan',rsf.doc.rsfpar('bool','n','','''Check for NaN values. Expensive!!'''))
sftouch.version('1.7')
sftouch.synopsis('''sftouch verb=n dir=. rec=n chk4nan=n''','''Will go down recursively in subdirectories. Current date and time is used.
Useful for determining disk leaks: Orphan binaries (those without headers) will
not be touched. You can remove them with commands such as:
find $DATAPATH -type f -mmin +15 -exec rm -f {} \;''')
rsf.doc.progs['sftouch']=sftouch

