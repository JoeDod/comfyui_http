import { app } from "../../scripts/app.js";
import { ComfyWidgets } from "../../scripts/widgets.js";

app.registerExtension({
	name: "Comfy.SimpleHttpRequest.ShowText",
	async beforeRegisterNodeDef(nodeType, nodeData, app) {
		if (nodeData.name === "SimpleShowText") {
			const onExecuted = nodeType.prototype.onExecuted;
			nodeType.prototype.onExecuted = function (message) {
				onExecuted?.apply(this, arguments);

				if (message && message.text) {
					// 尝试找到名为 "display_text" 的 widget
					let w = this.widgets && this.widgets.find((w) => w.name === "display_text");

					// 如果没找到，创建一个新的
					if (!w) {
						// ComfyWidgets["STRING"] 返回的是一个对象 { widget: ... }
						// 参数: node, name, [type, options], app
						const widgetData = ComfyWidgets["STRING"](this, "display_text", ["STRING", { multiline: true }], app);
						w = widgetData.widget;
						w.inputEl.readOnly = true;
						w.inputEl.style.opacity = 0.6;
					}

					// 更新值
					if (w) {
						w.value = message.text.join("");
						// 调整节点大小以适应内容（可选）
						this.onResize?.(this.size);
					}
				}
			};
		}
	},
});
