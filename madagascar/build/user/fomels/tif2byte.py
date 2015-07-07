sftif2byte = rsf.doc.rsfprog('sftif2byte','user/fomels/_tif2byte.c','''Convert TIFF image to byte RSF. ''')
sftif2byte.version('1.7')
sftif2byte.synopsis('''sftif2byte > out.rsf < file.tiff ''','''''')
rsf.doc.progs['sftif2byte']=sftif2byte

