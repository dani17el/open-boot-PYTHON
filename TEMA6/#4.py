

class Categorias:
    idcategoria = 0
    nombre = ""


class Proveedores:
    idproveedores = 0
    nombre = 0


class Productos:
    idproductos = 0
    CategoriaProducto = Categorias()
    Precio = 0
    Tamaño = 0
    TipoDeProducto = 0
    CIFProducto = Proveedores()
    

p = Productos()
p.CIFProducto.nombre
p.CategoriaProducto.idcategoria