import setuptools

VERSION = '0.0.2'


with open('README.md', 'r') as f:
    long_description = f.read()


with open('requirements.txt') as f:
    required = f.read().splitlines()


setuptools.setup(
    name='pyRHVoice',
    version=VERSION,
    author='Rustem Gazizov',
    author_email='r.gazizov@nnopolis.ru',
    description='Python wrapper for RHVoice',
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['pyrhvoice'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    install_requires=required,
)
