# 📚 Trang Web Học 360 Động Từ Bất Quy Tắc Tiếng Anh Toàn Diện

Trang web học tập tương tác hiện đại dành cho **đầy đủ 360 động từ bất quy tắc tiếng Anh**, được xây dựng dựa trên bảng chuẩn 12 trang:
- **Nguyên thể (V1), Quá khứ (V2), Quá khứ phân từ (V3)**
- **Phiên âm quốc tế chuẩn IPA**
- **Dịch nghĩa tiếng Việt chính xác**
- **Ví dụ câu ngữ cảnh tiếng Anh tự nhiên kèm dịch nghĩa tiếng Việt**
- **Hình ảnh minh họa chất lượng cao** cho toàn bộ 360 từ
- **Hệ thống phát âm bản ngữ (Web Speech API)** cho cả 3 dạng và câu ví dụ

---

## 🚀 Các Tính Năng Nổi Bật

1. **Bảng tra cứu thông minh (Word Explorer)**:
   - Tìm kiếm tức thì theo tiếng Anh (V1, V2, V3) hoặc tiếng Việt không dấu/có dấu.
   - Bộ lọc theo 4 nhóm biến đổi:
     - **Nhóm AAA**: 3 dạng như 1 (*cut - cut - cut, put - put - put*)
     - **Nhóm ABB**: V2 và V3 giống nhau (*buy - bought - bought, feel - felt - felt*)
     - **Nhóm ABA**: V1 và V3 giống nhau (*come - came - come, run - ran - run*)
     - **Nhóm ABC**: Cả 3 dạng khác nhau (*sing - sang - sung, write - wrote - written*)
     - **Top 100 từ thông dụng**, Từ đã lưu sao ⭐, Từ đã thuộc ✅, Từ cần ôn 🔄
   - Chuyển đổi linh hoạt giữa giao diện **Lưới thẻ ảnh (Card Grid)** và **Bảng dữ liệu (Data Table)**.

2. **Thẻ ghi nhớ Flashcards 3D (Interactive Flashcards)**:
   - Hiệu ứng lật thẻ 3D mượt mà.
   - Mặt trước: Hình ảnh, V1, IPA, Tùy chọn ẩn/hiện nghĩa để tự kiểm tra trí nhớ.
   - Mặt sau: Cả 3 cột V1 - V2 - V3, dịch nghĩa, câu ví dụ và dịch nghĩa câu.
   - Nút đánh giá: *Đã thuộc* vs *Cần ôn tập* giúp theo dõi tiến độ học.

3. **Chuyên đề Ngữ Pháp Chuyên Sâu: 12 Thì & 360 Động Từ Bất Quy Tắc**:
   - **Ma trận 12 thì tự động (Visual 12 Tenses Conjugator)**: Chọn bất kỳ từ nào trong 360 động từ -> Hệ thống tự động chia đầy đủ 12 thì (Khẳng định, Phủ định, Nghi vấn) kèm câu ví dụ thực tế và phát âm audio.
   - **Nhấn mạnh vai trò V1 - V2 - V3**:
     - *Thì Quá khứ đơn*: Bắt buộc dùng **V2 (Past Simple)**.
     - *Toàn bộ các thì Hoàn thành (Hiện tại, Quá khứ, Tương lai hoàn thành)*: Bắt buộc dùng **V3 (Past Participle)**.
     - *Các thì Tiếp diễn*: Quy tắc thêm đuôi **V-ing** chuẩn xác.
   - **Bài kiểm tra 12 Thì & Động từ (Tenses & Verbs Exam)**: Đề thi 10 câu ngẫu nhiên kiểm tra dấu hiệu nhận biết (*yesterday, already, by the time, since, look...*) và phản xạ chia V1/V2/V3 có giải thích ngữ pháp chi tiết.

4. **Luyện tập Trắc nghiệm (Quiz Mode)**:
   - 4 dạng câu hỏi: Tìm V2, Tìm V3, Tìm nghĩa tiếng Việt, Điền từ vào câu ví dụ.
   - Chấm điểm tức thì, chuỗi Streak 🔥, và giải thích chi tiết sau mỗi câu.

5. **Luyện gõ từ vựng (Typing Test)**:
   - Hiển thị từ V1 và nghĩa -> người học tự gõ V2 và V3 để rèn phản xạ chính tả.

6. **Phát âm Audio bản ngữ**:
   - Sử dụng Web Speech API chuẩn trình duyệt, hỗ trợ giọng US (Mỹ) và UK (Anh), không lo tốn băng thông hay lỗi kết nối.

7. **Chế độ Sáng / Tối (Dark / Light Mode)** & Tự động lưu tiến độ vào LocalStorage.

---

## 🛠️ Hướng Dẫn Sử Dụng & Khởi Chạy

Bạn có thể mở ứng dụng theo 2 cách cực kỳ đơn giản:

### Cách 1: Chạy trực tiếp bằng Python
Trong thư mục dự án, chạy lệnh:
```bash
python3 start.py
```
Sau đó mở trình duyệt tại: `http://localhost:8000/index.html`

### Cách 2: Mở trực tiếp tệp HTML
Bạn có thể mở trực tiếp tệp `index.html` bằng bất kỳ trình duyệt nào (Chrome, Edge, Firefox, Safari) mà không cần cài đặt thêm bất kỳ phần mềm nào.

---

## 📁 Cấu Trúc Thư Mục

```
irregular-verbs-360/
├── index.html              # Giao diện chính (HTML5 + Tailwind CSS + FontAwesome)
├── style.css               # Hiệu ứng 3D Flashcard, font chữ, animations
├── app.js                  # Toàn bộ logic ứng dụng động từ bất quy tắc
├── verbs_data.js           # Dữ liệu 360 động từ (JavaScript)
├── verbs_data.json         # Dữ liệu 360 động từ (JSON)
├── it_app.js               # Logic điều khiển danh mục Tiếng Anh CNTT (1,000 thuật ngữ)
├── it_terms_data.js        # Cơ sở dữ liệu 1,000 thuật ngữ CNTT (JavaScript)
├── it_terms_data.json      # Cơ sở dữ liệu 1,000 thuật ngữ CNTT (JSON)
├── domain_01_programming.py   # Dữ liệu 100 thuật ngữ Lập trình & Kiến trúc phần mềm
├── domain_02_dsa.py           # Dữ liệu 100 thuật ngữ Cấu trúc dữ liệu & Giải thuật
├── domain_03_database.py      # Dữ liệu 100 thuật ngữ Cơ sở dữ liệu & Kỹ thuật dữ liệu
├── domain_04_networking.py    # Dữ liệu 100 thuật ngữ Mạng máy tính & Giao thức
├── domain_05_security.py      # Dữ liệu 100 thuật ngữ An ninh mạng & Mật mã học
├── domain_06_os_hardware.py   # Dữ liệu 100 thuật ngữ Hệ điều hành & Phần cứng
├── domain_07_cloud_devops.py  # Dữ liệu 100 thuật ngữ Điện toán đám mây & DevOps
├── domain_08_web_mobile.py    # Dữ liệu 100 thuật ngữ Web, API & Mobile Engineering
├── domain_09_ai_ml.py         # Dữ liệu 100 thuật ngữ Trí tuệ nhân tạo, ML & LLMs
├── domain_10_qa_workplace.py  # Dữ liệu 100 thuật ngữ QA, Kiểm thử, Agile & Workplace
├── compile_1000_it_database.py # Script biên dịch & đồng bộ 1,000 thuật ngữ
├── start.py                # Máy chủ cục bộ mở nhanh trên trình duyệt
└── README.md               # Tài liệu hướng dẫn
```

---

## 💻 Danh Mục Chuyên Biệt: Tiếng Anh Chuyên Ngành CNTT (1,000 Core IT Terms)

Bộ dữ liệu đồ sộ gồm **1,000 thuật ngữ và từ vựng cốt lõi** chuẩn kỹ thuật quốc tế được chia đều thành **10 lĩnh vực chuyên sâu (100 thuật ngữ/lĩnh vực)**:

1. **Lập trình & Kiến trúc phần mềm (`programming` - 100 thuật ngữ)**:
   - *Algorithm, Refactor, Repository, Deploy, Debug, Framework, Compiler, Syntax, Recursion, Inheritance, Polymorphism, Encapsulation, Asynchronous, Dependency, Deprecated, Concurrency, Boilerplate, Immutable, Memory Leak, Design Pattern, SOLID Principles, Linter, Idiomatic, Metaprogramming...*
2. **Cấu trúc dữ liệu & Giải thuật (`dsa` - 100 thuật ngữ)**:
   - *Array, Linked List, Stack, Queue, Hash Table, Binary Tree, AVL Tree, Red-Black Tree, B-Tree, Trie, Graph, Heap, Big O Notation, Time Complexity, Space Complexity, Breadth-First Search, Depth-First Search, Dijkstra's Algorithm, Dynamic Programming, Memoization, Backtracking, Divide and Conquer, Greedy Algorithm, NP-Complete...*
3. **Cơ sở dữ liệu & Kỹ thuật dữ liệu (`database` - 100 thuật ngữ)**:
   - *Database Schema, SQL, NoSQL, Relational Database, Primary Key, Foreign Key, Index, Query Optimization, Transaction, ACID, Sharding, Replication, Normalization, Denormalization, Migration, Connection Pool, Stored Procedure, Deadlock, CAP Theorem, Data Warehouse, Data Lake, ETL, Change Data Capture, Redis, Cassandra...*
4. **Mạng máy tính & Giao thức mạng (`networking` - 100 thuật ngữ)**:
   - *IP Address, IPv4, IPv6, Subnet Mask, MAC Address, DNS, DHCP, TCP, UDP, HTTP, HTTPS, HTTP/2, HTTP/3, WebSocket, WebRTC, SSL/TLS, Handshake, Latency, Bandwidth, Throughput, Packet Loss, Routing, Default Gateway, NAT, Reverse Proxy, CDN, Socket, BGP, Port Forwarding, MTU...*
5. **An ninh mạng & Mật mã học (`security` - 100 thuật ngữ)**:
   - *Cybersecurity, Vulnerability, Exploit, Zero-day, Threat Actor, Firewall, Intrusion Detection System (IDS), Intrusion Prevention System (IPS), SIEM, Penetration Testing, Malware, Ransomware, Phishing, Social Engineering, DDoS Attack, Man-in-the-Middle (MitM), SQL Injection, XSS, CSRF, Cryptography, Symmetric Encryption, Asymmetric Encryption, AES, RSA, Hash Function, Salt, Digital Signature, PKI, Multi-Factor Authentication (MFA), OAuth 2.0, OpenID Connect, JWT, Principle of Least Privilege, Zero Trust, Sandbox...*
6. **Hệ điều hành & Phần cứng máy tính (`os_hardware` - 100 thuật ngữ)**:
   - *Operating System, Kernel, Monolithic Kernel, Microkernel, Process, Thread, Multithreading, Context Switch, Process Scheduling, Interrupt, System Call, Virtual Memory, Paging, Page Fault, Memory Segmentation, Cache Memory, CPU, GPU, TPU, Motherboard, RAM, ROM, SSD, NVMe, BIOS/UEFI, File System, Deadlock, Mutual Exclusion, Semaphore, Mutus, Race Condition, Shell, Terminal, POSIX, Driver, Firmware...*
7. **Điện toán đám mây & DevOps (`cloud_devops` - 100 thuật ngữ)**:
   - *Cloud Computing, IaaS, PaaS, SaaS, Public Cloud, Private Cloud, Hybrid Cloud, Multi-Cloud, Virtual Machine, Hypervisor, Docker, Containerization, Kubernetes, Pod, Container Orchestration, Microservices, Serverless, AWS Lambda, Cloud Function, Auto-scaling, Elasticity, High Availability, Fault Tolerance, Disaster Recovery, Load Balancer, CI/CD, Pipeline, Infrastructure as Code (IaC), Terraform, Ansible, GitOps, Observability, Telemetry, Prometheus, Grafana, Site Reliability Engineering (SRE), SLA, SLO, SLI...*
8. **Kỹ thuật Web, API & Ứng dụng Di động (`web_mobile` - 100 thuật ngữ)**:
   - *Frontend, Backend, Full-stack, DOM, Virtual DOM, Single Page Application (SPA), Server-Side Rendering (SSR), Static Site Generation (SSG), Hydration, Responsive Web Design, CSS Grid, Flexbox, API, RESTful API, Endpoint, HTTP Request Methods, GraphQL, Webhook, gRPC, CORS, WebAssembly, Web Worker, Service Worker, Progressive Web App (PWA), LocalStorage, SessionStorage, Cookie, Cross-Platform, React Native, Flutter, Native App, Deep Linking, Push Notification...*
9. **Trí tuệ nhân tạo, Học máy & LLMs (`ai_ml` - 100 thuật ngữ)**:
   - *Artificial Intelligence, Machine Learning, Deep Learning, Supervised Learning, Unsupervised Learning, Reinforcement Learning, Neural Network, Perceptron, Activation Function, Gradient Descent, Backpropagation, Loss Function, Overfitting, Underfitting, Epoch, Batch Size, Hyperparameter Tuning, Computer Vision, Convolutional Neural Network (CNN), NLP, Recurrent Neural Network (RNN), Transformer, Attention Mechanism, Large Language Model (LLM), Generative AI, Prompt Engineering, Hallucination, Fine-tuning, RAG, Vector Database, Embedding, Temperature, Tokenization, Zero-shot Learning, Few-shot Learning, Reinforcement Learning from Human Feedback (RLHF)...*
10. **Kiểm thử chất lượng (QA), Agile & Tiếng Anh Nơi Làm Việc Công Nghệ (`qa_workplace` - 100 thuật ngữ)**:
    - *Quality Assurance (QA), Quality Control (QC), Software Testing, Unit Testing, Integration Testing, End-to-End Testing (E2E), Regression Testing, Smoke Testing, Sanity Testing, User Acceptance Testing (UAT), Test Case, Test Suite, Bug, Defect, Edge Case, Test-Driven Development (TDD), Behavior-Driven Development (BDD), Code Review, Pull Request (PR), Agile Methodology, Scrum, Sprint, Sprint Planning, Daily Stand-up, Sprint Retrospective, Product Backlog, User Story, Acceptance Criteria, Burndown Chart, Kanban, Velocity, Tech Debt, Spike, Blocker, Production Incident, Post-mortem, Root Cause Analysis (RCA), Onboarding, Peer Review, Stakeholder, Deliverable, Milestone, SLA...*

### 🌟 Tính Năng Học Tập Tương Tác:
- **Lưới thẻ ảnh trực quan (Card Grid)**: 1,000 thẻ thuật ngữ sắc nét kèm icon, ảnh Unsplash chất lượng cao, nhãn phân loại, định nghĩa ngắn gọn và ví dụ câu thực tế.
- **Bảng dữ liệu tra cứu nhanh (Data Table)**: Bảng tra cứu tốc độ cao, hiển thị đầy đủ phiên âm IPA, từ loại, định nghĩa kỹ thuật và ví dụ.
- **Bộ lọc 10 chuyên ngành tức thì**: 10 nút bấm phân loại trực quan theo từng lĩnh vực, kết hợp bộ lọc *Từ đã lưu ⭐* và *Từ đã thuộc ✅*.
- **Tìm kiếm đa năng thông minh**: Tìm kiếm theo thuật ngữ tiếng Anh, phiên âm IPA, định nghĩa tiếng Việt (có dấu hoặc không dấu), ví dụ câu hoặc nhãn khái niệm.
- **Thẻ ghi nhớ Flashcards 3D thuật ngữ CNTT**: Lật thẻ 3D học sâu định nghĩa, ví dụ dự án thực tế và tự đánh giá mức độ ghi nhớ.
- **Trắc nghiệm kiến thức chuyên môn (IT Technical Quiz)**: Bộ câu hỏi trắc nghiệm tự động tạo ngẫu nhiên từ kho 1,000 từ, kèm hệ thống tính điểm và chuỗi Streak 🔥.
- **Phát âm âm thanh bản ngữ (Web Speech API)**: Nghe phát âm chuẩn từng từ và toàn bộ câu ví dụ với giọng Anh - Mỹ tự nhiên.
- **Lưu trữ tiến trình học tập**: Dữ liệu từ đã lưu và đã thuộc được lưu an toàn vào `LocalStorage` của trình duyệt.
