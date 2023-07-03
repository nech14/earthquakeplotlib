from setuptools import setup

setup(
    name='earthquakeplotlib',
    version='1.2',
    description='',
    license='MIT',
    author='Artem Vesnin',
    author_email='artemvesnin@gmail.com',
    url='',
    packages=['earthquakeplotlib'],
    install_requires=['h5py', 'datetime',
                      'numpy', 'matplotlib',
                      'cartopy', 'dateutil',
                      'scipy', 'pathlib'],
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
    python_requires='>=3',
)
