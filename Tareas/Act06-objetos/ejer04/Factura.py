class Factura (object):

    def __init__(self, base_imponible, iva, descuento):
        self.base_imponible = base_imponible
        self.iva = iva
        self.descuento = descuento

    def base_con_descuento(self):
        return self.base_imponible -  self.descuento

    def total_iva_incluido(self):
        return self.base_imponible - self.descuento + self.iva