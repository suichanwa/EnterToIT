function accountsMerge(accounts: string[][]): string[][] {
  //make a function that will merge the account by the names, it'll frist covert both string to lowercase and check by the name, and if the name which is gonna be in the frist array will matche the name from the second array it'll match it up
  // it has first to have the name, from the frist array, and the second to be the emial, and then attach them on the return

  const map: Record<string, string[]> = {};
  for (const account of accounts) {
    const name = account[0];
    const emails = account.slice(1);
    for (const email of emails) {
      map[email] = map[email] || [];
      map[email].push(name);
    }
  }
  return Object.entries(map).map(([email, names]) => [
    names[0],
    ...names.slice(1).sort(),
  ]);
}
