from rest_framework import serializers
from .models import ImageModel, PdfModel
from drf_extra_fields.fields import Base64ImageField, Base64FileField
import io
import PIL
from PIL import Image
import PyPDF2
import logging


# for allowed pdf file only in this field
class PDFBase64File(Base64FileField):
    ALLOWED_TYPES = ['pdf']

    def get_file_extension(self, filename, decoded_file):
        try:
            PyPDF2.PdfFileReader(io.BytesIO(decoded_file))
        except PyPDF2.utils.PdfReadError as e:
            logging.warning(e)
        else:
            return 'pdf'


class ImageModelSerilizer(serializers.ModelSerializer):
    image = Base64ImageField(required=True)

    class Meta:
        model = ImageModel
        fields = ["id", "title", "content", "image"]


class PdfModelSerilizer(serializers.ModelSerializer):
    pdf = PDFBase64File(required=True)

    class Meta:
        model = PdfModel
        fields = ["id", "title", "content", "pdf"]
