/* This file is automatically generated. DO NOT EDIT! */

#ifndef _dsp_h
#define _dsp_h


float fir(int ma, int na, float *a,
	  float *x, int d1);
/*< FIR filter
  na
  y(n) = sum a[k]*x[n-k] 
  k=ma
  >*/


float fir2(int m1, int n1, float *a1, 
	   int m2, int n2, float *a2,
	   float *x, int d1, int d2);
/*< FIR filter
  n2    n1
  y[m][n] = sum   sum a2[k2]*a1[k1]*x[m-k2][n-k1] 
  k2=m2 k1=m1
  >*/


float iir(int na, float *a, int nb, float *b,
	  float *x, int d1, float *y, int d2);
/*< IIR causal filter
  na                nb
  y(n) = ( sum a[k]*x[n-k] - sum b[k]*y[n-k] )/b[0]
  k=ma              k=mb
  >*/


void firs(int ma, int na, float *a,
	  float *x, int d1, int n1, 
	  float *y, int d2);
/*< FIR filter
  na
  y(n) = sum a[k]*x[n-k] 
  k=ma
  >*/


void iirs(int na, float *a, int nb, float *b,
	  float *x, int d1, int n1, 
	  float *y, int d2);
/*< IIR filter
  na                nb
  y(n) = ( sum a[k]*x[n-k] - sum b[k]*y[n-k] )/b[0]
  k=0               k=1
  >*/


void allpass(int na, float *a,
	     float *x, int d1, int n1, 
	     float *y, int d2);
/*< allpass filter
  na                na
  y(n) = ( sum a[k]*x[n-k] - sum a[na-k]*y[n-k] )/a[na]
  k=0               k=1
  >*/


sf_complex fir_freq(int m, int n, float *h, float f);
/*< FIR frequency response 
  n
  H(e^{jw}) = sum h[k] e^{-jwk}
  k=m
  >*/


sf_complex iir_freq(int ma, int na, float *a, 
		    int mb, int nb, float *b, float f);
/*< IIR frequency response 
  na
  sum a[k] e^{-jwk}
  k=ma
  H(e^{jw}) = ---------------------
  nb
  sum b[k] e^{-jwk}
  k=mb
  >*/


sf_complex allpass_freq(int n, float *a, float f);
/*< frequency response of allpass filter
  n
  sum a[k] e^{-jwk}
  k=-n
  H(e^{jw}) = ---------------------
  n
  sum a[k] e^{jwk}
  k=-n
  >*/

#endif
