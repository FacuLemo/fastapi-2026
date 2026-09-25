
from .articulos import ArticuloPublic, Articulo
from .proveedor import ProveedorPublic, Proveedor

#Articulo Anidado
class ArticuloNested(ArticuloPublic):
    proveedor: Proveedor | None = None


class ProveedorNested(ProveedorPublic):
    articulos: list[Articulo] = []
