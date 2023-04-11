def ResCalc(arn: int, ard: int, minHeight: int, maxHeight: int):
    miPx = minHeight
    maPx = maxHeight
    
    n = miPx
    retpx = []
    while n <= maPx:
        for i in range(miPx, maPx):
            if(i % 2 != 0):
                n += 1
                pass
            elif (i * arn) % ard == 0 and ((i * arn) % ard) / 2 == 0:
                n += 1
                retpx.append([i, int(i*(arn/ard))])
    return retpx

def ResCalc4(arn: int, ard: int, minHeight: int, maxHeight: int):
    miPx = minHeight
    maPx = maxHeight

    n = miPx
    retpx = []
    
    while n <= maPx:
        for i in range(miPx, maPx):
            if(i % 4 != 0):
                n += 1
                pass
            elif (i * arn) % ard == 0 and ((i * arn) % ard) / 4 == 0:
                n += 1
                retpx.append([i, int(i*(arn/ard))])
    return retpx

def ResCalc8(arn: int, ard: int, minHeight: int, maxHeight: int):
    miPx = minHeight
    maPx = maxHeight

    n = miPx
    retpx = []
    while n <= maPx:
        for i in range(miPx, maPx):
            if(i % 8 != 0):
                n += 1
                pass
            elif (i * arn) % ard == 0 and ((i * arn) % ard) / 8 == 0:
                n += 1
                retpx.append([i, int(i*(arn/ard))])
    return retpx

def ResCalc16(arn: int, ard: int, minHeight: int, maxHeight: int):
    miPx = minHeight
    maPx = maxHeight

    n = miPx
    retpx = []
    while n <= maPx:
        for i in range(miPx, maPx):
            if(i % 16 != 0):
                n += 1
                pass
            elif (i * arn) % ard == 0 and ((i * arn) % ard) / 16 == 0:
                n += 1
                retpx.append([i, int(i*(arn/ard))])
    return retpx

def ResCalc32(arn: int, ard: int, minHeight: int, maxHeight: int):
    miPx = minHeight
    maPx = maxHeight

    n = miPx
    retpx = []
    while n <= maPx:
        for i in range(miPx, maPx):
            if(i % 32 != 0):
                n += 1
                pass
            elif (i * arn) % ard == 0 and ((i * arn) % ard) / 32 == 0:
                n += 1
                retpx.append([i, int(i*(arn/ard))])
    return retpx
    
def ResCalc64(arn: int, ard: int, minHeight: int, maxHeight: int):
    miPx = minHeight
    maPx = maxHeight

    n = miPx
    retpx = []
    while n <= maPx:
        for i in range(miPx, maPx):
            if(i % 64 != 0):
                n += 1
                pass
            elif (i * arn) % ard == 0 and ((i * arn) % ard) / 64 == 0:
                n += 1
                retpx.append([i, int(i*(arn/ard))])
    return retpx
    
def ResCalc128(arn: int, ard: int, minHeight: int, maxHeight: int):
    miPx = minHeight
    maPx = maxHeight

    n = miPx
    retpx = []
    while n <= maPx:
        for i in range(miPx, maPx):
            if(i % 128 != 0):
                n += 1
                pass
            elif (i * arn) % ard == 0 and ((i * arn) % ard) / 128 == 0:
                n += 1
                retpx.append([i, int(i*(arn/ard))])
    return retpx
       
def ResCalc256(arn: int, ard: int, minHeight: int, maxHeight: int):
    miPx = minHeight
    maPx = maxHeight

    n = miPx
    retpx = []
    while n <= maPx:
        for i in range(miPx, maPx):
            if(i % 256 != 0):
                n += 1
                pass
            elif (i * arn) % ard == 0 and ((i * arn) % ard) / 256 == 0:
                n += 1
                retpx.append([i, int(i*(arn/ard))])
    return retpx