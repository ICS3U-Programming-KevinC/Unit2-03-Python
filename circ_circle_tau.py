# !/user/bin/env python3

# Created by Kevin Csiffary
# Date: Sep. 27, 2022
# This program calculates the circumference of a circle using tau
# with given radius.


import math


def main():
    radius = int(input("What is the radius of your circle(cm): "))
    print("")
    print(
        "The circumference of your circle is: 𝞽 * radius = {}cm".format(
            math.tau * radius
        )
    )


if __name__ == "__main__":
    main()
