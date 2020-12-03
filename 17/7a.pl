:- use_module(library(dcg/basics)).
% input parsing grammar
entries([]) --> eos, !.
entries([X|Xs]) --> entry(X), !, entries(Xs), {assert_entry(X)}.
entry(entry(Node, Weight, [])) -->
  nonblanks(Codes), " (", integer(Weight), ")\n", {atom_codes(Node, Codes)}.
entry(entry(Node, Weight, Children)) -->
  nonblanks(Codes), " (", integer(Weight), ") -> ", children(Children), {atom_codes(Node, Codes)}.
  
children([Child]) -->
  nonblanks(Codes), "\n", !, {atom_codes(Child, Codes)}.
children([Child|Children]) -->
  string_without(",", Codes), ", ", children(Children), {atom_codes(Child, Codes)}.
  
assert_entry(entry(Node, Weight, Children)) :-
  assertz(node(Node)),
  assertz(weight(Node, Weight)),
  maplist(assert_child(Node), Children).
assert_child(Node, Child) :-
  assertz(parent(Node, Child)).
% solution
  
start(OutputA, OutputB) :-
  phrase_from_file(entries(_), "advent17/7.txt"),
  solve_a(OutputA),
  solve_b(OutputB).
  
solve_a(Output) :-
  node(Output),
  not(parent(_, Output)).
  
solve_b(Output) :-
  Output = "unknown".