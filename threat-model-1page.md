# Threat Model - Lab 6 AES-CBC Socket

## Thông tin nhóm
- Thành viên 1: Nguyễn Văn Huy (1871020313)
- Thành viên 2: Phạm Anh Tú (1871020615)

## Assets
- Plaintext (Nội dung bản tin gốc cần bảo mật).
- Khóa AES (16/32 bytes) và IV (16 bytes).
- Ciphertext truyền trên mạng.

## Attacker model
Kẻ tấn công Man-in-the-Middle (MitM) nằm trong cùng mạng LAN, có công cụ dò quét cổng và khả năng bắt gói tin (sniffing) bằng Wireshark. Có khả năng sửa đổi nội dung luồng TCP byte stream.

## Threats
- **Key disclosure**: Khóa AES và IV đang được gửi hoàn toàn bằng plaintext qua `KEY_PORT`. Kẻ tấn công bắt được luồng này có thể giải mã lập tức `DATA_PORT`.
- **Tampering**: AES-CBC không có cơ chế xác thực toàn vẹn. Kẻ tấn công có thể lật bit (bit-flipping) của ciphertext, làm sai lệch plaintext khi Receiver giải mã.
- **Replay attack**: Kẻ tấn công có thể chụp lại toàn bộ gói tin data và key, sau đó gửi lại cho Receiver (Replay) để kích hoạt lại một hành động trái phép.

## Mitigations
- Không gửi key dưới dạng plaintext. Cần sử dụng thuật toán trao đổi khóa an toàn (Diffie-Hellman) hoặc bao bọc toàn bộ kết nối bằng TLS/SSL.
- Thay thế AES-CBC bằng AES-GCM (Authenticated Encryption with Associated Data) để phát hiện ngay lập tức nếu ciphertext bị chỉnh sửa (Tampering).
- Bổ sung Timestamp hoặc Nonce, Sequence number vào gói tin để hệ thống từ chối các gói tin cũ (chống Replay attack).

## Residual risks
Hiện tại hệ thống vẫn đang ở mức "mô phỏng học tập". Rủi ro còn lại là cực kỳ cao (Critical) vì kênh khóa hoàn toàn không được bảo vệ. Kẻ gian không cần phá mã AES mà chỉ cần nghe lén port 6001 là lấy được chìa khóa.