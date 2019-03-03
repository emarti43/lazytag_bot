# Lazytag Bot

Crystal Lin

Camille Rogers

Edgar Martinez

January 19, 2019

**OVERVIEW**

Wouldn't social media be so much easier if you didn't have to agonize over how to comment that friend's mundane photo? You want to seem like you paid attention-- without spending the time. To solve this worldwide problem, we decided to come up with Lazytag Bot, the comment generator for millennials with ultra-short attention spans.

The ultimate goal of Lazytag is to grab a photo from a social media post and generate a  non-committal sentence as a comment response. The bot should:

1. Classify an image from a website based on what is shown  (e.g. tree, person, dog etc.)
2. Generate a comment for the images, relating to what is shown in the picture.
3. Post that comment to the website.

This way all millennials can pretend they care about what their friends post on social media. ♥️

**REQUIREMENTS**
1. Python 3.6/3.7
2. Clarifai package  ```pip install clarifai``` or ```conda install clarifai```
3. NLTK package ```pip install nltk``` or ```conda install nltk```
4. Inflect package ```pip install inflect```
5. Markovify package ```pip install markovify```

**DATA SET**

The dataset we will be using is the Clarifai API. You send inputs (an image or video) to the service and it returns probablity/predictions of what it thinks is displayed. We will use the most accurate predictions to create a sentence for a social media post.

 https://clarifai.com/developer/guide/predict#images

**GOALS**

To reiterate, the bot will:

1. Grab an image from a website and identify what is contained in the image.
2. Generate a comment for the images, relating to what is shown in the picture.
3. Post the comment to the website under the image tag.

**Basic Goal.** Our basic goal is to train a machine learning network to take an image, identify what is contained in the image, and generate a comment related to what is contained in the image.

**Stretch Goal.** Our stretch goal is to scrape an image from a website (Reddit or Instagram), generate the comment (the basic goal), and post the comment under the image tag.



**METHOD**

1. Become familiar with the dataset and possibly change datasets to fit our needs
2. Find a image recognition dataset api for Lazytag Bot
3. Become familiar with parsing the English Language
4. Create grammar for English from a given dataset
5. Pulling image from a social media website (Reddit or Instagram) classifying it
6. Create a sentence involving what was contained in the image
7. Post the generated sentence to social media website under image tag

**REFERENCES**

Krizhevsky. [Learning Multiple Layers of Features from Tiny Images](https://www.cs.toronto.edu/~kriz/learning-features-2009-TR.pdf). 2009

        [https://www.cs.toronto.edu/~kriz/cifar.html](https://www.cs.toronto.edu/~kriz/cifar.html)

Auto Generation for Image ALT Text

[https://cloudinary.com/blog/making\_media\_accessible\_how\_to\_automatically\_generate\_alt\_text\_for\_images](https://cloudinary.com/blog/making_media_accessible_how_to_automatically_generate_alt_text_for_images)

Generating Textual Descriptions for Photographs

[https://machinelearningmastery.com/how-to-caption-photos-with-deep-learning/](https://machinelearningmastery.com/how-to-caption-photos-with-deep-learning/)

**APPENDIX A: Data Set Structure**

The Clarifai API will take the input of an image or a video and output probabilities based on the image.

Setting Up the Dataset:

1. Make sure to use python 3.6

2. To install do the command **pip install clarifai**

**APPENDIX B: Project Timeline**

**Week 3.** Become familiar with the dataset and possibly change datasets to fit our needs

**Week 4.** Find an image recognition api dataset that works with our project

**Week 5** Become familiar with parsing the English Language

**Week 6.** Create grammar for English from a given dataset

**   **

**Week 7**. Pulling image from a social media website (Reddit or Instagram) classifying it

**Week 8** Create a sentence involving what was contained in the image

**Week 9** Post the generated sentence to social media website under image tag

**Week 10.** Fix any bugs/Catch up on any tasks not completed
