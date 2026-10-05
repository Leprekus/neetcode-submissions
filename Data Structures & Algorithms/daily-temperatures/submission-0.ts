class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures: number[]): number[] {
        const items = temperatures;
        if(items.length === 0) return [];
        const stack = [0];
        const res   = new Array(items.length).fill(0);

        for(let i = 1; i < items.length; i++) {
            let prev = stack.at(-1);
            const curr = i;
            while(items[prev] < items[curr]) {
                res[prev] = curr - prev;
                stack.pop();
                prev = stack.at(-1);
            }
            stack.push(curr);
        }
        return res;
        
    }
}
