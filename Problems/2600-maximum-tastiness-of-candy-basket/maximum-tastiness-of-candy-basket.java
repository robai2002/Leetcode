import java.util.Arrays;
class Solution {
    public int maximumTastiness(int[] price, int k) {
        int pos = 0,imp =(int)1e9, mid,x;
        Arrays.sort(price);
        while(pos<imp){
           mid = (pos+imp+1)/2;
           if(C(mid,price,k))pos = mid;
           else imp = mid -1;
        }
        return pos;
    }

boolean C(int x,int[] price, int k){
    int last = price[0],count = 1,i=1;
    for(int p: price)
    {
        if(p-last>=x){
            last = p;
            count++;
        }
        if(count ==k)return true;
    }
    return false;
}
}