# -*- coding: utf-8 -*-
"""
Generator for IT English (Tiếng Anh Chuyên Ngành Công Nghệ Thông Tin) Database
Covers 6 Essential Domains:
1. Lập trình & Kỹ thuật phần mềm (Programming & Software Engineering)
2. Cơ sở dữ liệu & Quản lý dữ liệu (Databases & Big Data)
3. Mạng máy tính & An ninh mạng (Networking & Cybersecurity)
4. Điện toán đám mây & DevOps (Cloud Computing & DevOps)
5. Trí tuệ nhân tạo & Khoa học dữ liệu (AI & Machine Learning)
6. Phát triển Web & Mobile (Web & Mobile Engineering)
"""

import json

it_terms_raw = [
    # -------------------------------------------------------------
    # 1. LẬP TRÌNH & KỸ THUẬT PHẦN MỀM (PROGRAMMING & SOFTWARE ENGINEERING)
    # -------------------------------------------------------------
    (1, "Algorithm", "/ˈæl.ɡə.rɪ.ðəm/", "noun", "programming", "Lập trình",
     "Thuật toán: tập hợp các chỉ dẫn từng bước rõ ràng để giải quyết một bài toán hoặc thực hiện tính toán.",
     "The quicksort algorithm efficiently sorts millions of data items in log-linear time.",
     "Thuật toán quicksort sắp xếp hàng triệu phần tử dữ liệu một cách hiệu quả với độ phức tạp tuyến tính-lôgarit.",
     "Thuật toán, luồng xử lý", "⚙️",
     "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    (2, "Refactor", "/ˌriːˈfæk.tər/", "verb", "programming", "Lập trình",
     "Tái cấu trúc mã nguồn: cải thiện cấu trúc bên trong của mã mà không làm thay đổi hành vi bên ngoài của hệ thống.",
     "Senior developers regularly refactor legacy modules to improve code readability and maintainability.",
     "Các lập trình viên kỳ cựu thường xuyên tái cấu trúc các mô-đun cũ để tăng tính dễ đọc và bảo trì mã nguồn.",
     "Tái cấu trúc mã nguồn", "🔄",
     "https://images.unsplash.com/photo-1542838132-92c53300491e?w=600&auto=format&fit=crop&q=80"),

    (3, "Repository", "/rɪˈpɒz.ɪ.tər.i/", "noun", "programming", "Lập trình",
     "Kho lưu trữ (Repo): nơi lưu trữ tập trung mã nguồn, tài liệu và lịch sử các phiên bản thay đổi (Git).",
     "You should clone the Git repository to your local machine before creating a new feature branch.",
     "Bạn nên nhân bản kho lưu trữ Git về máy cục bộ trước khi tạo một nhánh tính năng mới.",
     "Kho lưu trữ mã nguồn Git", "📦",
     "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?w=600&auto=format&fit=crop&q=80"),

    (4, "Deploy", "/dɪˈplɔɪ/", "verb", "programming", "Lập trình",
     "Triển khai: đưa ứng dụng, phần mềm hoặc bản cập nhật lên máy chủ để người dùng cuối có thể truy cập.",
     "Our automated pipeline can build, test, and deploy the application to production in under ten minutes.",
     "Quy trình tự động của chúng tôi có thể đóng gói, kiểm thử và triển khai ứng dụng lên môi trường thực tế dưới mười phút.",
     "Triển khai máy chủ", "🚀",
     "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600&auto=format&fit=crop&q=80"),

    (5, "Debug", "/diːˈbʌɡ/", "verb", "programming", "Lập trình",
     "Gỡ lỗi: quá trình tìm kiếm, phân tích và sửa chữa các lỗi logic hoặc cú pháp trong chương trình máy tính.",
     "She spent the entire morning using breakpoints to debug a complex memory leak issue.",
     "Cô ấy đã dành cả buổi sáng dùng các điểm dừng (breakpoint) để gỡ lỗi rò rỉ bộ nhớ phức tạp.",
     "Gỡ lỗi chương trình", "🐛",
     "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    (6, "Framework", "/ˈfreɪm.wɜːk/", "noun", "programming", "Lập trình",
     "Bộ khung phần mềm: nền tảng chứa sẵn thư viện, quy chuẩn cấu trúc giúp lập trình viên phát triển ứng dụng nhanh hơn.",
     "Django is a robust Python web framework designed to make rapid web development seamless.",
     "Django là một bộ khung web Python mạnh mẽ được thiết kế để phát triển ứng dụng web nhanh chóng và liền mạch.",
     "Bộ khung phần mềm", "🧱",
     "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    (7, "Compiler", "/kəmˈpaɪ.lər/", "noun", "programming", "Lập trình",
     "Trình biên dịch: chương trình chuyển đổi mã nguồn bậc cao (C++, Rust...) thành mã máy nhị phân có thể thực thi.",
     "The Rust compiler caught the dangling pointer error before the code could even run.",
     "Trình biên dịch Rust đã bắt được lỗi con trỏ lơ lửng ngay trước khi mã nguồn kịp chạy.",
     "Trình biên dịch mã máy", "⚙️",
     "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    (8, "Syntax", "/ˈsɪn.tæks/", "noun", "programming", "Lập trình",
     "Cú pháp: tập hợp các quy tắc xác định cách kết hợp các ký hiệu và từ khóa để tạo thành câu lệnh hợp lệ trong ngôn ngữ lập trình.",
     "Missing a semicolon in C++ will immediately trigger a syntax error during compilation.",
     "Việc thiếu dấu chấm phẩy trong C++ sẽ ngay lập tức gây ra lỗi cú pháp trong quá trình biên dịch.",
     "Cú pháp câu lệnh", "📝",
     "https://images.unsplash.com/photo-1542838132-92c53300491e?w=600&auto=format&fit=crop&q=80"),

    (9, "Recursion", "/rɪˈkɜː.ʃən/", "noun", "programming", "Lập trình",
     "Đệ quy: kỹ thuật lập trình trong đó một hàm tự gọi lại chính nó để giải quyết các bài toán con nhỏ hơn.",
     "Binary tree traversals are most elegantly implemented using recursion with a base case.",
     "Duyệt cây nhị phân được cài đặt tao nhã nhất bằng cách sử dụng đệ quy có điều kiện dừng cơ sở.",
     "Hàm đệ quy lặp", "🔁",
     "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    (10, "Inheritance", "/ɪnˈher.ɪ.təns/", "noun", "programming", "Lập trình",
     "Kế thừa: nguyên lý hướng đối tượng cho phép một lớp con thừa hưởng thuộc tính và phương thức từ lớp cha.",
     "Through class inheritance, the ElectricCar class automatically inherits engine attributes from Vehicle.",
     "Thông qua tính kế thừa lớp, lớp ElectricCar tự động thừa hưởng các thuộc tính động cơ từ lớp Vehicle.",
     "Kế thừa hướng đối tượng", "🧬",
     "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    (11, "Polymorphism", "/ˌpɒl.iˈmɔː.fɪ.zəm/", "noun", "programming", "Lập trình",
     "Tính đa hình: khả năng các đối tượng khác nhau có thể phản hồi cùng một thông điệp/phương thức theo những cách riêng.",
     "Polymorphism allows our payment gateway to process credit cards, PayPal, and crypto through one method.",
     "Tính đa hình cho phép cổng thanh toán xử lý thẻ tín dụng, PayPal và tiền mã hóa qua cùng một phương thức.",
     "Đa hình đối tượng", "🎭",
     "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=600&auto=format&fit=crop&q=80"),

    (12, "Encapsulation", "/ɪnˌkæp.sjəˈleɪ.ʃən/", "noun", "programming", "Lập trình",
     "Đóng gói: cơ chế giấu kín dữ liệu nội bộ của đối tượng và chỉ cho phép truy xuất qua các phương thức công khai (getters/setters).",
     "Encapsulation protects sensitive internal object states from unauthorized external mutations.",
     "Tính đóng gói bảo vệ trạng thái nội bộ nhạy cảm của đối tượng khỏi những biến đổi trái phép từ bên ngoài.",
     "Đóng gói bảo vệ dữ liệu", "💊",
     "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    (13, "Asynchronous", "/eɪˈsɪŋ.krə.nəs/", "adjective", "programming", "Lập trình",
     "Bất đồng bộ (Async): phương thức thực thi không làm gián đoạn luồng chính, cho phép xử lý tác vụ nền mà không chặn chương trình.",
     "We used asynchronous JavaScript functions to fetch remote weather data without freezing the user interface.",
     "Chúng tôi sử dụng các hàm JavaScript bất đồng bộ để lấy dữ liệu thời tiết từ xa mà không làm đơ giao diện người dùng.",
     "Xử lý bất đồng bộ", "⚡",
     "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=600&auto=format&fit=crop&q=80"),

    (14, "Dependency", "/dɪˈpen.dən.si/", "noun", "programming", "Lập trình",
     "Sự phụ thuộc / Thư viện phụ thuộc: một thư viện, mô-đun hoặc gói mã ngoài mà phần mềm cần để hoạt động.",
     "The package manager scans the manifest file and installs all required project dependencies.",
     "Trình quản lý gói quét tệp kê khai và tự động cài đặt toàn bộ các thư viện phụ thuộc cần thiết cho dự án.",
     "Thư viện phụ thuộc", "🔗",
     "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    (15, "Deprecated", "/ˈdep.rə.keɪ.tɪd/", "adjective", "programming", "Lập trình",
     "Lỗi thời / Ngừng hỗ trợ: tính năng hoặc hàm cũ vẫn hoạt động nhưng không được khuyến khích sử dụng và sẽ bị xóa bỏ trong tương lai.",
     "This API endpoint is deprecated and will be permanently removed in version 3.0.",
     "Điểm cuối API này đã lỗi thời và sẽ bị xóa bỏ vĩnh viễn trong phiên bản 3.0.",
     "Hàm lỗi thời ngừng hỗ trợ", "⚠️",
     "https://images.unsplash.com/photo-1508873696983-2df5293cb395?w=600&auto=format&fit=crop&q=80"),

    (16, "Concurrency", "/kənˈkʌr.ən.si/", "noun", "programming", "Lập trình",
     "Đồng thời: khả năng của hệ thống thực thi hoặc xử lý nhiều tác vụ cùng một lúc trong một khoảng thời gian.",
     "Go language features goroutines that make handling high network concurrency simple and memory-efficient.",
     "Ngôn ngữ Go sở hữu goroutine giúp việc xử lý mức độ đồng thời cao của mạng trở nên đơn giản và tiết kiệm bộ nhớ.",
     "Xử lý đồng thời đa luồng", "🔀",
     "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    (17, "Boilerplate", "/ˈbɔɪ.lər.pleɪt/", "noun", "programming", "Lập trình",
     "Mã mẫu khuôn sẵn: những đoạn mã chuẩn lặp đi lặp lại bắt buộc phải có để khởi tạo dự án.",
     "Modern CLI generators eliminate boilerplate code by creating ready-to-run skeleton apps.",
     "Các bộ tạo mã dòng lệnh hiện đại giúp loại bỏ mã mẫu thừa thãi bằng cách dựng sẵn khung sườn ứng dụng hoàn chỉnh.",
     "Mã mẫu khởi tạo", "📋",
     "https://images.unsplash.com/photo-1484480974693-6ca0a78fb36b?w=600&auto=format&fit=crop&q=80"),

    (18, "Immutable", "/ɪˈmjuː.tə.bəl/", "adjective", "programming", "Lập trình",
     "Bất biến: dữ liệu hoặc đối tượng không thể bị thay đổi giá trị sau khi đã được khởi tạo.",
     "In functional programming, immutable data structures prevent unexpected side effects across threads.",
     "Trong lập trình hàm, các cấu trúc dữ liệu bất biến giúp ngăn ngừa các tác dụng phụ ngoài ý muốn giữa các luồng.",
     "Dữ liệu bất biến", "🔒",
     "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    # -------------------------------------------------------------
    # 2. CƠ SỞ DỮ LIỆU & DỮ LIỆU LỚN (DATABASES & BIG DATA)
    # -------------------------------------------------------------
    (19, "Schema", "/ˈskiː.mə/", "noun", "database", "Cơ sở dữ liệu",
     "Lược đồ cơ sở dữ liệu: cấu trúc khung định nghĩa bảng, các trường dữ liệu, kiểu dữ liệu và mối quan hệ giữa chúng.",
     "The database administrator altered the schema to add an email verification timestamp column.",
     "Quản trị viên cơ sở dữ liệu đã sửa đổi lược đồ để thêm cột mốc thời gian xác thực email.",
     "Lược đồ bảng dữ liệu", "🗂️",
     "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    (20, "Query", "/ˈkwɪə.ri/", "noun", "database", "Cơ sở dữ liệu",
     "Truy vấn: câu lệnh (như SQL) gửi tới hệ quản trị cơ sở dữ liệu để tìm kiếm, lấy hoặc cập nhật dữ liệu.",
     "Optimizing the SQL query reduced the dashboard load time from four seconds to fifty milliseconds.",
     "Việc tối ưu câu truy vấn SQL đã giảm thời gian tải bảng điều khiển từ bốn giây xuống còn năm mươi mili-giây.",
     "Câu lệnh truy vấn SQL", "🔍",
     "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    (21, "Transaction", "/trænˈzæk.ʃən/", "noun", "database", "Cơ sở dữ liệu",
     "Giao dịch: một chuỗi thao tác cơ sở dữ liệu được thực thi như một đơn vị duy nhất (hoặc thành công hết, hoặc hủy bỏ hết).",
     "Financial banking systems use database transactions to guarantee money is never debited without being credited.",
     "Hệ thống ngân hàng tài chính sử dụng giao dịch cơ sở dữ liệu để đảm bảo tiền không bao giờ bị trừ mà chưa được ghi có.",
     "Giao dịch an toàn ACID", "💳",
     "https://images.unsplash.com/photo-1556742049-0a67e5572244?w=600&auto=format&fit=crop&q=80"),

    (22, "Index", "/ˈɪn.deks/", "noun", "database", "Cơ sở dữ liệu",
     "Chỉ mục (Index): cấu trúc dữ liệu phụ trợ giúp hệ thống tăng tốc độ tìm kiếm bản ghi mà không phải quét toàn bộ bảng.",
     "Creating a B-tree index on the user email column drastically accelerated login authentication lookups.",
     "Tạo chỉ mục cây B-tree trên cột email người dùng đã tăng tốc đột phá việc tra cứu xác thực đăng nhập.",
     "Chỉ mục tăng tốc tìm kiếm", "⚡",
     "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    (23, "Sharding", "/ˈʃɑː.dɪŋ/", "noun", "database", "Cơ sở dữ liệu",
     "Phân mảnh (Sharding): kỹ thuật chia nhỏ một cơ sở dữ liệu khổng lồ thành nhiều phần nhỏ (shard) đặt trên các máy chủ khác nhau.",
     "Database sharding allowed the social network to scale horizontally to hundreds of millions of daily active users.",
     "Phân mảnh cơ sở dữ liệu đã cho phép mạng xã hội mở rộng theo chiều ngang tới hàng trăm triệu người dùng hàng ngày.",
     "Phân mảnh dữ liệu phân tán", "🧩",
     "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    (24, "Replication", "/ˌrep.lɪˈkeɪ.ʃən/", "noun", "database", "Cơ sở dữ liệu",
     "Nhân bản dữ liệu: quá trình sao chép dữ liệu từ máy chủ chính (primary) sang nhiều máy chủ phụ (replica) để dự phòng và chia tải đọc.",
     "Primary-replica replication ensures our service remains online even if one database server suffers hardware failure.",
     "Nhân bản chính-phụ đảm bảo dịch vụ của chúng tôi luôn trực tuyến ngay cả khi một máy chủ cơ sở dữ liệu bị hỏng phần cứng.",
     "Nhân bản dự phòng dữ liệu", "👯",
     "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&auto=format&fit=crop&q=80"),

    (25, "Normalization", "/ˌnɔː.məl.aɪˈzeɪ.ʃən/", "noun", "database", "Cơ sở dữ liệu",
     "Chuẩn hóa dữ liệu: quá trình tổ chức cấu trúc bảng nhằm giảm thiểu tối đa sự dư thừa dữ liệu và tránh bất thường khi cập nhật.",
     "Third normal form (3NF) database normalization eliminates duplicate storage of customer postal addresses.",
     "Chuẩn hóa cơ sở dữ liệu dạng chuẩn 3 (3NF) giúp loại bỏ việc lưu trữ trùng lặp địa chỉ bưu chính của khách hàng.",
     "Chuẩn hóa cấu trúc bảng", "📐",
     "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    (26, "Migration", "/maɪˈɡreɪ.ʃən/", "noun", "database", "Cơ sở dữ liệu",
     "Chuyển dịch dữ liệu: việc chạy các tệp lệnh có phiên bản để nâng cấp cấu trúc bảng dữ liệu một cách an toàn và tự động.",
     "Run the migration script to apply the latest database table modifications before starting the server.",
     "Hãy chạy tập lệnh di trú dữ liệu để áp dụng các thay đổi bảng mới nhất trước khi khởi động máy chủ.",
     "Di chuyển lược đồ dữ liệu", "🚚",
     "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=600&auto=format&fit=crop&q=80"),

    (27, "Deadlock", "/ˈded.lɒk/", "noun", "database", "Cơ sở dữ liệu",
     "Bế tắc (Deadlock): tình huống hai hay nhiều tiến trình cùng chờ đợi tài nguyên bị khóa bởi tiến trình kia, dẫn tới đứng nghẽn hệ thống.",
     "The database engine detected a transaction deadlock and automatically aborted the younger query.",
     "Công cụ cơ sở dữ liệu đã phát hiện sự bế tắc giao dịch và tự động hủy truy vấn được thực hiện sau.",
     "Bế tắc khóa tài nguyên", "🛑",
     "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    (28, "NoSQL", "/ˌnoʊˈes.kjuːˈel/", "noun", "database", "Cơ sở dữ liệu",
     "Cơ sở dữ liệu phi quan hệ: hệ cơ sở dữ liệu không dùng bảng quan hệ truyền thống, chuyên xử lý tài liệu JSON, khóa-giá trị hoặc đồ thị.",
     "MongoDB and Redis are popular NoSQL databases favored for flexible unstructured JSON data storage.",
     "MongoDB và Redis là những cơ sở dữ liệu NoSQL phổ biến được ưa chuộng để lưu trữ dữ liệu JSON phi cấu trúc linh hoạt.",
     "Cơ sở dữ liệu phi quan hệ", "📄",
     "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    # -------------------------------------------------------------
    # 3. MẠNG MÁY TÍNH & AN NINH MẠNG (NETWORKING & CYBERSECURITY)
    # -------------------------------------------------------------
    (29, "Encryption", "/ɪnˈkrɪp.ʃən/", "noun", "security", "Mạng & Bảo mật",
     "Mã hóa: quá trình chuyển đổi dữ liệu thô (plaintext) thành dữ liệu bảo mật (ciphertext) để chỉ người có khóa giải mã mới đọc được.",
     "End-to-end encryption guarantees that even the messaging service provider cannot read your private messages.",
     "Mã hóa đầu cuối đảm bảo ngay cả nhà cung cấp dịch vụ nhắn tin cũng không thể đọc được tin nhắn riêng tư của bạn.",
     "Mã hóa bảo mật thông tin", "🔐",
     "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=600&auto=format&fit=crop&q=80"),

    (30, "Authentication", "/ɔːˌθen.tɪˈkeɪ.ʃən/", "noun", "security", "Mạng & Bảo mật",
     "Xác thực: quá trình kiểm tra danh tính người dùng hoặc hệ thống (ví dụ qua mật khẩu, sinh trắc học hoặc OTP 2 lớp).",
     "Two-factor authentication (2FA) significantly reduces the risk of unauthorized account takeovers.",
     "Xác thực hai yếu tố (2FA) giúp giảm thiểu đáng kể nguy cơ tài khoản bị kẻ xấu chiếm đoạt trái phép.",
     "Xác thực danh tính 2FA", "🛡️",
     "https://images.unsplash.com/photo-1563986768609-322da13575f3?w=600&auto=format&fit=crop&q=80"),

    (31, "Vulnerability", "/ˌvʌl.nər.əˈbɪl.ə.ti/", "noun", "security", "Mạng & Bảo mật",
     "Lỗ hổng bảo mật: điểm yếu hoặc thiếu sót trong hệ thống hoặc phần mềm có thể bị tin tặc khai thác để tấn công.",
     "Security researchers discovered a critical remote code execution vulnerability in the open-source library.",
     "Các nhà nghiên cứu bảo mật đã phát hiện một lỗ hổng thực thi mã từ xa cực kỳ nghiêm trọng trong thư viện mã nguồn mở.",
     "Lỗ hổng an ninh mạng", "⚠️",
     "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    (32, "Firewall", "/ˈfaɪə.wɔːl/", "noun", "security", "Mạng & Bảo mật",
     "Tường lửa: hệ thống an ninh mạng giám sát và kiểm soát lưu lượng mạng vào/ra dựa trên các quy tắc an toàn đã thiết lập.",
     "The enterprise network firewall blocked unauthorized incoming connection attempts from suspicious IP addresses.",
     "Tường lửa mạng doanh nghiệp đã chặn các nỗ lực kết nối trái phép đến từ những dải địa chỉ IP đáng ngờ.",
     "Tường lửa ngăn chặn tấn công", "🧱",
     "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=600&auto=format&fit=crop&q=80"),

    (33, "Latency", "/ˈleɪ.tən.si/", "noun", "security", "Mạng & Bảo mật",
     "Độ trễ mạng: khoảng thời gian cần thiết để một gói tin dữ liệu di chuyển từ nguồn gửi đến đích nhận qua đường truyền.",
     "Migrating web servers to edge edge nodes reduced cross-continental network latency from 200ms to 25ms.",
     "Chuyển máy chủ web sang các nút biên mạng đã giảm độ trễ mạng liên lục địa từ 200 mili-giây xuống chỉ còn 25 mili-giây.",
     "Độ trễ đường truyền mạng", "⏱️",
     "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&auto=format&fit=crop&q=80"),

    (34, "Bandwidth", "/ˈbænd.wɪtθ/", "noun", "security", "Mạng & Bảo mật",
     "Băng thông: dung lượng tối đa mà một kết nối mạng có thể truyền tải dữ liệu trong một giây (thường đo bằng Mbps hoặc Gbps).",
     "Streaming ultra-high-definition 4K video requires stable internet bandwidth of at least 25 megabits per second.",
     "Phát trực tuyến video 4K siêu nét đòi hỏi băng thông internet ổn định tối thiểu hai mươi lăm megabit mỗi giây.",
     "Băng thông truyền tải dữ liệu", "📶",
     "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    (35, "Phishing", "/ˈfɪʃ.ɪŋ/", "noun", "security", "Mạng & Bảo mật",
     "Tấn công giả mạo (Phishing): hình thức lừa đảo qua email hoặc tin nhắn giả danh tổ chức uy tín để đánh cắp mật khẩu, thẻ tín dụng.",
     "Employees underwent cybersecurity training to identify spear-phishing emails pretending to come from the CEO.",
     "Nhân viên đã tham gia khóa đào tạo an ninh mạng để nhận biết các email lừa đảo mạo danh Tổng giám đốc.",
     "Tấn công giả mạo lừa đảo", "🎣",
     "https://images.unsplash.com/photo-1563986768609-322da13575f3?w=600&auto=format&fit=crop&q=80"),

    (36, "Proxy", "/ˈprɒk.si/", "noun", "security", "Mạng & Bảo mật",
     "Máy chủ trung gian (Proxy): máy chủ đóng vai trò làm trạm trung chuyển giữa thiết bị của người dùng và internet.",
     "A reverse proxy acts as an intermediary that forwards external client web requests to internal application servers.",
     "Máy chủ proxy ngược đóng vai trò trung gian chuyển tiếp các yêu cầu web từ máy khách bên ngoài đến các máy chủ ứng dụng nội bộ.",
     "Máy chủ trung gian bảo vệ", "🛡️",
     "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    (37, "Zero-day", "/ˌzɪə.roʊˈdeɪ/", "noun", "security", "Mạng & Bảo mật",
     "Lỗ hổng Zero-day: lỗ hổng bảo mật chưa từng được công bố và chưa có bản vá, khiến hệ thống cực kỳ dễ bị tấn công.",
     "Software vendors rushed to release an emergency patch after a zero-day exploit circulated on hacker forums.",
     "Các hãng phần mềm đã tức tốc tung bản vá khẩn cấp sau khi một vụ khai thác zero-day bị phát tán trên diễn đàn tin tặc.",
     "Lỗ hổng chưa có bản vá", "🚨",
     "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    (38, "SSL/TLS", "/ˌes.esˈel/", "noun", "security", "Mạng & Bảo mật",
     "Giao thức mã hóa truyền thông: chứng chỉ bảo mật mã hóa đường truyền giữa trình duyệt web và máy chủ (hiển thị ổ khóa HTTPS).",
     "Installing an SSL certificate enables secure HTTPS browsing and prevents man-in-the-middle eavesdropping.",
     "Cài đặt chứng chỉ SSL kích hoạt duyệt web an toàn qua HTTPS và ngăn chặn việc nghe lén của kẻ đứng giữa.",
     "Chứng chỉ mã hóa HTTPS", "🔒",
     "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=600&auto=format&fit=crop&q=80"),

    # -------------------------------------------------------------
    # 4. ĐIỆN TOÁN ĐÁM MÂY & DEVOPS (CLOUD & DEVOPS)
    # -------------------------------------------------------------
    (39, "Container", "/kənˈteɪ.nər/", "noun", "cloud", "Cloud & DevOps",
     "Bộ chứa (Container): đơn vị phần mềm tiêu chuẩn đóng gói mã nguồn và tất cả các phụ thuộc để ứng dụng chạy ổn định ở mọi môi trường.",
     "Docker containers encapsulate microservices so they run identically on a developer laptop or in the AWS cloud.",
     "Các bộ chứa Docker đóng gói các vi dịch vụ để chúng chạy giống hệt nhau trên laptop lập trình viên hay trên đám mây AWS.",
     "Đóng gói bộ chứa Docker", "📦",
     "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    (40, "Scalability", "/ˌskeɪ.ləˈbɪl.ə.ti/", "noun", "cloud", "Cloud & DevOps",
     "Khả năng mở rộng: năng lực của hệ thống thích ứng và xử lý khối lượng công việc ngày càng tăng mà không làm giảm hiệu năng.",
     "Cloud infrastructure offers elastic scalability by provisioning additional virtual servers during traffic spikes.",
     "Hạ tầng đám mây cung cấp khả năng co giãn linh hoạt bằng cách tự động cấp thêm máy chủ ảo khi lượng truy cập tăng vọt.",
     "Mở rộng tải linh hoạt", "📈",
     "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&auto=format&fit=crop&q=80"),

    (41, "Microservices", "/ˈmaɪ.kroʊˌsɜː.vɪ.sɪz/", "noun", "cloud", "Cloud & DevOps",
     "Kiến trúc vi dịch vụ: phương pháp thiết kế phần mềm thành một chuỗi các dịch vụ nhỏ độc lập, giao tiếp với nhau qua API.",
     "Transitioning from a monolithic architecture to microservices allowed teams to deploy features autonomously.",
     "Chuyển đổi từ kiến trúc nguyên khối sang vi dịch vụ cho phép các nhóm phát triển triển khai tính năng độc lập với nhau.",
     "Kiến trúc vi dịch vụ", "🧩",
     "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    (42, "CI/CD", "/ˌsiː.aɪ ˌsiːˈdiː/", "noun", "cloud", "Cloud & DevOps",
     "Tích hợp liên tục & Triển khai liên tục: quy trình tự động hóa kiểm thử mã nguồn mới và phát hành phần mềm liên tục.",
     "Setting up a CI/CD pipeline ensures automated unit tests run every time code is pushed to GitHub.",
     "Thiết lập quy trình CI/CD đảm bảo các bài kiểm thử đơn vị tự động chạy mỗi khi mã nguồn được đẩy lên GitHub.",
     "Tự động hóa tích hợp & triển khai", "🔄",
     "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600&auto=format&fit=crop&q=80"),

    (43, "Serverless", "/ˈsɜː.və.ləs/", "adjective", "cloud", "Cloud & DevOps",
     "Không máy chủ (Serverless): mô hình điện toán đám mây nơi nhà cung cấp tự quản lý máy chủ, lập trình viên chỉ cần viết code và trả phí theo lượt chạy.",
     "Using serverless AWS Lambda functions saved the company thousands of dollars on idle cloud compute costs.",
     "Sử dụng các hàm không máy chủ AWS Lambda đã tiết kiệm cho công ty hàng nghìn đô la chi phí máy chủ chạy không tải.",
     "Điện toán không máy chủ", "☁️",
     "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    (44, "Load Balancer", "/ˈloʊd ˌbæl.ən.sər/", "noun", "cloud", "Cloud & DevOps",
     "Bộ cân bằng tải: thiết bị phân bổ lưu lượng mạng truy cập đồng đều tới nhiều máy chủ để tối ưu hiệu suất và ngăn quá tải.",
     "The load balancer routes user requests to healthy servers, preventing any single machine from crashing under load.",
     "Bộ cân bằng tải điều phối yêu cầu người dùng tới các máy chủ khỏe mạnh, ngăn ngừa nguy cơ một máy chủ bị sập do quá tải.",
     "Cân bằng tải lưu lượng", "⚖️",
     "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    (45, "Kubernetes", "/ˌkjuː.bərˈnet.iːz/", "noun", "cloud", "Cloud & DevOps",
     "K8s: hệ thống mã nguồn mở hàng đầu dùng để tự động hóa việc triển khai, mở rộng và quản lý các ứng dụng dạng container.",
     "Kubernetes automatically restarts failed containers and schedules workloads across a cluster of server nodes.",
     "Kubernetes tự động khởi động lại các container bị lỗi và điều phối khối lượng công việc trên một cụm máy chủ.",
     "Điều phối cụm container K8s", "☸️",
     "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&auto=format&fit=crop&q=80"),

    (46, "Infrastructure as Code", "/ˈɪn.frəˌstrʌk.tʃər æz koʊd/", "noun", "cloud", "Cloud & DevOps",
     "Hạ tầng như mã nguồn (IaC): việc quản lý và cấp phát hạ tầng CNTT (máy chủ, mạng) thông qua các tệp cấu hình mã thay vì thao tác tay.",
     "Terraform enables teams to manage multi-cloud infrastructure as code with version-controlled state files.",
     "Terraform cho phép các đội ngũ quản lý hạ tầng đa đám mây dưới dạng mã nguồn với các tệp trạng thái có lưu vết phiên bản.",
     "Quản lý hạ tầng bằng mã", "📜",
     "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    # -------------------------------------------------------------
    # 5. TRÍ TUỆ NHÂN TẠO & KHOA HỌC DỮ LIỆU (AI & MACHINE LEARNING)
    # -------------------------------------------------------------
    (47, "Neural Network", "/ˈnjʊə.rəl ˈnet.wɜːk/", "noun", "ai", "Trí tuệ nhân tạo (AI)",
     "Mạng nơ-ron: mô hình điện toán lấy cảm hứng từ não người, gồm các lớp nút kết nối với nhau để nhận diện mẫu phức tạp.",
     "Deep convolutional neural networks achieve superhuman accuracy in medical image cancer diagnosis.",
     "Mạng nơ-ron tích chập sâu đạt được độ chính xác vượt trội hơn con người trong chẩn đoán ung thư qua hình ảnh y tế.",
     "Mạng nơ-ron nhân tạo", "🧠",
     "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=600&auto=format&fit=crop&q=80"),

    (48, "Overfitting", "/ˌoʊ.vərˈfɪt.ɪŋ/", "noun", "ai", "Trí tuệ nhân tạo (AI)",
     "Hiện tượng quá khớp: mô hình AI học vẹt dữ liệu huấn luyện quá mức khiến nó đạt điểm cao trên tập cũ nhưng dự đoán tệ trên dữ liệu mới.",
     "Dropout layers and data augmentation are widely used to prevent deep learning models from overfitting.",
     "Các lớp dropout và tăng cường dữ liệu được sử dụng rộng rãi để ngăn chặn mô hình học sâu bị hiện tượng quá khớp.",
     "Mô hình học vẹt quá khớp", "📉",
     "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    (49, "Epoch", "/ˈiː.pɒk/", "noun", "ai", "Trí tuệ nhân tạo (AI)",
     "Kỷ nguyên huấn luyện: một lượt hoàn chỉnh mô hình duyệt qua toàn bộ tập dữ liệu huấn luyện trong quá trình học máy.",
     "The model trained for fifty epochs before its validation loss converged to the global minimum.",
     "Mô hình đã được huấn luyện qua năm mươi kỷ nguyên trước khi độ mất mát xác thực hội tụ về điểm tối thiểu toàn cục.",
     "Vòng huấn luyện dữ liệu", "⏱️",
     "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    (50, "Inference", "/ˈɪn.fər.əns/", "noun", "ai", "Trí tuệ nhân tạo (AI)",
     "Suy luận mô hình: giai đoạn mô hình AI đã hoàn tất huấn luyện được đưa vào sử dụng thực tế để tạo ra các dự đoán mới.",
     "Optimizing AI models using quantization significantly lowers inference latency on mobile smartphones.",
     "Tối ưu mô hình AI bằng kỹ thuật lượng tử hóa giúp giảm đáng kể độ trễ suy luận trên điện thoại thông minh.",
     "Suy luận dự đoán AI", "⚡",
     "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=600&auto=format&fit=crop&q=80"),

    (51, "Fine-tuning", "/ˈfaɪn ˌtjuː.nɪŋ/", "noun", "ai", "Trí tuệ nhân tạo (AI)",
     "Tinh chỉnh mô hình: lấy một mô hình ngôn ngữ lớn (LLM) đã huấn luyện sẵn và tiếp tục dạy nó trên tập dữ liệu chuyên ngành cụ thể.",
     "Medical labs fine-tuned a foundation language model on clinical oncology textbooks to assist doctors.",
     "Phòng thí nghiệm y khoa đã tinh chỉnh mô hình ngôn ngữ nền tảng trên sách giáo khoa ung bướu lâm sàng để hỗ trợ bác sĩ.",
     "Tinh chỉnh mô hình chuyên sâu", "🎯",
     "https://images.unsplash.com/photo-1507668077129-56e32842fceb?w=600&auto=format&fit=crop&q=80"),

    (52, "Hallucination", "/həˌluː.sɪˈneɪ.ʃən/", "noun", "ai", "Trí tuệ nhân tạo (AI)",
     "Ảo giác AI: hiện tượng mô hình ngôn ngữ lớn tự bịa ra thông tin sai lệch nhưng trình bày với thái độ vô cùng tự tin và thuyết phục.",
     "Retrieval-Augmented Generation (RAG) grounds language models in verified documents to minimize AI hallucinations.",
     "Kỹ thuật sinh có bổ trợ tìm kiếm (RAG) ghim mô hình vào tài liệu xác thực để giảm thiểu tối đa hiện tượng ảo giác AI.",
     "Hiện tượng ảo giác AI bịa đặt", "🔮",
     "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=600&auto=format&fit=crop&q=80"),

    (53, "Transformer", "/trænsˈfɔː.mər/", "noun", "ai", "Trí tuệ nhân tạo (AI)",
     "Kiến trúc Transformer: đột phá kiến trúc học sâu dựa trên cơ chế tự chú ý (Self-Attention), nền tảng của GPT, Gemini và Claude.",
     "The Transformer architecture revolutionized artificial intelligence by enabling parallel training over massive text corpora.",
     "Kiến trúc Transformer đã cách mạng hóa trí tuệ nhân tạo bằng cách cho phép huấn luyện song song trên kho văn bản khổng lồ.",
     "Kiến trúc Transformer cốt lõi", "🤖",
     "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=600&auto=format&fit=crop&q=80"),

    (54, "Prompt", "/prɒmpt/", "noun", "ai", "Trí tuệ nhân tạo (AI)",
     "Lời nhắc / Câu lệnh đầu vào: đoạn văn bản hoặc chỉ dẫn mà người dùng gửi cho mô hình trí tuệ nhân tạo để nhận lại kết quả mong muốn.",
     "Crafting a clear, context-rich prompt yields vastly superior responses from conversational generative models.",
     "Soạn một câu lệnh đầu vào rõ ràng và giàu ngữ cảnh sẽ mang lại câu trả lời vượt trội hơn nhiều từ các mô hình tạo sinh.",
     "Câu lệnh lời nhắc AI", "💬",
     "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    # -------------------------------------------------------------
    # 6. PHÁT TRIỂN WEB & MOBILE (WEB & MOBILE ENGINEERING)
    # -------------------------------------------------------------
    (55, "Endpoint", "/ˈend.pɔɪnt/", "noun", "web", "Phát triển Web",
     "Điểm cuối API: một địa chỉ URL cụ thể trên máy chủ cung cấp tài nguyên hoặc xử lý các phương thức GET, POST, PUT, DELETE.",
     "The mobile client sends an HTTP POST request to the `/api/v1/auth/login` endpoint.",
     "Ứng dụng di động gửi một yêu cầu HTTP POST tới điểm cuối `/api/v1/auth/login` để đăng nhập.",
     "Điểm cuối kết nối API", "🌐",
     "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    (56, "Middleware", "/ˈmɪd.əl.weər/", "noun", "web", "Phát triển Web",
     "Phần mềm trung gian: lớp mã nằm giữa yêu cầu gửi đến và xử lý đích, chuyên làm nhiệm vụ xác thực, ghi nhật ký hoặc nén dữ liệu.",
     "We implemented custom authentication middleware to verify JWT bearer tokens before hitting protected routes.",
     "Chúng tôi cài đặt phần mềm trung gian xác thực riêng để kiểm tra token JWT trước khi cho phép truy cập các tuyến bảo mật.",
     "Phần mềm trung gian điều phối", "🛡️",
     "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    (57, "Responsive", "/rɪˈspɒn.sɪv/", "adjective", "web", "Phát triển Web",
     "Giao diện phản hồi linh hoạt: thiết kế web tự động co giãn và bố trí lại giao diện đẹp mắt trên màn hình điện thoại, máy tính bảng và desktop.",
     "Tailwind CSS flexbox utilities make creating fully responsive mobile-first websites fast and intuitive.",
     "Các tiện ích flexbox của Tailwind CSS giúp việc tạo các trang web phản hồi linh hoạt ưu tiên thiết bị di động trở nên nhanh chóng.",
     "Giao diện thích ứng đa màn hình", "📱",
     "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=600&auto=format&fit=crop&q=80"),

    (58, "Cache", "/kæʃ/", "noun", "web", "Phát triển Web",
     "Bộ nhớ đệm (Cache): vùng lưu trữ tốc độ cao tạm thời lưu lại dữ liệu thường dùng để các lần truy cập tiếp theo diễn ra tức thì.",
     "Configuring browser cache headers prevents repeated downloads of static CSS stylesheets and banner images.",
     "Cấu hình tiêu đề bộ nhớ đệm trình duyệt ngăn chặn việc tải lại nhiều lần các tệp CSS và hình ảnh biểu ngữ tĩnh.",
     "Bộ nhớ đệm tăng tốc web", "⚡",
     "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    (59, "State Management", "/steɪt ˈmæn.ɪdʒ.mənt/", "noun", "web", "Phát triển Web",
     "Quản lý trạng thái: cách tổ chức, lưu trữ và đồng bộ hóa trạng thái giao diện và dữ liệu người dùng trên toàn ứng dụng.",
     "Redux and Zustand provide predictable centralized state management for complex React frontends.",
     "Redux và Zustand cung cấp giải pháp quản lý trạng thái tập trung và dễ dự đoán cho các ứng dụng React phức tạp.",
     "Quản lý trạng thái ứng dụng", "🎛️",
     "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    (60, "Webhook", "/ˈweb.hʊk/", "noun", "web", "Phát triển Web",
     "Gọi ngược tự động (Webhook): cơ chế gửi thông báo tự động (HTTP POST) theo thời gian thực từ hệ thống này sang hệ thống khác khi có sự kiện phát sinh.",
     "Stripe automatically triggers a secure webhook to notify our backend whenever a customer subscription renews.",
     "Stripe tự động kích hoạt một webhook bảo mật để thông báo cho máy chủ của chúng tôi mỗi khi gói đăng ký của khách hàng được gia hạn.",
     "Gọi ngược thời gian thực", "🔔",
     "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?w=600&auto=format&fit=crop&q=80")
]

# Color palettes for IT cards
GRADIENTS_IT = [
    "from-cyan-600 to-blue-700",
    "from-indigo-600 to-violet-800",
    "from-emerald-600 to-teal-700",
    "from-fuchsia-600 to-purple-800",
    "from-blue-600 to-indigo-800",
    "from-amber-600 to-orange-700"
]

formatted_it_terms = []
for item in it_terms_raw:
    tid, term, ipa, pos, subcat, subcat_vi, meaning, example, example_vi, concept_tag, icon, img_url = item
    gradient = GRADIENTS_IT[tid % len(GRADIENTS_IT)]
    
    formatted_it_terms.append({
        "id": tid,
        "term": term,
        "ipa": ipa,
        "partOfSpeech": pos,
        "subCategory": subcat,
        "subCategoryVi": subcat_vi,
        "meaning": meaning,
        "example": example,
        "exampleVi": example_vi,
        "conceptTag": concept_tag,
        "icon": icon,
        "gradient": gradient,
        "image": img_url
    })

# Save JSON and JS
with open("/home/ken/.gemini/antigravity/scratch/irregular-verbs-360/it_terms_data.json", "w", encoding="utf-8") as f:
    json.dump(formatted_it_terms, f, ensure_ascii=False, indent=2)

js_content = "window.IT_TERMS_DATA = " + json.dumps(formatted_it_terms, ensure_ascii=False, indent=2) + ";\n"
with open("/home/ken/.gemini/antigravity/scratch/irregular-verbs-360/it_terms_data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Successfully generated {len(formatted_it_terms)} IT English terms database!")

more_terms = [
    # Programming & Architecture
    (61, "Pull Request", "/pʊl rɪˈkwest/", "noun", "programming", "Lập trình",
     "Yêu cầu kéo mã (PR): đề xuất trộn các thay đổi mã nguồn từ một nhánh nhánh vào nhánh chính để các lập trình viên khác bình duyệt.",
     "The team lead reviewed the pull request, left code comments, and approved the merge into main.",
     "Trưởng nhóm đã xem xét yêu cầu kéo mã, để lại nhận xét và phê duyệt việc gộp vào nhánh chính.",
     "Yêu cầu gộp mã nguồn", "🔀",
     "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?w=600&auto=format&fit=crop&q=80"),

    (62, "Merge Conflict", "/mɜːdʒ ˈkɒn.flɪkt/", "noun", "programming", "Lập trình",
     "Xung đột trộn mã: sự cố xảy ra khi hai người cùng sửa đổi các dòng mã giống nhau trên cùng một tệp trong Git.",
     "We resolved the Git merge conflict manually by deciding which team's changes to retain.",
     "Chúng tôi đã xử lý xung đột trộn mã Git bằng tay bằng cách quyết định giữ lại phần sửa đổi của nhóm nào.",
     "Xung đột phiên bản mã", "💥",
     "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    (63, "Garbage Collection", "/ˈɡɑː.bɪdʒ kəˈlek.ʃən/", "noun", "programming", "Lập trình",
     "Thu gom rác tự động: cơ chế quản lý bộ nhớ tự động giải phóng vùng nhớ heap của các đối tượng không còn được sử dụng.",
     "The Java Virtual Machine runs garbage collection in the background to reclaim allocated heap space.",
     "Máy ảo Java chạy trình thu gom rác ngầm để thu hồi không gian bộ nhớ heap đã cấp phát.",
     "Dọn dẹp bộ nhớ tự động", "🧹",
     "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    (64, "Race Condition", "/reɪs kənˈdɪʃ.ən/", "noun", "programming", "Lập trình",
     "Tình trạng tranh chấp (Race condition): lỗi phần mềm xảy ra khi kết quả đầu ra phụ thuộc vào thứ tự thực thi không lường trước giữa các luồng.",
     "Using mutex locks prevents race conditions when concurrent worker threads update bank balances.",
     "Sử dụng khóa mutex giúp ngăn chặn tình trạng tranh chấp khi các luồng chạy đồng thời cùng cập nhật số dư ngân hàng.",
     "Tranh chấp luồng dữ liệu", "🏁",
     "https://images.unsplash.com/photo-1542282088-72c9c27ed0cd?w=600&auto=format&fit=crop&q=80"),

    (65, "Memory Leak", "/ˈmem.ər.i liːk/", "noun", "programming", "Lập trình",
     "Rò rỉ bộ nhớ: hiện tượng chương trình máy tính liên tục cấp phát RAM nhưng không giải phóng, dẫn tới cạn kiệt bộ nhớ và sập máy.",
     "Unregistered event listeners caused a severe memory leak that made the browser tab consume 4GB of RAM.",
     "Các hàm lắng nghe sự kiện không được hủy đăng ký đã gây ra rò rỉ bộ nhớ nghiêm trọng khiến tab trình duyệt ngốn tới 4GB RAM.",
     "Rò rỉ cạn kiệt RAM", "💧",
     "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    (66, "Agile", "/ˈædʒ.aɪl/", "noun", "programming", "Lập trình",
     "Phương pháp luận Agile: mô hình phát triển phần mềm linh hoạt, chia nhỏ dự án thành các chu kỳ ngắn để thích ứng nhanh với thay đổi.",
     "Our software engineering team follows Agile principles with daily standups and bi-weekly sprint demos.",
     "Đội ngũ kỹ thuật phần mềm của chúng tôi tuân theo các nguyên lý Agile với các cuộc họp đứng hàng ngày và báo cáo sprint hai tuần một lần.",
     "Phương pháp phát triển linh hoạt", "🏃",
     "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=600&auto=format&fit=crop&q=80"),

    (67, "Scrum", "/skrʌm/", "noun", "programming", "Lập trình",
     "Khung làm việc Scrum: phương pháp quản lý dự án Agile phổ biến nhất, tổ chức công việc theo Sprint và các vai trò Product Owner, Scrum Master.",
     "During the sprint retrospective, the Scrum team discussed blockers and brainstormed process improvements.",
     "Trong buổi họp hồi cứu sprint, nhóm Scrum đã thảo luận các trở ngại và cùng đề xuất cải tiến quy trình.",
     "Khung quản lý dự án Scrum", "🏉",
     "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?w=600&auto=format&fit=crop&q=80"),

    # Database
    (68, "ACID Properties", "/ˈæs.ɪd ˈprɒp.ə.tiz/", "noun", "database", "Cơ sở dữ liệu",
     "Thuộc tính ACID: 4 tiêu chuẩn vàng bảo đảm độ tin cậy của giao dịch cơ sở dữ liệu: Tính nguyên tố, Tính nhất quán, Tính cô lập và Tính bền vững.",
     "Relational databases guarantee ACID properties to maintain data integrity during hardware outages.",
     "Các cơ sở dữ liệu quan hệ bảo đảm các thuộc tính ACID để duy trì tính toàn vẹn dữ liệu ngay cả khi gặp sự cố phần cứng.",
     "4 tiêu chuẩn vàng ACID", "🏛️",
     "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    (69, "Throughput", "/ˈθruː.pʊt/", "noun", "database", "Cơ sở dữ liệu",
     "Thông lượng: số lượng giao dịch, truy vấn hoặc khối lượng dữ liệu mà hệ thống có thể xử lý thành công trong một đơn vị thời gian (TPS/QPS).",
     "Upgrading to solid-state NVMe drives increased database write throughput to 50,000 queries per second.",
     "Nâng cấp lên ổ cứng SSD NVMe đã tăng thông lượng ghi cơ sở dữ liệu lên năm mươi nghìn truy vấn mỗi giây.",
     "Thông lượng xử lý dữ liệu", "⚡",
     "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    (70, "Data Warehouse", "/ˈdeɪ.tə ˈweə.haʊs/", "noun", "database", "Cơ sở dữ liệu",
     "Kho dữ liệu lớn (DWH): kho lưu trữ trung tâm tích hợp dữ liệu từ nhiều nguồn khác nhau, phục vụ việc phân tích kinh doanh và báo cáo BI.",
     "Business intelligence analysts query the Snowflake data warehouse to forecast quarterly sales trends.",
     "Các chuyên viên phân tích kinh doanh truy vấn kho dữ liệu Snowflake để dự báo xu hướng doanh số hàng quý.",
     "Kho dữ liệu phân tích BI", "🏢",
     "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    # Security
    (71, "SQL Injection", "/ˌes.kjuːˈel ɪnˈdʒek.ʃən/", "noun", "security", "Mạng & Bảo mật",
     "Tấn công tiêm mã SQL (SQLi): lỗ hổng bảo mật cho phép kẻ tấn công chèn các câu lệnh SQL độc hại vào trường nhập liệu để đánh cắp cơ sở dữ liệu.",
     "Using parameterized queries and prepared statements completely prevents SQL injection attacks.",
     "Sử dụng truy vấn có tham số và câu lệnh chuẩn bị sẵn giúp ngăn chặn hoàn toàn các cuộc tấn công tiêm mã SQL.",
     "Lỗ hổng tiêm mã SQL độc hại", "💉",
     "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    (72, "Cross-Site Scripting (XSS)", "/ˌkrɒs.saɪt ˈskrɪp.tɪŋ/", "noun", "security", "Mạng & Bảo mật",
     "Lỗ hổng XSS: kiểu tấn công chèn mã JavaScript độc hại vào trang web để mã đó tự động chạy trên trình duyệt của người dùng khác.",
     "Modern web frameworks sanitize user inputs automatically to guard against cross-site scripting attacks.",
     "Các bộ khung web hiện đại tự động làm sạch dữ liệu người dùng nhập vào để phòng vệ trước các cuộc tấn công XSS.",
     "Tấn công mã độc XSS", "☣️",
     "https://images.unsplash.com/photo-1563986768609-322da13575f3?w=600&auto=format&fit=crop&q=80"),

    (73, "DDoS Attack", "/ˌdiːˈdɒs əˈtæk/", "noun", "security", "Mạng & Bảo mật",
     "Tấn công từ chối dịch vụ phân tán: hành vi dùng mạng máy tính ma (botnet) gửi ồ ạt lưu lượng rác nhằm làm tê liệt máy chủ mục tiêu.",
     "Cloudflare successfully mitigated a massive multi-terabit distributed denial-of-service attack.",
     "Cloudflare đã giảm thiểu thành công một cuộc tấn công từ chối dịch vụ phân tán khổng lồ lên tới hàng terabit.",
     "Tấn công tràn lưu lượng DDoS", "🌊",
     "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=600&auto=format&fit=crop&q=80"),

    (74, "Public Key Infrastructure", "/ˈpʌb.lɪk kiː/", "noun", "security", "Mạng & Bảo mật",
     "Hạ tầng khóa công khai (PKI): hệ thống sử dụng cặp khóa bất đối xứng (khóa công khai để mã hóa, khóa bí mật để giải mã) để bảo mật thông tin.",
     "Asymmetric cryptography uses a public key to encrypt data and a private key to decrypt it.",
     "Mật mã học bất đối xứng sử dụng khóa công khai để mã hóa dữ liệu và khóa bí mật để giải mã dữ liệu đó.",
     "Cặp khóa mã hóa công khai", "🔑",
     "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=600&auto=format&fit=crop&q=80"),

    (75, "OAuth", "/ˈoʊ.ɔːθ/", "noun", "security", "Mạng & Bảo mật",
     "Giao thức ủy quyền OAuth: chuẩn bảo mật cho phép người dùng đăng nhập bằng tài khoản Google, GitHub mà không cần tiết lộ mật khẩu gốc.",
     "Websites implement OAuth 2.0 to allow seamless 'Sign in with Google' authentication.",
     "Các trang web triển khai OAuth 2.0 để cho phép xác thực đăng nhập một chạm thuận tiện thông qua tài khoản Google.",
     "Giao thức ủy quyền tài khoản", "🎫",
     "https://images.unsplash.com/photo-1563986768609-322da13575f3?w=600&auto=format&fit=crop&q=80"),

    # Cloud & DevOps
    (76, "Virtualization", "/ˌvɜː.tʃu.əl.aɪˈzeɪ.ʃən/", "noun", "cloud", "Cloud & DevOps",
     "Ảo hóa: công nghệ cho phép tạo ra nhiều máy ảo (VM) độc lập chạy cùng lúc trên một phần cứng vật lý duy nhất.",
     "Hardware virtualization enables multiple operating systems to share physical CPU and memory resources.",
     "Ảo hóa phần cứng cho phép nhiều hệ điều hành cùng chia sẻ tài nguyên CPU và bộ nhớ vật lý.",
     "Công nghệ máy ảo độc lập", "🖥️",
     "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&auto=format&fit=crop&q=80"),

    (77, "Auto-scaling", "/ˈɔː.toʊˌskeɪ.lɪŋ/", "noun", "cloud", "Cloud & DevOps",
     "Tự động co giãn: tính năng đám mây tự động tăng hoặc giảm số lượng máy chủ dựa trên lưu lượng người dùng thực tế theo thời gian thực.",
     "Auto-scaling automatically launched fifty additional server instances during the Black Friday flash sale.",
     "Tính năng tự động co giãn đã tự kích hoạt thêm năm mươi máy chủ trong đợt giảm giá chớp nhoáng ngày Black Friday.",
     "Tự động tăng giảm máy chủ", "📈",
     "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600&auto=format&fit=crop&q=80"),

    (78, "High Availability", "/haɪ əˌveɪ.ləˈbɪl.ə.ti/", "noun", "cloud", "Cloud & DevOps",
     "Tính sẵn sàng cao (HA): thiết kế hệ thống đảm bảo dịch vụ luôn hoạt động liên tục (đạt tỷ lệ 99.999% thời gian uptime) không bị gián đoạn.",
     "Deploying services across multiple availability zones guarantees high availability even if a data center loses power.",
     "Triển khai dịch vụ trên nhiều vùng sẵn sàng bảo đảm hệ thống luôn trực tuyến ngay cả khi một trung tâm dữ liệu bị mất điện.",
     "Sẵn sàng hoạt động 99.999%", "🟢",
     "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    # AI & Machine Learning
    (79, "Vector Database", "/ˈvek.tər ˈdeɪ.tə.beɪs/", "noun", "ai", "Trí tuệ nhân tạo (AI)",
     "Cơ sở dữ liệu vectơ: hệ cơ sở dữ liệu chuyên lưu trữ và tìm kiếm các vectơ nhúng ngữ nghĩa (embeddings) cho các ứng dụng AI tạo sinh.",
     "Pinecone and Milvus are dedicated vector databases optimized for millisecond similarity searches in RAG apps.",
     "Pinecone và Milvus là các cơ sở dữ liệu vectơ chuyên dụng được tối ưu hóa cho việc tìm kiếm độ tương đồng trong vài mili-giây cho ứng dụng RAG.",
     "Cơ sở dữ liệu vectơ ngữ nghĩa", "🧭",
     "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=600&auto=format&fit=crop&q=80"),

    (80, "Embedding", "/ɪmˈbed.ɪŋ/", "noun", "ai", "Trí tuệ nhân tạo (AI)",
     "Nhúng vectơ (Embedding): cách chuyển đổi từ ngữ, câu hoặc hình ảnh thành một dãy số thực phản ánh ý nghĩa ngữ nghĩa trong không gian đa chiều.",
     "Semantic embeddings place words with similar meanings close together in high-dimensional vector space.",
     "Các vectơ nhúng ngữ nghĩa đặt các từ có ý nghĩa tương đồng ở vị trí gần nhau trong không gian vectơ nhiều chiều.",
     "Vectơ số hóa ngữ nghĩa", "📊",
     "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    (81, "RAG (Retrieval-Augmented Generation)", "/ræɡ/", "noun", "ai", "Trí tuệ nhân tạo (AI)",
     "Sinh có bổ trợ tìm kiếm: kiến trúc AI kết hợp tìm kiếm tài liệu nội bộ với mô hình ngôn ngữ lớn để trả lời câu hỏi chính xác, không bị ảo giác.",
     "Enterprise chatbots use RAG to answer user questions using internal policy handbooks rather than general knowledge.",
     "Chatbot doanh nghiệp sử dụng kiến trúc RAG để trả lời câu hỏi của nhân viên dựa trên sổ tay quy định nội bộ thay vì tri thức chung.",
     "Kiến trúc AI sinh có tìm kiếm", "📚",
     "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=600&auto=format&fit=crop&q=80"),

    (82, "Large Language Model (LLM)", "/lɑːdʒ ˈlæŋ.ɡwɪdʒ ˈmɒd.əl/", "noun", "ai", "Trí tuệ nhân tạo (AI)",
     "Mô hình ngôn ngữ lớn: mô hình học sâu khổng lồ được huấn luyện trên hàng nghìn tỷ từ để hiểu và tạo ra văn bản tự nhiên như con người.",
     "Modern large language models exhibit advanced reasoning capabilities across law, medicine, and programming.",
     "Các mô hình ngôn ngữ lớn hiện đại thể hiện năng lực lập luận vượt trội trên nhiều lĩnh vực từ luật học, y khoa đến lập trình.",
     "Mô hình ngôn ngữ lớn LLM", "🤖",
     "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=600&auto=format&fit=crop&q=80"),

    (83, "Computer Vision", "/kəmˈpjuː.tər ˈvɪʒ.ən/", "noun", "ai", "Trí tuệ nhân tạo (AI)",
     "Thị giác máy tính: nhánh của AI đào tạo máy tính xử lý và thấu hiểu thế giới thị giác qua camera và hình ảnh kỹ thuật số.",
     "Self-driving vehicles use computer vision models to detect pedestrians, road lanes, and traffic lights in real time.",
     "Xe tự hành ứng dụng các mô hình thị giác máy tính để nhận diện người đi bộ, làn đường và đèn giao thông theo thời gian thực.",
     "Thị giác máy tính xe tự hành", "👁️",
     "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=600&auto=format&fit=crop&q=80"),

    # Web & Mobile
    (84, "WebSocket", "/ˈweb.sɒk.ɪt/", "noun", "web", "Phát triển Web",
     "Giao thức WebSocket: công nghệ truyền thông hai chiều thời gian thực toàn phần (full-duplex) qua một kết nối TCP duy nhất.",
     "Live stock trading platforms and multiplayer games use WebSockets for sub-millisecond bidirectional data sync.",
     "Sàn giao dịch chứng khoán trực tiếp và trò chơi nhiều người chơi sử dụng WebSocket để đồng bộ dữ liệu hai chiều siêu tốc.",
     "Truyền dữ liệu 2 chiều realtime", "🔌",
     "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    (85, "RESTful API", "/ˈrest.fʊl eɪ.piːˈaɪ/", "noun", "web", "Phát triển Web",
     "Giao diện lập trình ứng dụng RESTful: kiến trúc chuẩn mực sử dụng các phương thức HTTP (GET, POST, PUT, DELETE) để trao đổi dữ liệu JSON/XML.",
     "The backend exposes a clean RESTful API allowing the mobile iOS and Android apps to communicate seamlessly.",
     "Máy chủ phát triển một giao diện RESTful API chuẩn mực cho phép ứng dụng iOS và Android kết nối mượt mà.",
     "Chuẩn kiến trúc RESTful API", "🌐",
     "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    (86, "Server-Side Rendering (SSR)", "/ˈsɜː.vər saɪd/", "noun", "web", "Phát triển Web",
     "Kết xuất phía máy chủ (SSR): kỹ thuật kết xuất mã HTML hoàn chỉnh ngay trên máy chủ trước khi gửi về trình duyệt, giúp SEO tốt và hiển thị nhanh.",
     "Next.js utilizes server-side rendering so search engine crawlers can index web pages immediately.",
     "Next.js sử dụng kết xuất phía máy chủ để các bọ tìm kiếm có thể lập chỉ mục trang web ngay lập tức.",
     "Kết xuất HTML từ máy chủ", "🖥️",
     "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=600&auto=format&fit=crop&q=80"),

    (87, "GraphQL", "/ˌɡræf.kjuːˈel/", "noun", "web", "Phát triển Web",
     "Ngôn ngữ truy vấn API GraphQL: cho phép máy khách yêu cầu chính xác những trường dữ liệu mình cần, tránh tình trạng lấy thừa hay thiếu dữ liệu.",
     "With GraphQL, the client requests only the user name and avatar, eliminating unwanted network payload.",
     "Với GraphQL, máy khách chỉ yêu cầu đúng tên và ảnh đại diện của người dùng, giúp loại bỏ lượng dữ liệu mạng thừa thãi.",
     "Truy vấn API linh hoạt", "📊",
     "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    (88, "Cross-Origin (CORS)", "/kɔːrz/", "noun", "web", "Phát triển Web",
     "Chia sẻ tài nguyên khác nguồn (CORS): cơ chế bảo mật của trình duyệt ngăn chặn trang web ở tên miền này gửi yêu cầu AJAX sang tên miền khác khi chưa cho phép.",
     "The server must return appropriate CORS headers to permit incoming fetch requests from our frontend domain.",
     "Máy chủ phải trả về các tiêu đề CORS phù hợp để cho phép các yêu cầu fetch từ tên miền giao diện của chúng tôi.",
     "Cơ chế bảo mật tên miền CORS", "🛡️",
     "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=600&auto=format&fit=crop&q=80"),

    (89, "WebAssembly", "/ˌweb.əˈsem.bli/", "noun", "web", "Phát triển Web",
     "Mã nhị phân WebAssembly (Wasm): định dạng mã nhị phân hiệu năng cao cho phép chạy mã C++, Rust trực tiếp trong trình duyệt với tốc độ gần như native.",
     "Figma and Google Earth rely on WebAssembly to deliver near-desktop rendering speeds inside standard web browsers.",
     "Figma và Google Earth dựa vào WebAssembly để đạt được tốc độ kết xuất gần như ứng dụng máy tính ngay trong trình duyệt web.",
     "Mã nhị phân tốc độ cao Wasm", "🚀",
     "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    (90, "JSON Web Token (JWT)", "/ˌdʒeɪ.sɒn web ˈtoʊ.kən/", "noun", "web", "Phát triển Web",
     "Chuỗi mã xác thực JWT: định dạng nhỏ gọn và khép kín dùng để truyền thông tin xác thực an toàn giữa các bên dưới dạng đối tượng JSON ký số.",
     "After logging in, the mobile app stores the JWT token in secure storage and sends it with every API request.",
     "Sau khi đăng nhập thành công, ứng dụng di động lưu chuỗi mã JWT vào vùng nhớ bảo mật và gửi kèm trong mỗi yêu cầu API.",
     "Mã xác thực chữ ký số JWT", "🔑",
     "https://images.unsplash.com/photo-1563986768609-322da13575f3?w=600&auto=format&fit=crop&q=80")
]

for item in more_terms:
    tid, term, ipa, pos, subcat, subcat_vi, meaning, example, example_vi, concept_tag, icon, img_url = item
    gradient = GRADIENTS_IT[tid % len(GRADIENTS_IT)]
    formatted_it_terms.append({
        "id": tid,
        "term": term,
        "ipa": ipa,
        "partOfSpeech": pos,
        "subCategory": subcat,
        "subCategoryVi": subcat_vi,
        "meaning": meaning,
        "example": example,
        "exampleVi": example_vi,
        "conceptTag": concept_tag,
        "icon": icon,
        "gradient": gradient,
        "image": img_url
    })

# Save JSON and JS
with open("/home/ken/.gemini/antigravity/scratch/irregular-verbs-360/it_terms_data.json", "w", encoding="utf-8") as f:
    json.dump(formatted_it_terms, f, ensure_ascii=False, indent=2)

js_content = "window.IT_TERMS_DATA = " + json.dumps(formatted_it_terms, ensure_ascii=False, indent=2) + ";\n"
with open("/home/ken/.gemini/antigravity/scratch/irregular-verbs-360/it_terms_data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Total IT terms updated: {len(formatted_it_terms)}")

final_10 = [
    (91, "API (Application Programming Interface)", "/ˌeɪ.piːˈaɪ/", "noun", "programming", "Lập trình",
     "Giao diện lập trình ứng dụng: tập hợp các quy tắc và cơ chế cho phép các phần mềm và ứng dụng khác nhau giao tiếp và trao đổi dữ liệu.",
     "The weather service provides an open REST API so developers can display temperature data on their apps.",
     "Dịch vụ thời tiết cung cấp một API REST mở để các lập trình viên có thể hiển thị dữ liệu nhiệt độ trên ứng dụng của họ.",
     "Giao diện kết nối API", "🔌",
     "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    (92, "SDK (Software Development Kit)", "/ˌes.diːˈkeɪ/", "noun", "programming", "Lập trình",
     "Bộ công cụ phát triển phần mềm: gói tài nguyên hoàn chỉnh bao gồm thư viện, tài liệu hướng dẫn và trình biên dịch để xây dựng phần mềm trên nền tảng cụ thể.",
     "Apple released the new iOS SDK with updated APIs for augmented reality and machine learning.",
     "Apple đã phát hành bộ công cụ SDK iOS mới kèm các API được nâng cấp cho thực tế ảo tăng cường và học máy.",
     "Bộ công cụ phát triển phần mềm", "🧰",
     "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    (93, "DNS (Domain Name System)", "/ˌdiː.enˈes/", "noun", "security", "Mạng & Bảo mật",
     "Hệ thống phân giải tên miền: danh bạ của Internet, chuyển đổi tên miền thân thiện (google.com) thành địa chỉ IP số học (142.250.190.46).",
     "When DNS servers experience outages, internet users cannot resolve website domain names to their IP addresses.",
     "Khi các máy chủ DNS gặp sự cố, người dùng internet không thể phân giải tên miền trang web sang địa chỉ IP tương ứng.",
     "Hệ thống phân giải tên miền", "🌐",
     "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&auto=format&fit=crop&q=80"),

    (94, "Cookie", "/ˈkʊk.i/", "noun", "web", "Phát triển Web",
     "Tệp cookie: tệp dữ liệu nhỏ được máy chủ gửi tới trình duyệt người dùng để ghi nhớ thông tin đăng nhập, giỏ hàng hoặc tùy chọn cá nhân.",
     "Secure HTTP-only cookies prevent malicious cross-site scripts from stealing session credentials.",
     "Các cookie bảo mật có cờ HTTP-only giúp ngăn chặn các đoạn mã độc XSS đánh cắp thông tin phiên đăng nhập.",
     "Tệp cookie lưu phiên duyệt web", "🍪",
     "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=600&auto=format&fit=crop&q=80"),

    (95, "Session", "/ˈseʃ.ən/", "noun", "web", "Phát triển Web",
     "Phiên làm việc: khoảng thời gian liên tục từ khi người dùng đăng nhập hoặc truy cập trang web cho đến khi đăng xuất hoặc hết hạn.",
     "The user session automatically times out after fifteen minutes of user inactivity for security.",
     "Phiên làm việc của người dùng sẽ tự động hết hạn sau mười lăm phút không có hoạt động vì lý do an toàn bảo mật.",
     "Phiên làm việc người dùng", "⏳",
     "https://images.unsplash.com/photo-1563986768609-322da13575f3?w=600&auto=format&fit=crop&q=80"),

    (96, "DOM (Document Object Model)", "/dɒm/", "noun", "web", "Phát triển Web",
     "Mô hình đối tượng tài liệu: cấu trúc cây đại diện cho các phần tử HTML trên trang web, cho phép JavaScript truy cập và chỉnh sửa giao diện linh hoạt.",
     "React creates an in-memory Virtual DOM to compute minimal UI updates before patching the actual browser DOM.",
     "React tạo ra một DOM ảo trong bộ nhớ để tính toán các cập nhật giao diện tối thiểu trước khi gắn vào DOM trình duyệt thật.",
     "Cây mô hình đối tượng DOM", "🌲",
     "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=600&auto=format&fit=crop&q=80"),

    (97, "CDN (Content Delivery Network)", "/ˌsiː.diːˈen/", "noun", "cloud", "Cloud & DevOps",
     "Mạng phân phối nội dung: mạng lưới các máy chủ đặt khắp thế giới giúp chuyển phát hình ảnh, video và tệp web nhanh chóng tới người dùng gần nhất.",
     "Distributing website assets through a global CDN reduced page load latency from three seconds to under half a second.",
     "Phân phối tài nguyên trang web qua mạng CDN toàn cầu đã giảm độ trễ tải trang từ ba giây xuống dưới nửa giây.",
     "Mạng máy chủ phân phối toàn cầu", "🌍",
     "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&auto=format&fit=crop&q=80"),

    (98, "Payload", "/ˈpeɪ.loʊd/", "noun", "web", "Phát triển Web",
     "Phần tải dữ liệu cốt lõi: phần dữ liệu thực tế được truyền đi trong một gói tin HTTP hoặc mạng, tách biệt khỏi phần tiêu đề (headers) và siêu dữ liệu.",
     "The JSON request payload contains the user's updated profile information and billing address.",
     "Phần tải dữ liệu yêu cầu JSON chứa thông tin hồ sơ người dùng mới cập nhật và địa chỉ thanh toán.",
     "Phần dữ liệu truyền tải thực", "📦",
     "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    (99, "Loss Function", "/lɒs ˈfʌŋk.ʃən/", "noun", "ai", "Trí tuệ nhân tạo (AI)",
     "Hàm mất mát / Hàm chi phí: công thức toán học đo lường mức độ sai lệch giữa kết quả dự đoán của mô hình AI và giá trị thực tế.",
     "Gradient descent adjusts the neural network weights to minimize the cross-entropy loss function.",
     "Thuật toán hạ độ dốc (gradient descent) điều chỉnh trọng số mạng nơ-ron để cực tiểu hóa hàm mất mát entropy chéo.",
     "Hàm mất mát đo sai số", "📉",
     "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    (100, "Hyperparameter", "/ˌhaɪ.pər.pəˈræm.ɪ.tər/", "noun", "ai", "Trí tuệ nhân tạo (AI)",
     "Siêu tham số: các thông số cấu hình do kỹ sư máy học thiết lập trước khi huấn luyện (như tốc độ học learning rate, kích thước batch).",
     "Tuning hyperparameters like learning rate and batch size is essential to maximize model prediction accuracy.",
     "Tinh chỉnh các siêu tham số như tốc độ học và kích thước lô dữ liệu là tối quan trọng để tối đa hóa độ chính xác dự đoán của mô hình.",
     "Siêu tham số cấu hình AI", "🎛️",
     "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=600&auto=format&fit=crop&q=80")
]

for item in final_10:
    tid, term, ipa, pos, subcat, subcat_vi, meaning, example, example_vi, concept_tag, icon, img_url = item
    gradient = GRADIENTS_IT[tid % len(GRADIENTS_IT)]
    formatted_it_terms.append({
        "id": tid,
        "term": term,
        "ipa": ipa,
        "partOfSpeech": pos,
        "subCategory": subcat,
        "subCategoryVi": subcat_vi,
        "meaning": meaning,
        "example": example,
        "exampleVi": example_vi,
        "conceptTag": concept_tag,
        "icon": icon,
        "gradient": gradient,
        "image": img_url
    })

# Write final JSON and JS files
with open("/home/ken/.gemini/antigravity/scratch/irregular-verbs-360/it_terms_data.json", "w", encoding="utf-8") as f:
    json.dump(formatted_it_terms, f, ensure_ascii=False, indent=2)

js_content = "window.IT_TERMS_DATA = " + json.dumps(formatted_it_terms, ensure_ascii=False, indent=2) + ";\n"
with open("/home/ken/.gemini/antigravity/scratch/irregular-verbs-360/it_terms_data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Total IT terms updated: Exactly {len(formatted_it_terms)} terms!")
