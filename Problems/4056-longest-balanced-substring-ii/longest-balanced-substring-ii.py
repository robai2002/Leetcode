class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ab,bc,ca = 0,0,0
        mp = dict()
        mab = dict()
        mbc = dict()
        mca = dict()
        mp [(0,0,0)] =0
        mab[0],mbc[0],mca[0] = 0,0,0
        ans = 0
        la,lb,lc = -1,-1,-1
        cna,cnb,cnc=0,0,0
    
        for ind,ch in enumerate(s,start=1):
            if ch =='a':
                ab += 1
                ca -= 1  
                la = ind
                cnb,cnc=0,0
                cna +=1
            elif ch =='b':
                ab -= 1
                bc += 1
                lb = ind
                cna,cnc=0,0
                cnb+=1
            else:
                ca += 1
                bc -= 1
                lc = ind
                cna,cnb=0,0
                cnc += 1
            if (ab,bc,ca) in mp:ans = max(ans,ind-mp[(ab,bc,ca)])
            if ab in mab and mab[ab]>=lc: ans = max(ans,ind-mab[ab])
            if bc in mbc and mbc[bc]>=la: ans = max(ans,ind-mbc[bc])
            if ca in mca and mca[ca]>=lb:ans = max(ans,ind-mca[ca])
            # if bc in mbc:print(mbc[bc],end = " ")
           # print(bc,la)
                
            if (ab,bc,ca) not in mp: mp[(ab,bc,ca)] = ind
            if ab not in mab or mab[ab]<lc:mab[ab]=ind
            if bc not in mbc or mbc[bc]<la:mbc[bc]=ind
            if ca not in mca or mca[ca]<lb:mca[ca]=ind
            ans = max(ans,cna)
            ans = max(ans,cnb)
            ans = max(ans,cnc)
            #print(ab,bc,ca)
                
            
            
        return ans
            
        