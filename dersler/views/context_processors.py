from ..models import KategoriModel

def categories(request):
    return {
        "categories": KategoriModel.objects.all()
    }