

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(

    name='json-path', 

    version='0.0.1',  

    description='Get Json path from a nested json document. specify notation dot or bracket',  

    long_description=long_description, 

    long_description_content_type='text/markdown', 

    url='https://github.com/uniquetech/JSONPathGenerator.git',  

    author='hariharan sivakumar',  

    author_email='catchhster@gmail.com',  

   
    classifiers=[  

        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],


    keywords='Json Jsonpath xpath jsonnotation json parser safe parser',  

    package_dir={'': 'src'},  

    py_modules=["JSONPathGenerator.py"],

    python_requires='>=3.5, <4'
)