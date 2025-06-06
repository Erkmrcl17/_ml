# NQU AI Assistant

此專案是一個AI助理，整合語音辨識、語意理解、即時語音回覆與 Unity 動畫互動等功能，實現自然且即時的人機對話體驗。用戶可透過語音與虛擬角色互動，並由角色回應語音與動作。

![DEMO](https://youtu.be/T7zYKpIHq8w?si=K0JmboD7ac9XcAHx)

## 後端（Server）

使用 Python Flask 為核心架構，實作語音文字理解與生成，並整合以下元件：

🧠 RAG + PGVector：使用檢索增強生成技術與向量資料庫提升回答準確性

💬 LLM（如 GPT / Gemini）：進行自然語言回應生成

🗣️ edgeTTS：將生成的文字轉為語音並回傳

🔄 WebSocket 通訊：與前端即時傳遞資料與語音結果

## 支援功能：

🔁 短期對話記憶（Session 對話上下文）

🗣️ AI 回覆語音合成（TTS）

🌐 對方回覆翻譯功能（可開關）

🔇 隱藏回覆文字功能（僅語音）

📋 文字回覆複製功能

📝 對使用者輸入進行語法糾正

## 前端（Client）
使用 C# 搭配 Unity 開發，並整合本地或遠端語音辨識模型（Whisper）進行語音輸入。

功能特點：
📋 使用 Whisper 模型將語音轉為文字

🔄 將辨識後的語音文字透過 WebSocket 傳送至後端

🗣️ 接收語音回覆與文字資料後，於 Unity 中播放語音並驅動角色動畫

## 系統整合流程圖（概念）：

1.Client (C#) 使用 Whisper 辨識語音

2.傳送文字至 Server（WebSocket）

3.Server 使用 RAG + LLM 回答

4.使用 edgeTTS 將回答轉為語音

5.回傳語音與文字給 Unity

6.Unity 播放語音，並顯示對話內容或驅動角色表情/動畫

### 展示：
![image](https://github.com/Erkmrcl17/_ml/blob/main/pict/Cuplikan%20layar%202025-06-06%20235526.png)

![image](https://github.com/Erkmrcl17/_ml/blob/main/pict/Cuplikan%20layar%202025-06-06%20235711.png)
