from setuptools import setup


setup(
    name='kingorm',
    version='1.0.0',    
    description='King is an ORM for Python and SQLite. It is designed to be a lightweight solution for simple programs, where objects have to be stored. A programmer just needs to define fields in the model classes and that\'s it!',
    url='https://github.com/shuds13/pyexample',
    author='Anatoly Frolov',
    author_email='contact@anafro.ru',
    license='MIT',
    packages=['kingorm'],
    install_requires=[],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  
        'Programming Language :: Python :: 3.11',
        'Programming Language :: SQL',
    ],
)