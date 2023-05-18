// # Exercise 8: Widgets and Gizmos
// # (15 Lines)
// # An online retailer sells two products: widgets and gizmos. Each widget weighs 75
// # grams. Each gizmo weighs 112 grams. Write a program that reads the number of
// # widgets and the number of gizmos from the user. Then your program should compute
// # and display the total weight of the parts.

function widgets_and_gizmos(num_widgets, num_gizmos) {
    const widgets_weight = 75;
    const gizmo_weight = 112;
  
    const total_weight = (num_widgets * widgets_weight) + (num_gizmos * gizmo_weight);
  
    return total_weight;
  }
  
  console.log(widgets_and_gizmos(1, 2));
  