sfort3dpseudophomo = rsf.doc.rsfprog('sfort3dpseudophomo','user/chengjb/Mort3dpseudophomo.c','''3-D three-components wavefield modeling using pseudo-pure mode P-wave equation in tilted ORT media.''')
sfort3dpseudophomo.par('PseudoPurePy',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfort3dpseudophomo.par('PseudoPurePz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfort3dpseudophomo.par('ns',rsf.doc.rsfpar('int','301','',''''''))
sfort3dpseudophomo.par('ny',rsf.doc.rsfpar('int','101','',''''''))
sfort3dpseudophomo.par('nx',rsf.doc.rsfpar('int','101','',''''''))
sfort3dpseudophomo.par('nz',rsf.doc.rsfpar('int','101','',''''''))
sfort3dpseudophomo.par('dt',rsf.doc.rsfpar('float','0.001','',''''''))
sfort3dpseudophomo.par('dx',rsf.doc.rsfpar('float','0.0','',''''''))
sfort3dpseudophomo.par('dy',rsf.doc.rsfpar('float','0.0','',''''''))
sfort3dpseudophomo.par('dz',rsf.doc.rsfpar('float','0.0','',''''''))
sfort3dpseudophomo.par('vp0',rsf.doc.rsfpar('float','3000.0','',''''''))
sfort3dpseudophomo.par('vs0',rsf.doc.rsfpar('float','1500.0','',''''''))
sfort3dpseudophomo.par('epsi1',rsf.doc.rsfpar('float','0.2','',''''''))
sfort3dpseudophomo.par('epsi2',rsf.doc.rsfpar('float','0.067','',''''''))
sfort3dpseudophomo.par('del1',rsf.doc.rsfpar('float','0.1','',''''''))
sfort3dpseudophomo.par('del2',rsf.doc.rsfpar('float','-0.0422','',''''''))
sfort3dpseudophomo.par('del3',rsf.doc.rsfpar('float','0.125','',''''''))
sfort3dpseudophomo.par('gam1',rsf.doc.rsfpar('float','0.1','',''''''))
sfort3dpseudophomo.par('gam2',rsf.doc.rsfpar('float','0.047','',''''''))
sfort3dpseudophomo.par('bd',rsf.doc.rsfpar('int','20','',''''''))
sfort3dpseudophomo.version('1.7')
sfort3dpseudophomo.synopsis('''sfort3dpseudophomo > Fo1.rsf PseudoPurePy=Fo2.rsf PseudoPurePz=Fo3.rsf ns=301 ny=101 nx=101 nz=101 dt=0.001 dx=0.0 dy=0.0 dz=0.0 vp0=3000.0 vs0=1500.0 epsi1=0.2 epsi2=0.067 del1=0.1 del2=-0.0422 del3=0.125 gam1=0.1 gam2=0.047 bd=20''','''
   Refernces:
   Cheng et al. (15th IWSA, 2012);
   Cheng and Kang (SEG Abstract, 2012);
   Kang and Cheng (SEG Abstract, 2012)
   Wang et al.(SEG Abstract, 2012)      

   Copyright (C) 2012 Tongji University, Shanghai, China 

   Authors: Jiubing Cheng, Tengfei Wang and Wei Kang
     
   This code is first written by Tengfei Wang at Tongji University,
   and then optimzied by Jiubing Cheng for Madagascar version at BEG,
   University of Texas at Austin.

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
rsf.doc.progs['sfort3dpseudophomo']=sfort3dpseudophomo

