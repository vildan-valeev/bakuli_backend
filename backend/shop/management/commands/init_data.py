from django.core.management.base import BaseCommand

from shop.models import Store, Category, Item, Ingredient

stores = [
    {
        'title': 'Standort Hüblerstraße',
        'city': 'Dresden',
        'street': 'Hüblerstraße',
        'house_number': 2,
        'index': 1309,
    },
    {
        'title': 'Standort Altmarktgalerie',
        'city': 'Dresden',
        'street': 'Webergasse',
        'house_number': 1,
        'index': 1067,
    }
]

menu = [
    {
        'title': 'Fruchtiges Müsli',
        'category': 'Süße Bowls',
        'ingredients': [
            {
                'title': 'Bircher Müsli'
            },
            {
                'title': 'Banane'
            },
            {
                'title': 'Erdbeeren',
            },
            {
                'title': 'Orange'
            },
            {
                'title': 'Weintrauben',
            },
            {
                'title': 'Amaranth',
            },
            {
                'title': 'Pistazien',
            }
        ],
        'price': 6.90,
        'published': True,
        'additional': False
    },
    {
        'title': 'Beerenstarke Auszeit',
        'category': 'Süße Bowls',
        'ingredients': [
            {
                'title': 'Vollkorn-Haferflocken'
            },
            {
                'title': 'Mandelmilch'
            },
            {
                'title': 'Waldbeeren',
            },
            {
                'title': 'Ahornsirup'
            },
            {
                'title': 'Acaipulver',
            },
        ],
        'price': 5.90,
        'published': True,
        'additional': False
    },
    {
        'title': 'Italienische Pause',
        'category': 'Herzhafte Bowls',
        'ingredients': [
            {
                'title': 'Fussili integrale'
            },
            {
                'title': 'Cherrytomaten'
            },
            {
                'title': 'Zucchini',
            },
            {
                'title': 'Spitzpaprika'
            },
            {
                'title': 'Pesto à la Genovese',
            },
            {
                'title': 'Italienischer Hartkäse',
            },
            {
                'title': 'Cashewkerne',
            }
        ],
        'price': 7.90,
        'published': True,
        'additional': False
    },
    {
        'title': 'Asiatisches Allerlei',
        'category': 'Herzhafte Bowls',
        'ingredients': [
            {
                'title': 'Quinoa'
            },
            {
                'title': 'Gelbe-Linsen Bällchen'
            },
            {
                'title': 'Streifen von Rotkohl und Karotte',
            },
            {
                'title': 'Ingwer'
            },
            {
                'title': 'Zuckerschoten',
            },
            {
                'title': 'Geröstete Erdnüsse'
            },
            {
                'title': 'Koriander',
            },
            {
                'title': 'Glasierte Zwiebeln'
            },
            {
                'title': 'Himbeeren',
            },
        ],
        'price': 8.90,
        'published': True,
        'additional': False
    },
    {
        'title': 'Gegrilltes Tohuwabohu',
        'category': 'Herzhafte Bowls',
        'ingredients': [
            {
                'title': 'Grillgemüse Zucchini'
            },
            {
                'title': 'Aubergine und rote Paprika'
            },
            {
                'title': 'Bulgur mit Kreuzkümmel',
            },
            {
                'title': 'Pulled chicken',
            },
            {
                'title': 'Joghurtdressing mit Minze',
            },

        ],
        'price': 8.60,
        'published': True,
        'additional': False
    },
    {
        'title': 'Farbenfrohes Durcheinander',
        'category': 'Herzhafte Bowls',
        'ingredients': [
            {
                'title': 'Geflügelbällchen'
            },
            {
                'title': 'Green Power balls'
            },
            {
                'title': 'Kartoffelstampf',
            },
            {
                'title': 'Karotte',
            },
            {
                'title': 'Mais',
            },
            {
                'title': 'Brokkoli',
            },
            {
                'title': 'Blumenkohl',
            }

        ],
        'price': 8.90,
        'published': True,
        'additional': False
    },
    {
        'title': 'Drei Käse Hoch',
        'category': 'Herzhafte Bowls',
        'ingredients': [
            {
                'title': 'Gouda Würfel'
            },
            {
                'title': 'Mozzarella Bällchen'
            },
            {
                'title': 'Feta',
            },
            {
                'title': 'Caramelle Tricolore Rocota Spinachi',
            },
            {
                'title': 'Weintrauben rot und weiß',
            },
            {
                'title': 'Spicy Manila Feigensenf',
            },
        ],
        'price': 9.10,
        'published': True,
        'additional': False
    },
    {
        'title': 'Buntes Huhn',
        'category': 'Herzhafte Bowls',
        'ingredients': [
            {
                'title': 'Langkornreis'
            },
            {
                'title': 'Hähnchenbrust in Erdnusssoße marinierte Karottenstreifen'
            },
            {
                'title': 'Avocado',
            },
            {
                'title': 'Kichererbsen',
            },
            {
                'title': 'Paprika',
            },
        ],
        'price': 9.10,
        'published': True,
        'additional': False
    },
    {
        'title': 'Orientalisches Kuddelmuddel',
        'category': 'Herzhafte Bowls',
        'ingredients': [
            {
                'title': 'Tabulé'
            },
            {
                'title': 'Datteln'
            },
            {
                'title': 'Rosinen',
            },
            {
                'title': 'Kibbelinge',
            },
            {
                'title': 'Mango',
            },
            {
                'title': 'Gelbe Linsenbällchen',
            },
            {
                'title': 'Mango Sauce',
            }
        ],
        'price': 8.50,
        'published': True,
        'additional': False
    },
    {
        'title': 'M(a)isterhafte Pastrami',
        'category': 'Herzhafte Bowls',
        'ingredients': [
            {
                'title': 'Süßkartoffel'
            },
            {
                'title': 'Pastrami'
            },
            {
                'title': 'Krautsalat',
            },
            {
                'title': 'Mais',
            },
            {
                'title': 'Frenchdressing mit körnigem Dijonsenf',
            },

        ],
        'price': 11.20,
        'published': True,
        'additional': False
    },
    {
        'title': 'Roter Fisch',
        'category': 'Herzhafte Bowls',
        'ingredients': [
            {
                'title': 'Rote Beete-Tabule'
            },
            {
                'title': 'Geräucherter Heilbutt'
            },
            {
                'title': 'roter & schwarzer Kaviar',
            },
            {
                'title': 'Wiberg Karibik',
            },
            {
                'title': 'Edamame',
            },
            {
                'title': 'Paprika gelb & rot',
            },
            {
                'title': 'Karottenstreifen',
            },
            {
                'title': 'Zucchini gegrillt',
            }

        ],
        'price': 11.90,
        'published': True,
        'additional': False
    },
    {
        'title': 'Elsa Erdbeer',
        'category': 'Snacks',
        'ingredients': None,
        'price': 5.95,
        'published': True,
        'additional': False
    },
    {
        'title': 'Emma Erdnuss',
        'category': 'Snacks',
        'ingredients': None,
        'price': 6.95,
        'published': True,
        'additional': False
    },
    {
        'title': 'Hugo Haselnuss',
        'category': 'Snacks',
        'ingredients': None,
        'price': 6.95,
        'published': True,
        'additional': False
    },
    {
        'title': 'Conny Cashew',
        'category': 'Snacks',
        'ingredients': None,
        'price': 6.95,
        'published': True,
        'additional': False
    },
    {
        'title': 'Keo Tee',
        'category': 'Getränke',
        'ingredients': [
            {
                'title': 'Verschiedene Sorten'
            },
        ],
        'price': 2.40,
        'published': True,
        'additional': False
    },
    {
        'title': 'Ingwer Shots (Bio)',
        'category': 'Getränke',
        'ingredients': [
            {
                'title': 'Ingwer-Limette'
            },
            {
                'title': 'Ingwer-Kurkuma'
            },
            {
                'title': 'Ingwer-Beere'
            }
        ],
        'price': 2.50,
        'published': True,
        'additional': False
    },
    {
        'title': 'djahé Limo',
        'category': 'Getränke',
        'ingredients': [
            {
                'title': 'Ingwer-Zitrone'
            },
            {
                'title': 'Ingwer-Rhabarber'
            },
            {
                'title': 'Ingwer-Maracuja'
            }
        ],
        'price': 2.95,
        'published': True,
        'additional': False
    },
    {
        'title': 'djahé Eistee',
        'category': 'Getränke',
        'ingredients': [
            {
                'title': 'Green Jasmine'
            },
            {
                'title': 'Black Ginger'
            },
            {
                'title': 'Sparkling Matcha'
            }
        ],
        'price': 2.75,
        'published': True,
        'additional': False
    },
    {
        'title': 'Latte Macchiato',
        'category': 'Kaffee',
        'ingredients': None,
        'price': 3.00,
        'published': True,
        'additional': False
    },
    {
        'title': 'Café Latte',
        'category': 'Kaffee',
        'ingredients': None,
        'price': 2.90,
        'published': True,
        'additional': False
    },
    {
        'title': 'Cappuccino',
        'category': 'Kaffee',
        'ingredients': None,
        'price': 2.80,
        'published': True,
        'additional': False
    },
    {
        'title': 'Café Crema',
        'category': 'Kaffee',
        'ingredients': None,
        'price': 1.90,
        'published': True,
        'additional': False
    },
    {
        'title': 'Espresso Macchiato',
        'category': 'Kaffee',
        'ingredients': None,
        'price': 2.30,
        'published': True,
        'additional': False
    },
    {
        'title': 'Espresso',
        'category': 'Kaffee',
        'ingredients': None,
        'price': 1.90,
        'published': True,
        'additional': False
    },
    {
        'title': 'Limon',
        'category': 'Getränke',
        'ingredients': None,
        'price': 1.0,
        'published': True,
        'additional': True
    },
    {
        'title': 'Milk',
        'category': 'Kaffee',
        'ingredients': None,
        'price': 1.0,
        'published': True,
        'additional': True
    },
    {
        'title': 'Sugar',
        'category': 'Kaffee',
        'ingredients': None,
        'price': 1.0,
        'published': True,
        'additional': True
    },
]


class Command(BaseCommand):
    help = 'init default data for testing'

    def init_data(self, stores=None, menu=None):
        for s in stores:
            store, status = Store.objects.get_or_create(
                title=s['title'],
                city=s['city'],
                street=s['street'],
                house_number=s['house_number'],
                index=s['index'],

            )

            for i in menu:
                category, created = Category.objects.get_or_create(name=i['category'])
                item, created = Item.objects.get_or_create(
                    title=i['title'],
                    price=i['price'],
                    published=i['published'],
                    additional=i['additional'],
                )
                item.category.add(category)
                item.store.add(store)
                if i['ingredients'] is None:
                    continue
                for ing in i['ingredients']:
                    ingred, created = Ingredient.objects.get_or_create(title=ing['title'])
                    item.ingredients.add(ingred)

    def handle(self, *args, **options):
        return self.init_data(stores=stores, menu=menu)
