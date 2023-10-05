# SlidingPuzzle

该程序使用A\*算法解决数字华容道（3\*3以上）问题，并支持多种启发函数的定义。数字华容道是一个滑块拼图游戏，玩家需要以最少的步数移动特定初始排列顺序的数字块，使它们从小到大顺序排列。

### 使用方法

1. 克隆或下载代码到本地

2. 打开`main.py`文件，根据需要修改初始状态，空位用0占位

   ~~~python
   # [5, 3, 6]
   # [1, 8, 4]
   # [7, 2, 0]
   start_state = [5, 3, 6, 1, 8, 4, 7, 2, 0]
   ~~~

3. 运行`main.py`文件

   ~~~shell
   python main.py
   ~~~

4. 程序会输出求解结果，包括移动过程中每一步的状态和当前步数

   ~~~python
   Step 0: [5, 3, 6, 1, 8, 4, 7, 2, 0]
   Step 1: [5, 3, 6, 1, 8, 0, 7, 2, 4]
   Step 2: [5, 3, 6, 1, 0, 8, 7, 2, 4]
   Step 3: [5, 3, 6, 1, 2, 8, 7, 0, 4]
   Step 4: [5, 3, 6, 1, 2, 8, 7, 4, 0]
   Step 5: [5, 3, 6, 1, 2, 0, 7, 4, 8]
   Step 6: [5, 3, 0, 1, 2, 6, 7, 4, 8]
   Step 7: [5, 0, 3, 1, 2, 6, 7, 4, 8]
   Step 8: [5, 2, 3, 1, 0, 6, 7, 4, 8]
   Step 9: [5, 2, 3, 1, 4, 6, 7, 0, 8]
   Step 10: [5, 2, 3, 1, 4, 6, 7, 8, 0]
   Step 11: [5, 2, 3, 1, 4, 0, 7, 8, 6]
   Step 12: [5, 2, 0, 1, 4, 3, 7, 8, 6]
   Step 13: [5, 0, 2, 1, 4, 3, 7, 8, 6]
   Step 14: [0, 5, 2, 1, 4, 3, 7, 8, 6]
   Step 15: [1, 5, 2, 0, 4, 3, 7, 8, 6]
   Step 16: [1, 5, 2, 4, 0, 3, 7, 8, 6]
   Step 17: [1, 0, 2, 4, 5, 3, 7, 8, 6]
   Step 18: [1, 2, 0, 4, 5, 3, 7, 8, 6]
   Step 19: [1, 2, 3, 4, 5, 0, 7, 8, 6]
   Step 20: [1, 2, 3, 4, 5, 6, 7, 8, 0]
   ~~~

### 参数说明

* -st --strategy 选择启发函数的策略，其中：
  * 1：”不在位“的将牌数
  * 2：将牌“不在位”的距离和
  * 3：不使用启发函数（退化为广度优先）
* -si --size 数字华容道的大小，默认为3（即3*3）
