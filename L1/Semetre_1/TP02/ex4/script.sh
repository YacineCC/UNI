#DATE=`date +"%Y%m%d"`
DATE=$1

cheminLOG=archive/${DATE}/log
cheminERR=archive/${DATE}/err
mkdir archive/${DATE}
mkdir archive/${DATE}/log
mkdir archive/${DATE}/err
cp /home/perso/paiement/O12_TP/exercice_4/nontraite/${DATE}*.log ${cheminLOG}
cp /home/perso/paiement/O12_TP/exercice_4/nontraite/${DATE}*.err ${cheminERR}
