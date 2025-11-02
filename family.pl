% Facts
parent(john, mary).
parent(mary, susan).
parent(john, mike).
parent(mike, tom).

% Rules
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

% Queries and Results

% ?- sibling(mary, mike).
% true.

% ?- sibling(X, Y).
% X = mary, Y = mike ;
% X = mike, Y = mary.

% ?- sibling(susan, tom).
% false.

% ?- sibling(mike, mary).
% true.
