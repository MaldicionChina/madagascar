import rsf.doc

sfquantile = rsf.doc.rsfprog('sfquantile','user/ivlad/Mquantile.c','''Computes what clip value corresponds to a given pclip.''')
sfquantile.par('pclip',rsf.doc.rsfpar('float','','','''Percentage clip, between 0 and 100 '''))
sfquantile.par('memsize',rsf.doc.rsfpar('int','sf_memsize()','','''Max amount of RAM (in Mb) to be used '''))
sfquantile.version('1.7')
sfquantile.synopsis('''sfquantile < in.rsf pclip= memsize=sf_memsize()''','''Loads the entire dataset in core. Use it to find a clip= parameter for sfclip, given a wanted pclip=''')
rsf.doc.progs['sfquantile']=sfquantile

sfleftsize = rsf.doc.rsfprog('sfleftsize','user/ivlad/Mleftsize.c','''Computes Ni+1 x Ni+2 x ...''')
sfleftsize.par('i',rsf.doc.rsfpar('int','0','','''What size to start counting from. i=0 gets total number of elements '''))
sfleftsize.version('1.7')
sfleftsize.synopsis('''sfleftsize < in.rsf i=0''','''Wrapper for sf_leftsize''')
rsf.doc.progs['sfleftsize']=sfleftsize

sffiledims = rsf.doc.rsfprog('sffiledims','user/ivlad/Mfiledims.c','''Computes number of dimensions and their values''')
sffiledims.par('large',rsf.doc.rsfpar('bool','n','','''if y, file with large dimensions. '''))
sffiledims.par('parform',rsf.doc.rsfpar('bool','y','','''If y, print out parameter=value. If n, print out value. '''))
sffiledims.version('1.7')
sffiledims.synopsis('''sffiledims < in.rsf large=n parform=y''','''Wrapper for sf_filedims. ''')
rsf.doc.progs['sffiledims']=sffiledims

sffileflush = rsf.doc.rsfprog('sffileflush','user/ivlad/Mfileflush.c','''Creates just the ascii header from parameters''')
sffileflush.version('1.7')
sffileflush.synopsis('''sffileflush < in.rsf > out.rsf''','''Wrapper for sf_fileflush (copy RSF header of a file to another) ''')
rsf.doc.progs['sffileflush']=sffileflush

sfcreate = rsf.doc.rsfprog('sfcreate','user/ivlad/Mcreate.c','''Creates just the ascii header from parameters''')
sfcreate.par('n#',rsf.doc.rsfpar('int','','','''size of #-th axis '''))
sfcreate.version('1.7')
sfcreate.synopsis('''sfcreate > out.rsf n#=''','''Wrapper for sf_fileflush (creating RSF header from params) ''')
rsf.doc.progs['sfcreate']=sfcreate

sfgettype = rsf.doc.rsfprog('sfgettype','user/ivlad/Mgettype.c','''Displays numerical type of a dataset''')
sfgettype.version('1.7')
sfgettype.synopsis('''sfgettype < in.rsf''','''Output can be be: SF_CHAR, SF_COMPLEX, SF_FLOAT, SF_INT, SF_SHORT, SF_UCHAR
Shell/tester for sf_gettype''')
rsf.doc.progs['sfgettype']=sfgettype

sflmo = rsf.doc.rsfprog('sflmo','user/ivlad/Mlmo.c','''Linear move-out in the frequency domain''')
sflmo.par('p',rsf.doc.rsfpar('float','','','''Slope of LMO '''))
sflmo.version('1.7')
sflmo.synopsis('''sflmo < in.rsf > out.rsf p=''','''''')
rsf.doc.progs['sflmo']=sflmo

sfmulticheck = rsf.doc.rsfprog('sfmulticheck','user/ivlad/Mmulticheck.c','''Check whether all values in a dataset are a multiple of a factor or not ''')
sfmulticheck.par('i_fac',rsf.doc.rsfpar('int','','',''''''))
sfmulticheck.version('1.7')
sfmulticheck.synopsis('''sfmulticheck < in.rsf i_fac=''','''''')
rsf.doc.progs['sfmulticheck']=sfmulticheck

sfhist2 = rsf.doc.rsfprog('sfhist2','user/ivlad/Mhist2.c','''Compute a 2-D histogram of integer- or float-valued input data''')
sfhist2.par('inp2',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfhist2.par('n1',rsf.doc.rsfpar('int','','','''number of histogram samples in dimension 1 '''))
sfhist2.par('o1',rsf.doc.rsfpar('float','','','''histogram origin for dimension 1 '''))
sfhist2.par('d1',rsf.doc.rsfpar('float','','','''histogram sampling for dimension 1 '''))
sfhist2.par('n2',rsf.doc.rsfpar('int','','','''number of histogram samples in dimension 2 '''))
sfhist2.par('o2',rsf.doc.rsfpar('float','','','''histogram origin for dimension 2 '''))
sfhist2.par('d2',rsf.doc.rsfpar('float','','','''histogram sampling for dimension 2 '''))
sfhist2.version('1.7')
sfhist2.synopsis('''sfhist2 < in.rsf inp2=inp2.rsf > out.rsf n1= o1= d1= n2= o2= d2=''','''The output grid is not centered on the bins; it marks their "left edge".
I.e., the first sample holds the number of values between o1 and o1+d1''')
rsf.doc.progs['sfhist2']=sfhist2

sfsparsify = rsf.doc.rsfprog('sfsparsify','user/ivlad/Msparsify.c','''Transforms regular 2-D array to sparse array''')
sfsparsify.par('nonzero',rsf.doc.rsfpar('int','n1*n2','','''Number of nonzero elements in input '''))
sfsparsify.version('1.7')
sfsparsify.synopsis('''sfsparsify < in.rsf > out.rsf nonzero=n1*n2''','''Input is int or float array
Output is a float nonzero-by-3 array, where 
nonzero=`<input.rsf sfattr want=nonzero | awk -F '= ' '{ print $2 }';`
column 0 holds the data values (converted from int to float, if necessary),
column 1 holds coordinate values (i.e. o+i*d, not indices i) for dimension
1 of input, and column 2 the coordinate values for dimension 2 of input ''')
rsf.doc.progs['sfsparsify']=sfsparsify

sfcsqrtf = rsf.doc.rsfprog('sfcsqrtf','user/ivlad/Mcsqrtf.c','''Complex square root. Good example of I/O loop for applying a function.''')
sfcsqrtf.version('1.7')
sfcsqrtf.synopsis('''sfcsqrtf < in.rsf > out.rsf''','''Realized after I wrote this program that the sqrt function in sfmath does the
same job, but keeping it around as a simple example of buffer I/O. ''')
rsf.doc.progs['sfcsqrtf']=sfcsqrtf

sfpad2nextfastsize = rsf.doc.rsfprog('sfpad2nextfastsize','user/ivlad/Mpad2nextfastsize.c','''How much to pad to get to next fast c2c FFT size (factors: 2,3 and 5)''')
sfpad2nextfastsize.par('n',rsf.doc.rsfpar('int','','',''''''))
sfpad2nextfastsize.version('1.7')
sfpad2nextfastsize.synopsis('''sfpad2nextfastsize n=''','''Wrapper for kiss_fft_next_fast_size. ''')
rsf.doc.progs['sfpad2nextfastsize']=sfpad2nextfastsize

sfpclip = rsf.doc.rsfprog('sfpclip','user/ivlad/Mpclip.py','''Percentile clip. Shell for sfclip(sfquantile(input)).''')
sfpclip.par('inp',rsf.doc.rsfpar('string','','','''input file'''))
sfpclip.par('out',rsf.doc.rsfpar('string','','','''output file'''))
sfpclip.par('verb',rsf.doc.rsfpar('bool','n','','''if y, print system commands, outputs'''))
sfpclip.par('pclip',rsf.doc.rsfpar('float','99','','''percentile clip'''))
sfpclip.version('1.7')
sfpclip.synopsis('''sfpclip inp= out= verb=n pclip=99''','''''')
rsf.doc.progs['sfpclip']=sfpclip

sfprep4plot = rsf.doc.rsfprog('sfprep4plot','user/ivlad/Mprep4plot.py','''Resamples a 2-D dataset to the desired picture resolution, with antialias''')
sfprep4plot.par('inp',rsf.doc.rsfpar('string','','','''input file'''))
sfprep4plot.par('out',rsf.doc.rsfpar('string','','','''output file'''))
sfprep4plot.par('verb',rsf.doc.rsfpar('bool','n','','''if y, print system commands, outputs'''))
sfprep4plot.par('h',rsf.doc.rsfpar('int','768','','''output height'''))
sfprep4plot.par('w',rsf.doc.rsfpar('int','1024','','''output width'''))
sfprep4plot.par('h',rsf.doc.rsfpar('string','','',''''''))
sfprep4plot.par('w',rsf.doc.rsfpar('string','','',''''''))
sfprep4plot.par('unit',rsf.doc.rsfpar('string','px','','''unit of h and w. Can be: px, mm, cm, in'''))
sfprep4plot.par('ppi',rsf.doc.rsfpar('int','','','''outp. resolution (px/in). Necessary when unit!=px'''))
sfprep4plot.par('prar',rsf.doc.rsfpar('bool','y','','''if y, PReserve Aspect Ratio of input'''))
sfprep4plot.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfprep4plot')
sfprep4plot.version('1.7')
sfprep4plot.synopsis('''sfprep4plot inp= out= verb=n h=768 w=1024 h= w= unit=px ppi= prar=y''','''Only one of the h and w parameters needs to be specified.
If prar=n, no action will be taken on axis for which h/w was not specified
If prar=y and only one par (h or w) is specified, the picture will scale
along both axes until it is of the specified dimension.''')
rsf.doc.progs['sfprep4plot']=sfprep4plot

sfwiki2static = rsf.doc.rsfprog('sfwiki2static','user/ivlad/Mwiki2static.py','''Downloads the Madagascar wiki as static html''')
sfwiki2static.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag'''))
sfwiki2static.par('outdir',rsf.doc.rsfpar('string','.','',''''''))
sfwiki2static.version('1.7')
sfwiki2static.synopsis('''sfwiki2static verb=n outdir=.''','''Wiki pages are downloaded every time. Main_Page is moved to index.html
Html files in local dir are deleted if not present on the wiki, in order
to avoid accumulation of dead wiki pages. To save bandwidth cost and
download time, images and linked documents are downloaded only if a
local copy is not present.''')
rsf.doc.progs['sfwiki2static']=sfwiki2static

sfinvalid = rsf.doc.rsfprog('sfinvalid','user/ivlad/Minvalid.py','''Finds RSF files with missing or incomplete binaries or headers.''')
sfinvalid.par('verb',rsf.doc.rsfpar('bool','n','','''Display what is wrong with the dataset'''))
sfinvalid.par('dir',rsf.doc.rsfpar('string','.','','''Directory with files'''))
sfinvalid.par('rec',rsf.doc.rsfpar('bool','n','','''Whether to go down recursively'''))
sfinvalid.par('chk4nan',rsf.doc.rsfpar('bool','n','','''Check for NaN values. Expensive!!'''))
sfinvalid.version('1.7')
sfinvalid.synopsis('''sfinvalid verb=n dir=. rec=n chk4nan=n''','''Delete them all with shell constructs like: rm -f `sfinvalid dir=.`''')
rsf.doc.progs['sfinvalid']=sfinvalid

sfsplit = rsf.doc.rsfprog('sfsplit','user/ivlad/Msplit.py','''Splits file into slices along the last dimension''')
sfsplit.par('verb',rsf.doc.rsfpar('bool','n','',''''''))
sfsplit.par('inp',rsf.doc.rsfpar('string','','','''ifile.rsf'''))
sfsplit.par('outdir',rsf.doc.rsfpar('string','(out_basenm+ivlad.ext','',''''''))
sfsplit.par('nthick',rsf.doc.rsfpar('int','1','','''slice thickness'''))
sfsplit.version('1.7')
sfsplit.synopsis('''sfsplit verb=n inp= outdir=(out_basenm+ivlad.ext nthick=1''','''Usage:

sfsplit inp=file.rsf outdir=[file_split.rsf] nthick=[1]

Parameter nthick gives the maximum thickness of a slice. The last slice may
be thinner.''')
rsf.doc.progs['sfsplit']=sfsplit

sfzcp = rsf.doc.rsfprog('sfzcp','user/ivlad/Mzcp.py','''Copies header of float file, fills output binary with zeros''')
sfzcp.version('1.7')
sfzcp.synopsis('''sfzcp''','''Usage: sfzcp file1.rsf file2.rsf''')
rsf.doc.progs['sfzcp']=sfzcp

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

sfrmrf = rsf.doc.rsfprog('sfrmrf','user/ivlad/Mrmrf.py','''Recursively removes all RSF headers in a directory (associated binaries too)''')
sfrmrf.par('verb',rsf.doc.rsfpar('bool','n','','''Display headers and binaries being deleted'''))
sfrmrf.par('dir',rsf.doc.rsfpar('string','','','''Directory with files'''))
sfrmrf.par('rec',rsf.doc.rsfpar('bool','n','','''Whether to go down recursively'''))
sfrmrf.version('1.7')
sfrmrf.synopsis('''sfrmrf verb=n dir= rec=n''','''Missing binaries do not cause failure.''')
rsf.doc.progs['sfrmrf']=sfrmrf

sfcsv2rsf = rsf.doc.rsfprog('sfcsv2rsf','user/ivlad/Mcsv2rsf.py','''Convert a delimited-text ASCII file to RSF binary floating point or int.''')
sfcsv2rsf.par('delimiter',rsf.doc.rsfpar('string',',','','''Separator between values in input file'''))
sfcsv2rsf.par('dtype',rsf.doc.rsfpar('string','float','','''Input type'''))
sfcsv2rsf.par('verb',rsf.doc.rsfpar('bool','n','','''Whether to echo n1, n2, infill/truncation'''))
sfcsv2rsf.par('debug',rsf.doc.rsfpar('bool','n','','''Extra verbosity for debugging'''))
sfcsv2rsf.par('trunc',rsf.doc.rsfpar('bool','n','','''Truncate or add zeros if nr elems in rows differs'''))
sfcsv2rsf.par('o1',rsf.doc.rsfpar('float','0.','',''''''))
sfcsv2rsf.par('o2',rsf.doc.rsfpar('float','0.','',''''''))
sfcsv2rsf.par('d1',rsf.doc.rsfpar('float','1.','',''''''))
sfcsv2rsf.par('d2',rsf.doc.rsfpar('float','1.','',''''''))
sfcsv2rsf.par('unit1',rsf.doc.rsfpar('string','unknown','',''''''))
sfcsv2rsf.par('unit2',rsf.doc.rsfpar('string','unknown','',''''''))
sfcsv2rsf.par('label1',rsf.doc.rsfpar('string','unknown','',''''''))
sfcsv2rsf.par('label2',rsf.doc.rsfpar('string','unknown','',''''''))
sfcsv2rsf.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfcsv2rsf')
sfcsv2rsf.version('1.7')
sfcsv2rsf.synopsis('''sfcsv2rsf delimiter=, dtype=float verb=n debug=n trunc=n o1=0. o2=0. d1=1. d2=1. unit1=unknown unit2=unknown label1=unknown label2=unknown''','''Zeros will be added if number of elements is not the same in each row.
n1 and n2 are computed automatically. For consistency with sfdisfil and 
sfmatmult, output is C-style order (row-first), i.e. rows in input file 
become dimension-1 columns in output. Output encoding is native. If n2=1 in
output, the second dimension will not be written to the header.''')
rsf.doc.progs['sfcsv2rsf']=sfcsv2rsf

sfwuab = rsf.doc.rsfprog('sfwuab','user/ivlad/Mwuab.py','''Wrapper for Utilities Acting on Binaries''')
sfwuab.par('prog',rsf.doc.rsfpar('string','','','''Non-madagascar utility'''))
sfwuab.par('inp',rsf.doc.rsfpar('string','','','''Input file'''))
sfwuab.par('tpar',rsf.doc.rsfpar('string','','','''Translated params, i.e.: "ni1=n1 ni2=n2"'''))
sfwuab.par('ipar',rsf.doc.rsfpar('string','','','''Independent params, i.e. "perc=100 cmap=rgb"'''))
sfwuab.par('verb',rsf.doc.rsfpar('bool','n','',''''''))
sfwuab.version('1.7')
sfwuab.synopsis('''sfwuab prog= inp= tpar= ipar= verb=n''','''''')
rsf.doc.progs['sfwuab']=sfwuab

sfximage = rsf.doc.rsfprog('sfximage','user/ivlad/Mximage.py','''Displays a 2-D RSF file with Seismic Unix's ximage''')
sfximage.par('inp',rsf.doc.rsfpar('string','','','''Input file'''))
sfximage.par('par',rsf.doc.rsfpar('string','','','''ximage params that can't be found in RSF headr'''))
sfximage.par('verb',rsf.doc.rsfpar('bool','n','',''''''))
sfximage.version('1.7')
sfximage.synopsis('''sfximage inp= par= verb=n''','''Test with:
sfspike n1=5 n2=3 nsp=3 k1=1,3,4 k2=1,2,3 > junk.rsf;
sfximage inp=junk.rsf par="perc=100 cmap=rgb1 legend=1";
You should see a picture with blue background and red blobs.
See also sfimage.''')
rsf.doc.progs['sfximage']=sfximage

sfseekwin = rsf.doc.rsfprog('sfseekwin','user/ivlad/Mseekwin.f90','''Cannot take input from a pipe because stdin cannot be seeked through''')
sfseekwin.par('whence',rsf.doc.rsfpar('','sf_seek_set','',''''''))
sfseekwin.par('nseek',rsf.doc.rsfpar('','10         ','',''''''))
sfseekwin.par('nread',rsf.doc.rsfpar('','10         ','',''''''))
sfseekwin.version('1.7')
sfseekwin.synopsis('''sfseekwin < in.rsf > out.rsf whence=sf_seek_set nseek=10          nread=10         ''','''''')
rsf.doc.progs['sfseekwin']=sfseekwin

