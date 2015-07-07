/* Vplot filter for X-Window */

/*
  Copyright (C) 1987 The Board of Trustees of Stanford University
  
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
*/

/*
 *
 *  source file:   ./filters/x11penlib/x11penconf.c
 *
 * Joe Dellinger (SEP), June 11 1987
 *	Inserted this sample edit history entry.
 *	Please log any further modifications made to this file:
 * Stewart A. Levin (DRL), September 21, 1988
 *      Cribbed Xpen version
 * Dave Nichols (SEP), July 27, 1989
 *      Now uses new xraster routine, and corrected xarea .
 */

/*
 *
 *  source file:   ./filters/x11penlib/xarea.c
 *
 * Joe Dellinger (SEP), June 11 1987
 *	Inserted this sample edit history entry.
 *	Please log any further modifications made to this file:
 * Stewart A. Levin (DRL), September 21, 1988
 *	Cribbed xpen for X-11 Windows version.
 * Dave Nichols (SEP), July 27, 1989
 *	Corrected calling sequence for XFillPolygon
 */

/*
 *
 *  source file:   ./filters/x11penlib/xattr.c
 *
 * Joe Dellinger (SEP), June 11 1987
 *	Inserted this sample edit history entry.
 *	Please log any further modifications made to this file:
 * Stewart A. Levin (DRL), September 21, 1988
 *	Cribbed Xpen for XU01 Windows version.
 */

/*
 *
 *  source file:   ./filters/x11penlib/xclose.c
 *
 * Joe Dellinger (SEP), June 11 1987
 *	Inserted this sample edit history entry.
 *	Please log any further modifications made to this file:
 * Stewart A. Levin (DRL), September 21, 1988
 *      Cribbed xpen to support X-11 windows
 * Stewart A. Levin (DRL), December 30, 1988
 *      Exit on button press only, ignore keyboard.  This makes it easier
 *      to edit in another window without accidentally blowing plot away.
 */

/*
 *
 *  source file:   ./filters/x11penlib/xerase.c
 *
 * Joe Dellinger (SEP), June 11 1987
 *	Inserted this sample edit history entry.
 *	Please log any further modifications made to this file:
 * Stewart A. Levin (DRL), September 11, 1988
 *	Cribbed Xpen for X-11 Windows version.
 * Stewart A. Levin (Mobil), May 8, 1996
 *	Use R5 treatment of GC's.
 */

/*
 *
 *  source file:   ./filters/x11penlib/xgetpoint.c
 *
 * Joe Dellinger (SEP), June 11 1987
 *	Inserted this sample edit history entry.
 *	Please log any further modifications made to this file:
 * Stewart A. Levin (DRL), September 21, 1988
 *	Cribbed Xpen for X-11 Windows version.
 */

/*
 *
 *  source file:   ./filters/x11penlib/xopen.c
 *
 * Joe Dellinger (SEP), June 11 1987
 *	Inserted this sample edit history entry.
 *	Please log any further modifications made to this file:
 * Stewart A. Levin (DRL), September 21, 1988
 *      Cribbed xpen to support X-11 windows
 * Stewart A. Levin (DRL), January 16, 1989
 *	Added recognition of server subscreen notation
 * Steve Cole (SEP), July 6, 1989
 *      Added wait for exposure event to make it work with window manager.
 * Dave Nichols (SEP), July 27, 1989
 *      Changed colormap handling, if it can it gets its own colormap.
 */

/*
 *
 *  source file:   ./filters/x11penlib/xplot.c
 *
 * Joe Dellinger (SEP), June 11 1987
 *	Inserted this sample edit history entry.
 *	Please log any further modifications made to this file:
 * Stewart A. Levin (DRL), September 21, 1988
 *      Cribbed xpen to support X-11 Windows.
 */

/*
 *
 *  source file:   ./filters/x11penlib/xpoint.c
 *
 * Joe Dellinger (SEP), June 11 1987
 *	Inserted this sample edit history entry.
 *	Please log any further modifications made to this file:
 * Stewart A. Levin (DRL), September 21, 1988
 *	Cribbed Xpen for X-11 Windows.
 */

/*
 *
 *  source file:   ./filters/x11penlib/xraster.c
 *
 * Joe Dellinger (SEP), June 11 1987
 *	Inserted this sample edit history entry.
 *	Please log any further modifications made to this file:
 * Stewart A. Levin (DRL), September 21, 1988
 *	Cribbed Xpen for X-11 Windows version.
 * Dave Nichols (SEP), July 27, 1989
 *	Total rewrite, should support mono case and all orientations,
 *	and cases where we use a pulic colormap (e.g. DirectColor visuals).
 *      It is still slow(but more general), so go buy a faster machine.
 */

#include <string.h>
#include <stdio.h>

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

#include <X11/Xlib.h>
#include <X11/Xutil.h>

#include <rsfplot.h>

#include "../include/extern.h"
#include "../include/attrcom.h"
#include "../include/closestat.h"
#include "../include/mesgcom.h"
#include "../include/erasecom.h"
#include "../include/enum.h"
#include "../include/params.h"

#include "dovplot.h"
#include "init_vplot.h"

#include "../utilities/util.h"
#include "../genlib/genpen.h"

#include "x11doc.h"
#include "x11pen.h"

#include "_x11.h"

char name[] = "x11pen";

#include "_device.h"

/* physical device size */
int             version = 1;

#define MAXVERT 1000
XPoint vlist[MAXVERT];

void xarea (int npts, struct vertex  *head)
/*< area >*/
{
    int             i;

    /* translate data structures */
    for (i = 0; i < npts && i < MAXVERT; i++)
    {
	vlist[i].x = XCORD (head->x);
	vlist[i].y = YCORD (head->y);
	head = head->next;
    }
    XDrawLines(pen_display, pen_win, pen_gc, vlist, npts, CoordModeOrigin);
    XFillPolygon(pen_display, pen_win, pen_gc, vlist, npts, Complex, CoordModeOrigin);
}


/* we cannot control pixel values for public color table entries in X,
   so mapping is used */
/* colors 0, 1 for windows */

int             color;	/* current color */
static int imap = 2; /* allocated color count */
#define U0 (~((unsigned long) 0))
unsigned long  map[256] = { U0, U0, U0, U0, U0, U0, U0, U0,
			    U0, U0, U0, U0, U0, U0, U0, U0,
			    U0, U0, U0, U0, U0, U0, U0, U0,
			    U0, U0, U0, U0, U0, U0, U0, U0,
			    U0, U0, U0, U0, U0, U0, U0, U0,
			    U0, U0, U0, U0, U0, U0, U0, U0,
			    U0, U0, U0, U0, U0, U0, U0, U0,
			    U0, U0, U0, U0, U0, U0, U0, U0,
			    U0, U0, U0, U0, U0, U0, U0, U0,
			    U0, U0, U0, U0, U0, U0, U0, U0,
			    U0, U0, U0, U0, U0, U0, U0, U0,
			    U0, U0, U0, U0, U0, U0, U0, U0,
			    U0, U0, U0, U0, U0, U0, U0, U0,
			    U0, U0, U0, U0, U0, U0, U0, U0,
			    U0, U0, U0, U0, U0, U0, U0, U0,
			    U0, U0, U0, U0, U0, U0, U0, U0,
			    U0, U0, U0, U0, U0, U0, U0, U0,
			    U0, U0, U0, U0, U0, U0, U0, U0,
			    U0, U0, U0, U0, U0, U0, U0, U0,
			    U0, U0, U0, U0, U0, U0, U0, U0,
			    U0, U0, U0, U0, U0, U0, U0, U0,
			    U0, U0, U0, U0, U0, U0, U0, U0,
			    U0, U0, U0, U0, U0, U0, U0, U0,
			    U0, U0, U0, U0, U0, U0, U0, U0,
			    U0, U0, U0, U0, U0, U0, U0, U0,
			    U0, U0, U0, U0, U0, U0, U0, U0,
			    U0, U0, U0, U0, U0, U0, U0, U0,
			    U0, U0, U0, U0, U0, U0, U0, U0,
			    U0, U0, U0, U0, U0, U0, U0, U0,
			    U0, U0, U0, U0, U0, U0, U0, U0,
			    U0, U0, U0, U0, U0, U0, U0, U0,
			    U0, U0, U0, U0, U0, U0, U0, U0 };

void xattributes (int command, int v, int v1, int v2, int v3)
/*< attributes >*/
{
    XColor           def;

    switch (command)
    {
	case SET_COLOR:
	    if (!dev.num_col)
	    {
		if (v)
		    color = 1;
		else
		    color = 0;
	    }
	    else
	    {
		if (v < dev.num_col)
		    color = map[v];
	    }
	    XSetForeground(pen_display, pen_gc, color);
	    break;
	case SET_COLOR_TABLE:
	    if(map[v] != U0) {/* dealloc that color first if using public colormap*/
		if( !own_colormap ){
		    XFreeColors(pen_display, pen_colormap, map+v, 1, AllPlanes); 
		}
		imap--;
	    }
	    
	    if (++imap >= dev.num_col)
		break;
	    def.red = v1 << 8;
	    def.green = v2 << 8;
	    def.blue = v3 << 8;
	    def.pixel = v;
	    def.flags = DoRed | DoGreen | DoBlue;
	    
	    /* put the color in the colormap, we can specify the pixel value if we
	       own the colormap, otherwise we must accept what pixel we are given */
	    if( own_colormap ){
		def.pixel = v;
		XStoreColor( pen_display, pen_colormap, &def );
		map[v] = def.pixel;
	    }else{
		
	 	if( !XAllocColor(pen_display, pen_colormap, &def)){
		    map[v]=1;
		}else{
		    map[v] = def.pixel;
		}
	    }
	    
	    
	    
	    if(v == 0) { /* change of background color */
		XSetBackground(pen_display, pen_gc, def.pixel);
		XSetWindowBackground(pen_display, pen_win, def.pixel);
		XClearWindow(pen_display, pen_win);
	    }
	    break;
    }
}


void xclose (int status)
/*< close >*/
{
    XEvent event;
    int             /* fd ,*/ pid;
    char           *option;
    bool persist;

    switch (status)
    {
	
	case CLOSE_FLUSH:
	    XFlush (pen_display);
	    break;
	    
	case CLOSE_DONE:
	    
	    if ((option = XGetDefault (pen_display, name, "Stay")) != NULL)
		if ((option[0] == 'y') || (option[0] == 'Y') || (option[0] == '1'))
		    persist = true;
	    if (!sf_getbool("stay",&persist)) persist=false;
	    /* open terminal to count keys */

	    /* fd = open ("/dev/tty", 0); */
	    if (!persist)
	    {
		dev.message (MESG_TEXT, "Click mouse in window to end.\n");
		XSync (pen_display, True);
		/* die on mouse click */
		XSelectInput (pen_display, pen_win, ButtonPressMask);
		/* wait for mouse click in display */
		XNextEvent(pen_display, &event);
	    }
	    else
	    {
		pid = fork ();
		if (pid < 0)
		{
		    fprintf (stderr, "x11pen: xclose: Couldn't fork a child\n");
		    XCloseDisplay (pen_display);
		    exit (-1);
		}
		else
		    if (pid > 0)
		    {
			_exit (0);
		    }
		    else
			if (pid == 0)
			{
			    dev.message (MESG_TEXT, "Click mouse in vplot window to end.\n");
			    /*	XSync (pen_display, True); */
			    /* die on key or mouse click */
			    XSelectInput (pen_display, pen_win, ButtonPressMask);
			    XNextEvent(pen_display, &event);
			    XSelectInput (pen_display, pen_win, 0);
			}
	    }
	    
	    XCloseDisplay (pen_display);
    }
}

void xerase (int command)
/*< erase >*/
{
    unsigned long   erase_color;
    unsigned long	prev_color;
    XGCValues look_em_up;

    XGetGCValues(pen_display, pen_gc, GCForeground|GCBackground,&look_em_up);
    
    switch (command)
    {
	case ERASE_START:
	case ERASE_MIDDLE:
	case ERASE_BREAK:
	    if (!dev.num_col)
		erase_color = 0;
	    else
		erase_color = look_em_up.background;
	    prev_color = look_em_up.foreground;
	    XSetForeground(pen_display, pen_gc, erase_color);
	    XFillRectangle (pen_display, pen_win, pen_gc, 0, 0,
			    dev.xmax, dev.ymax);
	    XSetForeground(pen_display, pen_gc, prev_color);
	    break;
    }
}

int xgetpoint (int *x, int *y)
/*< getpoint >*/
{
    XEvent event;

    XSync (pen_display, True);
    XSelectInput (pen_display, pen_win, ButtonPressMask);
    XNextEvent(pen_display,&event);
    XSelectInput (pen_display, pen_win, 0);
    *x = XCORD (event.xbutton.x);
    *y = YCORD (event.xbutton.y);
    return (0);
}

/* pen colors */
/* black, blue, red, magenta, green, cyan, yellow, white */
unsigned char   red[256] = {0, 0, 255, 255, 0, 0, 255, 255};
unsigned char   green[256] = {0, 0, 0, 0, 255, 255, 255, 255};
unsigned char   blue[256] = {0, 255, 0, 255, 0, 255, 0, 255};

Display        *pen_display;
int		pen_screen;
Window          pen_win;
GC		pen_gc;
Visual 	       *pen_visual;
Colormap	pen_colormap;
int		own_colormap;
float           win_xfrac = .77;
float           win_yfrac = .56;
char           *align;

void opendev (int argc, char* argv[])
/*< open >*/
{
    int             win_x, win_y, i;
    char            title[50], *ap, *option;
    Display        *OpenDisplay ();
    XEvent		event;

    dev.erase = xerase;
    dev.close = xclose;
    dev.area = xarea;
    dev.raster = xraster;
    dev.point = xpoint;
    dev.attributes = xattributes;
    dev.getpoint = xgetpoint;
    dev.plot = xplot;

    dev.xmin = 0;
    dev.ymin = 0;
    dev.pixels_per_inch = 72.;
    dev.aspect_ratio = 1.;

    /* device capabilities */
    dev.need_end_erase = true;

    /* find a display server */
    pen_display = OpenDisplay ();
    if (pen_display == NULL)
	sf_error("Can't find a display");
    pen_screen = DefaultScreen(pen_display);
    
    /* pen window dimensions */
    if ((option = XGetDefault (pen_display, name, "Width")) != NULL)
	win_xfrac = (float) atof (option);
    if ((option = XGetDefault (pen_display, name, "Height")) != NULL)
	win_yfrac = (float) atof (option);
    sf_getfloat("width",&win_xfrac);
    sf_getfloat ("height",&win_yfrac);
    dev.xmax = win_xfrac * (DisplayWidth (pen_display,pen_screen) - 2 * BORDER);
    dev.ymax = win_yfrac * (DisplayHeight (pen_display,pen_screen) - TBORDER - BORDER);

    /* pen window alignment- win_x & win_y */
    align = sf_getstring("align");
    if (NULL == align) {
	align = sf_charalloc(5);

	if ((option = XGetDefault (pen_display, name, "Align")) != NULL) {
	    strcpy (align, option);
	} else {
	    strcpy (align, "tr");
	}
    }
    
    win_x = DisplayWidth (pen_display,pen_screen) - dev.xmax - 2 * BORDER;	/* right default */
    win_y = 0;			/* top default */
    for (ap = align; *ap != '\0'; ap++)
	switch (*ap)
	{
	    case 't':		/* top */
		win_y = 0;
		break;
	    case 'm':		/* middle vertical */
		win_y = (DisplayHeight (pen_display,pen_screen) - dev.ymax - TBORDER - BORDER) / 2;
		break;
	    case 'b':		/* bottom */
		win_y = DisplayHeight (pen_display,pen_screen) - dev.ymax - TBORDER - BORDER;
		break;
	    case 'l':		/* left */
		win_x = 0;
		break;
	    case 'c':		/* center horizontal */
		win_x = (DisplayWidth (pen_display,pen_screen) - dev.xmax - 2 * BORDER) / 2;
		break;
	    case 'r':		/* right horizontal */
		win_x = DisplayWidth (pen_display,pen_screen) - dev.xmax - 2 * BORDER;
		break;
	}
    
    pen_visual = DefaultVisual(pen_display, pen_screen);
    
    /* color support */
    dev.num_col = DisplayCells(pen_display, pen_screen);
    if( dev.num_col <= 2 ) mono=true;

#if defined(__cplusplus) || defined(c_plusplus)
    if ( pen_visual->c_class == PseudoColor ){
#else
    if ( pen_visual->class == PseudoColor ){
#endif	
	pen_colormap = XCreateColormap(pen_display,
				       RootWindow(pen_display, pen_screen), pen_visual,  AllocAll);
	own_colormap = 1;
    }else{
        pen_colormap = DefaultColormap(pen_display, pen_screen);
	own_colormap = 0;
    }
    
    
    /* spawn window */
    sprintf (title, "XPEN %d x %d", dev.xmax, dev.ymax);
    pen_win = XCreateSimpleWindow (pen_display, RootWindow(pen_display,pen_screen),
				   win_x, win_y, dev.xmax, dev.ymax, BORDER, None, None);
    XSetWindowBackground(pen_display, pen_win,
			 BlackPixel(pen_display,pen_screen));
    XSetWindowColormap( pen_display, pen_win, pen_colormap );
    XStoreName(pen_display, pen_win, title);
    XMapWindow (pen_display, pen_win);
    
    
    /* graphics context */
    pen_gc = XCreateGC(pen_display, pen_win, 0, NULL);
    XSetLineAttributes(pen_display,pen_gc, 0, LineSolid, CapButt, JoinRound);
    XSetPlaneMask(pen_display, pen_gc, AllPlanes);
    XSetFunction(pen_display, pen_gc, GXcopy);
    XSetFillRule(pen_display, pen_gc, WindingRule);
    XSetBackground(pen_display,pen_gc,BlackPixel(pen_display, pen_screen));
    
    /* color support */
    xattributes (SET_COLOR, 1, 0, 0, 0);
    
    if( dev.num_col > 2){
    	for (i = 0; i < 8; i++)
	    xattributes (SET_COLOR_TABLE, i, red[i], green[i], blue[i]);
    }
    
    /* ignore all events for now except expose events*/
    XSelectInput(pen_display,pen_win,ExposureMask);
    
    /* wait for exposure event */
    XNextEvent(pen_display,&event);
    switch(event.type) {
	case Expose:
	    break;
	default:
	    break;
    }
}

/* routine to find display server; check getpar */
Display  *OpenDisplay ()
{
    char            name[50], *host;
    Display		*display;
    
    display = NULL;
    
    /* check getpar first */
    host = sf_getstring("server"); /* X server */
    if (NULL != host)
    {
	display = XOpenDisplay (host);
	if (display != NULL)
	    sf_warning ("X-server=%s", DisplayString(display));
	else			/* add :0 to getpar name */
	{
	    sprintf (name, "%s:0", host);
	    display = XOpenDisplay (name);
	    if (display != NULL)
		fprintf (stderr, "X-server=%s\n", DisplayString(display));
	}
	return (display);
    }

    display = XOpenDisplay(NULL);
    if (display != NULL)
	sf_warning ("X-server=%s", DisplayString(display));
    return(display);
}

void xplot (int x, int y, int draw)
/*< plot >*/
{
    static int oldx = 0, oldy = 0;

    if (draw)
    {
	XDrawLine (pen_display, pen_win, pen_gc,
		   XCORD (oldx), YCORD (oldy), XCORD (x), YCORD (y));
    }
    oldx = x;
    oldy = y;
}

void xpoint (int x, int y)
/*< point >*/
{
    XDrawPoint (pen_display, pen_win, pen_gc, XCORD (x), YCORD (y));
}

void xraster (int count, int out_of, int xpos, int ypos, int length, int orient, 
	      unsigned char **raster, int dummy1, int dummy2)
/*< raster >*/
{
    XImage	*rasrect;
    char *data;
    int ii,h,w,xxpos,yypos;
    int xpix,xinc,ypix,yinc;
    
    switch ( orient ) { 
	case 0 :
	default:
	    xxpos = xpos; yypos = ypos; w = length; h = 1;
	    xpix =0 ; xinc =1; ypix=0, yinc=0;
	    break;
	case 1 :
	    xxpos = xpos; yypos = ypos; w = 1; h = length;
	    xpix =0 ; xinc =0; ypix=0, yinc=1;
	    break;
	case 2 :
	    xxpos = xpos-length ; yypos = ypos; w = length; h = 1;
	    xpix =length-1 ; xinc = -1; ypix=0, yinc=0;
	    break;
	case 3 :
	    xxpos = xpos; yypos = ypos+length; w = 1; h = length;
	    xpix =0 ; xinc =0; ypix=length-1, yinc= -1;
	    break;
    }
    
    if( mono ){
    	data = sf_charalloc( (w+7)/8*h ); 
    	rasrect = XCreateImage( pen_display, pen_visual,
				1, ZPixmap, 0,data, w, h, 8, 0 );
    }else{
    	data = sf_charalloc( w*h ); 
    	rasrect = XCreateImage( pen_display, pen_visual,
				8, ZPixmap, 0,data, w, h, 8, 0 );
    }
    
    if( own_colormap || mono ){
	
	/* raster values really are pixels if we have our own colormap or if
	   it is a mono display */
	
	for( ii=0 ; ii <length ; ii++ ){
	    XPutPixel( rasrect, xpix, ypix, (unsigned long)raster[0][ii] );
	    xpix += xinc; ypix += yinc;
	}
    }else{
	
	/* if we are using a public colormap we need to translate vplot-raster
	   values into X-pixel values using the map array */
	
	for( ii=0 ; ii <length ; ii++ ){
	    XPutPixel( rasrect, xpix, ypix, (unsigned long)map[raster[0][ii]] );
	    xpix += xinc; ypix += yinc;
	}
    }
    
    XPutImage(pen_display,pen_win,pen_gc,rasrect,0,0,
	      XCORD(xxpos),YCORD(yypos),w,h);
    XDestroyImage(rasrect);
}
/*
  Copyright (C) 1987 The Board of Trustees of Stanford University
  
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
*/

/*
 *
 *  source file:   ./filters/init_vplot.c
 *
 * Joe Dellinger (SEP), Feb 18 1988
 *	Inserted this sample edit history entry.
 *	Please log any further modifications made to this file:
 * Joe Dellinger, Feb 20 1988
 *	#define GETPAR to be fetch if SEPlib version.
 * Joe Dellinger Feb 24 1988
 * 	Moved gen_do_dovplot to genlib, where it belongs.
 *	txfont, txprec, txovly, overlay defaults remembered.
 * Joe Dellinger Feb 28 1988
 *	Changed fatness to scale with size of screen and scale,
 *	like any regular geometric attribute.
 * Joe Dellinger Mar 4 1988
 *	Fixed slight bug with fatness scaling and style=old.
 * Joe Dellinger Mar 17 1988
 *	Added "colormask" option.
 * Joe Dellinger April 15 1988
 *	Check for illegal colormask values.
 * Joe Dellinger Oct 28 1988
 *	Put in "no_stretch_text" flag.
 * Steve Cole Feb 2 1989
 *      Added default x and y scale parameters for use by vppen.
 * Joe Dellinger May 7 1989
 *	Added break=ignore option.
 *	Made txsquare=yes the default.
 * Joe Dellinger May 20 1989
 *	"/dev/tty" may NOT be openable. Behave gracefully in this case.
 * Joe Dellinger August 2 1989
 *	Put in redpow, greenpow, bluepow, redmap, greenmap, bluemap
 * W. Bauske IBM 03-26-91 
 *	Apply the SysV fixes to the code for the RS/6000
 *	Removed re-declare of system alloc routines for RS/6000
 * Dave Nichols 9-17-92
 *      Include stdlib.h if it is available instead of defining malloc.  
 * Stew Levin  2/27/95 
 *	Solaris mods.
 * Bob Clapp 1/24/96
 *      Changed a whole bunch of fetches to getches
 * Bob Clapp 10/98 
 *      Changed signals from bsd to posix1 for linux
 */

#include	<stdio.h>
#include	<math.h>

extern FILE * fdopen (int fd, const char *mode);

#include	<sys/ioctl.h>
#include	<sys/types.h>
#include	<sys/stat.h>
#include <fcntl.h>

#include <unistd.h>

#include	<ctype.h>
#include	<string.h>

#include <rsfplot.h>
/*^*/

#include	"../include/params.h"	/* for machine dependencies */
#include	"../include/enum.h"
#include	"../include/err.h"
#include	"../include/attrcom.h"
#include	"../include/intcom.h"
#include	"../include/mesgcom.h"
#include	"../include/erasecom.h"
#include	"../include/closestat.h"
#include	"../include/pat.h"
#include	"../include/vertex.h"
#include	"../include/round.h"
#include	"../include/extern.h"

#include "../utilities/util.h"
#include "../genlib/genpen.h"

#include "init_vplot.h"

#define		OPEN_ERROR	-1

/*
 * Other things that may need to be reset in dev.open
 * (Can't reset them some of them in dev.reset, because the user may
 * override from the command line.)
 */
/* should pipes be allowed for input? */
int             allow_pipe = YES;

/*
 * These may be reset to device-dependent defaults.
 */
float           fatmult = 1.;
float           patternmult = 1.;

/*
 * Look in extern.h for a better-organized list of the preceding.
 * Here I have left things which are also filter options with the
 * other filter options, even though they also belong in the above
 * categories.
 */

/*
 * flags and variables
 */
char            callname[25];
int             xcenterflag, ycenterflag;
int             ever_called = NO;
int             first_time = YES;
int             device_open = NO;	/* used by ERR */
int             out_isatty = YES;	/* If NO, output is a file or pipe */
int             nplots = 0;	/* number of plots made */
bool             no_stretch_text = true;	/* Don't allow stretched text? */

/*
 * coordinate variables
 */
int             xwmax, xwmin, ywmax, ywmin;	/* window */
int             xnew, ynew;	/* new pen location */
int             xold, yold;	/* old pen location */
char           *txbuffer;
int             txbuflen, vxbuflen;
struct vertex  *vxbuffer;
int             xret, yret;
float           mxx, mxy, myx, myy;
/*
 * This is so the device can throw in a coordinate transformation
 * for its convenience ON TOP OF whatever transformation the user
 * wants.
 */
int             default_rotate = 0, default_hshift = 0, default_vshift = 0;
float           default_scale = 1., default_xscale = 1., default_yscale = 1.;

/*
 * attribute variables
 */
int             linestyle;
int             cur_color = DEFAULT_COLOR;
int             pat_color = DEFAULT_COLOR + 1;
int             next_color;

int             default_txfont, default_txprec, default_txovly;
int             fat = 0;
int             afat = 0;
int             ipat = 0;	/* currently loaded pattern */
struct pat      pat[NPAT + 1];
float           dashsum = 0.;
int             dashon = NO;	/* Dashed lines? */
float           dashes[MAXDASH * 2];
float           dashpos = 0.;	/* Position in current dashing pattern */
int             color_set[MAX_COL + 1][_NUM_PRIM];
int             num_col_8;


/*
 * filter options - flags
 */

/*
 * Invras determines the polarity of dithered raster.
 * invras=n means raster works the same way as vectors; what is normally
 * WHITE on most devices is BLACK on a hardcopy black and white device.
 * invras=y is the proper default to make dithered images not come out as negatives
 */
bool             invras = true;
bool             window = true;
bool             shade = true;
bool             framewindows = false;
bool             endpause = false;
bool             honor_background = true;

bool             wantras = true;
bool             colormask[5];

/*
 * filter options - enumerated
 */
vp_plotstyle    style = VP_NO_STYLE_YET;
vp_plotstyle    default_style = VP_STANDARD;
int             rotate;
int             size = RELATIVE;
int             erase = FORCE_INITIAL | DO_LITERALS;

/*
 * filter options - valued
 */
int             xcenter, ycenter;	/* Vplot of point to force as center */
int             fatbase = 0;
int             epause = 0;	/* time to pause before erasing screen */
bool            overlay = false;	/* 1=overlay 0=replace */
int             default_overlay;
bool		serifs_OK = true;  /* If false, substitute serif fonts */

/*
 * 0 = none
 * 1 = random
 * 2 = Ordered
 * 3 = Floyd-Steinberg
 * 4 = Halftone
 */
int             dither = 1;	/* Dithering type */

int             xWmax, xWmin, yWmax, yWmin;
float           hshift, vshift;	/* Allow global translation of plot */
float           scale;	/* global scale */
float           xscale;	/* global x-scale */
float           yscale;	/* global y-scale */
float           hdevscale;	/* Vplot units to device units for x */
float           vdevscale;	/* Vplot units to device units for y */
float           txscale;/* global text scale */
float           mkscale;/* global marker scale */
float           dashscale;	/* global dashed line scale */
char            *interact=NULL;	/* Where to store coordinate
						 * file */
float           greyc = 1.;	/* Nonlinear correction */
float           pixc = 1.;	/* Pixel overlap correction */
float           redpow = 1., redmap[4] = {1., 0., 0., 0.};
float           greenpow = 1., greenmap[4] = {0., 1., 0., 0.};
float           bluepow = 1., bluemap[4] = {0., 0., 1., 0.};

/* filter options - resettable between plots */
int             user_rotate;
float           user_txscale;
float           user_mkscale;
float           user_dashscale;
float           user_scale;
float           user_xscale;
float           user_yscale;
int             user_size;
float           user_hshift;
float           user_vshift;
bool             user_xwmax_flag;
float           user_xwmax;
bool             user_ywmax_flag;
float           user_ywmax;
bool             user_xwmin_flag;
float           user_xwmin;
bool            user_ywmin_flag;
float           user_ywmin;

int             ifat = 0;
float           fatmult_orig;

bool mono;

/*
 * file and terminal control variables
 */
int             pltoutfd, stderrfd, controlfd;
FILE *pltout;

void  (*message) (int command, const char* string) = genmessage;
struct stat     stderrstat;
struct stat     pltoutstat;
FILE           *pltin;

FILE           *controltty;
char            outbuf[BUFSIZ];

#include <stdlib.h>

char            group_name[MAXFLEN + 1];
int             group_number = 0;
FILE           *pltinarray[MAXIN];
char            pltinname[MAXIN][MAXFLEN + 1];
char            pltname[MAXFLEN + 1] = "";

extern void reset_windows (void);

void init_vplot (int argc, char* argv[])
/*< Initialize and declare global variables. >*/
{
    char           *stringptr;
    int             ii;
    char            *string;
    float           ftemp;


    txbuffer = (char *) malloc (TXBUFLEN);
    txbuflen = TXBUFLEN;
/*
 * Sun III lint complains about "pointer alignment problem" here,
 * although the documentation makes it sound like that shouldn't
 * be possible.
 */
    vxbuffer = (struct vertex *) malloc (sizeof (struct vertex) * VXBUFLEN);
    vxbuflen = VXBUFLEN;

    /*
     * If the device can't do color, it can set mono to YES If device is
     * mono, this overrides the user's insistence that it isn't. So GETPAR
     * before we call dev.open. 
     */
    if (!sf_getbool ("mono",&mono)) mono=false;
    /* no color */

    /*
     * Initialize all patterns to be undefined. (device can create a
     * device-dependent default set if it wishes) 
     */
    for (ii = 0; ii <= NPAT; ii++)
    {
	pat[ii].patbits = NULL;
    }

/*
 * The device-independent code MAY NOT actually read from
 * the terminal itself. However, these variables are 
 * declared so that the device-dependent routines can use
 * them if they wish as a courtesy.
 */
    controlfd = open ("/dev/tty", 0);
    if (controlfd == OPEN_ERROR)
    {
	controltty = NULL;
    }
    else
    {
	controltty = fdopen (controlfd, "r");
    }

    pltout = stdout;

    /*
     * Call device open before doing anything else. this finalizes pltout 
     */
    dev.open (argc,argv);
    device_open = YES;

    /*
     * If graphics output going to control terminal, disable echoing and
     * arrange for use of device's message routine 
     */
    pltoutfd = fileno (pltout);
    stderrfd = fileno (stderr);
    out_isatty = isatty (pltoutfd);

    sf_getbool ("endpause", &endpause);
    sf_getbool ("cachepipe",&dev.cachepipe);
    sf_getbool ("shade", &shade);
    sf_getbool ("wantras", &wantras);
    sf_getbool ("window", &window);
    sf_getbool ("frame", &framewindows);
    sf_getbool ("overlay", &overlay);
    default_overlay = overlay;
    sf_getbool ("invras", &invras);
    sf_getbool ("txsquare", &no_stretch_text);
    sf_getbool ("serifs", &serifs_OK);
    sf_getbool ("background",&honor_background);

    if (!sf_getbools ("colormask",colormask,5)) 
	colormask[0] = colormask[1] = colormask[2] = 
	    colormask[3] = colormask[4] = true;
    if (!colormask[4] && colormask[3]) colormask[4] = true;

    if (!sf_getfloat ("redpow",  &redpow)) redpow=1.0;
    if (!sf_getfloat ("greenpow",  &greenpow)) greenpow=1.0;
    if (!sf_getfloat ("bluepow",  &bluepow)) bluepow=1.0;

    if (redpow <= 0. || greenpow <= 0. || bluepow <= 0.)
	ERR (FATAL, name, "Invalid color pow option.");
    
    sf_getfloats ("red",  redmap, 4);
    sf_getfloats ("green",  greenmap, 4);
    sf_getfloats ("blue",  bluemap, 4);

    sf_getint ("dither",  &dither); /* dithering to improve raster display, see "man vplotraster"
                    0    No dither,
                    1    Random Dither
                    2    Ordered Dither
                    3    Minimized Average Error Method
                    4    Digital Halftoning */
    sf_getfloat ("greyc",  &greyc); /* "grey correction" modifies the grey scale used to display a raster to simulate the nonlinearity of displays, see "man vplotraster" */
    sf_getfloat ("pixc",  &pixc);   /* "pixel  correction" controls  alteration of the grey scale, see "man vplotraster". */

    sf_getint ("txfont",  &dev.txfont);
    sf_getint ("txprec",  &dev.txprec);
    sf_getint ("txovly",  &dev.txovly);

    if (! serifs_OK)
    {
        if (dev.txfont == DEFAULT_HARDCOPY_FONT) dev.txfont = DEFAULT_SANSSERIF_FONT;
        if (dev.txfont == GREEK_SERIF_FONT) dev.txfont = GREEK_SANSSERIF_FONT;
    }

    default_txfont = dev.txfont;
    default_txprec = dev.txprec;
    default_txovly = dev.txovly;

    if (NULL != (string = sf_getstring ("erase")))
    {
	if ((string[0] == 'n') || (string[0] == 'N'))
	    erase = NO;
	else
	if ((string[0] == 'o') || (string[0] == 'O'))
	    erase = FORCE_INITIAL;
	else
	if ((string[0] == 'l') || (string[0] == 'L'))
	    erase = DO_LITERALS;
	else
	    erase = FORCE_INITIAL | DO_LITERALS;
    }

    if (NULL != (string = sf_getstring ("break")))
    {
	if (string[0] == 'b')
	    dev.brake = BREAK_BREAK;
	else
	if (string[0] == 'e')
	    dev.brake = BREAK_ERASE;
	else
	    dev.brake = BREAK_IGNORE;
    }

    xcenter = 0;
    ycenter = 0;
    xcenterflag = NO;
    ycenterflag = NO;
    if (sf_getfloat ("xcenter",  &ftemp))
    {
	xcenterflag = YES;
	xcenter = ROUND (ftemp * RPERIN);
    }
    if (sf_getfloat ("ycenter",  &ftemp))
    {
	ycenterflag = YES;
	ycenter = ROUND (ftemp * RPERIN);
    }

    if ((stringptr = getenv ("PATTERNMULT")) != NULL)
    {
	sscanf (stringptr, "%f", &patternmult);
    }
    if (!sf_getfloat ("patternmult",  &patternmult)) patternmult = 1.;

    interact = sf_getstring ("interact");
    if (!sf_getint ("pause",  &epause)) epause=0;

    if (NULL != interact)
    {
	epause = 0;		/* interact makes it own sort of pausing */
	endpause = false;
    }

    /*
     * Find the default style 
     */
    stringptr = NULL;
    if (NULL != (string = sf_getstring ("style")))
	stringptr = string;
    else
	stringptr = getenv ("PLOTSTYLE");
    if (stringptr != NULL)
    {
	if ((stringptr[0] == 'r') || (stringptr[0] == 'R') ||
	    (stringptr[0] == 'm') || (stringptr[0] == 'M'))
	    default_style = VP_ROTATED;
	else
	if ((stringptr[0] == 'o') || (stringptr[0] == 'O'))
	    default_style = VP_OLD;
	else
	if ((stringptr[0] == 'a') || (stringptr[0] == 'A'))
	    default_style = VP_ABSOLUTE;
	else
	    default_style = VP_STANDARD;
    }

/*
 * Options changeable between calls to dovplot
 * (By calling reset_parameters or reset())
 * Dovplot calls reset every time it starts. It only calls
 * reset_parameters the first time.
 *
 * Things in this category:
 * user_*
 * fatmult_orig, fatbase
 */

    if (!sf_getfloat ("fatmult",  &fatmult)) {
	if ((stringptr = getenv ("FATMULT")) != NULL)
	{
	    sscanf (stringptr, "%f", &fatmult);
	}
    }

    fatmult_orig = fatmult;

    if (!sf_getint ("rotate",  &user_rotate)) user_rotate = 0;

    if (!sf_getfloat ("txscale",  &user_txscale)) user_txscale = 1.0;
    if (!sf_getfloat ("mkscale",  &user_mkscale)) user_mkscale = 1.0;
    if (!sf_getfloat ("dashscale",  &user_dashscale)) user_dashscale = 1.0;

    if (!sf_getfloat ("scale",  &user_scale)) user_scale = 1.0;
    if (!sf_getfloat ("xscale",  &user_xscale)) user_xscale = 1.0;
    if (!sf_getfloat ("yscale",  &user_yscale)) user_yscale = 1.0;

    user_size = size;
    if (NULL != (string = sf_getstring ("size")))
    {
	if ((string[0] == 'a') || (string[0] == 'A'))
	    user_size = VP_ABSOLUTE;
	else
	    user_size = RELATIVE;
    }

    if (!sf_getfloat ("hshift",  &user_hshift) &&
	!sf_getfloat ("xshift",  &user_hshift)) user_hshift = 0.;
    if (!sf_getfloat ("vshift",  &user_vshift) &&
	!sf_getfloat ("yshift",  &user_vshift)) user_vshift = 0.;

    user_xwmax_flag = sf_getfloat ("xwmax",  &user_xwmax);
    user_ywmax_flag = sf_getfloat ("ywmax",  &user_ywmax);
    user_xwmin_flag = sf_getfloat ("xwmin",  &user_xwmin);
    user_ywmin_flag = sf_getfloat ("ywmin",  &user_ywmin);

    if (!sf_getint ("fat",  &fatbase)) fatbase = 0;
    /* base line fatness */


/*
 *  These parameters can simply be changed at any time with no
 *  need for re-initialization of anything else:
 *
 *  shade, wantras
 *
 */

}

void init_colors (void)
/*< init colors >*/
{
int             ii;

    /*
     * Set up the default color table 
     */

/*
 * First 7 colors are assumed to map to the standard 7 pen colors
 * on ALL devices, even those with no settable colors!
 */
    for (ii = 0; ii < 8; ii++)
    {
/*     if(color_set[ii][STATUS]!=SET){*/
	    color_set[ii][STATUS] = SET;
	    color_set[ii][_RED] = MAX_GUN * ((ii & 2) / 2);
	    color_set[ii][_GREEN] = MAX_GUN * ((ii & 4) / 4);
	    color_set[ii][_BLUE] = MAX_GUN * ((ii & 1) / 1);
	    color_set[ii][_GREY] = greycorr ((int) ((MAX_GUN * ii) / 7));
/*   }*/
    }

    if (mono)
    {
	/* Monochrome devices are assumed to have no settable colors */
	dev.num_col = 0;
    }

    num_col_8 = (dev.num_col > 8) ? dev.num_col : 8;

    if (mono)
    {
	color_set[0][MAP] = 0;
	for (ii = 1; ii <= MAX_COL; ii++)
	{
/*     if(color_set[ii][STATUS]!=SET)*/
	    color_set[ii][MAP] = 7;
	}
	for (ii = num_col_8; ii < 256; ii++)
	{
/*     if(color_set[ii][STATUS]!=SET)*/
	    color_set[ii][_GREY] = color_set[((ii - 8) % 7) + 1][_GREY];
	}
	/* Put a grey scale in the upper half of the color table */
	for (ii = 256; ii <= MAX_COL; ii++)
	{
/*     if(color_set[ii][STATUS]!=SET)*/
	    color_set[ii][_GREY] = greycorr (ii - 256);
	}
    }
    else
    {
	/*
	 * Unmapped colors shouldn't be mapped; ie, they map to themselves 
	 */

	for (ii = 0; ii < num_col_8; ii++)
	{
	    color_set[ii][MAP] = ii;
	 }
	/*
	 * Colors outside the range of this terminal map cyclically back into
	 * colors 1 through 7 
	 */
	for (ii = num_col_8; ii <= MAX_COL; ii++)
	{
	    color_set[ii][MAP] = ((ii - 8) % 7) + 1;
	}
    }
}

void setstyle (vp_plotstyle new_style)
/*< set style >*/
{
    /*
     * Check to see if the style has changed 
     */
    if (new_style == style)
	return;

    style = new_style;
    reset_parameters ();
}

void reset_parameters (void)
/*< reset parameters >*/
{
    float           inches;	/* scaling base for y axis */
    float           screenheight, screenwidth;	/* true size of the screen */
    int             ix, iy;

    dev.xorigin = 0;
    dev.yorigin = 0;

    rotate = default_rotate;
    rotate += user_rotate;

    txscale = user_txscale;
    mkscale = user_mkscale;
    dashscale = user_dashscale;

    scale = default_scale * user_scale;
    xscale = default_xscale * user_xscale;
    yscale = default_yscale * user_yscale;

    fatmult = fatmult_orig;

    size = user_size;

    switch (style)
    {
/*
 * The old standard on the machine erebus.
 * Pretty much dead now. Still useful for some old programs nobody's
 * wanted to update.
 */
	case VP_OLD:
	    txscale /= 3.;
	    fatmult /= 3.;
	    scale *= 3.;
	    inches = VP_STANDARD_HEIGHT;
	    break;
/*
 * The old standard on the machine mazama. A useful coordinate system
 * for geological sorts of plots. 
 * The Y axis goes the long way, across the screen, which is the device's
 * horizontal axis.
 */
	case VP_ROTATED:
	    rotate += 90;
	    inches = VP_ROTATED_HEIGHT;
	    break;
	case VP_ABSOLUTE:
	    size = VP_ABSOLUTE;
	case VP_STANDARD:
	default:
	    inches = VP_STANDARD_HEIGHT;
	    break;
    }

    if (rotate >= 0)
	rotate = rotate % 360;
    else
	rotate = ((rotate % 360) + 360) % 360;

    mxx = cosf (SF_PI * rotate / 180.);
    myy = cosf (SF_PI * rotate / 180.);
    mxy = sinf (SF_PI * rotate / 180.);
    myx = -sinf (SF_PI * rotate / 180.);

    if (size == VP_ABSOLUTE)
    {
	vdevscale = dev.pixels_per_inch / (float) (RPERIN * dev.aspect_ratio);
	hdevscale = dev.pixels_per_inch / (float) RPERIN;
    }
    else
    {
	/*
	 * Fit the inches x inches unit square into a displayable box with
	 * aspect ratio SCREEN_RATIO 
	 */
	screenwidth = (dev.xmax - dev.xmin) * dev.pixels_per_inch;
	screenheight =
	 (dev.ymax - dev.ymin) * dev.pixels_per_inch * dev.aspect_ratio;
	if ((screenheight / screenwidth) > VP_SCREEN_RATIO)
	{
	    vdevscale = (VP_SCREEN_RATIO * ((dev.xmax - dev.xmin) / dev.aspect_ratio)) /
	     (inches * RPERIN);
	    hdevscale = vdevscale * dev.aspect_ratio;
	}
	else
	{
	    vdevscale = (dev.ymax - dev.ymin) / (inches * RPERIN);
	    hdevscale = vdevscale * dev.aspect_ratio;
	}
    }

    hshift = default_hshift;
    vshift = default_vshift;

    if (style == VP_ROTATED)
    {
	vshift += dev.ymax - dev.ymin;
    }

    yscale *= scale;
    xscale *= scale;
    mkscale *= scale;

/*
 * Set up fatness multiplication factor
 */
    fatmult *= scale * hdevscale * RPERIN / FATPERIN;

    /*
     * The point (xcenter,ycenter) in vplot coordinates is to be centered in
     * the screen. 
     */
    if (xcenterflag || ycenterflag)
    {
	vptodevxy (xcenter, ycenter, &ix, &iy);
	if (xcenterflag)
	{
	    hshift += (dev.xmax + dev.xmin) / 2 - ix;
	}
	if (ycenterflag)
	{
	    vshift += (dev.ymax + dev.ymin) / 2 - iy;
	}
    }

    hshift += user_hshift * dev.pixels_per_inch;
    vshift += user_vshift * dev.pixels_per_inch / dev.aspect_ratio;

/* plot window parameters defaulted */
/* to maximum size */

    devtovpw (dev.xmin, dev.ymin, dev.xmax, dev.ymax,
	      &xWmin, &yWmin, &xWmax, &yWmax);

    if (user_xwmax_flag)
	xWmax = ROUND (user_xwmax * RPERIN);
    if (user_ywmax_flag)
	yWmax = ROUND (user_ywmax * RPERIN);
    if (user_xwmin_flag)
	xWmin = ROUND (user_xwmin * RPERIN);
    if (user_ywmin_flag)
	yWmin = ROUND (user_ywmin * RPERIN);

    vptodevw (xWmin, yWmin, xWmax, yWmax, &xWmin, &yWmin, &xWmax, &yWmax);

    wlimit (dev.xmin, dev.xmax, &xWmin, &xWmax);
    wlimit (dev.ymin, dev.ymax, &yWmin, &yWmax);

    xwmax = xWmax;		/* plot window parameters defaulted */
    xwmin = xWmin;		/* to maximum size 		 */
    ywmax = yWmax;
    ywmin = yWmin;
    reset_windows ();
}

void wlimit (int min, int max, int *xmin, int *xmax)
/*< wlimit >*/
{
    if (*xmin < min)
	*xmin = min;

    if (*xmax > max)
	*xmax = max;
}
