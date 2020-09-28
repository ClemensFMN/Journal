S3:=SymmetricGroup(3);
es:=Elements(S3);

a := es[4];

cgs := List([a]);

for e in es do
    itm := e*a*e^-1;
    Add(cgs, itm);
od;

cgs := Set(cgs);
