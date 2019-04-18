# [Recording location coordinate converter](https://github.com/c22n/udish-coord-converter)

Translates coordinates on circular microscopy dish in separate recording
sessions based on two reference marks on the dish surface. Assumes that one of
the reference marks is set to zero in both first and second sessions. Uses the
transform of the second reference mark to calculate the transform of other
locations on the dish and the dish rotation, to allow recordings in same
locations.

Written for use with software on microscopes of [FILM microscopy
facility](http://www.imperial.ac.uk/medicine/facility-for-imaging-by-light-microscopy/) 
at Imperial College London, but should work for any microscopy software that
allows setting a coordinate system based on a reference point.

Procedure
---------

1.  Set zero location on first reference mark.
2.  Note coordinate of second reference mark.
3.  Make recordings as per experiment being conducted, noting coordinates of
    each recording location.
4.  In second recording session (after dish may have been removed to stain for
    different fluorescent marker), start by again setting zero location to
    first reference mark.
5.  Note coordinate of second reference mark in this second session.
6.  Open binder link above and input coordinate data into Jupyter notebook
    cell to calculate converter coordinates to return to the same location.
