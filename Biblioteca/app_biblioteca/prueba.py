from models import Libro


def Catalogo(request):

    catalogo = Libro.objects.all()

    print(catalogo)
