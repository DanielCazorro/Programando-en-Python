// # Exercise 3: Area of a Room
// # Write a program that asks the user to enter the width and length of a room. Once these values have been read, your program should compute and display the area of the room. The length and the width will be entered as floating-point numbers. Include units in your prompt and output message; either feet or meters, depending on which
// # unit you are more comfortable working with.

function area_of_a_room() {
    /*
    Asks for room dimensions and outputs area
    */
    let width = parseFloat(prompt("Ancho: "));
    let length = parseFloat(prompt("Alto: "));
  
    let area = width * length;
  
    console.log(`Su habitación de ${width.toFixed(2)} metros de ancho y ${length.toFixed(2)} metros de alto tiene un área de: ${area.toFixed(2)} metros cuadrados`);
  }
  
  area_of_a_room();
  