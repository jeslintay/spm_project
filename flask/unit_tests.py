import unittest

from roles import Listing, Applicants, Staff, Staff_Skill
from login import Accesscontrol

class TestListing(unittest.TestCase):
    def test_to_dict(self):
        l1 = Listing(role_name='Junior Engineer', role_descr='not senior engineer', skills_required='coding', role_deadline='2024-12-31')

        self.assertEqual(l1.to_dict(), {
            'role_name': 'Junior Engineer',
            'role_descr': 'not senior engineer',
            'skills_required': 'coding',
            'role_deadline': '2024-12-31'
            }
        )

    
class TestApplicants(unittest.TestCase):
    def test_to_dict(self):
        a1 = Applicants(
            app_ID=1,
            Staff_ID=1,
            Staff_FName='John',
            Staff_LName='Doe',
            role_name='Junior Engineer'
        )
        
        self.assertEqual(a1.to_dict(),  
            {
            'app_ID': 1,
            'Staff_ID': 1,
            'Staff_FName': 'John',
            'Staff_LName': 'Doe',
            'role_name': 'Junior Engineer'
            }
        )


class TestStaff(unittest.TestCase):
    def test_to_dict(self):
        s1 = Staff(
            Staff_ID=130002 ,
            Staff_FName='John',
            Staff_LName='Doe',
            Dept='IT',
            Country='Singapore',
            Email='john@doe.com',
            Access_Right=1)
        
        self.assertEqual(s1.json(),  
            {
            'Staff_ID': 130002,
            'Staff_FName': 'John',
            'Staff_LName': 'Doe',
            'Dept': 'IT',
            'Country': 'Singapore',
            'Email': 'john@doe.com',
            'Access_Right': 1
            }
        )

class TestStaff_Skill(unittest.TestCase):
    def test_to_dict(self):
        sk1 = Staff_Skill(
            Staff_ID=130002,
            Skill_Name='Python',
        )
        
        self.assertEqual(sk1.json(),  
            {
            'Staff_ID': 130002,
            'Skill_Name': 'Python'
            }
        )

class TestAccesscontrol(unittest.TestCase):
    def test_to_dict(self):
        a1 = Accesscontrol(
            Access_ID=99,
            Access_Control_Name='Tester'
        )
        
        self.assertEqual(a1.json(),  
            {
            'Access_ID': 99,
            'Access_Control_Name': 'Tester'
            }
        )

if __name__ == '__main__':  
    unittest.main()
    