#%% X-bar and R Chart
# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics

# Set random seed
np.random.seed(42)

# Create dummy data
x = np.array([list(np.random.normal(loc=10, scale=2, size=5)),
        list(np.random.normal(loc=10, scale=2, size=5)),
        list(np.random.normal(loc=10, scale=2, size=5)),
        list(np.random.normal(loc=10, scale=2, size=5)),
        list(np.random.normal(loc=10, scale=2, size=5)),
        list(np.random.normal(loc=17, scale=2, size=5)),
        list(np.random.normal(loc=10, scale=2, size=5)),
        list(np.random.normal(loc=10, scale=2, size=5)),
        list(np.random.normal(loc=10, scale=2, size=5)),
        list(np.random.normal(loc=10, scale=2, size=5))])
       
# Define list variable for groups means
x_bar = []

# Define list variable for groups ranges
r = [] 

# Get and append groups means and ranges
for group in x:
    x_bar.append(group.mean())
    r.append(group.max() - group.min())
    
# Plot x-bar and R charts
fig, axs = plt.subplots(2, figsize=(15,15))

# x-bar chart
axs[0].plot(x_bar, linestyle='-', marker='o', color='black')
axs[0].axhline((statistics.mean(x_bar)+0.577*statistics.mean(r)), color='red', linestyle='dashed')
axs[0].axhline((statistics.mean(x_bar)-0.577*statistics.mean(r)), color='red', linestyle='dashed')
axs[0].axhline((statistics.mean(x_bar)), color='blue')
axs[0].set_title('x-bar Chart')
axs[0].set(xlabel='Group', ylabel='Mean')

# R chart
axs[1].plot(r, linestyle='-', marker='o', color='black')
axs[1].axhline((2.574*statistics.mean(r)), color='red', linestyle='dashed')
axs[1].axhline((0*statistics.mean(r)), color='red', linestyle='dashed')
axs[1].axhline((statistics.mean(r)), color='blue')
axs[1].set_ylim(bottom=0)
axs[1].set_title('R Chart')
axs[1].set(xlabel='Group', ylabel='Range')

# Validate points out of control limits for x-bar chart
i = 0
control = True
for group in x_bar:
    if group > statistics.mean(x_bar)+0.577*statistics.mean(r) or group < statistics.mean(x_bar)-0.577*statistics.mean(r):
        print('Group', i, 'out of mean control limits!')
        control = False
    i += 1
if control == True:
    print('All points within control limits.')
    
# Validate points out of control limits for R chart
i = 0
control = True
for group in r:
    if group > 2.574*statistics.mean(r):
        print('Group', i, 'out of range cotrol limits!')
        control = False
    i += 1
if control == True:
    print('All points within control limits.')

#%% X-bar and S chart
# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics

# Set random seed
np.random.seed(42)

# Create dummy data
x = np.array([list(np.random.normal(loc=10, scale=2, size=11)),
        list(np.random.normal(loc=10, scale=2, size=11)),
        list(np.random.normal(loc=10, scale=2, size=11)),
        list(np.random.normal(loc=10, scale=2, size=11)),
        list(np.random.normal(loc=10, scale=2, size=11)),
        list(np.random.normal(loc=10, scale=2, size=11)),
        list(np.random.normal(loc=10, scale=2, size=11)),
        list(np.random.normal(loc=13, scale=2, size=11)),
        list(np.random.normal(loc=10, scale=2, size=11)),
        list(np.random.normal(loc=10, scale=2, size=11))])
        
# Define list variable for groups means
x_bar = []

# Define list variable for groups standard deviation
s = [] 

# Get and append groups means and standard deviations
for group in x:
    x_bar.append(group.mean())
    s.append(np.std(group))
    
# Plot x-bar and s charts
fig, axs = plt.subplots(2, figsize=(15,15))

# x-bar chart
axs[0].plot(x_bar, linestyle='-', marker='o', color='black')
axs[0].axhline((statistics.mean(x_bar)+0.927*statistics.mean(s)), color='red', linestyle='dashed')
axs[0].axhline((statistics.mean(x_bar)-0.927*statistics.mean(s)), color='red', linestyle='dashed')
axs[0].axhline((statistics.mean(x_bar)), color='blue')
axs[0].set_title('x-bar Chart')
axs[0].set(xlabel='Group', ylabel='Mean')

# s chart
axs[1].plot(s, linestyle='-', marker='o', color='black')
axs[1].axhline((1.649*statistics.mean(s)), color='red', linestyle='dashed')
axs[1].axhline((0.321*statistics.mean(s)), color='red', linestyle='dashed')
axs[1].axhline((statistics.mean(s)), color='blue')
axs[1].set_title('s Chart')
axs[1].set(xlabel='Group', ylabel='Range')

# Validate points out of control limits for x-bar chart
i = 0
control = True
for group in x_bar:
    if group > statistics.mean(x_bar)+0.927*statistics.mean(s) or group < statistics.mean(x_bar)-0.927*statistics.mean(s):
        print('Group', i, 'out of mean control limits!')
        control = False
    i += 1
if control == True:
    print('All points within control limits.')
    
# Validate points out of control limits for s chart
i = 0
control = True
for group in s:
    if group > 1.649*statistics.mean(s) or group < 0.321*statistics.mean(s):
        print('Group', i, 'out of standard deviation cotrol limits!')
        control = False
    i += 1
if control == True:
    print('All points within control limits.')
#%% p- chart
# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics

# Set random seed
np.random.seed(42)

# Create dummy data
p = {'defects':np.random.randint(1,5,10).tolist(),
    'group_size':np.random.randint(10,15,10).tolist()}
    
# Convert data to data frame
p = pd.DataFrame(p)

# Add 'p' column to data frame
p['p'] = p['defects']/p['group_size']

# Plot p-chart
plt.figure(figsize=(15,7.5))
plt.plot(p['p'], linestyle='-', marker='o', color='black')
plt.step(x=range(0,len(p['p'])), y=statistics.mean(p['p'])+3*(np.sqrt((statistics.mean(p['p'])*(1-statistics.mean(p['p'])))/(p['group_size']))), color='red', linestyle='dashed')
plt.step(x=range(0,len(p['p'])), y=statistics.mean(p['p'])-3*(np.sqrt((statistics.mean(p['p'])*(1-statistics.mean(p['p'])))/(p['group_size']))), color='red', linestyle='dashed')
plt.axhline(statistics.mean(p['p']), color='blue')
plt.ylim(bottom=0)
plt.title('p Chart')
plt.xlabel('Group')
plt.ylabel('Fraction Defective')

# Validate points out of control limits
i = 0
control = True
for group in p['p']:
    if group > (statistics.mean(p['p'])+3*(np.sqrt((statistics.mean(p['p'])*(1-statistics.mean(p['p'])))/statistics.mean(p['group_size'])))) or group < (statistics.mean(p['p'])-3*(np.sqrt((statistics.mean(p['p'])*(1-statistics.mean(p['p'])))/statistics.mean(p['group_size'])))):
        print('Group', i, 'out of fraction defective cotrol limits!')
        control = False
    i += 1
if control == True:
    print('All points within control limits.')
#%% np-chart
# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics

# Set random seed
np.random.seed(42)

# Create dummy data
data = {'defects':np.random.randint(1,5,10).tolist(),
        'group_size':np.repeat(10,10).tolist()}

# Convert data to data frame
data = pd.DataFrame(data)

# Add 'np' column to data frame
data['np'] = data['defects']/data['group_size']

# Plot np-chart
plt.figure(figsize=(15,7.5))
plt.plot(p['p'], linestyle='-', marker='o', color='black')
plt.axhline(statistics.mean(data['np'])+3*(np.sqrt((statistics.mean(data['np'])*(1-statistics.mean(data['np'])))/statistics.mean(data['group_size']))), color='red', linestyle='dashed')
plt.axhline(statistics.mean(data['np'])-3*(np.sqrt((statistics.mean(data['np'])*(1-statistics.mean(data['np'])))/statistics.mean(data['group_size']))), color='red', linestyle='dashed')
plt.axhline(statistics.mean(data['np']), color='blue')
plt.ylim(bottom=0)
plt.title('np Chart')
plt.xlabel('Group')
plt.ylabel('Fraction Defective')

# Validate points out of control limits
i = 0
control = True
for group in data['np']:
    if group > (statistics.mean(data['np'])+3*(np.sqrt((statistics.mean(data['np'])*(1-statistics.mean(data['np'])))/statistics.mean(data['group_size'])))) or group < (statistics.mean(data['np'])-3*(np.sqrt((statistics.mean(data['np'])*(1-statistics.mean(data['np'])))/statistics.mean(data['group_size'])))):
        print('Group', i, 'out of fraction defective cotrol limits!')
        control = False
    i += 1
if control == True:
    print('All points within control limits.')
#%% C-Chart
# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics

# Set random seed
np.random.seed(42)

# Create dummy data
c = {'defects':np.random.randint(0,5,10).tolist(),
    'group_size':np.repeat(10,10).tolist()}

# Convert data to data frame
c = pd.DataFrame(c)

# Plot c-chart
plt.figure(figsize=(15,7.5))
plt.plot(c['defects'], linestyle='-', marker='o', color='black')
plt.axhline(statistics.mean(c['defects'])+3*np.sqrt(statistics.mean(c['defects'])), color='red', linestyle='dashed')
plt.axhline(statistics.mean(c['defects'])-3*np.sqrt(statistics.mean(c['defects'])), color='red', linestyle='dashed')
plt.axhline(statistics.mean(c['defects']), color='blue')
plt.ylim(bottom=0)
plt.title('c Chart')
plt.xlabel('Group')
plt.ylabel('Defect Count')

# Validate points out of control limits
i = 0
control = True
for group in c['defects']:
    if group > statistics.mean(c['defects'])+3*np.sqrt(statistics.mean(c['defects'])) or group < statistics.mean(c['defects'])-3*np.sqrt(statistics.mean(c['defects'])):
        print('Group', i, 'out of defects cotrol limits!')
        control = False
    i += 1
if control == True:
    print('All points within control limits.')
#%% u-Chart
# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics

# Set random seed
np.random.seed(42)

# Create dummy data
u = {'defects':np.random.randint(1,5,10).tolist(),
    'group_size':np.random.randint(10,15,10).tolist()}

# Convert data to data frame
u = pd.DataFrame(u)

# Add 'u' column to data frame
u['u'] = u['defects']/u['group_size']

# Plot u-chart
plt.figure(figsize=(15,7.5))
plt.plot(u['u'], linestyle='-', marker='o', color='black')
plt.step(x=range(0, len(u['u'])), y=u['u'].mean()+3*np.sqrt(u['u'].mean()/u['group_size']), color='red', linestyle='dashed')
plt.step(x=range(0, len(u['u'])), y=u['u'].mean()-3*np.sqrt(u['u'].mean()/u['group_size']), color='red', linestyle='dashed')
plt.axhline(statistics.mean(u['u']), color='blue')
plt.ylim(bottom=0)
plt.title('u Chart')
plt.xlabel('Group')
plt.ylabel('Fraction Defective')

# Validate points out of control limits
i = 0
control = True
for group in u['u']:
    if group > u['u'].mean()+3*np.sqrt(u['u'].mean()/u['group_size'][i]) or group < u['u'].mean()-3*np.sqrt(u['u'].mean()/u['group_size'][i]):
        print('Group', i, 'out of fraction defective cotrol limits!')
        control = False
    i += 1
if control == True:
    print('All points within control limits.')