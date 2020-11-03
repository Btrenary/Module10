import unittest
from class_definitions import Student as t


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = t.Student('Trenary', 'Brady', 'CompSci', 4.0)

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.first_name, 'Brady')
        self.assertEqual(self.student.last_name, 'Trenary')
        self.assertEqual(self.student.major, 'CompSci')
        self.assertEqual(self.student.gpa, 4.0)

    def test_object_created_all_attributes(self):
        student = t.Student('Trenary', 'Brady', 'CompSci', 4.0)
        assert student.last_name == 'Trenary'
        assert student.first_name == 'Brady'
        assert student.major == 'CompSci'
        assert student.gpa == 4.0

    def test_student_str(self):
        self.assertEqual(str(self.student), "Trenary, Brady has major CompSci with gpa: 4.0")

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            stu = t.Student('Tren154ary', 'Brady', 'CompSci', 4.0)

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            stu = t.Student('Trenary', 'Br1865ady', 'CompSci', 4.0)

    def test_object_not_created_error_major(self):
        self.assertEqual(True, False)

    def test_object_not_created_error_gpa(self):
        self.assertEqual()


if __name__ == '__main__':
    unittest.main()
