class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        // 三次翻转搞定
        k = k % nums.size();
        reverse(nums.begin(), nums.begin() + nums.size() - k);
        reverse(nums.begin() + nums.size() - k, nums.end());
        reverse(nums.begin(), nums.end());
    }
};


"""
可以采用翻转的方式，比如12345经过翻转就变成了54321，
这样已经做到了把前面的数字放到后面去
比如，我们只需要把12放在后面去，目标数组就是34512
与54321对比发现我们就只需要在把分界线前后数组再进行翻转一次就可得到目标数组了
所以此题只需要采取三次翻转的方式就可以得到目标数组
首先翻转分界线前后数组，再整体翻转一次即可。

"""