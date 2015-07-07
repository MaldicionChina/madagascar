sftti3de = rsf.doc.rsfprog('sftti3de','user/chengjb/Mtti3de.c','''3-D three-components wavefield modeling using elasic wave equation in tilted TI media.''')
sftti3de.par('vs0',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftti3de.par('epsi',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftti3de.par('del',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftti3de.par('gam',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftti3de.par('the',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftti3de.par('phi',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftti3de.par('Elasticy',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti3de.par('Elasticz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti3de.par('ns',rsf.doc.rsfpar('int','301','',''''''))
sftti3de.par('dt',rsf.doc.rsfpar('float','0.001','',''''''))
sftti3de.par('bd',rsf.doc.rsfpar('int','20','',''''''))
sftti3de.version('1.7')
sftti3de.synopsis('''sftti3de < Fvp0.rsf vs0=Fvs0.rsf epsi=Fep.rsf del=Fde.rsf gam=Fga.rsf the=Fthe.rsf phi=Fphi.rsf > Fo1.rsf Elasticy=Fo2.rsf Elasticz=Fo3.rsf ns=301 dt=0.001 bd=20''','''
   Copyright (C) 2012 Tongji University, Shanghai, China 

   Authors: Jiubing Cheng, Tengfei Wang and Wei Kang
     
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
rsf.doc.progs['sftti3de']=sftti3de

