function findHighAccessEmployees(access_times: string[][]): string[] {
    const map: Record<string, string[]> = {};

    for (const [name, time] of access_times) {
        if (!map[name]) map[name] = [];
        map[name].push(time);
    }

    const toMinutes = (t: string): number => {
        const h = parseInt(t.slice(0, 2), 10);
        const m = parseInt(t.slice(2, 4), 10);
        return h * 60 + m;
    };

    const result: string[] = [];

    for (const name in map) {
        const times = map[name].sort(
            (a, b) => toMinutes(a) - toMinutes(b)
        );

        let left = 0;

        for (let right = 0; right < times.length; right++) {
            while (toMinutes(times[right]) - toMinutes(times[left]) >= 60) {
                left++;
            }

            if (right - left + 1 >= 3) {
                result.push(name);
                break;
            }
        }
    }

    return result;
}
