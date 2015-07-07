sfkine2dvti = rsf.doc.rsfprog('sfkine2dvti','user/chengjb/Mkine2dvti.c','''2-D two-components wavefield modeling using pseudo-pure mode P-wave equation in VTI media.''')
sfkine2dvti.par('WFp',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfkine2dvti.par('WFs',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfkine2dvti.par('nx',rsf.doc.rsfpar('int','201','',''''''))
sfkine2dvti.par('nz',rsf.doc.rsfpar('int','201','',''''''))
sfkine2dvti.par('dx',rsf.doc.rsfpar('float','0.008','',''''''))
sfkine2dvti.par('dz',rsf.doc.rsfpar('float','0.008','',''''''))
sfkine2dvti.par('time',rsf.doc.rsfpar('float','0.2','','''unit: SECOND '''))
sfkine2dvti.par('da',rsf.doc.rsfpar('float','0.05','',''''''))
sfkine2dvti.par('vp0',rsf.doc.rsfpar('float','3000.0','',''''''))
sfkine2dvti.par('vs0',rsf.doc.rsfpar('float','1200.0','',''''''))
sfkine2dvti.par('eps',rsf.doc.rsfpar('float','0.2','',''''''))
sfkine2dvti.par('del',rsf.doc.rsfpar('float','0.1','',''''''))
sfkine2dvti.par('the',rsf.doc.rsfpar('float','0.0','',''''''))
sfkine2dvti.par('t0',rsf.doc.rsfpar('float','0.04','',''''''))
sfkine2dvti.par('f0',rsf.doc.rsfpar('float','20.0','',''''''))
sfkine2dvti.version('1.7')
sfkine2dvti.synopsis('''sfkine2dvti > Fo1.rsf WFp=Fo2.rsf WFs=Fo3.rsf nx=201 nz=201 dx=0.008 dz=0.008 time=0.2 da=0.05 vp0=3000.0 vs0=1200.0 eps=0.2 del=0.1 the=0.0 t0=0.04 f0=20.0''','''   Copyright (C) 2012 Tongji University, Shanghai, China 
   Authors: Jiubing Cheng and Wei Kang
     
   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2 of the License, or
   (at your option) any later version.
             
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
                   
   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
''')
rsf.doc.progs['sfkine2dvti']=sfkine2dvti

