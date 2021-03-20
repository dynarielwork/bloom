from django.forms import ModelForm

from apps.store.models import Product, ProductImage

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'image', 'title', 'description', 'price', 'num_available', 'key_features']

