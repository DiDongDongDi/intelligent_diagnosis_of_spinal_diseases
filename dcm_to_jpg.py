#!/usr/bin/python
# -*- coding=utf-8 -*-

"""
@file: dcm_to_jpg
@author: 王庆宇
@create: 2020-06-27
"""

import os
import sys

import matplotlib.pyplot as plt
import pydicom
import scipy.misc


def convert_dcm_to_jpg(source_file, target_file):
    """将dcm文件转为jpg文件

    Args:
        source_file (str): 源文件
        target_file (str): 目标文件
    """

    ds = pydicom.read_file(source_file)
    img = ds.pixel_array
    scipy.misc.imsave(target_file, img)


def convert_dcm_to_jpg_dir(source_dir, target_dir):
    """将源目录中的dcm文件转换为目标目录中的jpg文件

    源目录中的非dcm文件也会被复制

    Args:
        source_dir (str): 源目录
        target_dir (str): 目标目录
    """


    walk = os.walk(target_dir)
    for dir_path, __, file_names in walk:
        



def option_help():
    print("usage: dcm_to_jpg.py [source_path] [target_path]")
    print("dcm_to_jpg is a tool for converting dcm file to jpg file.")


def main():
    if len(sys.argv) != 3:
        option_help()
    else:
        source_path = sys.argv[1]
        target_path = sys.argv[2]

        if os.path.isfile(source_path) and source_path.endswith(".dcm"):
            if target_path.endswith(".jpg"):
                target_parent_dir = os.path.dirname(target_path)
                if os.path.isdir(target_parent_dir):
                    convert_dcm_to_jpg(source_path, target_path)
                else:
                    print("Error: can not find directory {}.".format(target_parent_dir))
            elif os.path.isdir(target_path):
                file_name = os.path.basename(source_path)
                file_name = file_name.replace(".dcm", ".jpg")
                target_path = os.path.join(target_path, file_name)
                convert_dcm_to_jpg(source_path, target_path)
            else:
                print("Error: can not find directory {}.".format(target_path))
        elif os.path.isdir(source_path):
            if not os.path.isdir(target_path):
                os.mkdir(target_path)
            
        else:
            print("Error: source path {} is not exist".format(source_path))


if __name__ == "__main__":
    main()
