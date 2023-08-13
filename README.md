# RDI
API for a document
processing service. Users can upload images and PDF files to the API,
and the API will perform some operations on the files and return the
results.

Create a Django project and a REST API using Django Rest Framework
(DRF).
The API should have the following endpoints:
`POST /api/upload/`: Accepts image and PDF files in base64
○
format and saves them to the server.
`GET /api/images/`: Returns a list of all uploaded images.
○
`GET /api/pdfs/`: Returns a list of all uploaded PDFs.
○
`GET /api/images/{id}/`: Returns the details of a specific image,
○
like the location, width, height, number of channels.
`GET /api/pdfs/{id}/`: Returns the details of a specific PDF, like
○
the location, number of pages, page width, page height.
`DELETE /api/images/{id}/`: Deletes a specific image.
○
`DELETE /api/pdfs/{id}/`: Deletes a specific PDF.
○
`POST /api/rotate/`: Accepts an image ID and rotation angle,
○
rotates the image, and returns the rotated image.
`POST /api/convert-pdf-to-image/`: Accepts a PDF ID, converts
○
the PDF to an image, and returns the image.
Implement the necessary models, serializers, views, and URLs to handle
the API endpoints.
The image and PDF files should be saved in a directory on the server,
and the file paths should be stored in the database.
Implement proper error handling and validation for the API endpoints.
Dockerize the Django project
