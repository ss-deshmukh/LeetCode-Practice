1impl Solution {
2    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
3        for i in 0..nums.len() {
4            for j in (i + 1)..nums.len() {
5                if nums[i] + nums[j] == target {
6                    return vec![i as i32, j as i32];
7                }
8            }
9        }
10        vec![]
11    }
12}