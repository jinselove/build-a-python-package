## How to install the package
© Copyright 2012, Scott Torborg. Revision 35daf993. 

https://python-packaging.readthedocs.io/en/latest/minimal.html#publishing-on-pypi

### 1. install locally
  
  * Install the package locally
  
  	`pip install .` 
  
  * install the package with a symlink so that changes to the source files will be immediately available to other users of the package on our system)

	`pip install -e .`
    
  * To load the package
  
   	`>>> import funnist`  

### 2. Publishing on PyPI

  * register the package (this will reserve the name, upload package metadata, and create the pypi.python.org webpage)  

	`python setup.py register`
    
  * Upload the source codes

	1. create a source distribution (the following code will create a dist/funniest-0.1.tar.gz)

		`python setup.py sdist`
        
    2. upload the code

		`python setup.py sdist upload`
        
    3. for more help

		`python setup.py --help-commands`
    4. install the package

		`pip install funnist`
