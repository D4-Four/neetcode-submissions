// Singly Linked List Node
class ListNode {
    public:
        int val;
        ListNode* next;
    
        // Constructor that sets 'next' to nullptr by default
        ListNode(int val) : val(val), next(nullptr) {}
    
        // Constructor that accepts both value and next node
        ListNode(int val, ListNode* next) : val(val), next(next) {}
};

class LinkedList {
private:
    ListNode* head;
    ListNode* tail;
public:
    LinkedList(){
        head = new ListNode(-1);
        tail = head;
    }

    int get(int index) {
        int i = 0;
        ListNode* curr = head->next;
        while(curr){
            if(i == index){
                return curr->val;
            }
            i++;
            curr = curr->next;
        }
        return -1;
    }

    void insertHead(int val) {
        ListNode* newnode = new ListNode(val);
        newnode->next = head->next;
        head->next = newnode;
        if (newnode->next == nullptr) {  // If list was empty before insertion
           tail = newnode;
        }
    }
    
    void insertTail(int val) {
        ListNode* lastnode = new ListNode(val);
        tail->next = lastnode;
        tail = tail->next;
    }

bool remove(int index) {
        int i = 0;
        ListNode* curr = head;
        while (i < index && curr != nullptr) {
            i++;
            curr = curr->next;
        }

        // Remove the node ahead of curr
        if (curr != nullptr && curr->next != nullptr) {
            if (curr->next == tail) {
                tail = curr;
            }
            ListNode* toDelete = curr->next;
            curr->next = curr->next->next;
            delete toDelete;
            return true;
        }
        return false;
    }

    // Method to get values of the linked list
    vector<int> getValues() {
        vector<int> res;
        ListNode* curr = head->next;
        while (curr != nullptr) {
            res.push_back(curr->val);
            curr = curr->next;
        }
        return res;
    }
};