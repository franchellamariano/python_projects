#!/usr/bin/env python
# coding: utf-8

# # Activity: Explore sampling

# ## Introduction
# In this activity, you will engage in effective sampling of a dataset in order to make it easier to analyze. As a data professional you will often work with extremely large datasets, and utilizing proper sampling techniques helps you improve your efficiency in this work. 
# 
# For this activity, you are a member of an analytics team for the Environmental Protection Agency. You are assigned to analyze data on air quality with respect to carbon monoxide—a major air pollutant—and report your findings. The data utilized in this activity includes information from over 200 sites, identified by their state name, county name, city name, and local site name. You will use effective sampling within this dataset. 

# ## Step 1: Imports

# ### Import packages
# 
# Import `pandas`,  `numpy`, `matplotlib`, `statsmodels`, and `scipy`. 

# In[23]:


# Import libraries and packages

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy.stats as stats


# ### Load the dataset
# 
# As shown in this cell, the dataset has been automatically loaded in for you. You do not need to download the .csv file, or provide more code, in order to access the dataset and proceed with this lab. Please continue with this activity by completing the following instructions.

# In[2]:


# RUN THIS CELL TO IMPORT YOUR DATA.

### YOUR CODE HERE ###
epa_data = pd.read_csv("c4_epa_air_quality.csv", index_col = 0)


# <details>
#   <summary><h4>Hint 1</h4></summary>
# 
# Use the function in the `pandas` library that allows you to read in data from a csv file and load it into a DataFrame. 
# 
# </details>

# <details>
#   <summary><h4>Hint 2</h4></summary>
# 
# Use the `read_csv` function from the pandas `library`. Set the `index_col` parameter to `0` to read in the first column as an index (and to avoid `"Unnamed: 0"` appearing as a column in the resulting Dataframe).
# 
# </details>

# ## Step 2: Data exploration

# ### Examine the data
# 
# To understand how the dataset is structured, examine the first 10 rows of the data.

# In[3]:


# First 10 rows of the data

epa_data.head(10)


# <details>
#   <summary><h4><strong> Hint 1 </STRONG></h4></summary>
# 
# Use the function in the `pandas` library that allows you to get a specific number of rows from the top of a DataFrame. 
# 
# </details>

# <details>
#   <summary><h4><strong> Hint 2 </STRONG></h4></summary>
# 
# Use the `head` function from the `pandas` library. Set the `n` parameter to `10` to print out the first 10 rows.
# 
# </details>

# ### Generate a table of descriptive statistics
# 
# Generate a table of some descriptive statistics about the data. Specify that all columns of the input be included in the output.

# In[4]:


epa_data.describe()


# <details>
#   <summary><h4>Hint 1</h4></summary>
# 
# Use function in the `pandas` library that allows you to generate a table of basic descriptive statistics in a DataFrame.
# 
# </details>

# <details>
#   <summary><h4>Hint 2</h4></summary>
# 
# Use the `describe` function from the `pandas` library. Set the `include` parameter passed in to this function to 'all' to specify that all columns of the input be included in the output.
# 
# </details>

# **Question:** Based on the preceding table of descriptive statistics, what is the mean value of the `aqi` column? 

# The mean value of the aqi column is 6.757692

# **Question:** Based on the preceding table of descriptive statistics, what do you notice about the count value for the `aqi` column?

# The count value for the aqi column is 260

# ### Use the `mean()` function on the `aqi`  column
# 
# Now, use the `mean()` function on the `aqi`  column and assign the value to a variable `population_mean`. The value should be the same as the one generated by the `describe()` method in the above table. 

# In[5]:


epa_data["aqi"].mean()


# <details>
#   <summary><h4><strong> Hint 1 </STRONG></h4></summary>
# 
# Use the function in the `pandas` library that allows you to generate a mean value for a column in a DataFrame.
# 
# </details>

# <details>
#   <summary><h4><strong> Hint 2 </STRONG></h4></summary>
# 
# Use the `mean()` method.
# 
# </details>

# ## Step 3: Statistical tests

# ### Sample with replacement
# 
# First, name a new variable `sampled_data`. Then, use the `sample()` dataframe method to draw 50 samples from `epa_data`. Set `replace` equal to `'True'` to specify sampling with replacement. For `random_state`, choose an arbitrary number for random seed. Make that arbitrary number `42`.

# In[7]:


sampled_data = epa_data.sample(n = 50, replace = True, random_state = 42)


# ### Output the first 10 rows
# 
# Output the first 10 rows of the DataFrame. 

# In[8]:


sampled_data.head(10)


# <details>
#   <summary><h4><strong> Hint 1 </STRONG></h4></summary>
# 
# Use the function in the `pandas` library that allows you to get a specific number of rows from the top of a DataFrame. 
# 
# </details>

# <details>
#   <summary><h4><strong> Hint 2 </STRONG></h4></summary>
# 
# Use the `head` function from the `pandas` library. Set the `n` parameter to `10` to print out the first 10 rows.
# 
# </details>

# **Question:** In the DataFrame output, why is the row index 102 repeated twice? 

# Because we sampled randomly with replacement, 102 happened to be chosen twice.

# ### Compute the mean value from the `aqi` column
# 
# Compute the mean value from the `aqi` column in `sampled_data` and assign the value to the variable `sample_mean`.

# In[10]:


sample_mean = sampled_data["aqi"].mean()
sample_mean


#  **Question:**  Why is `sample_mean` different from `population_mean`?
# 

# sample_mean is different than population_mean because it is the mean of the sampled data and not the whole population.

# ### Apply the central limit theorem
# 
# Imagine repeating the the earlier sample with replacement 10,000 times and obtaining 10,000 point estimates of the mean. In other words, imagine taking 10,000 random samples of 50 AQI values and computing the mean for each sample. According to the **central limit theorem**, the mean of a sampling distribution should be roughly equal to the population mean. Complete the following steps to compute the mean of the sampling distribution with 10,000 samples. 
# 
# * Create an empty list and assign it to a variable called `estimate_list`. 
# * Iterate through a `for` loop 10,000 times. To do this, make sure to utilize the `range()` function to generate a sequence of numbers from 0 to 9,999. 
# * In each iteration of the loop, use the `sample()` function to take a random sample (with replacement) of 50 AQI values from the population. Do not set `random_state` to a value.
# * Use the list `append()` function to add the value of the sample `mean` to each item in the list.
# 

# In[13]:


estimate_list = []
for i in range(10000):
    estimate_list.append(epa_data["aqi"].sample(n=50,replace=True).mean())


# <details>
#   <summary><h4><strong> Hint 1 </STRONG></h4></summary>
# 
# Review [the content about sampling in Python](https://www.coursera.org/learn/the-power-of-statistics/lecture/SNOE0/sampling-distributions-with-python). 
# 
# </details>

# ### Create a new DataFrame
# 
# Next, create a new DataFrame from the list of 10,000 estimates. Name the new variable `estimate_df`.

# In[17]:


estimate_df = pd.DataFrame(data = {"estimate": estimate_list})
estimate_df


# <details>
#   <summary><h4><strong> Hint 1 </STRONG></h4></summary>
# 
# Review [the content about sampling in Python](https://www.coursera.org/learn/the-power-of-statistics/lecture/SNOE0/sampling-distributions-with-python). 
# 
# </details>

# <details>
# <summary><h4><strong> Hint 2 </STRONG></h4></summary>
# 
# Use the `mean()` function.
# 
# </details>

# ### Compute the mean() of the sampling distribution
# 
# Next, compute the `mean()` of the sampling distribution of 10,000 random samples and store the result in a new variable `mean_sample_means`.

# In[19]:


mean_sample_means = estimate_df["estimate"].mean()
mean_sample_means


# <details>
#   <summary><h4><strong> Hint 1 </STRONG></h4></summary>
# 
# Use the function in the `pandas` library that allows you to generate a mean value for a column in a DataFrame.
# 
# </details>

# <details>
#   <summary><h4><strong> Hint 2 </STRONG></h4></summary>
# 
# Use the `mean()` function.
# 
# </details>

# <details>
#   <summary><h4><strong> Hint 3 </STRONG></h4></summary>
# 
# This value is contained in `mean_sample_means`.
# 
# </details>

# <details>
#   <summary><h4><strong> Hint 4 </STRONG></h4></summary>
# 
# According to the central limit theorem, the mean of the preceding sampling distribution should be roughly equal to the population mean. 
# 
# </details>

# **Question:** How are the central limit theorem and random sampling (with replacement) related?

# The concept of random sampling with replacement is interconnected with the central limit theorem, as it involves drawing observations independently from a population. According to the central limit theorem, when the sample size is sufficiently large and observations are drawn independently or with replacement, the sampling distribution of the sample mean approximates a normal distribution. Additionally, the mean parameter corresponds to the population mean, while the variance parameter represents the standard error.

# ### Output the distribution using a histogram
# 
# Output the distribution of these estimates using a histogram. This provides an idea of the sampling distribution.

# In[20]:


estimate_df['estimate'].hist()


# <details>
#   <summary><h4><strong> Hint 1 </STRONG></h4></summary>
# 
# Use the `hist()` function. 
# 
# </details>

# ### Calculate the standard error
# 
# Calculate the standard error of the mean AQI using the initial sample of 50. The **standard error** of a statistic measures the sample-to-sample variability of the sample statistic. It provides a numerical measure of sampling variability and answers the question: How far is a statistic based on one particular sample from the actual value of the statistic?

# In[21]:


standard_error = sampled_data["aqi"].std() / np.sqrt(len(sampled_data))
standard_error


# <details>
#   <summary><h4><strong> Hint 1 </STRONG></h4></summary>
# 
# Use the `std()` function and the `np.sqrt()` function.
# 
# </details>

# # Considerations
# 
# **What are some key takeaways that you learned from this lab?**
# 
# **What findings would you share with others?**
# 
# **What would you convey to external stakeholders?**
# 
# 
# 

# **Congratulations!** You've completed this lab. However, you may not notice a green check mark next to this item on Coursera's platform. Please continue your progress regardless of the check mark. Just click on the "save" icon at the top of this notebook to ensure your work has been logged.
