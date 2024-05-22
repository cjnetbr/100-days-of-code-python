'''
Instructions
Você tem acesso a um banco de dados de pontuações de alunos no formato de um dicionário. 
As chaves em student_scores são os nomes dos alunos e os valores são as notas dos exames.


Escreva um programa que converta suas pontuações em notas. Ao final do seu programa, 
você deverá ter um novo dicionário chamado student_grades que deverá conter os nomes 
dos alunos para as chaves e suas notas para os valores.

A versão final do dicionário student_grades será verificada..

DO NOT modify lines 1-7 to change the existing student_scores dictionary.

DO NOT write any print statements.

This is the scoring criteria:

Scores 91 - 100: Grade = "Outstanding"

Scores 81 - 90: Grade = "Exceeds Expectations"

Scores 71 - 80: Grade = "Acceptable"

Scores 70 or lower: Grade = "Fail"

Expected Output
'{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'
Dica
Lembre-se de que percorrer um dicionário fornecerá apenas as chaves e não os valores.

Em caso de dúvida sobre por que seu código não está fazendo o que você esperava, você 
sempre pode imprimir os valores intermediários.

Ao final do seu programa, a instrução print mostrará o dicionário student_scores final, 
não altere isso.

'''

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

# STEP-1: Create an empty dictionary called student_grades.
student_grades = {}

# STEP-2: Write your code below to add the grades to student_grades.
