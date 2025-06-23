from rest_framework import serializers
from .models import Contact, Author, Book


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["id", "name", "email", "phone_number", "address"]
        # fields = "__all__"
        extra_kwargs = {
            "name": {
                "min_length": 3,
                # "max_length": 10,
                "error_messages": {
                    "min_length": "Name should be minimum 3 characters long",
                    # "max_length": "Name cannot be more than 10 character",
                },
            },
            # "address":{"required":False}
        }


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        # fields = ["id", "name"]
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all()
    )  # Dropdown for authors

    class Meta:
        model = Book
        # fields = ["id", "name"]
        fields = ["id", "title", "author"]
