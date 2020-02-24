from rasterio.transform import Affine
import rasterio

def write(filename, x, y, z):
    # x, y are 1D arrays containing the coordinate values along each axis
    # z is a 2D array of shape (len(y), len(x)) containing the pixel values

    # 1. Find corner of image: 1/2 pixel from bottom left pixel center
    dx = x[1] - x[0]
    dy = y[1] - y[0]
    x0 = x[0] - dx / 2
    y0 = y[0] - dy / 2

    # 2. Set up transform to convert grid indices to coordinates
    transform = Affine.translation(x0, y0) * Affine.scale(dx, dy)

    # 3. Open the file
    output = rasterio.open(
            filename,
            'w',
            driver='GTiff',
            height=z.shape[0],
            width=z.shape[1],
            count=1,
            dtype=z.dtype,
            crs='EPSG:3857',
            transform=transform,
            compress='lzw'
            )

    # Write and close
    output.write(z, 1)
    output.close()
