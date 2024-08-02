% Prolog Database for Fruit Colors

% Facts
color(apple, red).
color(banana, yellow).
color(grape, purple).
color(orange, orange).
color(kiwi, brown).

% Rule to find the color of a fruit
find_color(Fruit, Color) :-
    color(Fruit, Color).

% Query examples:
% ?- find_color(apple, Color).
% Color = red.

% ?- find_color(banana, Color).
% Color = yellow.
