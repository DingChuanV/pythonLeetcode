class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        """
        2240. 买钢笔和铅笔的方案数
        给你一个整数 total ，表示你拥有的总钱数。同时给你两个整数 cost1 和 cost2 ，分别表示一支钢笔和一支铅笔的价格。
        你可以花费你部分或者全部的钱，去买任意数目的两种笔。
        请你返回购买钢笔和铅笔的 不同方案数目 。
        输入：total = 20, cost1 = 10, cost2 = 5
        输出：9
        解释：一支钢笔的价格为 10 ，一支铅笔的价格为 5 。
        - 如果你买 0 支钢笔，那么你可以买 0 ，1 ，2 ，3 或者 4 支铅笔。
        - 如果你买 1 支钢笔，那么你可以买 0 ，1 或者 2 支铅笔。
        - 如果你买 2 支钢笔，那么你没法买任何铅笔。
        所以买钢笔和铅笔的总方案数为 5 + 3 + 1 = 9 种
        :param total:
        :param cost1:
        :param cost2:
        :return:
        """
        ans = 0
        for x in range(total // cost1 + 1):
            y = (total - (x * cost1)) // cost2 + 1
            ans += y
        return ans


if __name__ == '__main__':
    print(Solution().waysToBuyPensPencils(20, 10, 5))
