//Start with this Map setup:

//Map<String, String> contacts = {
  //"Alice": "9876543210",
  //"Bob": "8765432109",
  //"Charlie": "7654321098"
//};

//String searchName = "Bob";

//Your task is to look up if searchName exists in the phonebook.

//The Condition:
   //If the name exists in the map, print: "Bob's number is 8765432109"
   //If the name doesn't exist (e.g., if searchName = "Rahul"), print: "Contact not found".

void main() {
  Map<String, String?> contacts = {
    "Alice": "9876543210",
    "Bob": "8765432109",
    "Charlie": "7654321098"
  };
  
  String searchName = "roy"; 
  
  if (contacts.containsKey(searchName)) {
    String? searchNumber = contacts[searchName];
    print("$searchName's number is $searchNumber");
  }
  else {
    print("Contact not found");
  }

}