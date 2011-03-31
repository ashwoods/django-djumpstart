import os
import re
import shutil
import stat
import sys

from string import Template

def copy_template(src, dest, replace=None):
    """
    Copy all files in the source path to the destination path.
    
    To replace boilerplate strings in the source data, pass a dictionary to the
    ``replace`` argument where each key is the boilerplate string and the
    corresponding value is the string which should replace it.
    replacements, so directories and file names may also be modified.
    
    """
    for path, dirs, files in os.walk(src):
        relative_path = path[len(src):].lstrip('/')
        # Replace boilerplate strings in destination directory.
        os.mkdir(os.path.join(dest, relative_path))
        for i, subdir in enumerate(dirs):
            if subdir.startswith('.'):
                del dirs[i]
        for filename in files:
            if (filename.startswith('djumpstart') or
                filename.endswith('.pyc')):
                continue
            src_file_path = os.path.join(path, filename)
            # Replace boilerplate strings in destination filename.
            dest_file_path = os.path.join(dest, relative_path, filename)
            copy_template_file(src_file_path, dest_file_path, replace)


def copy_template_file(src, dest, replace=None):
    """
    Copy a source file to a new destination file.
    
    To replace boilerplate strings in the source data, pass a dictionary to the
    ``replace`` argument where each key is the boilerplate string and the
    corresponding value is the string which should replace it.
    
    """
    replace = replace or {}
    # Read the data from the source file.
    src_file = open(src, 'r')
    data = src_file.read()
    src_file.close()
    # Replace boilerplate strings.
    s = Template(data)
    rendered_template = s.safe_substitute(replace)
    # Write the data to the destination file.
    dest_file = open(dest, 'w')
    dest_file.write(rendered_template)
    dest_file.close()
    # Copy permissions from source file.
    shutil.copymode(src, dest)
    # Make new file writable.
    if os.access(dest, os.W_OK):
        st = os.stat(dest)
        new_permissions = stat.S_IMODE(st.st_mode) | stat.S_IWUSR
        os.chmod(dest, new_permissions)


def get_template_vars(path):
    """
    Look for a ``.djumpstart.py`` file the given path and parse it.
    
    Return a list of 3-part tuples, each containing a boilerplate variable,
    optional description and default value.
    
    If no file was found (or no lines contained boilerplate variables), return
    an empty list.
    
    """
    djumpstart_path = os.path.join(path, 'djumpstart_vars.py')
    if os.path.isfile(djumpstart_path):
        sys.path.insert(0, path)
        from djumpstart_vars import DJUMPSTART_TEMPLATE_VARS
        return DJUMPSTART_TEMPLATE_VARS
    else:
        return {}
