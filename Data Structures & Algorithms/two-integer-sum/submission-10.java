class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> diffs = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int curDif = target - num;

            if (diffs.containsKey(curDif)) {
                return new int[] {diffs.get(curDif), i};
            }

            diffs.put(num, i);
        }

        return new int[] {};
    }
}
