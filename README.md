# Lazytag Bot

Crystal Lin
Camille Rogers

Edgar Martinez

January 19, 2019

**OVERVIEW**

Wouldn&#39;t social media be so much easier if you didn&#39;t have to agonize over how to comment that friend&#39;s mundane photo? You want to seem like you paid attention-- without spending the time. To solve this worldwide problem, we decided to come up with Lazytag Bot, the comment generator for millennials with ultra-short attention spans.

The ultimate goal of Lazytag is to grab a photo from a social media post and generate a  non-committal sentence as a comment response. The bot should:

1. Classify an image from a website based on what is shown  (e.g. tree, person, dog etc.)
2. Generate a comment for the images, relating to what is shown in the picture.
3. Post that comment to the website.

This way all millennials can pretend they care about what their friends post on social media. ♥️

**DATA SET**

The dataset we will be using to train our object recognition model is the Caffee dataset developed by Berkeley AI Research. Caffe is a deep learning  pre-trained dataset and perfect for developing our Lazytag bot. A pre-trained dataset is necessary for our project since we are developing a sentence based on the information the dataset provides us from an image. 

 http://caffe.berkeleyvision.org/

**GOALS**

To reiterate, the bot will:

1. Grab an image from a website and identify what is contained in the image.
2. Generate a comment for the images, relating to what is shown in the picture.
3. Post the comment to the website under the image tag.

**Basic Goal.** Our basic goal is to train a machine learning network to take an image, identify what is contained in the image, and generate a comment related to what is contained in the image.

**Stretch Goal.** Our stretch goal is to scrape an image from a website (Reddit or Instagram), generate the comment (the basic goal), and post the comment under the image tag.



**METHOD**

1. Become familiar with the dataset and possibly change datasets to fit our needs
2. Create a model in order to analyze images (i.e. tell the difference between a tree,)
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

Example of some of the classes in the dataset we are going to use for Lazytag Bot. CIFAR-10 contains 10 classes. Our data set is similar in structure but instead contains 100 classes with &quot;fine&quot; labels and &quot;coarse&quot; superlabels.

CIFAR-10



**APPENDIX B: Project Timeline**

**Week 3.** Become familiar with the dataset and possibly change datasets to fit our needs

**Week 4.** Create a model in order to analyze images (i.e. tell the difference between a tree)

**Week 5** Become familiar with parsing the English Language

**Week 6.** Create grammar for English from a given dataset

**   **

**Week 7**. Pulling image from a social media website (Reddit or Instagram) classifying it

**Week 8** Create a sentence involving what was contained in the image

**Week 9** Post the generated sentence to social media website under image tag

**Week 10.** Fix any bugs/Catch up on any tasks not completed
