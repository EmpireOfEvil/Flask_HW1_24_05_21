class Merch:
    def __init__(self, name, price, sourcepic = None):
        self.name = name
        self.price = price
        self.sourcepic = sourcepic

warehouse = {'shoes':[Merch('Туфелька', 2000, 'tufelka.jpg'),
                      Merch('Скуфелька', 1500, 'skufelka.jpg'),
                      ],
             'shirts':[Merch('Футболка парадная', 1000, 'pivozavr.jpg'),
                       Merch('Футболка нарядная', 1000, 'magic_cat.jpg'),
                       Merch('Футболка прохладная', 1000, 'pivo.jpg'),
                       ],
             'outwear':[Merch('Китель Брежнева с орденами (оригинал)', 100500, 'brezhnev.jpg'),
                        ],
             }