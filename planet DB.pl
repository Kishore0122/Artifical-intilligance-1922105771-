% Prolog Database with Planets

% Facts
planet('Mercury', 'Terrestrial', 57.9, 0).
planet('Venus', 'Terrestrial', 108.2, 0).
planet('Earth', 'Terrestrial', 149.6, 1).
planet('Mars', 'Terrestrial', 227.9, 2).
planet('Jupiter', 'Gas Giant', 778.3, 79).
planet('Saturn', 'Gas Giant', 1427.0, 83).
planet('Uranus', 'Ice Giant', 2871.0, 27).
planet('Neptune', 'Ice Giant', 4497.1, 14).

% Rules
% Find the type of a planet
planet_type(Name, Type) :- planet(Name, Type, _, _).

% Find the distance of a planet from the Sun
planet_distance(Name, Distance) :- planet(Name, _, Distance, _).

% Find the number of moons of a planet
planet_moons(Name, Moons) :- planet(Name, _, _, Moons).

% Find planets by type
planets_by_type(Type, Planets) :-
    findall(Name, planet(Name, Type, _, _), Planets).

% Find planets by distance range from the Sun
planets_by_distance(MinDistance, MaxDistance, Planets) :-
    findall(Name, (planet(Name, _, Distance, _), Distance >= MinDistance, Distance =< MaxDistance), Planets).

% Query examples:
% ?- planet_type('Earth', Type).
% Type = 'Terrestrial'.

% ?- planet_distance('Jupiter', Distance).
% Distance = 778.3.

% ?- planet_moons('Mars', Moons).
% Moons = 2.

% ?- planets_by_type('Gas Giant', Planets).
% Planets = ['Jupiter', 'Saturn'].

% ?- planets_by_distance(100, 300, Planets).
% Planets = ['Venus', 'Earth', 'Mars'].
