// # Create a program that reads the length and width of a farmer’s field from the user in
// # feet. Display the area of the field in acres.
// # Hint: There are 43,560 square feet in an acre.

function feet(length, width) {
  let area = length * width;
  let area_acre = area / 43560;

  return area_acre;
}

console.log(feet(50, 50));
