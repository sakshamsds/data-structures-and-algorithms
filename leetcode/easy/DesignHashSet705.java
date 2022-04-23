package easy;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;

// https://www.youtube.com/watch?v=NrMaQL_4Npo
// https://leetcode.com/problems/design-hashset/
// 705. Design HashSet

public class DesignHashSet705 {
    public static void main(String[] args) {

        Set<Integer> set = new HashSet<>();
        set.contains(72);
        System.out.println(set.contains(72));
        System.out.println(set.remove(91));
        System.out.println(set.add(48));
        System.out.println(set.add(41));
        System.out.println(set.contains(96));
        System.out.println(set.remove(87));
        System.out.println(set.contains(48));
        // System.out.println(set.toString());
    }
}

class MyHashSet {
    // input -> hashcode(input) -> bucket
    // private final int MAX_VALUE = 1000000;

    // bucket size
    final int BUCKET_SIZE = 1000;
    List<List<Integer>> parentList;
    int num = 0;

    public MyHashSet() {
        parentList = new ArrayList<>(BUCKET_SIZE);
        for (int i = 0; i < BUCKET_SIZE; i++) {
            parentList.add(null);
        }
        print("constructor", -1, new LinkedList<>(), -1);
    }

    public void add(int key) {
        int bucket = key % BUCKET_SIZE;
        List<Integer> childList = parentList.get(bucket);
        if (childList == null) {
            List<Integer> list = new LinkedList<>();
            list.add(key);
            parentList.add(bucket, list);
        } else if (!childList.contains(key)) {
            childList.add(key);
        }
        print("add", key, childList, bucket);
    }

    public void remove(int key) {
        int bucket = key % BUCKET_SIZE;
        List<Integer> childList = parentList.get(bucket);
        if (childList != null) {
            childList.remove(Integer.valueOf(key));
        }
        print("remove", key, childList, bucket);
    }

    public boolean contains(int key) {
        int bucket = key % BUCKET_SIZE;
        List<Integer> childList = parentList.get(bucket);
        print("contains", key, childList, bucket);
        return childList != null && childList.contains(key);
    }

    private void print(String method, int key, List<Integer> childList, int bucket) {
        num++;
        if (childList != null) {
            System.out.println(
                    "iteration: " + num + "\tkey: " + key + "\tbucket: " + bucket + "\t" + childList.toString() + "\t" + method);
        } else {
            System.out.println(
                    "iteration: " + num + "\tkey: " + key + "\tbucket: " + bucket + "\t" + "childList is null" + "\t" + method);
        }
    }
}
