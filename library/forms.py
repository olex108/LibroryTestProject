from django import forms
from .models import Authors, Books, Categories

from django.core.exceptions import ValidationError


def validator_year(value):
    """Validates that the year input is valid."""

    try:
        int(value)
    except ValueError:
        raise ValidationError("Year must be an integer")
    if value >= 2026:
        raise ValidationError("Year must be greater than or equal to 2026")


def validator_name(value):
    """Validates that the name input is valid start with a title letter and contains only letters."""

    if not value.isalpha():
        raise ValidationError("Name must be alphanumeric")
    if not value.istitle():
        raise ValidationError("Name must start with a title letter")


class AuthorsForm(forms.ModelForm):
    class Meta:
        model = Authors
        fields = ["first_name", "lust_name", "mid_name", "birthday", "portrait"]

    def __init__(self, *args, **kwargs):
        super(AuthorsForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "First Name",
        })
        self.fields["mid_name"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Mid Name",
        })
        self.fields["birthday"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Birthday year",
        })
        self.fields["portrait"].widget.attrs.update({
            "class": "form-control",
        })

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        validator_name(first_name)
        return first_name

    def clean_lust_name(self):
        lust_name = self.cleaned_data.get("lust_name")
        validator_name(lust_name)
        return lust_name

    def clean_mid_name(self):
        mid_name = self.cleaned_data.get("mid_name")
        validator_name(mid_name)
        return mid_name

    def clean_birthday(self):
        birthday = self.cleaned_data.get("birthday")
        validator_year(birthday)
        return birthday


class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ["title", "category_pk", "author_pk", "publication_year", "description"]

    def __init__(self, *args, **kwargs):
        super(BooksForm, self).__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Title",
        })
        self.fields["category_pk"].widget.attrs.update({
            "class": "form-control",
        })
        self.fields["author_pk"].widget.attrs.update({
            "class": "form-control",
        })
        self.fields["publication_year"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Publication year",
        })
        self.fields["description"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Description",
        })

    def clean_publication_year(self):
        publication_year = self.cleaned_data.get("publication_year")
        validator_year(publication_year)
        return publication_year


class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ["name", "description"]

    def __init__(self, *args, **kwargs):
        super(CategoriesForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Category name",
        })
        self.fields["description"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "description",
        })