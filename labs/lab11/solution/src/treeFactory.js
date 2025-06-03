const TreeType = require('./treeType');

/**
 * TreeFactory: a Flyweight factory. Manages shared TreeType instances.
 */
class TreeFactory {
  constructor() {
    // Map key: `${name}_${color}_${texture}` → TreeType instance
    this.treeTypes = new Map();
  }

  /**
   * getTreeType(name, color, texture):
   * Returns an existing TreeType (flyweight) or creates a new one if needed.
   */
  getTreeType(name, color, texture) {
    const key = `${name}_${color}_${texture}`;
    if (!this.treeTypes.has(key)) {
      const newType = new TreeType(name, color, texture);
      this.treeTypes.set(key, newType);
    }
    return this.treeTypes.get(key);
  }

  /**
   * getTotalTreeTypes():
   * Returns the count of unique TreeType flyweights created.
   */
  getTotalTreeTypes() {
    return this.treeTypes.size;
  }
}

module.exports = new TreeFactory();
