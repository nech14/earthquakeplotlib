from setuptools import setup

setup(
    name='vesninlib',
    version='1.0',
    description='',
    license='MIT',
    author='Artem Vesnin',
    author_email='artemvesnin@gmail.com',
    url='',
    packages=['vesninlib'],
    install_requires=['requests', 'h5py',
                      'numpy','matplotlib',
                      'cartopy',
                      'scipy',
                      'pathlib', 'matplotlib'], # it is empty since we use standard python library
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
    python_requires='>=3',
)
