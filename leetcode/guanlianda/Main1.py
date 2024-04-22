class Solution:
    """
    小明送外卖

    小明是一家店铺的专职外卖员。
    小明每天会接到很多不同地方的n个外卖订单，其中第i个订单会在si时刻下单，花费小明t;时间往返，并赚取a;元酬劳。
    小明每次只能送1单外卖，订单一旦错过就会被派给其他外卖员。
    如果小明提前知道了今天的全部订单，请你帮小明选择最优的接单方式，使得今天赚取的酬劳最多

    对于每一组数据，包含4行数据
    第一行是外卖订单数: n。
    第二行有n个数字s; (i=1,2,3.....n)表示第的订单的下单时刻为S;i
    第三行有n个数字 (i=1,2,3....n)表示第i的订单的往返时间为t;
    第四行有n个数字a’ (i=1,2,3...n)表示第i的订单的酬劳为ai。

    输出
    输出一个整数 表示小明最多可赚取最多的酬劳


    样例输入
    5
    1 3 6 7 1
    4 3 4 3 9
    2 5 5 3 4
    样例输出
    14

    小明选择接2、3、5单可以赶在下一单到来前结束当前订单，并可以赚取14元。
    提示:如果小明在t时刻返回，她可以接包括t时刻以及之后到来的订单，但不能接t-1时刻以及之前的订单
    """


