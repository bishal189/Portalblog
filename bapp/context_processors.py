
from .models import Category
def get_category(request):
    category=Category.objects.all()
    return dict(category=category)
