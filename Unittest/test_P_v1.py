import unittest
from Windows_Back_End.add_data_for_ii_v4 import *
from Windows_Back_End.add_norm_znach_v2 import *
from Windows_Back_End.add_patient_v4 import *
from Windows_Back_End.home_v12 import *


class MyTestCase(unittest.TestCase):

    def setUp(self):

       
        # self.NormDB_ = NormDB(ID='1', cd1='1', cd2='1', cd3='1', scd1='1', scd2='1', scd3='1', h='1', c='1')
    #     self.AddPatient_ = AddPatient(
    #         ID='1',
    #         f='Петров',
    #         i='Григорий',
    #         o='Тимофеевич',
    #         snils='000-000-111 46',
    #         address='Курск Вокзал',
    #         data_b='01.01.1900',
    #         diagnoz='не выявлено'
    # )

        self.Long_GG_ = Long_GG(
            edf_file=r'C:\Users\nero1\PycharmProjects\diplom\Data\EDF\123e.edf',
            index_znach='1',
            sig_1='11250',
            sig_2='13500'
        )

    # def test_test_NormDB_(self):
    #
    #     self.assertEqual(self.NormDB_.ID, '1')
    #     self.assertEqual(self.NormDB_.cD1, '1')
    #     self.assertEqual(self.NormDB_.cD2, '1')
    #     self.assertEqual(self.NormDB_.cD3, '1')
    #     self.assertEqual(self.NormDB_.ScD1, '1')
    #     self.assertEqual(self.NormDB_.ScD2, '1')
    #     self.assertEqual(self.NormDB_.ScD3, '1')
    #     self.assertEqual(self.NormDB_.H, '1')
    #     self.assertEqual(self.NormDB_.C, '1')

    # def test_AddPatient_(self):
    #     self.assertEqual(self.AddPatient_.ID, '1')
    #     self.assertEqual(self.AddPatient_.f, 'Петров')
    #     self.assertEqual(self.AddPatient_.i, 'Григорий')
    #     self.assertEqual(self.AddPatient_.o, 'Тимофеевич')
    #     self.assertEqual(self.AddPatient_.snils, '000-000-111 46')
    #     self.assertEqual(self.AddPatient_.address, 'Курск Вокзал')
    #     self.assertEqual(self.AddPatient_.data_b, '01.01.1900')
    #     self.assertEqual(self.AddPatient_.diagnoz, 'не выявлено')

    def test_Long_GG_(self):
        self.assertEqual(self.Long_GG_.edf_file, r'C:\Users\nero1\PycharmProjects\diplom\Data\EDF\123e.edf')
        self.assertEqual(self.Long_GG_.index_znach, '1')
        self.assertEqual(self.Long_GG_.sig_1, '11250')
        self.assertEqual(self.Long_GG_.sig_2, '13500')


if __name__ == '__main__':
    unittest.main()



