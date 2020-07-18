#!/usr/bin/python
# -*- coding=utf-8 -*-

"""
@file: dcm_to_jpg
@author: 王庆宇
@create: 2020-06-27
"""

import os
import shutil
import sys

import matplotlib.pyplot as plt
import pydicom
import scipy.misc


def convert_dcm_to_jpg(dcm_file, jpg_file):
    """将dcm文件转为jpg文件

    Args:
        dcm_file (str): dcm文件
        jpg_file (str): jpg文件
    """

    print("Converting {} to {}".format(dcm_file, jpg_file))
    ds = pydicom.read_file(dcm_file)
    img = ds.pixel_array
    scipy.misc.imsave(jpg_file, img)


def convert_dcm_to_jpg_dir(dcm_dir, jpg_dir):
    """将dcm目录中的dcm文件转换为jpg目录中的jpg文件

    dcm目录中的非dcm文件也会被复制

    Args:
        dcm_dir (str): dcm目录
        jpg_dir (str): jpg目录
    """

    shutil.copytree(dcm_dir, jpg_dir)
    walk = os.walk(jpg_dir)
    for dir_path, __, file_names in walk:
        for file_name in file_names:
            if file_name.endswith(".dcm"):
                dcm_file_path = os.path.join(dir_path, file_name)
                file_name = file_name.replace(".dcm", ".jpg")
                jpg_file_path = os.path.join(dir_path, file_name)
                convert_dcm_to_jpg(dcm_file_path, jpg_file_path)
                os.remove(dcm_file_path)


def option_help():
    print("usage: dcm_to_jpg.py [dcm_path] [jpg_path]")
    print("dcm_to_jpg is a tool for converting dcm file to jpg file.")


def main():
    if len(sys.argv) != 3:
        option_help()
    else:
        dcm_path = sys.argv[1]
        jpg_path = sys.argv[2]

        if os.path.isfile(dcm_path) and dcm_path.endswith(".dcm"):
            if jpg_path.endswith(".jpg"):
                jpg_parent_dir = os.path.dirname(jpg_path)
                if os.path.isdir(jpg_parent_dir):
                    convert_dcm_to_jpg(dcm_path, jpg_path)
                else:
                    print("Error: can not find directory {}.".format(jpg_parent_dir))
            elif os.path.isdir(jpg_path):
                file_name = os.path.basename(dcm_path)
                file_name = file_name.replace(".dcm", ".jpg")
                jpg_path = os.path.join(jpg_path, file_name)
                convert_dcm_to_jpg(dcm_path, jpg_path)
            else:
                print("Error: can not find directory {}.".format(jpg_path))
        elif os.path.isdir(dcm_path):
            convert_dcm_to_jpg_dir(dcm_path, jpg_path)
        else:
            print("Error: dcm path {} is not exist".format(dcm_path))


if __name__ == "__main__":
    main()
