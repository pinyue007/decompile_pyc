# -*- coding: utf-8 -*-

import os
import sys

def decompile_file(filename_pyc):
    python_path = os.path.dirname(sys.executable)
    uncompyle6 = os.path.join(python_path, 'Scripts', 'uncompyle6')
    filename_py = filename_pyc[:-1]
    command = uncompyle6 + ' ' + filename_pyc + ' > ' + filename_py
    try:
        os.system(command)
    except:
        print 'ERROR'

def handle_path(root_path):
    if not os.path.isdir(root_path):
        raise u'{}不是目录'.format(root_path)
    for root, _, files in os.walk(root_path):
        for filename in files:
            if filename.endswith('.pyc'):
                file_path = os.path.join(root, filename)
                decompile_file(file_path)

if __name__ == '__main__':
    root_path = 'D:\\pyc_code_path'
    handle_path(root_path)
