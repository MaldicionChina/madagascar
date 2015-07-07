/* This file is automatically generated. DO NOT EDIT! */

#ifndef _ssr3_h
#define _ssr3_h


#include <rsf.h>


#include "weutil.h"


/*------------------------------------------------------------*/
ssr3d ssr3_init( cub3d cub,
		 int px,
		 int py,
		 int tx,
		 int ty,
		 float dsmax
    );
/*< initialize >*/


/*------------------------------------------------------------*/
void ssr3_close(ssr3d ssr);
/*< free allocated storage >*/


/*------------------------------------------------------------*/
void ssr3_ssf(
    sf_complex       w /* frequency */,
    sf_complex    **wx /* wavefield */,
    cub3d          cub,
    ssr3d          ssr,
    tap3d          tap,
    slo3d          slo,
    int            imz,
    int         ompith
    );
/*< Wavefield extrapolation by SSF >*/


/*------------------------------------------------------------*/
void ssr3_sso(
    sf_complex    w /* frequency */,
    sf_complex **wx /* wavefield */,
    cub3d          cub,
    ssr3d          ssr,
    tap3d          tap,
    slo3d          slo,
    int            imz,
    int         ompith
    );
/*< Wavefield extrapolation by SSF w/ one reference slowness >*/


/*------------------------------------------------------------*/
void ssr3_phs(
    sf_complex    w /* frequency */,
    sf_complex **wx /* wavefield */,
    cub3d          cub,
    ssr3d          ssr,
    tap3d          tap,
    slo3d          slo,
    int            imz,
    int         ompith
    );
/*< Wavefield extrapolation by phase-shift >*/


/*------------------------------------------------------------*/
void ssr3_pho(
    sf_complex    w /* frequency */,
    sf_complex **wx /* wavefield */,
    cub3d          cub,
    ssr3d          ssr,
    tap3d          tap,
    slo3d          slo,
    int            imz,
    int         ompith
    );
/*< Wavefield extrapolation by phase-shift w/ one reference >*/

#endif
