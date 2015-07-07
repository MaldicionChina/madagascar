sfsegyread = rsf.doc.rsfprog('sfsegyread','system/seismic/Msegyread.c','''Convert a SEG-Y or SU dataset to RSF.''')
sfsegyread.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsegyread.par('tfile',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsegyread.par('verb',rsf.doc.rsfpar('bool','n','','''Verbosity flag '''))
sfsegyread.par('su',rsf.doc.rsfpar('bool','','','''y if input is SU, n if input is SEGY '''))
sfsegyread.par('suxdr',rsf.doc.rsfpar('bool','n','','''y, SU has XDR support '''))
sfsegyread.par('endian',rsf.doc.rsfpar('bool','y','','''Whether to automatically estimate endianness or not '''))
sfsegyread.par('n2',rsf.doc.rsfpar('int','0','','''number of traces to read (if 0, read all traces) '''))
sfsegyread.par('format',rsf.doc.rsfpar('int','segyformat (bhead)','[1,2,3,5]','''Data format. The default is taken from binary header.
	   1 is IBM floating point
	   2 is 4-byte integer
	   3 is 2-byte integer
	   5 is IEEE floating point
       6 is native_float (same as RSF binary default)
	'''))
sfsegyread.par('ns',rsf.doc.rsfpar('int','segyns (bhead)','','''Number of samples. The default is taken from binary header '''))
sfsegyread.par('ns',rsf.doc.rsfpar('int','itrace[ segykey("ns")]','',''''''))
sfsegyread.par('tape',rsf.doc.rsfpar('string ',desc='''input data '''))
sfsegyread.par('hfile',rsf.doc.rsfpar('string ',desc='''output text data header file '''))
sfsegyread.par('bfile',rsf.doc.rsfpar('string ',desc='''output binary data header file '''))
sfsegyread.par('mask',rsf.doc.rsfpar('string ',desc='''optional header mask for reading only selected traces (auxiliary input file name)'''))
sfsegyread.par('read',rsf.doc.rsfpar('string ',desc='''what to read: h - header, d - data, b - both (default) '''))
sfsegyread.par('tfile',rsf.doc.rsfpar('string ',desc='''output trace header file (auxiliary output file name)'''))
sfsegyread.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfsegyread')
sfsegyread.version('1.7 Msegyread.c 13681 2014-12-14 00:35:32Z kschleicher')
sfsegyread.synopsis('''sfsegyread mask=msk.rsf > out.rsf tfile=hdr.rsf verb=n su= suxdr=n endian=y n2=0 format=segyformat (bhead) ns=segyns (bhead) ns=itrace[ segykey("ns")] tape= hfile= bfile= read=''','''
Data headers and trace headers are separated from the data.

"suread" is equivalent to "segyread su=y"


SEGY key names:

tracl: trace sequence number within line 0

tracr: trace sequence number within reel 4

fldr:     field record number 8 

tracf:    trace number within field record 12 

ep:       energy source point number 16 

cdp:      CDP ensemble number 20 

cdpt:     trace number within CDP ensemble 24 

trid:     trace identification code:
1 = seismic data
2 = dead
3 = dummy
4 = time break
5 = uphole
6 = sweep
7 = timing
8 = water break
9---, N = optional use (N = 32,767) 28 

nvs:      number of vertically summed traces 30 

nhs:      number of horizontally summed traces 32 

duse:     data use:
1 = production
2 = test 34

offset:   distance from source point to receiver
group (negative if opposite to direction
in which the line was shot) 36 

gelev:    receiver group elevation from sea level
(above sea level is positive) 40 

selev:    source elevation from sea level
(above sea level is positive) 44 

sdepth:   source depth (positive) 48 

gdel:     datum elevation at receiver group 52 

sdel:     datum elevation at source 56 

swdep:    water depth at source 60 

gwdep:    water depth at receiver group 64 

scalel:   scale factor for previous 7 entries
with value plus or minus 10 to the
power 0, 1, 2, 3, or 4 (if positive,
multiply, if negative divide) 68 

scalco:   scale factor for next 4 entries
with value plus or minus 10 to the
power 0, 1, 2, 3, or 4 (if positive,
multiply, if negative divide) 70 

sx:       X source coordinate 72 

sy:       Y source coordinate 76 

gx:       X group coordinate 80 

gy:       Y group coordinate 84 

counit:   coordinate units code:
for previous four entries
1 = length (meters or feet)
2 = seconds of arc (in this case, the
X values are unsigned longitude and the Y values
are latitude, a positive value designates
the number of seconds east of Greenwich
or north of the equator 88 

wevel:     weathering velocity 90 

swevel:    subweathering velocity 92 

sut:       uphole time at source 94 

gut:       uphole time at receiver group 96 

sstat:     source static correction 98 

gstat:     group static correction 100 

tstat:     total static applied 102 

laga:      lag time A, time in ms between end of 240-
byte trace identification header and time
break, positive if time break occurs after
end of header, time break is defined as
the initiation pulse which maybe recorded
on an auxiliary trace or as otherwise
specified by the recording system 104 

lagb:      lag time B, time in ms between the time
break and the initiation time of the energy source,
may be positive or negative 106 

delrt:     delay recording time, time in ms between
initiation time of energy source and time
when recording of data samples begins
(for deep water work if recording does not
start at zero time) 108 

muts:      mute time--start 110 

mute:      mute time--end 112 

ns:        number of samples in this trace 114 

dt:        sample interval, in micro-seconds 116 

gain:      gain type of field instruments code:
1 = fixed
2 = binary
3 = floating point
4 ---- N = optional use 118 

igc:       instrument gain constant 120 

igi:       instrument early or initial gain 122 

corr:      correlated:
1 = no
2 = yes 124

sfs:       sweep frequency at start 126 

sfe:       sweep frequency at end 128 

slen:      sweep length in ms 130 

styp:      sweep type code:
1 = linear
2 = cos-squared
3 = other 132

stas:      sweep trace length at start in ms 134 

stae:      sweep trace length at end in ms 136 

tatyp:     taper type: 1=linear, 2=cos^2, 3=other 138 

afilf:     alias filter frequency if used 140 

afils:     alias filter slope 142 

nofilf:    notch filter frequency if used 144 

nofils:    notch filter slope 146 

lcf:       low cut frequency if used 148 

hcf:       high cut frequncy if used 150 

lcs:       low cut slope 152 

hcs:       high cut slope 154 

year:      year data recorded 156 

day:       day of year 158 

hour:      hour of day (24 hour clock) 160 

minute:    minute of hour 162 

sec:       second of minute 164 

timbas:    time basis code:
1 = local
2 = GMT
3 = other 166

trwf:      trace weighting factor, defined as 1/2^N
volts for the least sigificant bit 168 

grnors:    geophone group number of roll switch
position one 170

grnofr:    geophone group number of trace one within
original field record 172

grnlof:    geophone group number of last trace within
original field record 174

gaps:      gap size (total number of groups dropped) 176 

otrav:     overtravel taper code: 
1 = down (or behind)
2 = up (or ahead) 178

cdpx:   X coordinate of CDP 180

cdpy:   Y coordinate of CDP 184

iline:  in-line number 188 

xline:  cross-line number 192

shnum:  shotpoint number 196

shsca:  shotpoint scalar 200

tval:   trace value meas. 202

tconst4: transduction const 204

tconst2: transduction const 208

tunits:  transduction units 210

device:  device identifier 212

tscalar: time scalar 214

stype:   source type 216

sendir:  source energy dir. 218
 
unknown: unknown 222

smeas4:  source measurement 224

smeas2:  source measurement 228

smeasu:  source measurement unit 230 

unass1:  unassigned 232

unass2:  unassigned 236
''')
rsf.doc.progs['sfsegyread']=sfsegyread

