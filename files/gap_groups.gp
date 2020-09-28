ShowMulTable := function(g)
local e, n, M, i, j, ind;
e := Elements(g);
n :=Order(g);

M :=MultiplicationTable(g);

for i in [1..n] do
   for j in [1..n] do
      ind := M[i][j];
      Print(e[ind], "   ");
   od;
   Print("\n");
od;
Print("\n");
end;
