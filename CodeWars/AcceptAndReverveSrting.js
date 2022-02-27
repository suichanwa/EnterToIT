
function reverseWords(str) {
  let revers = str
  .split(" ")
  .map(word => word.split("")
  .reverse()
  .join(""));
  return revers.join(" ");
}
