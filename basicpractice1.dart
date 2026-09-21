//Start with this list of numbers: [120, 45, 90, 150, 30, 200, 75]

//Create a new empty list to hold the filtered results.

//Use a loop to go through the prices.

//Filter condition: If a price is less than 100, add it to your new list.

//Print out the final filtered list.

void main() {
   List<int> list = [120, 45, 90, 150, 30, 200, 75];
   List<int> newlist = [];
  
   for (var num in list) {
    if (num < 100) {
      newlist.add(num);
    }
   }
  
  print(newlist);
}

