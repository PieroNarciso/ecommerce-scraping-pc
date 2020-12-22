import argparse
from argparse import Namespace

from ecommerce.spiders import ecommerce_spider as spiders


class Parser(object):
    description = "This program is to query and parse data from web e-commerce"
    parser = argparse.ArgumentParser(
            prog="E-commerce Parser",
            description=description
        )
    def __init__(self):
        self.get_parser()

    def get_parser(self) -> None:
        self.parser.add_argument("--query", "-Q", nargs="+", required=True)
        self.parser.add_argument("--store", "-S", required=True,
                help="(impacto, sercoplus, compuvision, cyccomputer, all)"
            )

    def get_args(self) -> Namespace:
        args: Namespace = self.parser.parse_args()
        return args

    def get_store(self, args: Namespace=None, arg: str=None):
        store_map = {
                "sercoplus": spiders.SercoplusSpider,
                "impacto": spiders.ImpactoSpider,
                "compuvision": spiders.CompuvisionSpider,
                "cyccomputer": spiders.CyCComputerSpider
            }
        if args:
            if args.store == "all":
                return store_map.values()
            STORE: str = args.store
            return [store_map[STORE]]
        elif arg:
            return [store_map[arg]]
        else:
            raise ValueError("No argument was provided")

