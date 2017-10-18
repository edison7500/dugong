class SEOMixin(object):

    def get_seo_meta(self, obj):
        meta = {
            "title": obj.title,
        }

        return meta