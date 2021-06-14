import os
import unittest
import unittest.mock

# TestCase 를 작성하기 위해 unittest.TestCase를 상속한 테스트 클래스를 작성합니다. 
# test_ 라는 이름으로 시작하는 메소드는 모두 테스트 메소드가 됩니다.
# test_run() 메소드는 단순 실행여부만 판별합니다.
# unittest.main() 코드를 통해 테스트가 수행됩니다.

# class Test_Sample01(unittest.TestCase):
#     def test_sum(self):
#         self.assertTrue(21 == sum([10, 11]))

def custom_function(file_name):
    with open(file_name, 'rt', encoding='utf-8') as f:
        return sum(1 for _ in f)


# TestCase를 작성
class CustomTests(unittest.TestCase):

    def setUp(self):
        """테스트 시작되기 전 파일 작성"""
        self.file_name = 'test_file.txt'
        with open(self.file_name, 'wt', encoding='utf-8') as f:
            f.write("""
            파이썬에는 정말 단위테스트 모듈이 기본으로 포함되어 있나요? 진짜?
            멋지군요!
            단위테스트를 잘 수행해보고 싶습니다!
            """.strip())

    def tearDown(self):
        """테스트 종료 후 파일 삭제 """
        try:
            os.remove(self.file_name)
        except:
            pass

    def test_runs(self):
        """단순 실행여부 판별하는 테스트 메소드"""

        custom_function(self.file_name)

    def test_line_count(self):
        self.assertEqual(custom_function(self.file_name), 3)

    def test_no_file(self):
        with self.assertRaises(IOError):
            custom_function(self.file_name)  

if __name__ == '__main__':
    unittest.main()
    # unittest.mock.Mock() # 나중에 Mock 에 대해서 다시 학습
    # unittest.mock.MagicMock() # 나중에 MagicMock 에 대해서 다시 학습
    # unittest.mock.patch() # # 나중에 patch 에 대해서 다시 학습