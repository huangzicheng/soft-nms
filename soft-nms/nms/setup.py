# from distutils.core import setup
# from Cython.Build import cythonize
#
#
# import  numpy as np
# setup(
#     ext_modules = cythonize("cpu_nms.pyx"),
#
# )

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as np
ext_modules = [Extension("cpu_nms",["cpu_nms.pyx"])]
setup(
    name = "cpu pyx",
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules,
include_dirs=[np.get_include()]
)