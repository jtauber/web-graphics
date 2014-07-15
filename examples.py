#!/usr/bin/env python

from web_graphics import write_png, gradient, LINEAR_X, LINEAR_Y, RADIAL, NO_NOISE, GAUSSIAN, HSV

## EXAMPLES

# normally you would make these with width=1 but below I've made them 50
# so you can more easily see the result

# body background from old jtauber.com and quisition.com
write_png("example1.png", 50, 143, gradient(LINEAR_Y, NO_NOISE, [
    (1.0, (0xA1, 0xA1, 0xA1), (0xDF, 0xDF, 0xDF)),
]))

# header background similar to that on old jtauber.com
write_png("example2.png", 50, 90, gradient(LINEAR_Y, NO_NOISE, [
    (0.43, (0xBF, 0x94, 0xC0), (0x4C, 0x26, 0x4C)),  # top
    (0.85, (0x4C, 0x26, 0x4C), (0x27, 0x13, 0x27)),  # bottom
    (1.00, (0x66, 0x66, 0x66), (0xFF, 0xFF, 0xFF)),  # shadow
]))

# original header gradient from pinax
write_png("example3.png", 50, 80, gradient(LINEAR_Y, NO_NOISE, [
    (0.72, (0x00, 0x26, 0x4D), (0x00, 0x40, 0x80)),
    (1.00, (0x00, 0x40, 0x80), (0x00, 0x6C, 0xCF)),  # glow
]))

# old form input background from pinax
write_png("example4.png", 50, 25, gradient(LINEAR_Y, NO_NOISE, [
    (0.33, (0xDD, 0xDD, 0xDD), (0xF3, 0xF3, 0xF3)),  # top-shadow
    (1.00, (0xF3, 0xF3, 0xF3), (0xF3, 0xF3, 0xF3)),
]))

# current header gradient from pinax
write_png("example5.png", 50, 80, gradient(LINEAR_Y, NO_NOISE, [
    (1.00, (0x00, 0x11, 0x33), (0x00, 0x55, 0x77)),
]))

# showing gradient not going all the way to 1.0
write_png("example6.png", 50, 80, gradient(LINEAR_Y, NO_NOISE, [
    (0.5, (0x00, 0x11, 0x33), (0x00, 0x55, 0x77)),
]))


# hsv example

write_png("example7.png", 200, 40, gradient(LINEAR_Y, NO_NOISE, [
    (0.5, HSV(0.55, 0.2, 0.40), HSV(0.55, 0.2, 0.54)),
    (1.0, HSV(0.55, 0.2, 0.47), HSV(0.55, 0.2, 0.61)),
]))


# radial gradient

write_png("example8.png", 400, 400, gradient(RADIAL(0.5, 0.5), NO_NOISE, [
    (1.0, (0xCC, 0xCC, 0xCC), (0x00, 0x00, 0x00)),
]))

write_png("example9.png", 400, 400, gradient(RADIAL(0.5, 0.0), NO_NOISE, [
    (0.5, (0xCC, 0xCC, 0xCC), (0x00, 0x00, 0x00)),
]))


# gaussian noise

write_png("example10.png", 400, 400, gradient(LINEAR_Y, GAUSSIAN(0.01), [
    (1.00, (0x00, 0x11, 0x33), (0x00, 0x55, 0x77)),
]))

write_png("example11.png", 960, 200, gradient(RADIAL(0.5, 0.0), GAUSSIAN(0.01), [
    (0.8, (0x22, 0x22, 0x22), (0x00, 0x00, 0x00)),
]))


# horizontal gradient
write_png("example12.png", 5000, 50, gradient(LINEAR_X, GAUSSIAN(0.005), [
    (0.40, (0x00, 0x00, 0x00), (0x00, 0x00, 0x00)),
    (0.59, (0x00, 0x00, 0x00), (0x1B, 0x1C, 0x1E)),
]))


write_png("example13.png", 100, 500, gradient(LINEAR_Y, GAUSSIAN(0.01), [
    (0.3, HSV(0.6, 0.75, 0.1), HSV(0.6, 0.75, 0.2)),
]))
