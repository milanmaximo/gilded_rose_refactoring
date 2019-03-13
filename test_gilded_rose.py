# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # items
    def test_name(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_sell_in(self):
        items = [Item("foo", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)

    def test_quality(self):
        items = [Item("foo", 5, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)

    # conditions
    def test_date_passed(self):
        items = [Item("foo", 0, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(3, items[0].quality)

    def test_positive_quality(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_brie_increase(self):
        items = [Item("Aged Brie", 3, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)

    def test_max_quality(self):
        items = [Item("Aged Brie", 3, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 3, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)
        self.assertEqual(items[-1].sell_in, items[0].sell_in)

    def test_backstage(self):
        days_left = [0, 20, 10, 5]
        for i in range(0, len(days_left)):
            items = [Item("Backstage passes to a TAFKAL80ETC concert", days_left[i], 10)]
            gilded_rose = GildedRose(items)
            gilded_rose.update_quality()
            if i == 0:
                self.assertEqual(0, items[0].quality)
            else:
                self.assertEqual(10 + i, items[0].quality)

    # conjured items
    def test_conjured(self):
        days_left = [0, 0, 10]
        quality = [10, 0, 10]
        expected_quality = [6, 0, 8]
        for i in range(0, len(days_left)):
            items = [Item("Conjured mana cake", days_left[i], quality[i])]
            gilded_rose = GildedRose(items)
            gilded_rose.update_quality()
            self.assertEqual(expected_quality[i], items[0].quality)


if __name__ == '__main__':
    unittest.main()
