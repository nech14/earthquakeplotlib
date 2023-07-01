from setuptools import setup

setup(
    name='vesninlib',
    version='1.0.1',
    description='',
    license='MIT',
    author='Artem Vesnin',
    author_email='artemvesnin@gmail.com',
    url='',
    packages=['vesninlib'],
    install_requires=['h5py', 'datetime',
                      'numpy','matplotlib',
                      'cartopy', 'dateutil',
                      'scipy', 'matplotlib',
                      'pathlib'],
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
    python_requires='>=3',
)
