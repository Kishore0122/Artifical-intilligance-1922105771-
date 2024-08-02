% Prolog Database for Diet Suggestions based on Disease

% Facts
% Disease and recommended food
recommended_food(diabetes, 'vegetables').
recommended_food(diabetes, 'whole grains').
recommended_food(diabetes, 'lean protein').
recommended_food(hypertension, 'fruits').
recommended_food(hypertension, 'low-fat dairy').
recommended_food(hypertension, 'whole grains').
recommended_food(cardiovascular_disease, 'fruits').
recommended_food(cardiovascular_disease, 'vegetables').
recommended_food(cardiovascular_disease, 'fish').
recommended_food(obesity, 'fruits').
recommended_food(obesity, 'vegetables').
recommended_food(obesity, 'whole grains').

% Disease and foods to avoid
avoid_food(diabetes, 'sugar').
avoid_food(diabetes, 'refined carbs').
avoid_food(diabetes, 'saturated fat').
avoid_food(hypertension, 'salt').
avoid_food(hypertension, 'processed foods').
avoid_food(cardiovascular_disease, 'trans fats').
avoid_food(cardiovascular_disease, 'red meat').
avoid_food(obesity, 'sugar').
avoid_food(obesity, 'fast food').
avoid_food(obesity, 'processed snacks').

% Rules
% Suggest diet for a specific disease
suggest_diet(Disease, Foods) :-
    findall(Food, recommended_food(Disease, Food), Foods).

% Suggest foods to avoid for a specific disease
suggest_avoid(Disease, Foods) :-
    findall(Food, avoid_food(Disease, Food), Foods).

% Query examples:
% ?- suggest_diet(diabetes, Foods).
% Foods = ['vegetables', 'whole grains', 'lean protein'].

% ?- suggest_avoid(hypertension, Foods).
% Foods = ['salt', 'processed foods'].
