# class 학생:
#     def __init__(self, name, koeran, math, english, science):
#         self.name = name
#         self.koeran = koeran
#         self.math = math
#         self.english = english        
#         self.science = science
#     def 총점(self):
#         return self.koeran + self.math + self.english + self.science
#     def 평균(self):
#         return self.총점() / 4
#     def 출력(self):
#         print(self.name, self.총점(), self.평균(), sep="\t")
# # 학생 리스트를 선언합니다.
# students = [
#     학생("윤인성", 87, 98, 88, 95),
#     학생("연하진", 92, 98, 96, 98),
#     학생("구지연", 76, 96, 94, 90),
#     학생("나선주", 98, 92, 96, 92),
#     학생("윤아린", 95, 98, 98, 98),
#     학생("윤명월", 64, 88, 92, 92)
# ]
# # 학생을 한 명씩 반복합니다.
# print("이름", "총점", "평균", sep="\t")
# for student in students:
#     student.출력()

# class Student:
#     def __str__(self):
#         return "문자열"
#     def __init__(self, 이름, 나이):
#         print("객체가 생성되었습니다.")
#         self.이름 = 이름
#         self.나이 = 나이
#     def __del__(self):
#         print("객체가 소멸되었습니다.")
#     def 출력(self):
#         print(self.이름, self.나이)   
        
# student = Student("김용재", 19)
# student.출력()
# print(str(student))

# 클래스를 선업합니다.
# class Student:
#     #생략
#     def __eq__(self, value):
#         if not isinstance(value, Student):
#             raise TypeError("student 클래스의 인스턴스만 비교할 수 있습니다")
#         return self.get_sum() == value.get_sum()
#     #생략
    
# student_a = Student("윤인성", 87, 98, 88, 95)

# student_a == 10

