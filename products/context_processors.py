from .models import Category, Brand
from django.conf import settings

def categories_processor(request):
    """
    Supplies all root categories, brands, and Google Maps API key globally to templates.
    """
    root_categories = Category.objects.filter(parent_category__isnull=True).prefetch_related('subcategories')
    brands = Brand.objects.all().order_by('name')
    return {
        'global_categories': root_categories,
        'global_brands': brands,
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
