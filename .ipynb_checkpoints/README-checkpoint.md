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


Our group used the principles of cross-correlation to vertically search profiles and match expected oceanographic profile feature templates to real user data.

TMIFVP currently supplies three typical templates for matching. 

***

### Steps to Achieve Profile Nirvana
#### 1. User provides two 1-dimensional arrays to the interface, one of which is temperature (for the purpose of this example; multiple variables are possible) and the other depth. Those two arrays are returned as a table and visualized profiles. 


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

<p align="center">
  <img src=data/haifa_depth.png>
</p>


#### 2. TMIFVP provides a "template" shape that has typical numbers and dimensions for an oceanographic profile. This will act as a pattern matching feature for real data. 

* The three templates currently used for matching are 1. Exponential, 2. Gaussian, and 3. Step profile. 

* Templates should be scaled towards the smaller end of the spectrum: the cross-correlation won't work if the template is larger than the profile. Additionally, if the template is too large it will smooth the entire profile. Instead of selecting small similar features, it may grab spaces between features that have a similar shape.

* There are several template options in 2d array format. Below is an example of a possible template. Choose the template that you would expect to find in your data depending on location, season, etc. 


<p align="center">
  <img src=data/Exponential_example.png>
</p>

* This would be used to match real user data, such as the example below.

<p align="center">
  <img src=data/Profile_example.png>
</p>


#### 3. TMIFVP uses the SciPy cross-correlation function to match the two arrays: pattern & profile. 

* The cross-correlation function will find the location of a possible matching pattern. Maximum correlation occurs when they are the same size. 
* Profile is segmented depending on where the maximum correlation occurs. 


<p align="center">
  <img src=data/template_match.png>
</p>


#### 4. Optimize template to match the chosen segment.

Within each segment:
* In case a step template: Use Procrustes analysis to align template to the profile chunk. In statistics, Procrustes analysis is a form of statistical shape analysis used to analyse the distribution of a set of shapes. The function handles the scaling of the template matching for you. The name Procrustes (Greek: Προκρούστης) refers to a bandit from Greek mythology who made his victims fit his bed either by stretching their limbs or cutting them off (source: Wikipedia).
<p align="center">
  <img src=data/Prokrustes.jpg>
</p>

* In case of Gaussian or exponential templates, use a normal fit. 

<p align="center">
  <img src=data/Gaussian_fit.png
  style="width:500px;height:400px;">
</p>

* For all templates, calculate the similarity using the root means square error, or RMSE. RMSE is a frequently used measure of the differences between values (sample or population values) predicted by a model or an estimator and the values observed. The RMSD represents the square root of the second sample moment of the differences between predicted values and observed values or the quadratic mean of these differences (source: Wikipedia).

**TBD**
#### 5. Find best template-chunk pair for each profile, ie, the highest similarity score.
* This produces a quality score from 0 - 1, resulting from matching the template and the chunk of the profile. 
**TBD**

#### 6. Produce figures and output from TMIFVP.
* Histogram of quality distribution
<p align="center">
  <img src=data/score_distribution.png
  style="width:500px;height:400px;">
>
</p>

* Seaborn jointplot of physical location and quality score relationship.
<p align="center">
  <img src=data/jointplot.png>
</p>

* Map of profile locations, shaded by quality. The darker the shade, the higher the quality score.

<p align="center">
  <img src=data/example_map.png>
</p>

***

### Background Reading

Useful links:
    
https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.correlate.html
    
A short explanation of cross correlation and convolution (slides)

https://users.cs.northwestern.edu/~pardo/courses/eecs352/lectures/MPM16-topic8-Convolution.pdf

A slightly graphic description of the inspiration for the Procrustes analysis.

https://en.wikipedia.org/wiki/Procrustes

***
