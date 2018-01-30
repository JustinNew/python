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