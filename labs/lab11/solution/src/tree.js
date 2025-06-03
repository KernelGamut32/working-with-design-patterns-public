/**
 * Tree: represents an individual tree.
 * - x, y: extrinsic (unique) location
 * - type: reference to a shared TreeType (intrinsic state)
 */
class Tree {
  constructor(x, y, type) {
    this.x = x;
    this.y = y;
    this.type = type; // Instance of TreeType
  }

  /**
   * draw(): delegates drawing to the shared TreeType, passing this tree's coordinates.
   */
  draw() {
    this.type.draw(this.x, this.y);
  }
}

module.exports = Tree;
