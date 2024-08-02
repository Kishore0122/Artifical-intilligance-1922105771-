% Prolog implementation of the Monkey and Banana problem

% Initial state: state(MonkeyPosition, BoxPosition, BananaPosition)
initial_state(state(on_floor, at_door, at_middle)).

% Goal state: Monkey is on the box and Banana is reachable
goal_state(state(on_box, _, at_middle)).

% Move actions
move(state(on_floor, at_door, at_middle), state(on_floor, at_middle, at_middle)).
move(state(on_floor, at_middle, at_middle), state(on_box, at_middle, at_middle)).
move(state(on_box, at_middle, at_middle), state(on_box, at_middle, at_middle)).

% Solve the problem
solve(S) :- initial_state(S), goal_state(G), move(S, G).
