function majorityElement(nums: number[]): number {
    nums.sort((a, b) => a - b);
    const majorityCount = Math.floor(nums.length / 2);
    let count = 1;

    for (let i = 1; i < nums.length; i++) {
        if (nums[i] === nums[i - 1]) {
            count++;
        } else {
            count = 1;
        }

        if (count > majorityCount) {
            return nums[i];
        }
    }

    return nums[0];
}
