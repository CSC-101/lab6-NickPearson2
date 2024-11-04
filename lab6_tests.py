import data
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_selection_sort_books1(self):
        book1 = data.Book(["JK Rowling","Jake Notan"],"Happy Times")
        book2 = data.Book(["JK Rowling", "Jake Notan"], "Percy Jackson")
        book3 = data.Book(["JK Rowling", "Jake Notan"], "Happy Guy")
        book4 = data.Book(["JK Rowling", "Jake Notan"], "Always Good")
        list = [book1, book2, book3, book4]
        sorted_list = [book4,book3,book1,book2]
        self.assertEqual(list, list)
        lab6.selection_sort_books(list)
        self.assertEqual(list, sorted_list)
    def test_selection_sort_books_empty(self):
        book1 = data.Book(["JK Rowling","Jake Notan"],"Happy Times")
        book2 = data.Book(["JK Rowling", "Jake Notan"], "Percy Jackson")
        book3 = data.Book(["JK Rowling", "Jake Notan"], "Happy Guy")
        book4 = data.Book(["JK Rowling", "Jake Notan"], "Always Good")
        list = []
        sorted_list = []
        self.assertEqual(list, list)
        lab6.selection_sort_books(list)
        self.assertEqual(list, sorted_list)
    # Part 2
    def test_swap_case(self):
        string = "HeLLo"
        result = "hEllO"
        self.assertEqual(lab6.swap_case(string), result)
    def test_swap_case_none(self):
        string = ""
        result = ""
        self.assertEqual(lab6.swap_case(string), result)
    # Part 3
    def test_str_translate(self):
        string = "Mississippi"
        result = "Missississi"
        self.assertEqual(lab6.str_translate(string,"p","s"), result)
    def test_str_translate_2(self):
        string = "abcdcba"
        result = "xbcdcbx"
        self.assertEqual(lab6.str_translate(string,"a","x"), result)
    # Part 4
    def test_histogram1(self):
        string = "hello wow hi hello hi and one and on and"
        dictionary = {"hello":2,"wow":1,"hi":2,"and":3,"one":1,"on":1}
        self.assertEqual(lab6.histogram(string), dictionary)
    def test_histogram2(self):
        string = "Today we went to the park and we played tag"
        dictionary = {"Today":1, "we":2,"went":1,"to":1,"the":1,"park":1,"and":1,"played":1,"tag":1}
        self.assertEqual(lab6.histogram(string), dictionary)




if __name__ == '__main__':
    unittest.main()
