# -*- coding: UTF-8 -*-

import os
import shutil
import traceback
import logging
import stat

def clean_folder(folder_name):
    """
    清空文件夹
    """
    try:
        if os.path.isdir(folder_name):
            files = os.listdir(folder_name)
            for file_cell in files:
                # 部分生成的文件为只读，增加写的权限，进行删除
                os.chmod( os.path.join(folder_name, file_cell), stat.S_IWRITE )
            os.chmod(folder_name, stat.S_IWRITE)
            shutil.rmtree(folder_name)
        os.mkdir(folder_name)
    except Exception:
        logging.exception("Exception Logged")
        raise Exception("failed to clean folder")

def clean_folders(folder_name_list):
    '''
    批量清空文件夹
    '''
    for folder_name in folder_name_list:
        clean_folder(folder_name)

def append_temp_path_to_path(temp_folder):
    """
    修改系统环境变量，临时增加指定目录
    """
    logging.info("Preparing to add temp folder %s into environment, origin environment path as %s" % (temp_folder, os.environ["PATH"]))
    if not temp_folder in os.environ["PATH"]:
        os.environ["PATH"] += os.pathsep + temp_folder
    logging.info("Successfully add temp folder %s into environment, environment as %s" % (temp_folder, os.environ["PATH"]))

def check_if_file_exists(file_path):
    """
    检查文件是否存在
    """
    logging.info("准备校验文件是否存在, 文件名为%s" % file_path)
    return os.path.isfile(file_path)