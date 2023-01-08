
region_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


def function (region_list):
    zweite_liste = []
    finale_liste=[]
    for i in range(len(region_list)):
        laengeZahlAußen = len(region_list)-1
        laengeZahlInnen = len(region_list[i])-1
        zweite_liste = []
        for k in range (len(region_list[i])):
            zaehlvariable = 0
            if k!=0:
                zaehlvariable += region_list[i][k-1]
            if k!=(len(region_list[i])-1):
                zaehlvariable += region_list[i][k+1]
            if i<laengeZahlAußen:
                zaehlvariable += region_list[i+1][k]
            if i!=laengeZahlAußen and k!=laengeZahlInnen:
                zaehlvariable += region_list[i+1][k+1]
            if i!=laengeZahlAußen and k!=0:
                zaehlvariable += region_list[i+1][k-1]
            if i!=0:
                zaehlvariable += region_list[i-1][k]
            if i!=0 and k!=laengeZahlInnen:
                zaehlvariable += region_list[i-1][k+1]
            if i!=0 and k!=0:
                zaehlvariable += region_list[i-1][k-1]
            zweite_liste.append(zaehlvariable)
        finale_liste.append(zweite_liste)
    return finale_liste




for liste in function(region_list):
        print(liste)
        """for item in liste:
            print(item)"""

        





"""
in der gleichen Ebene +1
in der zweiten Ebene 0,1
"""