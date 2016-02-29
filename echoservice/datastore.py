# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 13:05:29 2016

@author: sarath
"""
import os
DIR = os.path.dirname(os.path.abspath(__file__))
from utils import hangup 

class  Datastore(object):
    """  Datastore """
    def __init__(self, test, id, digits = None, data = None):
        super(Datastore, self).__init__()
        self._test = test
        self._id = id
        self._data = data
        if digits is not None and len(str(digits)) > 0:
            self._id += "_" + str(digits)

    def save(self):
        if  os.path.isdir("{0}/datastore/{1}".format(DIR, self._test)) is False:
            os.makedirs("{0}/datastore/{1}".format(DIR, self._test))
        f = open("{0}/datastore/{1}/{2}.xml".format(DIR, self._test, self._id),'w')
        f.write(self._data)
        f.close()
        return True

    def get_valid_file_path(self, file_path):
        dirname = os.path.dirname(file_path)
        basename, ext  = os.path.splitext(os.path.basename(file_path))

        while basename is not "" and os.path.isfile(os.path.join(dirname, basename) + ext) is not True:
            basename = basename[:-1 * basename[::-1].find('_') - 1]
        if basename is "":
            return os.path.join(DIR, "datastore", "hangup.xml")
        else:
            return os.path.join(dirname, basename) + ext

    def read(self):
        try:
            file_path = self.get_valid_file_path("{0}/datastore/{1}/{2}.xml".format(DIR, self._test, self._id))
            f = open(file_path, 'r')
            self._data = f.read()
            f.close()
        except Exception:
            self._data = hangup(self._test, self._id)
        return self._data