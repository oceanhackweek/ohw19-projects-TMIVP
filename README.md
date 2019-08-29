<h1><center>TMIFVP</center></h1>

***

<h1><center>TMI for Fun Vertical Profiles</center></h1>


<h1><center>or</center></h1>

<h1><center>Template Matching to Identify Features in Vertical Profiles</center></h1>

***

#### Collaborators
Anna-Lena Deppenmeier: NCAR

Daniel Wang: Virginia Institute of Marine Science, William & Mary

Karina Ramos Musalem: University of British Columbia

Kathy Gunn: University of Miami

Paige Lavin: University of Washington


Regina Lionheart: University of Washington

***

### The Problem

Interested in finding a specific feature in your depth profiles? Want to know where those features are clustered? Then TMIVP, built upon the ideas of the visionary non-conformist demigod Procrustes, is for you. 

Between unpredictable mixed layer temperature profiles, various clines, and nutrient spikes, understanding and searching through CTD profiles (along with other types of profiles) are a persistant issue in environmental science. TMIVP aims to match and quantify the difference between a template profile and user-submitted data, clearly highlighting features for quality matching scores and location of problematic or interesting attributes. More broadly, this pipeline could be used to analyze and compare many types of graphs and profiles, including but not limited to:

+ Michaelis-Menten population curves to characterize population growth
+ Metabolomic and proteomic spectrographic peaks to understand analytical drift, matrix effects and other obscuring variations
+ Environmental time series data to identify outliers

Below, our cut-to-fit-the-bed template matching pipeline.

***

### The Solution

*This needs to be expanded upon once we have more specifics*

Our group used the principles of cross-correlation to vertically search profiles and match features to a template.

<span style="color:red">**WHY THIS KIND OF TEMPLATE? WHAT'S THE JUSTIFICATION?**</span>

***

### Steps to Achieve Profile Nirvana
#### 1. User provides two 1-dimensional arrays to the interface, one of which is temperature (for the purpose of this example; multiple variables are possible) and the other depth. Those two arrays are returned as a table and visualized profiles. 
<span style="color: red">**CHECK THAT THIS IS TRUE, SET UP FUNCTION TO DO SO.** </span>


*Example Table and Graph*

Depth = y | Temperature = x
--- | --- 
5  | 29.66  
23 | 27.62
32 | 24.81   
50 | 22.81   
59 | 21.58 
68 | 21.15 
77 | 20.38 



!<center>![Text here](data/haifa_depth.png)</center>

#### 2. TMIFVP provides a "template" shape that has typical numbers and dimensions for an oceanographic profile. This will act as a pattern matching feature for real data. 

* <span style="color:red">**TEMPLATE SHOULD BE SMALLER- ADD JUSTIFY** </span>
Because the cross-correlation won't work if the template is larger than the profile, and the template has to be too small because if it's too large it will smooth the entire profile. Instead of grabbing small similar features, it will grab a space between are similar.

* <span style="color:red">**EXPLAIN HOW WE PRODUCE THE TEMPLATE, add example picture** </span>
We will provide the user with some template options, which exist as a list of numbers (2d array).  

#### 3. TMIFVP uses the SciPy cross-correlation function to match the two arrays: pattern & profile. 

* The cross-correlation function will find the location of a possible matching pattern. Maximum correlation occurs when they are the same size. 
* Find the maximum of segmented profile, take the median of that array, shift pattern by the median (aka the "lag"). The lag tells you how far you need to shift the pattern to match the profile the most. Crop the signal to where it matches the template, then proceed to the Procrustes analysis.


#### 4. Select section of the profile that matches the template.

Cut the user profile by n times the width of the feature. 
Within each chunk:
* Use Procrustes analysis to align template to the profile chunk. In statistics, Procrustes analysis is a form of statistical shape analysis used to analyse the distribution of a set of shapes. The function handles the scaling of the template matching for you. The name Procrustes (Greek: Προκρούστης) refers to a bandit from Greek mythology who made his victims fit his bed either by stretching their limbs or cutting them off (source: Wikipedia).
!<center>![Text here](data/Prokrustes.jpg)</center>

* Calculate the similarity. <span style="color:red">**WHAT SPECIFICALLY ARE WE USING TO DO THAT**</span>.

#### 5. Find best template-chunk pair for each profile, ie, the highest similarity score.
* This produces a quality score from 0 - 1, resulting from matching the template and the chunk of the profile. 

#### 6. Cluster the similarity score?

***

### Background Reading

Useful links:
    
https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.correlate.html
    
A short explanation of cross correlation and convolution (slides)

https://users.cs.northwestern.edu/~pardo/courses/eecs352/lectures/MPM16-topic8-Convolution.pdf

A slightly graphic description of the inspiration for the Procrustes analysis.

https://en.wikipedia.org/wiki/Procrustes

***

Extra Notes

Features with the same area but different shapes can pose a problem.

Possibly add lon and latitude for global placement
Add in photo.

Will have a number for every profile. Cluster those numbers. Provides a dynamically adjustable threshold. 
What kind of vertical resolution for your profile do you  need? Do a cross correlation at increasing frequency. 

Eventually vertical segmentation to account for multiple matching features?

***