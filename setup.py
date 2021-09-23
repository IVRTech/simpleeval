from setuptools import setup

__version__ = '0.9.11'

setup(
    name='simpleeval',
    py_modules=['simpleeval'],
    version=__version__,
    description='A simple, safe single expression evaluator library.',
    long_description=open('README.rst', 'r').read(),
    long_description_content_type='text/x-rst',
    author='IVR Technology Group',
    author_email='developers@ivrtechnology.com',
    url='https://github.com/IVRTech/simpleeval/',
    download_url='https://github.com/IVRTech/simpleeval/releases/tag/' + __version__,
    keywords=['eval', 'simple', 'expression', 'parse', 'ast'],
    test_suite='test_simpleeval',
    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Topic :: Software Development :: Libraries :: Python Modules',
                 'Programming Language :: Python',
                 ],
)
