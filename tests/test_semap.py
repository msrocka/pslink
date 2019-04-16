import unittest

import pslink.semap as semap


class SemapTest(unittest.TestCase):

    def test_closest_broader(self):
        text = '''
        "cheese"       , "milk and milk based products"^
        "milk"         , "milk and milk based products"^
        "cheese, goat" , "cheese"^
        "cheese, cow"  , "cheese"^
        "milk, cow"    , "milk"^ , "cow milk"=
        '''
        g = semap.parse_text(text)
        self.assertEqual(("cheese", 1, 1),
                         g.closest_broader("cheese, goat", "cheese, cow"))
        self.assertEqual(("cheese", 0, 0),
                         g.closest_broader("cheese", "cheese"))
        self.assertEqual(("cheese", 1, 0),
                         g.closest_broader("cheese, goat", "cheese"))
        self.assertEqual(("cheese", 0, 1),
                         g.closest_broader("cheese", "cheese, cow"))

        self.assertEqual(("milk and milk based products", 2, 2),
                         g.closest_broader("cow milk", "cheese, goat"))

    def test_product_link(self):
        g = semap.read_file('../products.semapl')
        pinfo = semap.ProductInfo()
        pinfo.process_uuid = "a"
        pinfo.process_name = "b"
        pinfo.product_uuid = "c"
        pinfo.product_name = "silicon, electronic grade, at plant"
        pinfo.product_unit = "kg"
        g.link_products([pinfo])


if __name__ == "__main__":
    unittest.main()
