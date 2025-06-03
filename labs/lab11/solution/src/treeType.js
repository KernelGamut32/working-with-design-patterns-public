/**
 * The Flyweight class that holds intrinsic (shared) state:
 * - name: species (e.g., "Oak", "Pine")
 * - color: leaf/needle color
 * - texture: simulated texture (e.g., a filename string)
 */
class TreeType {
  constructor(name, color, texture) {
    this.name = name;
    this.color = color;
    this.texture = texture;
  }

  /**
   * draw(x, y):
   * Simulates rendering a tree at coordinates (x, y).
   * In a GUI scenario, this would draw an image; here, we log details.
   */
  draw(x, y) {
    console.log(
      `Drawing a ${this.name} tree at (${x}, ${y}) with color=[${this.color}] and texture=[${this.texture}]`
    );
  }
}

module.exports = TreeType;
