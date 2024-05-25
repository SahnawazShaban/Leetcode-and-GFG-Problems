public class HashTable {
    private HashTable[] buckets;
    private int noOfBucket;
    private int size;

    public HashTable(){
        size = 10;
    }
    public HashTable(int capacity){
        this.buckets = new HashTable[noOfBucket];
        this.noOfBucket = capacity;
        this.size = 0;
    }

    public class HashNode{
        private Integer key;
        private String value;
        private HashTable next;

        public HashNode(Integer key,String value){
            this.key = key;
            this.value = value;
        }
    }

    public int size(){
        return size;
    }
    public boolean isEmpty(){
        return size == 0;
    }
    public void put(int key,String value){

    }
    public int get(int key){
        return key;
    }
    public int remove(int key){
        return key;
    }
}
