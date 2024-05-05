from setuptools import setup, find_packages


with open("README.md", "r") as readme:
    long_description = readme.read()


setup(
    name='kingorm',
    version='1.0.0',    
    description='King is an ORM for Python and SQLite. It is designed to be a lightweight solution for simple programs, where objects have to be stored. A programmer just needs to define fields in the model classes and that\'s it!',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/king-orm/orm/',
    author='Anatoly Frolov',
    author_email='contact@anafro.ru',
    license='MIT',
    packages=find_packages(),

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  
        'Programming Language :: Python :: 3.11',
        'Programming Language :: SQL',
        "Operating System :: OS Independent",
    ],
)