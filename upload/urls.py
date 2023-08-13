from django.urls import path
from . import views


urlpatterns = [
    path('upload/', views.upload_image_or_pdf),
    path('images/', views.get_images),
    path('pdfs/', views.get_pdfs),
    path('images/<int:id>', views.get_image_or_delete),
    path('pdfs/<int:id>', views.get_pdf_or_delete),
    path('rotate/', views.rotate),
    path('convert-pdf-to-image/', views.convert_pdf_to_image)

]
