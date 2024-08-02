% Define parent relationships
parent(john, mary).
parent(john, mike).
parent(susan, mary).
parent(susan, mike).
parent(mary, jake).
parent(paul, jake).
parent(mike, kate).
parent(mike, tom).
parent(anna, kate).
parent(anna, tom).

father(F, C) :- parent(F, C), male(F).
mother(M, C) :- parent(M, C), female(M).


% Define gender
male(john).
male(mike).
male(paul).
male(jake).
male(tom).

female(susan).
female(mary).
female(anna).
female(kate).



% Query examples:
% ?- father('John', Child).
% Child = 'Mary' ;
% Child = 'James'.

% ?- mother('Susan', Child).
% Child = 'Mary' ;
% Child = 'James'.