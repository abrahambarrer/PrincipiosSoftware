from modules.bodega import Bodega
from modules.caja import Caja


def main():
    file = ''
    caja = Caja(file)
    bodega = Bodega(file)

    caja.vender("huevo", 10)
    bodega.reabastecer()

if __name__ == '__main__':
    main()