const Tree = require('./tree');
const treeFactory = require('./treeFactory');

/**
 * Forest: manages a collection of Tree instances.
 */
class Forest {
  constructor() {
    // Array of Tree objects
    this.trees = [];
  }

  /**
   * plantTree(x, y, name, color, texture):
   * - Retrieves/creates a TreeType flyweight from the factory
   * - Creates a new Tree instance with extrinsic coords (x, y) and the shared type
   */
  plantTree(x, y, name, color, texture) {
    const type = treeFactory.getTreeType(name, color, texture);
    const tree = new Tree(x, y, type);
    this.trees.push(tree);
  }

  /**
   * draw():
   * Iterates through all Tree instances and calls draw() on each.
   */
  draw() {
    this.trees.forEach((tree) => tree.draw());
  }

  /**
   * getTreeCount(): returns total number of Tree instances planted.
   */
  getTreeCount() {
    return this.trees.length;
  }

  /**
   * getTreeTypeCount(): returns number of unique TreeType flyweights in use.
   */
  getTreeTypeCount() {
    return treeFactory.getTotalTreeTypes();
  }
}

module.exports = Forest;
