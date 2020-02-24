import numpy

def kernel(x, kernel_radius):
    normx = x / kernel_radius
    return numpy.exp(-0.5 * normx * normx)

def grid_data(data, xgrid, ygrid, radius):
    # Initialize output arrays
    ny = len(ygrid)
    nx = len(xgrid)
    values = numpy.zeros((ny, nx))
    density = numpy.zeros((ny, nx))

    # Store some window sizes in units of grid spacing
    dg = xgrid[1] - xgrid[0]
    halfwin = int( numpy.round(4 * radius / dg) )
    window = 2 * halfwin + 1
    
    def get_window_ends(x, x0, n):
        i0 = int(numpy.round((x - x0) / dg)) - halfwin
        i1 = i0 + window
        return max(0, i0), min(i1, n)
        
    def add_data(x, y, val):
        # Find the indices of the bottom left corner of the affected area
        ix0, ix1 = get_window_ends(x, xgrid[0], nx)
        iy0, iy1 = get_window_ends(y, ygrid[0], ny)
    
        # Compute the kernel values in X and Y
        xkernel = kernel(xgrid[ix0:ix1] - x, radius)
        ykernel = kernel(ygrid[iy0:iy1] - y, radius)
    
        # Accumulate kernel and kernel * data, row by row
        for i in range(len(ykernel)):
            rowkernel = xkernel * ykernel[i]
            density[iy0 + i,ix0:ix1] += rowkernel
            values[iy0 + i,ix0:ix1] += rowkernel * val

        return
    
    # Loop over data rows, accumulate results
    for index, row in data.iterrows():
        add_data(*row.values)
    
    # Normalize values
    values = numpy.divide(values, density, out=numpy.zeros_like(density), where=density>0.01)
    
    return values, density
