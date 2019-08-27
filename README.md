# TMIFVP
***
## TMI for Fun Vertical Profiles

### or

## Template Matching to Identify Features in Vertical Profiles
***

#### Collaborators
Paige Lavin: University of Washington

Regina Lionheart: University of Washington

Karina Ramos Musalem: University of British Columbia

Kathy Gunn: University of Miami

Daniel Wang: Virginia Institute of Marine Science, William & Mary

Anna-Lena Deppenmeier: NCAR

***

### The Problem

Tired of cruddy depth profiles? Want to know just how bad your instruments effed up their data collection? Then TMIVP is for you. 

Between instrumentation, environmental factors, and poor data acquisition methods, understanding and troubleshooting low-quality CTD profiles (along with other types of profile graphs) are a persistant issue in environmental science. TMIVP aims to quantify the difference between a template CTD profile and user-submitted data, clearly highlighting features for classification of problematic or interesting attributes. More broadly, this pipeline could be used to analyze and compare many types of line graphs, including but not limited to:

+ Michaelis-Menten population curves to characterize population growth
+ Metabolomic and proteomic spectrographic peaks to understand analytical drift, matrix effects and other obscuring variations
+ Environmental time series data to identify outliers

### The Solution

***
*This needs to be expanded upon once we have more specifics*
Our group used **SPECIFICS GO HERE** to compare **OUR REAL DATA IN THIS REAL LOCATION** to a template profile from a given location. 
***

### Steps to achieve Profile Nirvana
1. User provides two 1-dimensional arrays to the interface, one temperature and one depth to visualize their profile. **ARE THESE FROM A (net)CDF?** These are combined to create a uniform table of depth and temperature.

2. User selects a shape template he/she wants to find in a profile. 


2. TMIFVP code searches for 

...Combine to create a table, example below:

Temperature = x | Depth = y
--- | --- 
blah | whatevs
blah | whatevs
blah | whatevs   


2. Pick a pattern from that user-given profile with the "correct" numbers and dimensions. 
..* Provide a template CTD cast. 

3. "Match" the two. Take areas under the curve? Image hashing? Gruesome bed cutting pipeline.
..* Vertically segment by user-defined parameters. 

Possibly add lon and latitude for global placement
Add in photo.

You have some template and profile and convolve it along the user profile
Code will return correlation across convolved profile
track cross-correlations between template and profile
Will have a number for every profile. Cluster those numbers. Provides a dynamically adjustable threshold. 
What kind of vertical resolution for your profile do you need? Do a cross correlation at increasing frequency. 

Procrustes takes care of the scaling for you. 


***


