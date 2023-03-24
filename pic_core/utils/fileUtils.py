import json
import os
import re
import shutil
from pathlib2 import Path

from pic_core.utils.log import getMyLogger
log = getMyLogger(__name__)


class FileUtils(object):
    def __init__(self):
        self._source = None
        self._destination = None

    @staticmethod
    def shutil_copy(_source, _destination):
        log.debug(f'shutil.copy() from {_source} to {_destination}')
        shutil.copy(_source, _destination)

    @staticmethod
    def shutil_copy2(_source, _destination):
        log.debug(f'shutil.copy2() from {_source} to {_destination}')
        shutil.copy2(_source, _destination)

    @staticmethod
    def shutil_copytree(_source, _destination):
        log.debug(f'shutil.copytree() from {_source} to {_destination}')
        shutil.copytree(_source, _destination)

    @staticmethod
    def shutil_move(_source, _destination):
        log.debug(f'shutil.move() file or directory from {_source} to {_destination}')
        shutil.move(_source, _destination)

    @staticmethod
    def shutil_rmtree(_source):
        log.debug(f'shutil.rmtree() remove file or directory {_source}')
        shutil.rmtree(_source)

    @staticmethod
    def path_stat(_file):
        log.debug(f'Path.stat() for File {_file} is - {Path(_file).stat()}')
        return Path(_file).stat()

    @staticmethod
    def os_copy(_source, _destination):
        log.debug(f'os.system() cp from {_source} to {_destination}')
        os.system(f'cp {_source} {_destination}')

    @staticmethod
    def os_mv(_source, _destination):
        log.debug(f'os.system() mv from {_source} to {_destination}')
        os.system(f'mv {_source} {_destination}')

    @staticmethod
    def os_rename(_oldName, _newName):
        log.debug(f'os.rename() from {_oldName} to {_newName}')
        os.rename(_oldName, _newName)

    @staticmethod
    def os_rm(_file):
        log.debug(f'os.system() rm file {_file}')
        os.system(f'rm {_file} ')

    @staticmethod
    def os_walk(_path):
        """ Another 'search file' within given directory"""
        _result_list = []
        log.debug(f'os.walk() in directory {_path}')
        for root, dirs, files in os.walk(_path):
            for d in dirs:
                for file in files:
                    _result_list.append({"root": root, "dir": d, "file": file})

        return _result_list

    @staticmethod
    def search_file(_file_pattern,_search_dir):
        _file_lst = []
        for file in Path(_search_dir).glob(_file_pattern):
            _file_lst.append(file)
        return _file_lst

    @staticmethod
    def get_line_cnt(_file):
        with open(_file, 'r') as fp:
            for count, line in enumerate(fp):
                pass
        log.debug(f"file lines count - {count+1}")
        return count+1

    @staticmethod
    def find_str(_str, _file, ignore_case=False):
        _result_lst = []
        with open(_file, 'r') as fp:
            for l_indx, line in enumerate(fp):
                # search string
                if ignore_case and re.search(_str, line, re.IGNORECASE):
                    _dict = {"line": l_indx + 1, "value": line}
                    _result_lst.append(_dict)
                elif re.search(_str, line ):
                    _dict = {"line": l_indx + 1, "value": line}
                    _result_lst.append(_dict)
        return _result_lst

    @staticmethod
    def del_lines_contains_str(_str, _file, ignore_case=False):
        with open(_file, 'r') as fp:
            with open("temp.txt", "w") as _output:
                for l_indx, line in enumerate(fp):
                    # search string
                    if ignore_case:
                        if not re.search(_str, line, re.IGNORECASE):
                            _output.write(line)
                    else:
                        if not re.search(_str, line):
                            _output.write(line)
        # replace file with original name
        os.replace('temp.txt', _file)

    @staticmethod
    def del_lines_range(_from_line_no,_to_line_no, _file):
        with open(_file, "r+") as fp:
            # read an store all lines into list
            lines = fp.readlines()
            # move file pointer to the beginning of a file
            fp.seek(0)
            # truncate the file
            fp.truncate()
            # i.e line no = 3 => line index = 2;
            # start writing lines until [index = _from_line_no -1]
            # then continue writing lines from [index = _to_line_no] until EOF
            fp.writelines(lines[:_from_line_no-1])
            fp.writelines(lines[_to_line_no:])

    @staticmethod
    def get_filesize(_file):
        _size_bytes = Path(_file).stat().st_size
        _size_n = None
        """ Convert bytes to KB, or MB or GB"""
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if _size_bytes < 1024.0:
                _size_n = "%3.1f %s" % (_size_bytes, x)
                break
            _size_bytes /= 1024.0
        return _size_n

    @staticmethod
    def get_file_name(_file_str):
        """ First convert file String to Pathlib.Path(), before operating """
        _path= Path(_file_str)
        return _path.name

    @staticmethod
    def get_file_stem(_file_str):
        """ return file name without suffix """
        _path= Path(_file_str)
        return _path.stem

    @staticmethod
    def get_file_parts(_file_str):
        """ First convert file String to Pathlib.Path(), before operating """
        _path= Path(_file_str)
        return _path.parts

    @staticmethod
    def get_file_suffix(_file_str):
        """ Only return file name suffix """
        _path= Path(_file_str)
        return _path.suffix

    @staticmethod
    def get_path_parent(_path_str):
        """ return path parent """
        _path= Path(_path_str)
        return _path.parent

    @staticmethod
    def get_path_anchor(_path_str):
        """ return path anchor """
        _path= Path(_path_str)
        return _path.anchor

    @staticmethod
    def match_pattern(_path_str, _pattern):
        """ return True/False against path match _pattern (i.e. '*.md')  """
        _path = Path(_path_str)
        return _path.match(_pattern)

    @staticmethod
    def pretty_print_json(json_object, indent=2, sort_keys=False):
        """pretty print a json object in command line"""
        print(json.dumps(json_object, indent=indent, sort_keys=sort_keys))
