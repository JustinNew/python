######################################################################################################
# Plot and show image in python.
import pylab
from matplotlib import pyplot as plt

plt.plot([1,2,3,4], [2,3,4,5])
pylab.show()

# datetime
from datetime import datetime
from datetime import timedelta
t = datetime(2019,1,2,0,0).date()
t2 = datetime(2019,1,2,0,0).date() + timedelta(7)

# To '2019-01-02'
datetime.strftime(t, '%Y-%m-%d')

# One default argument depending on another argument
def func(n=5.0, delta=None):
     if delta is None:
         delta = n/10

# to_datetime() format
pd.to_datetime(df_avail['local_time'], format='%Y-%m-%d %H:%M:%S')

# Add datetime with hour
# pd.to_timedelta
df['hours_to_add'] = pd.to_timedelta(df['hour'], 'h')
df['local_time'] = df['date'] + df['hours_to_add']
