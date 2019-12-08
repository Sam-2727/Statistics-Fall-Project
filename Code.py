#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 08:42:20 2019

@author: samchristian
"""

import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('/Users/samchristian/Downloads/1552314849354O-result.csv')
data = data[np.isfinite(data['parallax']) & np.isfinite(data['metallicity'])]
print(len(data))
parallax = data['parallax']
metallicity = data['metallicity']
Q1P = parallax.quantile(0.25)
Q3P = parallax.quantile(0.75)
IQRP = Q3P - Q1P
Q1M = metallicity.quantile(0.25)
Q3M = metallicity.quantile(0.75)
IQRM = Q3M - Q1M
print(len(parallax))
parallax = parallax[((parallax > Q1P-1.5*IQRP) & (parallax < Q3P + 1.5*IQRP)) | ((metallicity > Q1M-1.5*IQRM) & (metallicity < Q1M+1.5*IQRM))]
print(len(parallax))
metallicity = metallicity[((parallax > Q1P-1.5*IQRP) & (parallax < Q3P + 1.5*IQRP)) | ((metallicity > Q1M-1.5*IQRM) & (metallicity < Q1M+1.5*IQRM))]
print(stats.linregress(metallicity, parallax))
#plt.hist(parallax)
sns.residplot(metallicity, parallax, lowess=True, color="g")
plt.hist(metallicity, bins = 100)
#sns.distplot(parallax, bins = 50)
