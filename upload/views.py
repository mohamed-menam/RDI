from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import ImageModelSerilizer, PdfModelSerilizer
from . models import ImageModel, PdfModel
# use for rotate image
from PIL import Image
# use for convert pdf to image
from pdf2image import convert_from_path
# use for get width, height, number of channels for image.
import cv2 as cv
# use for pdf
import PyPDF2


# `POST /api/upload/`: Accepts image and PDF files in base64 format and saves them to the server.

@api_view(["POST"])
def upload_image_or_pdf(request):
    if request.method == "POST":
        data = request.data
        serializerimg = ImageModelSerilizer(data=data)
        if serializerimg.is_valid():
            article = serializerimg.save()
            data = serializerimg.data
            return Response(data=data)

        serializerpdf = PdfModelSerilizer(data=data)
        if serializerpdf.is_valid():

            article = serializerpdf.save()
            data = serializerpdf.data
            return Response(data=data)
        return Response(serializerpdf.errors, status=400)


# `GET /api/images/`: Returns a list of all uploaded images.
@api_view(["GET"])
def get_images(request):
    queryset = ImageModel.objects.all()
    serializer = ImageModelSerilizer(
        queryset, many=True, context={'request': request})
    return Response(serializer.data)


# `GET /api/pdfs/`: Returns a list of all uploaded PDFs.
@api_view(["GET"])
def get_pdfs(request):
    queryset = PdfModel.objects.all()
    serializer = PdfModelSerilizer(
        queryset, many=True, context={'request': request})
    return Response(serializer.data)


# `GET /api/images/{id}/`: Returns the details of a specific image
# `DELETE /api/images/{id}/`: Deletes a specific image.
@api_view(['GET', 'DELETE'])
def get_image_or_delete(request, id):
    image = get_object_or_404(ImageModel, pk=id)
    if request.method == 'GET':
        # Returns the details of a specific image
        serializer = ImageModelSerilizer(image)
        x = serializer["image"]
        print("+++++++++++++", serializer["image"], x.value)
        m = str(x.value)

        img = cv.imread("/home/m-menam/RDI/"+m)
        height = img.shape[0]
        width = img.shape[1]
        channels = img.shape[2]

        return Response({"id": serializer.data["id"],
                         "location": serializer.data["image"],
                         "height": height,
                         "width": width,
                         "channels": channels
                         })
#   Deletes a specific image.
    elif request.method == "DELETE":
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# `GET /api/pdfs/{id}/`: Returns the details of a specific PDF
# `DELETE /api/pdfs/{id}/`: Deletes a specific PDF.


@api_view(['GET', 'DELETE'])
def get_pdf_or_delete(request, id):
    pdf = get_object_or_404(PdfModel, pk=id)

    #  Returns the details of a specific PDF
    if request.method == 'GET':
        serializer = PdfModelSerilizer(pdf)
        x = serializer["pdf"]
        print("+++++++++++++", serializer["pdf"], x.value)
        m = str(x.value)
        file = open("/home/m-menam/RDI/"+m, 'rb')
        readpdf = PyPDF2.PdfFileReader(file)
        totalpages = readpdf.numPages
        info = readpdf.getDocumentInfo()
        return Response({
            "title": serializer.data["title"],
            "content": serializer.data["content"],
            "location": serializer.data["pdf"],
            "number of pages": totalpages,
            "info": info

        })
    # Deletes a specific PDF.
    elif request.method == "DELETE":
        pdf.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# POST /api/rotate/`: Accepts an image ID and rotation angle,
# rotates the image, and returns the rotated image


@api_view(["POST"])
def rotate(request):
    data = request.data
    print(data, data["id"])
    queryset = get_object_or_404(ImageModel, pk=data["id"])
    serializer = ImageModelSerilizer(queryset)
    x = serializer["image"]
    print("+++++++++++++", serializer["image"], x.value)
    m = str(x.value)
    colorImage = Image.open("/home/m-menam/RDI/"+m)
    rotated = colorImage.rotate(data["angel"])
    rotated.show()
    return Response(serializer.data)

# `POST /api/convert-pdf-to-image/`: Accepts a PDF ID, converts
# the PDF to an image, and returns the image.


@api_view(["POST"])
def convert_pdf_to_image(request):
    data = request.data
    print(data, data["id"])
    queryset = get_object_or_404(PdfModel, pk=data["id"])
    serializer = PdfModelSerilizer(queryset)
    x = serializer["pdf"]
    print("+++++++++++++", serializer["pdf"], x.value)
    m = str(x.value)
    images = convert_from_path("/home/m-menam/RDI/"+m)

    for i in range(len(images)):

        # Save pages as images in the pdf
        images[i].show()

    return Response(serializer.data)
