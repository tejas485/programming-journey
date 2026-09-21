//You have three variables representing a user's name:
   //String firstName = "Rahul";
   //String? middleName; [This is nullable (currently null)]
   //String lastName = "Sharma";
//Your task is to construct their full name into a single string.

//The Condition:
   //If middleName is null, the full name should just be "Rahul Sharma".
   //If middleName has a value (e.g., "Kumar"), the full name should be "Rahul Kumar Sharma".

//Print the final full name string.

void main(){
  String firstName = "Rahul";
  String? middlename = "Anurag";
  String lastName = "Sharma";
  
  String fullName;
  
  if (middlename == null) {
    fullName = "$firstName $lastName";
  }
  else {
    fullName = "$firstName $middlename $lastName";
  }
  
  print(fullName);
}
