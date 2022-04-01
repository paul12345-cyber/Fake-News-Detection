# Fake-News-Detection
 
 <p>This repository host a deployment of a natural language processing model for fake news detection. <br />The model was trained on a dataset
obtained from <a href="https://www.kaggle.com/c/fake-news/data">kaggle</a>. We applied the following NLP techniques:</p>
<ul>
 <li>Stopwords removal</li>
 <li>Non-alphanumeric characters removal</li>
 <li>Stemming</li>
 <li>Vectorization via TF-IDF</li>
</ul>
<p>We trained a support vector machine model (svm) on the dataset and obtained an accuracy of 93.3% via a Gridsearch.<br />
The model is deployed on Heroku cloud platform and can be accessed <a href="https://fakenews-nlp.herokuapp.com/">here</a>. </p>
