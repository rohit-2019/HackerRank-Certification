class Comparator {
    boolean compare(int a,int b){
        if (a==b){
            return true;
        }else{
            return false;
        }
    }

     boolean compare(String a,String b){
        if (a.equals(b)){
            return true;
        }else{
            return false;
        }
    }

     boolean compare(int[] a,int[] b){
        if (a.length==b.length && Arrays.equals(a, b)){
            return true;
        }else{
            return false;
        }
    }
}
