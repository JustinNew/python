Python
==========

### Sorting difference in Pandas and Coding (List)

List: l = [(1,2), (3,5), (6,3)]

  - l.sort(key=lambda x: x[1], reverse=True)

or, DataFrame  
  
  - df.sort_values(by=['A','B'], ascending=[1,0])
  
Note:

  - Coding: 'key', 'reverse', 'names'
  - DataFrame uses concepts from Excel: 'by', 'ascending', 'columns'
  
### No change conditions in 'while' or 'for' loop

The behavior of the following code is error-prone:

```python
i = 0
j = 0
while i < 5 - j:
    i += 1
	j += 1
```

### Numpy.Random

  - np.random.random: [0,1) uniform distribution
  - np.random.randint(low, high, size): random integer in range [low, high). **VS** random.randint(a,b) includes b ~ [a,b]. 
  - np.random.randn(): standard normal distribution 
  
### Import Self Defined Function

Import function from file.py use:
```
from file import function
```
  - Make sure 'file' is not one of Python's core modules.
  - If you are calling a.py from b.py, make sure the two files are in the same directoty.
  
### Install Package In Anaconda

To install a non-conda package:
  - $ conda info --envs
  - $ source activate myenvvalue
  - $ pip install packagename

### Import a package from different directory

  - When importing a file, Python only searches the current directory, the directory that the entry-point script is running from, and sys.path which includes locations such as the package installation directory (it's actually a little more complex than this, but this covers most cases).

The way to import the module from a directory is as follows:
  - First, ADD __INIT__
    - Ensure that a file called __init__ is added to the folder that contains the module you want to import. This file is typically empty.
  - Then, IMPORT MODULE
    - If the directory is in the working directory:
      - Import the module using the following syntax 'from <folder>.<filename> import <module>'.
      - <folder> is in the same directory as the running python file.
    - If the directory is not in the same working directory:
      - When modules are in parallel locations, as in the question:
        ```sh
        application/app2/some_folder/some_file.py
        application/app2/another_folder/another_file.py
        ```
        - This shorthand makes one module visible to the other:
        ```python
        import sys
        sys.path.append('../')
        ```
    - Or, 
      ```python
      import sys
      sys.path.insert(0, '/path/to/application/app/folder')

      import file
      ```
      or,
      ```python
      sys.path.append('/path/to/application/app/folder')
      ```
