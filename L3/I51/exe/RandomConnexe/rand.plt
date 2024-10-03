set title "essai"
set term png
set output "../../sorties/rand.png"
plot '../../entrees/rand.dat' w l, 0.5*x*log(x) w l
