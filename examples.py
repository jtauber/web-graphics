#!/usr/bin/env python

from graphics import write_png, gradient, LINEAR, RADIAL

## EXAMPLES

# normally you would make these with width=1 but below I've made them 50
# so you can more easily see the result

# body background from jtauber.com and quisition.com
write_png("example1.png", 50, 143, gradient(LINEAR, [
    (1.0, (0xA1, 0xA1, 0xA1), (0xDF, 0xDF, 0xDF)),
]))

# header background similar to that on jtauber.com
write_png("example2.png", 50, 90, gradient(LINEAR, [
    (0.43, (0xBF, 0x94, 0xC0), (0x4C, 0x26, 0x4C)), # top
    (0.85, (0x4C, 0x26, 0x4C), (0x27, 0x13, 0x27)), # bottom
    (1.0,  (0x66, 0x66, 0x66), (0xFF, 0xFF, 0xFF)), # shadow
]))

# original header gradient from pinax
write_png("example3.png", 50, 80, gradient(LINEAR, [
    (0.72, (0x00, 0x26, 0x4D), (0x00, 0x40, 0x80)),
    (1.0,  (0x00, 0x40, 0x80), (0x00, 0x6C, 0xCF)), # glow
]))

# form input background from pinax
write_png("example4.png", 50, 25, gradient(LINEAR, [
    (0.33, (0xDD, 0xDD, 0xDD), (0xF3, 0xF3, 0xF3)), # top-shadow
    (1.0,  (0xF3, 0xF3, 0xF3), (0xF3, 0xF3, 0xF3)),
]))

# current header gradient from pinax
write_png("example5.png", 50, 80, gradient(LINEAR, [
    (1.00, (0x00, 0x11, 0x33), (0x00, 0x55, 0x77)),
]))

# showing gradient not going all the way to 1.0
write_png("example6.png", 50, 80, gradient(LINEAR, [
    (0.5, (0x00, 0x11, 0x33), (0x00, 0x55, 0x77)),
]))


# hsv example

from colorsys import hsv_to_rgb

write_png("example7.png", 200, 40, gradient(LINEAR, [
    (0.5, hsv_to_rgb(0.55, 0.4, 122), hsv_to_rgb(0.55, 0.4, 161)),
    (1.0, hsv_to_rgb(0.55, 0.4, 143), hsv_to_rgb(0.55, 0.4, 175)),
]))


# radial gradient

write_png("example8.png", 400, 400, gradient(RADIAL(0.5, 0.5), [
    (1.0, (0xCC, 0xCC, 0xCC), (0x00, 0x00, 0x00)),
]))

write_png("example9.png", 400, 400, gradient(RADIAL(0.5, 0.0), [
    (0.5, (0xCC, 0xCC, 0xCC), (0x00, 0x00, 0x00)),
]))
