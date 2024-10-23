public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int,int> map = new();
        for (int i=0; i < nums.Length; i++) {
            int diff = target - nums[i];
            if (map.ContainsKey(nums[i])) {
                return new int[] {map[nums[i]], i};
            }
            map.TryAdd(diff, i);
        }
        return null;
    }
}