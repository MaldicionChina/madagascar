sfsepcmplx2rsf = rsf.doc.rsfprog('sfsepcmplx2rsf','user/seplib_compat/Msepcmplx2rsf.py','''Convert legacy SEPlib complex datasets to RSF''')
sfsepcmplx2rsf.par('file',rsf.doc.rsfpar('string','','','''Name of file to process'''))
sfsepcmplx2rsf.par('preserve_t',rsf.doc.rsfpar('bool','y','','''Whether to preserve timestamp'''))
sfsepcmplx2rsf.par('verb',rsf.doc.rsfpar('bool','n','','''Say if file was converted or unchanged'''))
sfsepcmplx2rsf.version('1.7')
sfsepcmplx2rsf.synopsis('''sfsepcmplx2rsf file= preserve_t=y verb=n''','''
I.e. from 

esize=8 data_format=xdr_float

to 

esize=8 data_format=xdr_complex 

This combination is tolerated by SEPlib versions released after 2011-01-20,
and required by all versions of Madagascar. Previous to the date above, it
was impossible to have a complex single-precision dataset that was valid both
in SEPlib and Madagascar

This program opens the SEPlib file in read-write mode!

Handles in=stdin case (header and data in one file)
''')
rsf.doc.progs['sfsepcmplx2rsf']=sfsepcmplx2rsf

