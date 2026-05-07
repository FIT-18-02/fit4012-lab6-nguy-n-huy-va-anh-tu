# Threat Model - Lab 6 AES-CBC Socket

## Thông tin nhóm

- Thành viên 1: TODO_STUDENT
- Thành viên 2: TODO_STUDENT

## Assets

TODO_STUDENT: Liệt kê tài sản cần bảo vệ, ví dụ plaintext, AES key, IV, ciphertext, file đầu vào, file đầu ra và log.

## Attacker model

TODO_STUDENT: Mô tả đối tượng tấn công có thể nghe lén mạng LAN, bắt gói tin, sửa ciphertext, replay packet hoặc đọc log.

## Threats

TODO_STUDENT: Nêu ít nhất 3 mối đe dọa cụ thể, ví dụ:
- Key disclosure do key/IV gửi plaintext.
- Tampering do ciphertext bị sửa.
- Replay attack do packet cũ bị gửi lại.
- Log leakage do key bị ghi vào log.
- No authentication do Receiver không xác thực Sender.

## Mitigations

TODO_STUDENT: Nêu ít nhất 3 biện pháp giảm thiểu, ví dụ:
- Không gửi key plaintext trong hệ thống thật.
- Dùng TLS hoặc cơ chế trao đổi khóa an toàn.
- Dùng AES-GCM để có xác thực dữ liệu.
- Không ghi key thật vào log trong môi trường thật.
- Thêm nonce/timestamp để giảm replay.
- Thêm xác thực Sender.

## Residual risks

TODO_STUDENT: Nêu ít nhất 1 rủi ro còn lại, ví dụ hệ thống vẫn chưa an toàn vì key channel chỉ là mô phỏng, chưa có TLS, chưa có xác thực và chưa chống replay đầy đủ.
