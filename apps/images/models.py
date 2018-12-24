from .abstracts import ImageAbstractModel


class Image(ImageAbstractModel):
    class Meta(ImageAbstractModel.Meta):
        db_table = "generic_image"
