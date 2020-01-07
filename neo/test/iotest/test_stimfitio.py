"""
Tests of neo.io.stimfitio
"""

# needed for python 3 compatibility

import sys

import unittest

from neo.io import StimfitIO
from neo.io.stimfitio import HAS_STFIO
from neo.test.iotest.common_io_test import BaseTestIO


@unittest.skipIf(sys.version_info[0] > 2, "not Python 3 compatible")
@unittest.skipUnless(HAS_STFIO, "requires stfio")
class TestStimfitIO(BaseTestIO, unittest.TestCase):
    files_to_test = ['File_stimfit_1.h5',
                     'File_stimfit_2.h5',
                     'File_stimfit_3.h5',
                     'File_stimfit_4.h5',
                     'File_stimfit_5.h5',
                     'File_stimfit_6.h5',
                     ]
    files_to_download = files_to_test
    ioclass = StimfitIO


if __name__ == "__main__":
    unittest.main()
