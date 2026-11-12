# git-practice

一个用来练 Git 协作的玩具项目。功能不重要，**提交历史才是重点**。

## 这是什么

一个只有命令行的小待办程序，数据存在 `todos.json` 里。

```powershell
python main.py add "交实验报告"
python main.py add "复习线性代数"
python main.py list
python main.py done 1
```

## 练习任务

下面这些是给你练 Git 的，按顺序做，每做完一条就 commit 一次：

- [ ] 把项目初始化成 Git 仓库，推到 GitHub
- [ ] 新建一个分支 `feature/删除功能`，加上"删除某一项"的功能，开 PR 合并
- [ ] 再新建一个分支 `feature/优先级`，给待办加上优先级字段，开 PR 合并
- [ ] 和同学同时改同一行，制造一次冲突，然后解决它
- [ ] 用 `git log --oneline --graph` 看一遍自己的提交历史

## 规则

1. 一个提交只做一件事
2. 提交信息写清楚"做了什么"，不写 "update"
3. 推之前先拉
4. `todos.json` 是本地产物，不提交
