from itertools import product

from bueno.modules.bodega import Bodega
from bueno.modules.caja import Caja

def main():
    file = "/docs/db.csv"
    caja = Caja(file)
    bodega = Bodega(file)

    producto = "oreis"

    caja.vender(producto)

    caja.vender(producto, 5)

if __name__ == '__main__':
    main()