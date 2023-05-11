# Image Clustering
Image clustering on TikTok video snapshots to identify vaping trends: Made as a part of the Computational Media Lab

## Process
The following diagram is a nutshell of our evaluation procedure. Corresponding datasets and scripts are attached in this repository with more detailed instructions below.

![Process Diagram](figures/process_diagram.png)


## Data Collection

We collected data over several days using [a TikTok website scraper from this repository](https://github.com/drawrowfly/tiktok-scraper). In order to replicate this project, you will need access to the project data archive. The data is stored in this archive in a single screenshots folder with all images named by TikTok ID. The folder name: “Image Clustering/Screenshots”.


## Data Preparation

After excluding 672 videos due to non-English content, lack of e-cigarette-related content, unavailability at the time of screenshot, and the use of 20 videos for coder training, we were left with a sample of 838 screenshots from TikTok videos. To identify the most representative frame, a team member watched each video multiple times and selected the most salient visual aspect that captured the vaping content. This was done based on themes from prior research, such as vape tricks, e-cigarette modification, and product reviews. The screenshot taken reflected the central theme of the vape content in each video, and ensured consistency in the analysis. This approach allowed us to focus on the most important aspects of the vaping-related content, such as the type of device used, appearance of vapor clouds, and social context of the vaping. The resulting sample provided us with valuable data to analyze and interpret. Further details about our observations can be found in the results section.


## Code

### Google Colab

The Jupyter notebook present in [colab-run](colab-run) can be used to directly run on Google Colab. You can open the file in Google Colab and all file imports will be handled directly over there. The file paths in images_path should point to the directory where your images are stored. This is stored in “Image Clustering/Screenshots” from our data archive.

### Local

First, you have to download tensorflow for your system by following instructions for your operating system [from this source.](https://www.tensorflow.org/install). Generally, the following command can be run:

``` pip install tensorflow ```

Then, make sure img_names variable in [experiment.py](experiment.py) points to the folder where your image screenshots are stored.

Finally, you can run our experiments from [gridsearch.py](gridsearch.py). If you would like to modify any of clustering, dimensionality reduction, or embedding algorithms, you can add corresponding functions in the named files and then accordingly modify [experiment.py](experiment.py). 


