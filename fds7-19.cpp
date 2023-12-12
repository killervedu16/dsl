#include <iostream>
#include <string>

using namespace std;


struct StudentNode {
    int prn;
    string name;
    StudentNode* next;
};


class StudentClub {
private:
    StudentNode* head;

public:
    
    StudentClub() : head(nullptr) {}

    
    void addMember(int prn, const string& name) {
        StudentNode* newNode = new StudentNode{prn, name, nullptr};

       
        if (!head) {
            head = newNode;
        } else {
           
            StudentNode* current = head;
            while (current->next) {
                current = current->next;
            }
            current->next = newNode;
        }
    }

    
    void deleteMember(int prn) {
        if (!head) {
            cout << "Club is empty. No members to delete." << endl;
            return;
        }

        
        if (head->prn == prn) {
            StudentNode* temp = head;
            head = head->next;
            delete temp;
            cout << "President removed from the club." << endl;
            return;
        }

        
        StudentNode* current = head;
        while (current->next && current->next->prn != prn) {
            current = current->next;
        }

        if (current->next) {
            StudentNode* temp = current->next;
            current->next = current->next->next;
            delete temp;
            cout << "Member with PRN " << prn << " removed from the club." << endl;
        } else {
            cout << "Member with PRN " << prn << " not found in the club." << endl;
        }
    }

    
    int getTotalMembers() {
        int count = 0;
        StudentNode* current = head;
        while (current) {
            count++;
            current = current->next;
        }
        return count;
    }

   
    void displayMembers() {
        if (!head) {
            cout << "Club is empty. No members to display." << endl;
            return;
        }

        cout << "Club Members:" << endl;
        StudentNode* current = head;
        while (current) {
            cout << "PRN: " << current->prn << ", Name: " << current->name << endl;
            current = current->next;
        }
    }

    
    void concatenateLists(StudentClub& otherList) {
        if (!otherList.head) {
            cout << "The second list is empty. Nothing to concatenate." << endl;
            return;
        }

        if (!head) {
            head = otherList.head;
            otherList.head = nullptr;
            cout << "Lists concatenated successfully." << endl;
            return;
        }

        StudentNode* current = head;
        while (current->next) {
            current = current->next;
        }

        current->next = otherList.head;
        otherList.head = nullptr;

        cout << "Lists concatenated successfully." << endl;
    }
};

int main() {
   
    StudentClub division1, division2;

    
    division1.addMember(1001, "John");
    division1.addMember(1002, "Jane");
    division1.addMember(1003, "Bob");

   
    division2.addMember(2001, "Alice");
    division2.addMember(2002, "Charlie");

   
    cout << "Division 1:" << endl;
    division1.displayMembers();

    
    cout << "\nDivision 2:" << endl;
    division2.displayMembers();

    
    division1.concatenateLists(division2);

   
    cout << "\nAfter Concatenation:" << endl;
    division1.displayMembers();

    return 0;
}

