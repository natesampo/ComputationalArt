""" TODO: Put your header comment here """

import random
import math
from PIL import Image


def prod(f, x, y):
    return evaluate_random_function(f[1], x, y) * evaluate_random_function(f[2], x, y)

def avg(f, x, y):
    return (evaluate_random_function(f[1], x, y) + evaluate_random_function(f[2], x, y)) / 2

def cos_pi(f, x, y):
    return math.cos(math.pi * evaluate_random_function(f[1], x, y))

def sin_pi(f, x, y):
    return math.sin(math.pi * evaluate_random_function(f[1], x, y))

def first(x, y):
    return x

def second(x, y):
    return y

def power(f, x, y):
    return evaluate_random_function(f[1], x, y) ** 3

def neg(f, x, y):
    return evaluate_random_function(f[1], x, y) * -1


def build_random_function(f, min_depth, curr_depth, max_depth):
    """ Builds a random function of depth at least min_depth and depth
        at most max_depth (see assignment writeup for definition of depth
        in this context)

        min_depth: the minimum depth of the random function
        max_depth: the maximum depth of the random function
        returns: the randomly generated function represented as a nested list
                 (see assignment writeup for details on the representation of
                 these functions)
    """
    if curr_depth < max_depth:
        if curr_depth < min_depth:
            r = random.randint(1,6)
            if r == 1:
                f = ['prod', build_random_function(f, min_depth, curr_depth + 1, max_depth), build_random_function(f, min_depth, curr_depth + 1, max_depth)]
            if r == 2:
                f = ['avg', build_random_function(f, min_depth, curr_depth + 1, max_depth), build_random_function(f, min_depth, curr_depth + 1, max_depth)]
            if r == 3:
                f = ['power', build_random_function(f, min_depth, curr_depth + 1, max_depth)]
            if r == 4:
                f = ['neg', build_random_function(f, min_depth, curr_depth + 1, max_depth)]
            if r == 5:
                f = ['cos_pi', build_random_function(f, min_depth, curr_depth + 1, max_depth)]
            if r == 6:
                f = ['sin_pi', build_random_function(f, min_depth, curr_depth + 1, max_depth)]
        else:
            r = random.randint(1,7)
            if r == 1:
                f = ['prod', build_random_function(f, min_depth, curr_depth + 1, max_depth), build_random_function(f, min_depth, curr_depth + 1, max_depth)]
            if r == 2:
                f = ['avg', build_random_function(f, min_depth, curr_depth + 1, max_depth), build_random_function(f, min_depth, curr_depth + 1, max_depth)]
            if r == 3:
                f = ['power', build_random_function(f, min_depth, curr_depth + 1, max_depth)]
            if r == 4:
                f = ['neg', build_random_function(f, min_depth, curr_depth + 1, max_depth)]
            if r == 5:
                f = ['cos_pi', build_random_function(f, min_depth, curr_depth + 1, max_depth)]
            if r == 6:
                f = ['sin_pi', build_random_function(f, min_depth, curr_depth + 1, max_depth)]
            if r == 7:
                f = ['x']
            if r == 8:
                f = ['y']
    else:
        r = random.randint(1,2)
        if r == 1:
            f = ['x']
        if r == 2:
            f = ['y']
    return f


def evaluate_random_function(f, x, y):
    """ Evaluate the random function f with inputs x,y
        Representation of the function f is defined in the assignment writeup

        f: the function to evaluate
        x: the value of x to be used to evaluate the function
        y: the value of y to be used to evaluate the function
        returns: the function value

        >>> evaluate_random_function(['x'],-0.5, 0.75)
        -0.5
        >>> evaluate_random_function(['y'],0.1,0.02)
        0.02
    """
    function_dict = {'prod':prod, 'avg':avg, 'cos_pi':cos_pi, 'sin_pi':sin_pi, 'x':first, 'y':second, 'power':power, 'neg':neg}
    argument_dict = {'prod':(f,x,y), 'avg':(f,x,y), 'cos_pi':(f,x,y), 'sin_pi':(f,x,y), 'x':(x,y), 'y':(x,y), 'power':(f,x,y), 'neg':(f,x,y)}
    return function_dict[f[0]](*argument_dict[f[0]])


def remap_interval(val,
                   input_interval_start,
                   input_interval_end,
                   output_interval_start,
                   output_interval_end):
    """ Given an input value in the interval [input_interval_start,
        input_interval_end], return an output value scaled to fall within
        the output interval [output_interval_start, output_interval_end].

        val: the value to remap
        input_interval_start: the start of the interval that contains all
                              possible values for val
        input_interval_end: the end of the interval that contains all possible
                            values for val
        output_interval_start: the start of the interval that contains all
                               possible output values
        output_inteval_end: the end of the interval that contains all possible
                            output values
        returns: the value remapped from the input to the output interval

        >>> remap_interval(0.5, 0, 1, 0, 10)
        5.0
        >>> remap_interval(5, 4, 6, 0, 2)
        1.0
        >>> remap_interval(5, 4, 6, 1, 2)
        1.5
    """
    if val != input_interval_end:
        return (output_interval_end - output_interval_start) * ((val - input_interval_start) / (input_interval_end - input_interval_start)) + output_interval_start
    else:
        return output_interval_end


def color_map(val):
    """ Maps input value between -1 and 1 to an integer 0-255, suitable for
        use as an RGB color code.

        val: value to remap, must be a float in the interval [-1, 1]
        returns: integer in the interval [0,255]

        >>> color_map(-1.0)
        0
        >>> color_map(1.0)
        255
        >>> color_map(0.0)
        127
        >>> color_map(0.5)
        191
    """
    # NOTE: This relies on remap_interval, which you must provide
    color_code = remap_interval(val, -1, 1, 0, 255)
    return int(color_code)


def test_image(filename, x_size=350, y_size=350):
    """ Generate test image with random pixels and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (random.randint(0, 255),  # Red channel
                            random.randint(0, 255),  # Green channel
                            random.randint(0, 255))  # Blue channel

    im.save(filename)


def generate_art(filename, x_size=350, y_size=350):
    """ Generate computational art and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Functions for red, green, and blue channels - where the magic happens!
    red_function = build_random_function([], 7, 0, 9)
    green_function = build_random_function([], 7, 0, 9)
    blue_function = build_random_function([], 7, 0, 9)

    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (
                    color_map(evaluate_random_function(red_function, x, y)),
                    color_map(evaluate_random_function(green_function, x, y)),
                    color_map(evaluate_random_function(blue_function, x, y))
                    )

    im.save(filename)


if __name__ == '__main__':
    #import doctest
    #doctest.testmod()
    generate_art("myart.png")
