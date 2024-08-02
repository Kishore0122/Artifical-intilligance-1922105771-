person('John Doe', date(1990, 5, 20)).
person('Jane Smith', date(1985, 8, 15)).
person('Alice Johnson', date(1992, 12, 5)).
person('Bob Brown', date(1980, 3, 10)).


birthdate(Name, Date) :- person(Name, Date).


name_by_birthdate(Date, Name) :- person(Name, Date).

% Example Queries:
% ?- birthdate('John Doe', Date).
% ?- name_by_birthdate(date(1990, 5, 20), Name).
