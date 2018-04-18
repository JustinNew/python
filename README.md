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