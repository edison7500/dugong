import jieba
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

# from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline


def jieba_tokenize(text):
    return jieba.lcut(text)


def get_pipeline():
    pipeline = Pipeline(
        [
            ("vector", CountVectorizer(tokenizer=jieba_tokenize, lowercase=False)),
            ("transform", TfidfTransformer()),
            ("bayes", MultinomialNB()),
        ]
    )

    return pipeline
