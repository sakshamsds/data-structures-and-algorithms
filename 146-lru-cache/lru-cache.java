class Node {
    int key;
    int value;
    Node next;
    Node prev;
    public Node (int key, int value) {
        this.key = key;
        this.value = value;
    }
}

class LRUCache {

    private Node left;
    private Node right;
    private Map<Integer, Node> store;
    private int capacity;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        store = new HashMap<>();
        left = new Node(-1, -1);
        right = new Node(-1, -1);
        left.next = right;
        right.prev = left;
    }
     
    public int get(int key) {
        if (!store.containsKey(key)) {
            return -1;
        }
        Node node = store.get(key);
        remove(node);
        add(node);
        return node.value;

    }
    
    public void put(int key, int value) {
        if (store.containsKey(key)) {
            Node oldNode = store.get(key);
            remove(oldNode);
        }

        Node newNode = new Node(key, value);
        store.put(key, newNode);
        add(newNode);

        if (store.size() > capacity) {
            store.remove(left.next.key);
            remove(left.next);
        }
    }

    // prev -> right
    // prev <- right
    public void add(Node node) {
        Node prevNode = right.prev;
        prevNode.next = node;
        right.prev = node;
        node.next = right;
        node.prev = prevNode;
    }

    public void remove(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */