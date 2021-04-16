# import Java a convertir en python

/ *
int[]
tab = {0, 1, 2, 3, 4, 5};
int
n = 5;
int
e = 0;
for (int i=0;i < n;i++){
if (tab[i] == e){
System.out.println("OK - i = "+i+" - tab = "+tab[i]);
} else {
System.out.println("NO - i = "+i);
}
e++;
}
* /

/ *
int[]
tab = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
int
i = 1;
int
e = 0;

while (i < tab.length - 1){
while (e < i - 1){
System.out.println("e = "+e+" - i = "+i+" - tabe/i = "+tab[i]+" - tab/e = "+tab[e]);
if (tab[i] == tab[e]){
System.out.println("OK - i = "+i+" - tab dans i = "+tab[i]+" - tab dans e = "+tab[e]);
} else {
System.out.println("NO - i = null");
}
e++;
}
i + +;
}
* /

/ *
int[]
tab1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
int[]
tab2 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
int
i = 0;
while (i < tab1.length - 1 & & i < tab2.length - 1){
if (tab1[i] == i & & tab2[i] == i){
System.out.println("OK - i = "+i+" - tab1 = "+tab1[i]+" - tab2 = "+tab2[i]);
} else {
System.out.println("NO - i = "+i);
}
i++;
} * /