% Facts
parent(john, mary).
parent(mary, susan).
parent(john, mike).
parent(mike, tom).

% Rules
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
