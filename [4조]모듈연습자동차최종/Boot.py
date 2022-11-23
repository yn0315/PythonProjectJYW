def boot(braeaka=0,geara=0,speeda=0,boota=0):
    try:
        if boota == 0:
            if braeaka != 0 and geara == 0 and speeda == 0:
                return 2
            else:
                return 1
        elif boota ==1:
            if braeaka == 0 and geara == 0 and speeda == 0:
                return 2
            else:
                return 0
        elif boota ==2:
            if braeaka !=0 and geara == 0 and speeda ==0:
                return 0
            else:
                return 2
    except:
        pass

