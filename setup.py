from setuptools import setup, find_packages


setup(
    name='matrixCICD',
    version='2.1',
    license='MIT',
    author="Diego Chahuan and Preston Chao",
    author_email='docl@ug.kth.se',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/dchahuan/CD_DEMO',
    keywords='Pipeline/Matrix',
    install_requires=[
          'pytest',
      ],
)