import zlib
import struct
import array

def output_chunk(out, chunk_type, data):
    out.write(struct.pack("!I", len(data)))
    out.write(chunk_type)
    out.write(data)
    checksum = zlib.crc32(data, zlib.crc32(chunk_type))
    out.write(struct.pack("!I", checksum))

def get_data(width, height, rgb_func):
    fw = float(width)
    fh = float(height)
    compressor = zlib.compressobj()
    data = array.array("B")
    for y in range(height):
        data.append(0)
        fy = float(y)
        for x in range(width):
            fx = float(x)
            data.extend([int(v * 255) for v in rgb_func(fx / fw, fy / fh)])
    compressed = compressor.compress(data.tostring())
    flushed = compressor.flush()
    return compressed + flushed

def write_png(filename, width, height, rgb_func):
    out = open(filename, "w")
    out.write(struct.pack("8B", 137, 80, 78, 71, 13, 10, 26, 10))
    output_chunk(out, "IHDR", struct.pack("!2I5B", width, height, 8, 2, 0, 0, 0))
    output_chunk(out, "IDAT", get_data(width, height, rgb_func))
    output_chunk(out, "IEND", "")
    out.close()


def linear_gradient(start_value, stop_value, start_offset=0.0, stop_offset=1.0):
    return lambda offset: (start_value + ((offset - start_offset) / (stop_offset - start_offset) * (stop_value - start_value))) / 255.0

def LINEAR(x, y):
    return y

def RADIAL(center_x, center_y):
    return lambda x, y: (x - center_x) ** 2 + (y - center_y) ** 2

def gradient(func, DATA):
    def gradient_function(x, y):
        initial_offset = 0.0
        f = func(x, y)
        for offset, start, end in DATA:
            if f < offset:
                r = linear_gradient(start[0], end[0], initial_offset, offset)(f)
                g = linear_gradient(start[1], end[1], initial_offset, offset)(f)
                b = linear_gradient(start[2], end[2], initial_offset, offset)(f)
                return r, g, b
            initial_offset = offset
    return gradient_function
