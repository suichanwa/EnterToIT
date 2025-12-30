function missingNumber(nums: number[]): number {
 //so what we need to do is find the number that is missing from the array
 //firt of all let's sort the array
 //then we will figure out what's the amount of total numbers n that is in the array
 //then we will loop throw it with a for in loop
 //and check which number is missing
    nums.sort((a, b) => a - b);
    const n = nums.length;
    for (let i = 0; i <= n; i++) {
        if (i === n || nums[i] !== i) {
            return i;
        }
    }
    return nums[0];
};