from distutils.core import setup

description = open('README.rst').readlines()

setup(name='PyIneq',
      version='0.0.1',
      description='A Python Package To Quantitative Analysis Of Inequality',
      long_description=open('README.rst').read(),
      author='Maximiliano Greco',
      author_email='mmngreco@gmail.com',
      url='mmngreco.github.io',
      packages=['pyineq'],
      classifiers=['Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'Topic :: Software Development :: Build Tools',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                    ],
      install_requires=['numpy', 'pandas'],
     )