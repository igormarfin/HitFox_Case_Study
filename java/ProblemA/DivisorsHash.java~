//package mypackage;
//package com.mypackage;

import java.util.*;
import java.lang.*;
//import org.apache.commons.lang.ArrayUtils;


public class DivisorsHash {
// TODO

    private int _key;
    //    private Arrays divisors;
    private int [] divisors;

    public DivisorsHash(int key){
        _key = key   ;

    }

    public void setKey(int key){

        _key=key;

    }

    public int getKey() {

        return _key;

    }

    public static int[] convertIntegers(ArrayList<Integer> integers)
{
    int[] ret = new int[integers.size()];
    Iterator<Integer> iterator = integers.iterator();
    for (int i = 0; i < ret.length; i++)
    {
        ret[i] = iterator.next().intValue();
    }
    return ret;
}

    public int [] findDivisors(){


        ArrayList<Integer> _divisors = new ArrayList<Integer>();

        int keysqrt = (int) Math.sqrt(Math.abs(_key));

        for(int i =1; i <= keysqrt; i++){

            if (_key%i == 0) {
            _divisors.add(i);
            if (i>1 && i<_key/i) {
                _divisors.add(_key/i);
            }
            }
        }
        //        divisors = _divisors.toArray( new int[ _divisors.size() ] );
        //divisors = ArrayUtils.toPrimitive(_divisors.toArray(new Integer[0]));

        divisors= convertIntegers(_divisors);

        Arrays.sort(divisors);
        return divisors;

    }


    @Override
        public String toString() {



            String str = Integer.toString(_key);
            str+=" ==> [ ";
            for (int i=0; i<divisors.length; i++){
                        str+= String.valueOf(new Integer(divisors[i])) + ",";
            }

            str=str.substring(0, str.length()-1);
            str+="] ";
            return str;

   }



///Testing

public static void main(String[] args) 
{

    int key=10;
    DivisorsHash DH = new DivisorsHash(key);
    DH.findDivisors();
    System.out.println(DH );
}
}