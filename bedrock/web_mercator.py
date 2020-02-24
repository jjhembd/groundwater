import numpy

earth_radius = 6378137

def lon_to_x(lon):
    lon = numpy.radians(lon)
    return earth_radius * lon

def lat_to_y(lat):
    lat = numpy.radians(lat)
    exp_y = numpy.tan(numpy.pi / 4 + lat / 2)
    return earth_radius * numpy.log(exp_y)

def dx_to_zoom(dx, tilesize):
    z = numpy.log2(2 * numpy.pi * earth_radius / tilesize / dx)
    return numpy.round(z)

def snap_dx(dx):
    z = dx_to_zoom(dx, 512)
    return 2 * numpy.pi * earth_radius / 512 / 2 ** z

def get_grid1d(xmin, xmax, dx):
    # Snap to nearest grid center. Note: first gridpoint is at dx / 2
    x1 = numpy.floor(xmin / dx) * dx + dx / 2
    x2 = numpy.floor(xmax / dx) * dx + dx / 2

    # Find the number of gridpoints spanning [xmin, xmax]
    ngrid = int( numpy.round((x2 - x1) / dx) ) + 1

    return numpy.linspace(x1, x2, ngrid)

def get_tilegrid(xmin, xmax, dx, tilesize = 512):
    dx = snap_dx(dx)
    tilewidth = tilesize * dx

    # Find the indices of the tile edges spanning xmin, xmax
    it0 = numpy.floor(xmin / tilewidth)
    it1 = numpy.ceil(xmax / tilewidth)

    # Find the centers of the pixels at the edges of this group of tiles
    x0 = it0 * tilewidth + dx / 2
    x1 = it1 * tilewidth - dx / 2

    # Return an array of all the pixel centers in this group of tiles
    ngrid = int( (it1 - it0) * tilesize )
    return numpy.linspace(x0, x1, ngrid)
