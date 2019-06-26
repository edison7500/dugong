import jieba
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
# from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from .models import TrainingSet


def jieba_tokenize(text):
    return jieba.lcut(text)


def get_pipeline():
    x = TrainingSet.objects.filter().values_list('body', flat=True)
    y = TrainingSet.objects.filter().values_list('target', flat=True)
    pipeline = Pipeline([
         ('vector', CountVectorizer(tokenizer=jieba_tokenize, lowercase=False)),
         ('transform', TfidfTransformer()),
         ('bayes', MultinomialNB())
    ])

    pipeline.fit(x, y)

    return pipeline
