# school_helper

## Django application

You can register as a student or a teacher. Teachers have staff status and CRUD permissions for Lesson, Exam, Question and Answer models. To add an exam, questions and answers teachers have to do so through the admin panel. Each user can create Notes, where they can write down whatever they wish.

#### How to create exams

First you add an Exam and write a name you see fit. Then from the next 2 dropdown menus, you choose a subject to which the exam will be attached and from the Teacher dropdown menu you find your username and select it. Then in the next for fields you select the percentage(as integer) of correct answers for each grade(using the bulgarian grading scale - 2 being the worst and 6 the best). Then you save the exam and go to add Question. In the text field you write the question, from the exam dropdown menu, you choose the exam to which to attach the question. In the table at the bottom you write the answers from which the students should choose and select ONLY ONE correct answer.

***The exams logic depends on the teachers being responsible with their actions.***  

**I will update that in the future but currently the deadline on the project has come.**

## Frontend part - React

Frontend part is not finished, so the project currently runs solely on the backend django server.
