from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",Hello_world, name ="sample"), 
    path("students/", Student_form, name = "students"),
    path("students_list/", student_listing,name = "students_list"),
    path("edit_student/<int:id>", students_edit, name="edit_stu"),
    path("delete_stud/<int:id>",deleteview, name = "delete")

]

if settings.DEBUG:
    # print("^^^^^^^^^^",settings.MEDIA_URL)
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )