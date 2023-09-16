class student:
  def __init__(self,name,roll_number,cgpa):
    self.name=name
    self.roll_number=roll_number
    self.cgpa=cgpa
  def sort_students(student_list):
    sorted_students=sorted(student_list,key=lambda student:student.cgpa,reverse=true)
    return sorted_students
#example usage with different students:
students[students("emma","101",3.9),students("oliver","102",3.8),students("sophia","103",4.0),students("liam","104",3.7)]
sorted_students=sort_students(students)
#print the sorted students
for student in sorted_students:
  print(f"name:{student.name},roll number{student.roll_number},cgpa:{student.cgpa}")


