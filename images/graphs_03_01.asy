unitsize(1cm);
size(5cm);

draw((0,0)--(1,0)--(1,1)--(0,1)--cycle);
label("$1$", (0,0), SW);
label("$2$", (1,0), SE);
label("$3$", (1,1), NE);
label("$4$", (0,1), NW);


draw((5,0)--(6,0));
draw((5,0)--(5,1));
label("$1$", (5,0), SW);
label("$2$", (6,0), SE);
label("$4$", (5,1), NW);

