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
