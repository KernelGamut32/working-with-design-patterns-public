# Lab 11 - Flyweight Pattern

## Overview

In this lab, students will explore and implement the Flyweight design pattern through a Node.js application that simulates planting and drawing a large number of trees in a “forest.” By the end of this exercise, students should understand how splitting intrinsic (shared) and extrinsic (unique) state helps reduce memory usage when many similar objects exist.

---

## Learning Objectives

1. Understand the Flyweight pattern

- Distinguish between intrinsic (shared) and extrinsic (unique) state.
- See how a factory (`TreeFactory`) can manage and reuse shared instances (`TreeType`).

2. Set up and run the provided Node.js application

- Inspect the project structure and key files.
- Execute the demo and observe console output.

3. Analyze Flyweight benefits

- Count total `Tree` instances vs. total `TreeType` flyweights.
- Reason through memory savings when scaling up object creation.

4. Extend and modify the code

- Add a new tree species.
- Change planting logic (e.g., number of trees, coordinate ranges).
- Verify that flyweights are being reused properly.

5. Reflect on use cases

- Identify scenarios in real-world software (e.g., GUI rendering, game development) where Flyweight is advantageous.
- Discuss trade-offs and potential limitations.

---

## Prerequisites

Before starting this lab, ensure you have:

1. **Node.js (v14+)** and **npm** installed.
2. A code editor (e.g., VS Code, WebStorm, Sublime).
3. Basic familiarity with:
   - JavaScript/Node.js syntax
   - `npm init`, `npm install`
   - Express routing (`express.Router`)
   - ES5/ES6 module exports (`module.exports`, `require`)

---

## Lab Setup

1. Open a terminal, create a new directory for the lab, and initialize the Node project:

```bash
mkdir flyweight-demo
cd flyweight-demo
```

2. Initialize a new `package.json`:

```bash
npm init -y
```

---

## Repository Structure

Place all files under a single directory called `flyweight-demo/`:

```text
flyweight-demo/
├── package.json
└── src
    ├── treeType.js
    ├── treeFactory.js
    ├── tree.js
    ├── forest.js
    └── index.js
```

---

## Examine the Code

src/treeType.js

```javascript
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
```

src/treeFactory.js

```javascript
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
```

src/tree.js

```javascript
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
```

src/forest.js

```javascript
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
```

src/index.js

```javascript
const Forest = require('./forest');

/**
 * Main demonstration:
 * 1. Creates a Forest instance.
 * 2. Plants a large number of trees, reusing TreeType flyweights.
 * 3. Draws all trees (via console.log).
 * 4. Prints statistics to illustrate Flyweight usage.
 */
function main() {
  const forest = new Forest();

  // Define some tree species (intrinsic properties)
  const speciesData = [
    { name: 'Oak', color: 'Green', texture: 'OakTexture.png' },
    { name: 'Pine', color: 'DarkGreen', texture: 'PineTexture.png' },
    { name: 'Cherry Blossom', color: 'Pink', texture: 'CherryTexture.png' },
  ];

  // Plant 1,000 trees total
  const totalTreesToPlant = 1000;
  for (let i = 0; i < totalTreesToPlant; i++) {
    // Randomly pick one species
    const { name, color, texture } =
      speciesData[Math.floor(Math.random() * speciesData.length)];

    // Generate random coordinates (0–999)
    const x = Math.floor(Math.random() * 1000);
    const y = Math.floor(Math.random() * 1000);

    forest.plantTree(x, y, name, color, texture);
  }

  // Draw all trees (simulated)
  console.log('--- Drawing all trees in the forest ---');
  forest.draw();

  // Output statistics
  console.log('----------------------------------------');
  console.log(`Total trees planted: ${forest.getTreeCount()}`);
  console.log(`Total unique tree types: ${forest.getTreeTypeCount()}`);
  console.log(
    `Memory savings: instead of ${forest.getTreeCount()} distinct types, only ${forest.getTreeTypeCount()} shared flyweights were created.\n`
  );
}

// Run the demo
main();
```

To test/execute, run `npm start`.

---

## Discussion Questions

- Why are there only 3 unique `TreeType` instances even though 1,000 `Tree` objects were planted?
- What part of the code ensures reuse of the same `TreeType`?
- Which data is stored on each `Tree` instance, and which data is shared?
