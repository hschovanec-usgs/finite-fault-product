from distutils.core import setup
import glob

setup(name='finite-fault-product',
      version='0.1dev',
      description='USGS finite fault product creater.',
      include_package_data=True,
      author='Heather Schovanec',
      author_email='hschovanec@usgs.gov',
      url='',
      packages=['fault',
                'fault/io',
                'product'],
      package_data={
          'fault': glob.glob('fault/*.cpt')
      },
      scripts=['bin/deleteproduct',
               'bin/getproduct',
               'bin/sendproduct']
      )
