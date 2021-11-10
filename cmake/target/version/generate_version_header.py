#!/usr/bin/env python3
"""
# ===============================================================================
# NAME: generate_version_header.py
#
# DESCRIPTION:  Creates a version header file of specified name.
#               It takes as input a filename and creates a header file
#               with a constant string which is the git hash of the current version
#
# USAGE: ./generate_version_header.py /path/tofile/version.hpp
#
# AUTHOR: sfregoso
# EMAIL:  sfregoso@jpl.nasa.gov
# DATE CREATED  : Oct. 15, 2021
#
# Copyright 2021, California Institute of Technology.
# ALL RIGHTS RESERVED. U.S. Government Sponsorship acknowledged.
# ===============================================================================
"""
import sys
import os
import subprocess


def get_version_str():
    """
    System call to get the git hash

    Return: String with git hash
    """
    output = subprocess.check_output(["git", "describe", "--tags"])
    return output.strip().decode("ascii")


def create_version_file(filename):
    """
    Create the version file using the provided name and path.
    """

    # Check if file exists, if it does, overwrite it
    if os.path.isfile(filename):

        print("WARNING:  File [%s] exists and will be overwritten." % (filename))

    # Open file for writing
    with open(filename, "w") as fid:

        fid.write("/*\n")
        fid.write(
            "    This file has been autogenerated using [%s].\n"
            % (os.path.basename(__file__))
        )
        fid.write("    This file may be overwritten.\n")
        fid.write("*/\n")
        fid.write("#ifndef _VERSION_HPP_\n")
        fid.write("#define _VERSION_HPP_\n")
        fid.write("\n")
        fid.write('static const char* VERSION = "%s";\n' % (get_version_str()))
        fid.write("\n")
        fid.write("#endif\n")
        fid.write("\n\r")


if __name__ == "__main__":

    FNAME = sys.argv[1]

    create_version_file(FNAME)
