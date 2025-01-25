#!/usr/bin/env python3
import requests
import json
from datetime import datetime


def send_dingtalk_message():
    # 钉钉机器人的Webhook地址列表
    webhooks = [
        "https://oapi.dingtalk.com/robot/send?access_token=002f008b27dc5656fc58c98c60492fea21662bca977b98a75d6cc8e693af5803"
    ]

    # 获取当前时间
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 构造消息内容
    message = {
        "msgtype": "markdown",
        "markdown": {
            "title": "网站更新成功通知",
            "text": f"### ✅ 网站更新成功\n\n"
            + f"- **时间**：{current_time}\n"
            + f"- **站点**：[blog.w1ndys.top](https://blog.w1ndys.top)\n"
            + f"- **状态**：部署完成\n\n"
            + "网站已完成更新！",
        },
    }

    # 发送消息到所有webhook
    headers = {"Content-Type": "application/json"}
    for webhook in webhooks:
        try:
            response = requests.post(webhook, data=json.dumps(message), headers=headers)
            if response.status_code == 200:
                response_data = response.json()
                if response_data.get("errcode") == 0:
                    print(f"成功通知发送成功 - Webhook: {webhook}")
                else:
                    print(
                        f"成功通知发送失败 - Webhook: {webhook}, 错误: {response_data.get('errmsg')}"
                    )
            else:
                print(
                    f"HTTP错误 - Webhook: {webhook}, 状态码: {response.status_code}, 响应内容: {response.text}"
                )
        except Exception as e:
            print(f"发送通知时发生错误 - Webhook: {webhook}, 错误: {str(e)}")


if __name__ == "__main__":
    send_dingtalk_message()
