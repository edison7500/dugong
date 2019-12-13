import shutil
import tempfile
from datetime import datetime, timedelta

import jieba
import pandas as pd
from django.conf import settings
from django.core.management.base import BaseCommand
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

from apps.blog.models import Post, get_stop_words

idf_path = getattr(settings, "IDF_PATH", None)


def jieba_token(value):
    return jieba.cut(value, cut_all=False)


class Command(BaseCommand):
    help = "gen article tfidf file"
    docs = list()

    # def add_arguments(self, parser):
    #     parser.add_argument("-d", "--delta", type=int, help="cal", default=30)

    def handle(self, *args, **options):
        # days = options["delta"]
        for row in Post.objects.filter(status=Post.publish):
            self.docs.append(row.process_content())

        count_vect = CountVectorizer(tokenizer=jieba_token, min_df=1, stop_words=get_stop_words())
        tfidf_transformer = TfidfTransformer(smooth_idf=True, use_idf=True)
        x_counts = count_vect.fit_transform(self.docs)
        tfidf_transformer.fit_transform(x_counts)
        df = pd.DataFrame(tfidf_transformer.idf_, index=count_vect.get_feature_names(), columns=["idf_weights"])
        fp = tempfile.NamedTemporaryFile()
        for row in df.sort_values("idf_weights", ascending=False).itertuples():
            _ = "%s %.9f\n" % (row[0], row[1])
            fp.write(bytes(_.encode("utf-8")))
        shutil.copy(src=fp.name, dst=idf_path)
        fp.close()

