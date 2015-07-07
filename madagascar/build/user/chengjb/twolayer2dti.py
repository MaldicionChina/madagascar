sftwolayer2dti = rsf.doc.rsfprog('sftwolayer2dti','user/chengjb/Mtwolayer2dti.c','''2-D two-components wavefield modeling using pseudo-pure mode P-wave equation in VTI media.''')
sftwolayer2dti.par('vs0',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftwolayer2dti.par('epsi',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftwolayer2dti.par('del',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftwolayer2dti.par('the',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftwolayer2dti.par('nx',rsf.doc.rsfpar('int','201','',''''''))
sftwolayer2dti.par('nz',rsf.doc.rsfpar('int','201','',''''''))
sftwolayer2dti.par('dx',rsf.doc.rsfpar('float','0.008','',''''''))
sftwolayer2dti.par('dz',rsf.doc.rsfpar('float','0.008','',''''''))
sftwolayer2dti.par('vp0_1',rsf.doc.rsfpar('float','3000.0','',''''''))
sftwolayer2dti.par('vs0_1',rsf.doc.rsfpar('float','1200.0','',''''''))
sftwolayer2dti.par('eps_1',rsf.doc.rsfpar('float','0.2','',''''''))
sftwolayer2dti.par('del_1',rsf.doc.rsfpar('float','0.1','',''''''))
sftwolayer2dti.par('the_1',rsf.doc.rsfpar('float','0.0','',''''''))
sftwolayer2dti.par('vp0_2',rsf.doc.rsfpar('float','3000.0','',''''''))
sftwolayer2dti.par('vs0_2',rsf.doc.rsfpar('float','1200.0','',''''''))
sftwolayer2dti.par('eps_2',rsf.doc.rsfpar('float','0.2','',''''''))
sftwolayer2dti.par('del_2',rsf.doc.rsfpar('float','0.1','',''''''))
sftwolayer2dti.par('the_2',rsf.doc.rsfpar('float','30.0','','''Unit: degree '''))
sftwolayer2dti.version('1.7')
sftwolayer2dti.synopsis('''sftwolayer2dti > Fo1.rsf vs0=Fo2.rsf epsi=Fo3.rsf del=Fo4.rsf the=Fo5.rsf nx=201 nz=201 dx=0.008 dz=0.008 vp0_1=3000.0 vs0_1=1200.0 eps_1=0.2 del_1=0.1 the_1=0.0 vp0_2=3000.0 vs0_2=1200.0 eps_2=0.2 del_2=0.1 the_2=30.0''','''   Copyright (C) 2012 Tongji University, Shanghai, China 
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
rsf.doc.progs['sftwolayer2dti']=sftwolayer2dti

