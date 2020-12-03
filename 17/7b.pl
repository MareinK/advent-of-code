solve_b(Output) :-
  node(Node),
  balanced(Node),
  total_weight(Node, TW),
  correct_weight(Node, CW),
  TW \= CW,
  weight(Node, W),
  Output is W + CW - TW.
balanced(Node) :-
  children(Node, Children),
  maplist(total_weight, Children, ChildWeights),
  maplist(=(_), ChildWeights).
  
children(Node, Children) :-
  findall(Child, parent(Node, Child), Children).
  
total_weight(Node, Weight) :-
  children(Node, Children),
  maplist(total_weight, Children, ChildWeights),
  sumlist(ChildWeights, ChildWeight),
  weight(Node, NodeWeight),
  Weight is ChildWeight + NodeWeight.
correct_weight(Node, CorrectWeight) :-
  parent(Parent, Node),
  children(Parent, Children),
  maplist(total_weight, Children, ChildWeights),
  most_common(ChildWeights, CorrectWeight).
% source: https://stackoverflow.com/a/13674376/2124834
most_common(L, M) :-
  setof(I-E, C^(aggregate(count, member(E, L), C), I is -C), [_-M|_]).