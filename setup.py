#!/usr/bin/env python
from os.path import join
import sys

from nitime import  __version__, __doc__

## Apply the matthew-monkey patch
from build_helpers import generate_a_pyrex_source
from numpy.distutils.command import build_src
build_src.build_src.generate_a_pyrex_source = generate_a_pyrex_source

def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration

    config = Configuration(None, parent_package, top_path)
    config.set_options(ignore_setup_xxx_py=True,
                       assume_default_configuration=True,
                       delegate_options_to_subpackages=True,
                       quiet=True)
    # The quiet=True option will silence all of the name setting warnings:
    # Ignoring attempt to set 'name' (from 'nitime.core' to 
    #    'nitime.core.image')
    # Robert Kern recommends setting quiet=True on the numpy list, stating
    # these messages are probably only used in debugging numpy distutils.

    config.get_version('nitime/version.py') # sets config.version

    return config


def main():
    from numpy.distutils.core import setup
    
    setup( name = 'nitime',
           description = 'Nitime: timeseries analysis for neuroscience data',
           author = 'Various',
           author_email = 'nipy-devel@neuroimaging.scipy.org',
           url = 'http://neuroimaging.scipy.org',
           long_description = __doc__,
           packages = ['nitime',
                       'nitime.fmri', 'nitime.fmri.tests',
                       'nitime.fixes',
                       'nitime.tests'],
           configuration = configuration)


if __name__ == "__main__":
    main()
