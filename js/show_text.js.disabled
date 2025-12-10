import { app } from "../../scripts/app.js";
import { ComfyWidgets } from "../../scripts/widgets.js";

app.registerExtension({
	name: "Comfy.SimpleHttpRequest.ShowText",
	async beforeRegisterNodeDef(nodeType, nodeData, app) {
		if (nodeData.name === "SimpleShowText") {
			// 在节点创建时添加 Widget，这样它就一直存在且可见
			const onNodeCreated = nodeType.prototype.onNodeCreated;
			nodeType.prototype.onNodeCreated = function () {
				const r = onNodeCreated ? onNodeCreated.apply(this, arguments) : undefined;

				// 创建一个名为 "result" 的多行文本控件
				// ComfyWidgets["STRING"] 会自动将其添加到 this.widgets 中
				// 这里的 "result" 是显示在界面上的标签名
				const w = ComfyWidgets["STRING"](this, "result", ["STRING", { multiline: true }], app).widget;

				// 默认就是可编辑的，所以不需要设置 readOnly
				// 如果你想让它看起来更像一个输出框，可以保留 opacity 设置，或者去掉让它完全像一个输入框
				// w.inputEl.style.opacity = 0.6; 

				return r;
			};

			// 节点执行完成后更新 Widget 的值
			const onExecuted = nodeType.prototype.onExecuted;
			nodeType.prototype.onExecuted = function (message) {
				onExecuted?.apply(this, arguments);

				if (message && message.text) {
					const w = this.widgets && this.widgets.find((w) => w.name === "result");
					if (w) {
						w.value = message.text.join("");
						// 触发重绘，确保内容更新
						this.onResize?.(this.size);
					}
				}
			};
		}
	},
});
