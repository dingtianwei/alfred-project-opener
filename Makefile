all:
	@echo "请使用make sync同步代码到workflow"
.PHONY: sync
sync: ## 安装github hook
	sh ./sync.sh
