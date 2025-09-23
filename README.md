
````
# 📝 Django Forms – Complete Reference
````

## 📁 `__pycache__`
- Python compiles `.py` files to `.pyc` bytecode for **faster execution**.
- These compiled files are stored inside the `__pycache__` folder.
- ✅ Safe to delete. Python will recreate it on next run (only first request will be slightly slower).

---

## 📝 Django Forms
Forms handle:
1. **Input rendering** (HTML form fields)
2. **Validation**
3. **Saving data** (if using `ModelForm`)

---

## ⚡ Forms Creation (`forms.py`)
Create a form inside `app/forms.py`.

### 1️⃣ Using `forms.Form`
For **custom** forms not tied to a database model:
```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
````

* Manual save is required:

```python
if form.is_valid():
    Contact.objects.create(**form.cleaned_data)
```

### 2️⃣ Using `forms.ModelForm`

For forms **linked to a model** (recommended for CRUD):

```python
from django import forms
from .models import Students

class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'email', 'age', 'img']
```

✅ Fields and validation are auto-generated from the model.

---

## 🔄 `forms.Form` vs `forms.ModelForm`

| Feature          | `forms.Form`       | `forms.ModelForm`                    |
| ---------------- | ------------------ | ------------------------------------ |
| Model connection | ❌ No               | ✅ Yes                                |
| Auto save        | ❌ Must call model  | ✅ `form.save()`                      |
| Validation       | Manual/field based | Model constraints + extra validators |

---

## ✅ Validation & Save from `views.py`

Example **Create** view:

```python
from django.shortcuts import render, redirect
from .forms import StudentsForm

def student_create(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()            # saves directly to DB
            return redirect('students_list')
    else:
        form = StudentsForm()      # blank form
    return render(request, 'home.html', {'form': form})
```

* `request.POST` → text data
* `request.FILES` → uploaded files/images

---

## ✏️ Update Using `instance`

Editing an existing record:

```python
from django.shortcuts import get_object_or_404

def student_edit(request, id):
    student = get_object_or_404(Students, pk=id)
    if request.method == 'POST':
        form = StudentsForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()   # updates instead of creating new
            return redirect('students_list')
    else:
        form = StudentsForm(instance=student)   # pre-fill existing data
    return render(request, 'edit_form.html', {'form': form})
```

* `instance` ensures `save()` updates the **same row**.

---

## 🎨 Template Rendering of Form Data

Example template:

```html
<form method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}  <!-- renders each field wrapped in <p> tags -->
    <button type="submit">Submit</button>
</form>
```

Rendering options:

* `{{ form.as_p }}` → `<p>` tags
* `{{ form.as_table }}` → `<tr>` rows
* `{{ form.as_ul }}` → `<li>` items

⚡ Always include:

* **Submit button** to trigger POST
* **CSRF token** for security
* `enctype="multipart/form-data"` when uploading files

---

## 🖼️ Image Rendering

### Model

```python
class Students(models.Model):
    img = models.FileField(upload_to="Students_app/Photos", default="sad.jpg")
```

### Template

```html
<img src="{{ student.img.url }}" alt="Student Photo">
```

* Use `{{ img.url }}` to access the uploaded file path.

---

## ⚙️ MEDIA\_URL and MEDIA\_ROOT

In `settings.py`:

```python
import os
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

* `MEDIA_ROOT` → physical folder where uploaded files are stored.
* `MEDIA_URL`  → URL prefix to serve those files.

In `urls.py` (development):

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 🧩 Form Object in `views.py`

Always create a form object:

* **GET** → empty or prefilled (for edit)
* **POST** → bind submitted data for validation

```python
form = StudentsForm(request.POST or None, request.FILES or None)
```

---

## 🔒 Custom Validators

Create reusable validation functions:

```python
from django.core.exceptions import ValidationError

def age_validator(value):
    if value < 18:
        raise ValidationError("Age must be at least 18.")

def img_validator(value):
    if value.name == "sad.jpg":
        raise ValidationError("Please upload a different image.")
```

Attach to fields:

```python
class StudentsForm(forms.ModelForm):
    age = forms.IntegerField(validators=[age_validator])
    img = forms.FileField(validators=[img_validator])
    class Meta:
        model = Students
        fields = ['name', 'email', 'age', 'img']
```

Display errors in template:

```html
{{ form.age.errors }}
{{ form.img.errors }}
```

---

## ✅ CRUD Summary

| Operation  | View Function    | Key Logic                          |
| ---------- | ---------------- | ---------------------------------- |
| **Create** | `student_create` | `form.save()`                      |
| **Read**   | `students_list`  | `Students.objects.all()`           |
| **Update** | `student_edit`   | `instance=student` + `form.save()` |
| **Delete** | `student_delete` | `student.delete()`                 |

---

### 🎯 Folder Layout Example

```
students_project/
│
├─ students_app/
│  ├─ forms.py
│  ├─ models.py
│  ├─ views.py
│  ├─ templates/
│  │   ├─ home.html
│  │   ├─ edit_form.html
│  │   └─ students_list.html
│  └─ ...
├─ media/
│   └─ Students_app/Photos/   # uploaded images
└─ manage.py
```

---

## 💡 Key Takeaways

* Use **ModelForm** for quick CRUD with built-in validation.
* Always include `enctype="multipart/form-data"` when handling files.
* `instance` updates existing records; without it, a new row is created.
* Errors can be shown in templates via `{{ form.errors }}` or field-specific errors.

Happy Django Coding! 🚀

```

---

This `README.md` can be committed to your repo to document all the concepts and serve as a quick refresher for future projects.
```
