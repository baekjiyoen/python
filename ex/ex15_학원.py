# 학원
# 교실
# 학생 - 이름
# 강사

'''
json
배열 : []
객체 : {}
값이 여러개일때는 ,(콤마)로 구분
숫자는 ""(쌍따옴표)에 넣지 않아도됨
{
    "키" : "값"
    , "강사" : {"이름" : "오미선" ,"과목" : "웹프로그래밍" }
    , "학생" : [
        {"이름" : "김윤상" , "id" :"1"}
        , {"이름" : "김건" , "id" :"2"}
        , {"이름" : "김재현" , "id" :"3"}
        , {"이름" : "박근민" , "id" :"4"}
        , {"이름" : "백지연" , "id" :"5"}
        , {"이름" : "김태형" , "id" :"6"}       
    ]    
}
'''
class Teacher :
    def __init__(self,name,subjcet) -> None :
        # 인스턴스 변수 생성
        self.name = name
        self.subject = subjcet
        
        def __str__(self) -> str :
            return f'teacher(name: {self.name} , subject : {self.subject})' 
        
t = Teacher('오미선','웹프로그래밍')  
print(t)

class Student :
    def __init__(self,name,student_id) -> None :
        self.name = name
        self.student_id = student_id
        
        
    def __str__(self) -> str:
        return f' student(name: {self.name}, student_id : {self.student_id})'

class Academy :
        
    def __init__(self) -> None :
        self.teacher = None
        self.students = []
        
    # 파라메터로 전달된 강사를 인스턴스변수에 설정
    def add_teacher(self, teacher) :
        self.teacher = teacher
        print(f'{teacher.name} 님이 학원에 배정되었습니다')
        
    def add_student(self, student) :
        # 학생 리스트에 요소를 추가
        self.students.append(student)
        print(f'{student.name} 님이 학원에 등록했습니다')
    
    # 교사정보를 문자열로 반환 
    def get_teacher_info(self) :
        if self.teacher : 
            return str(self.teacher)
        else :
            return '교사가 배정되지 않았습니다'
        
    # 학생정보를 문자열로 반환    
    def get_students_info(self) :
       s_str = ''
       for s in self.students :
        s_str += s.__str__() + '\n'
       return s_str
   
    def __str__(self) -> str :
        teacher_info = self.get_teacher_info()
        students_info = self.get_students_info()
        return self.get_teacher_info(self)  + '\n' + self.get_students_info(self)    

    
    # 다른모듈에서 실행할경우 실행되지 않음
    if __name__ == '__main__' :
        t = Teacher('오미선','웹프로그래밍')
        print(t)
        
        s1 = Student('김윤상' ,1)
        s2 = Student('김  건' ,2)
        s3 = Student('김재현' ,3)
        s4 = Student('박근민' ,4)
        s5 = Student('백지연' ,5)
        s6 = Student('김태형' ,6)
        s7 = Student('김주희' ,7)
        students = [s1,s2,s3,s4,s5,s6,s7]
        # print(students)        
        for s in students :
            print(s)
            
        academy = Academy()
        academy.add_teacher(t)
        academy.add_student(s1)
        academy.add_student(s2)
        academy.add_student(s3)
        academy.add_student(s4)
        academy.add_student(s5)
        academy.add_student(s6)
        academy.add_student(s7)
        print(academy.get_students_info())
        print(academy.get_students_info())
        print(academy)    