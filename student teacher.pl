
teaches('Mr. Smith', 'Math101').
teaches('Ms. Johnson', 'Eng202').
teaches('Dr. Brown', 'Sci303').

studies('Alice', 'Math101').
studies('Bob', 'Eng202').
studies('Charlie', 'Sci303').
studies('David', 'Math101').
studies('Eve', 'Sci303').

teacher_of(Student, SubjectCode, Teacher) :-
    studies(Student, SubjectCode),
    teaches(Teacher, SubjectCode).

% Find the students taught by a particular teacher
students_of_teacher(Teacher, Students) :-
    findall(Student, (teaches(Teacher, SubjectCode), studies(Student, SubjectCode)), Students).


% Query examples:
% ?- teacher_of('Alice', 'Math101', Teacher).
% Teacher = 'Mr. Smith'.



% Query examples:
% ?- students_of_teacher('Mr. Smith', Students).
% Students = ['Alice', 'David'].

% ?- students_of_teacher('Dr. Brown', Students).
% Students = ['Charlie', 'Eve'].
