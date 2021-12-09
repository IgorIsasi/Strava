def main():
    if __name__ == '__main__':
        kodifikatu(-179.9832104)
        kodifikatu(38.5)
        kodifikatu(-120.2)
        kodifikatu(40.7)
        kodifikatu(-120.95)
        kodifikatu(43.252)
        kodifikatu(-126.453)       


def kodifikatu(zenb):
        # 2. Birderkatu zenbakia bider 1e5 eta borobildu    
        balioa = round(zenb * 100000)
        
        # Kontuan izan, balio negatibo bat, biren osagarriaren metodoa # erabiliz kalkulatu behar dela. Balio binarioa ezeztuz
        # eta emaitzari bat gehituz.
        if zenb < 0:
            balioa = (1 << 32) + balioa
        else:
            if (balioa & (1 << (32 - 1))) != 0:
                balioa = balioa - (1 << 32)

        balioBitar=f"{balioa:016b}" #balioa bitarrera pasatu

        while len(balioBitar) < 32:
            balioBitar = "0" + balioBitar #balio bitarrari hasierako zeroak gehitu

        # 4. Mugitu bitak 1 ezkerrera
        maskara = 2 ** len(balioBitar) - 1
        balioBitar = format((int(balioBitar,2) << 1) & maskara,"b")

        while len(balioBitar) < 32:
            balioBitar = "0" + balioBitar #balio bitarrari hasierako zeroak gehitu (bitak mugitzean gerta daiteke zeroak desagertzea)
        
        # 5. Jatorrizko balioa negatiboa bada, # balio binario ezeztu:
        if zenb <0:
            balioBitar = format(int(balioBitar,2) ^ 0xFFFFFFFF,"b")

            while len(balioBitar) < 32:
                balioBitar = "0" + balioBitar #balio bitarrari hasierako zeroak gehitu (ezeztatzean desagertu daitezke)

        # 6. Hartu bit-ak bostnaka geratzen den zenbakia > 0x20 den bitartean
        balioBitarAldrebes = balioBitar[::-1] #bitak alderantzizko ordenean gorde chunk-ak beharrezko ordenean gordetzeko (eskuinetik ezkerrera)
        chunks = []
        sartu = True
        for i  in range(0,len(balioBitarAldrebes),5):
            if (int(balioBitarAldrebes[i:i+5]) > 0) | (sartu == True): #hasierako chunk hutsak sartu behar dira, amaierakoak ez (bitak aldrebes daude)
                chunks.append(balioBitarAldrebes[i:i+5])
                if int(balioBitarAldrebes[i:i+5]) > 0: #azkenengo chunk hutsak ez sartzeko
                    sartu = False

        polyline = ""
        for i in range (len(chunks)):
            chunks[i] = chunks[i][::-1] #chunk bakoitzaren biten ordena alderantziz jarri (lehendik alderantziz zeuden, orain orden egokian jarri)
            #print(chunks[i]) #chunk-aren balio bitarra
            chunks[i] = int(chunks[i],2) #chunk-aren balioa hamartarrera pasatu
            if i < len(chunks)-1:
                chunks[i] = chunks[i] | 0x20 #balioari OR 0x20 egin azkenengo chunk-a ez bada
            chunks[i] = int(chunks[i]) + 63 #balioari 63 gehitu
            #print(chunks[i]) #chunk-aren balioa hamartarrean
            polyline = polyline + chr(int(chunks[i])) #chunk-en ASCII balioa string-ean sartu kateatuz
        print(zenb, ": ", polyline)
        return polyline

main()