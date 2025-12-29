function romanToInt(s: string): number {
  const values: number[] = [];

  for (const char of s) {
    switch (char) {
      case "I":
        values.push(1);
        break;
      case "V":
        values.push(5);
        break;
      case "X":
        values.push(10);
        break;
      case "L":
        values.push(50);
        break;
      case "C":
        values.push(100);
        break;
      case "D":
        values.push(500);
        break;
      case "M":
        values.push(1000);
        break;
    }
  }

  let total = 0;
  for (let i = 0; i < values.length; i++) {
    if (i < values.length - 1 && values[i] < values[i + 1]) {
      total -= values[i];
    } else {
      total += values[i];
    }
  }

  return total;
}
