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

The behavior of the following code is unknown:

```python
i = 0
j = 0
while i < 5 - j:
    i += 1
	j += 1
```

### Numpy.Random

  - random.random: [0,1) uniform distribution
  - random.randint(low, high, size): random integer in range [low, high) 
  - random.randn(): standard normal distribution 