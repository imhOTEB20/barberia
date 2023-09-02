

class Producto():
    def __init__(self, nombre, id_marca, precio_venta, stock):
        self.nombre = nombre
        self.id_marca = id_marca
        self.precio_venta = precio_venta
        self.stock = stock
    
    @classmethod
    def get_producto(cls, id_producto):
        #funcion que trae el producto con el id_especificado de la base de datos
        pass

    @classmethod
    def get_productos(cls):
        #funcion que trae todo los productos de la base de datos
        pass

    @classmethod
    def crear_producto(cls, Producto):
        #funcion que inserta un nuevo producto en la tabla productos de la base de datos.
        pass

    @classmethod
    def editar_producto(cls, id_producto):
        #funcion que edita uno o mas datos de un producto
        pass

    @classmethod
    def eliminar_producto(cls, id_producto):
        #funcion que elimina un producto por su id.
        pass

    @classmethod
    def eliminar_productos(cls):
        #funcion que elimina todos los productos de la tabla productos de la base de datos.
        pass