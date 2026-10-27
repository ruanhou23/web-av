# -*- coding: utf-8 -*-
"""Domain 10: Software Testing, QA, Agile & Tech Workplace English (100 core terms)"""

terms = [
    ("Software Testing", "/ˈsɒft.weər ˈtes.tɪŋ/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Kiểm thử phần mềm: quá trình thực thi chương trình để đánh giá và đảm bảo chất lượng, tìm ra các lỗi trước khi phát hành.",
     "Thorough software testing reduces costly production incidents and protects business reputations.", "Kiểm thử phần mềm kỹ lưỡng giúp giảm các sự cố sản xuất tốn kém và bảo vệ uy tín doanh nghiệp.",
     "Kiểm thử phần mềm", "🧪", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("Quality Assurance (QA)", "/ˈkwɒl.ə.ti əˈʃɔː.rəns/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Đảm bảo chất lượng (QA): quy trình tập trung vào việc ngăn ngừa lỗi bằng cách thiết lập và giám sát quy trình phát triển.",
     "The QA team defines release criteria and establishes automated test suites.", "Đội ngũ QA định nghĩa tiêu chí phát hành và thiết lập bộ kiểm thử tự động.",
     "Đảm bảo chất lượng QA", "🛡️", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("Quality Control (QC)", "/ˈkwɒl.ə.ti kənˈtrəʊl/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Kiểm soát chất lượng (QC): hoạt động kiểm tra thực tế sản phẩm phần mềm hoàn thành để tìm và phát hiện các lỗi cụ thể.",
     "While QA focuses on the development process, QC inspects the final software deliverables.", "Trong khi QA tập trung vào quy trình phát triển, QC kiểm tra các sản phẩm phần mềm cuối cùng.",
     "Kiểm soát chất lượng QC", "🔍", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("Manual Testing", "/ˈmæn.ju.əl ˈtes.tɪŋ/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Kiểm thử thủ công: kiểm thử viên trực tiếp thao tác trên phần mềm như người dùng thật mà không dùng công cụ tự động hóa.",
     "Manual testing is invaluable for evaluating visual aesthetics and exploratory user experiences.", "Kiểm thử thủ công rất có giá trị trong việc đánh giá thẩm mỹ và trải nghiệm người dùng thăm dò.",
     "Kiểm thử thủ công", "✍️", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("Automated Testing", "/ˈɔː.tə.meɪ.tɪd ˈtes.tɪŋ/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Kiểm thử tự động: sử dụng các đoạn kịch bản mã để tự động chạy các trường hợp kiểm thử lặp đi lặp lại nhanh chóng.",
     "Automated testing runs thousands of test scenarios in minutes across every pull request.", "Kiểm thử tự động chạy hàng ngàn kịch bản chỉ trong vài phút qua mỗi pull request.",
     "Kiểm thử tự động", "🤖", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("Test-Driven Development (TDD)", "/test ˌdrɪv.ən/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Phát triển hướng kiểm thử: phương pháp viết mã kiểm thử trước khi viết mã tính năng (chu trình Đỏ - Xanh - Tái cấu trúc).",
     "TDD encourages modular, decoupled software architectures by forcing developers to design for testability.", "TDD khuyến khích kiến trúc tách rời bằng cách buộc lập trình viên thiết kế để dễ kiểm thử.",
     "Phát triển hướng kiểm thử TDD", "🔄", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("Behavior-Driven Development (BDD)", "/bɪˈheɪ.vjər ˌdrɪv.ən/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Phát triển hướng hành vi: phương pháp dùng ngôn ngữ tự nhiên (Given-When-Then qua Cucumber) để gắn kết kinh doanh và kỹ thuật.",
     "BDD aligns business analysts and developers using human-readable feature specifications.", "BDD gắn kết chuyên viên nghiệp vụ và kỹ sư bằng thông số tính năng dễ đọc như văn bản thường.",
     "Phát triển hướng hành vi BDD", "📑", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("Unit Test", "/ˈjuː.nɪt test/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Kiểm thử đơn vị: kiểm thử các thành phần nhỏ nhất độc lập của mã nguồn (hàm, phương thức) trong sự cô lập.",
     "Unit tests execute in milliseconds because they isolate logic from real databases and networks.", "Kiểm thử đơn vị chạy trong mili-giây vì cô lập logic khỏi CSDL và mạng thực tế.",
     "Kiểm thử đơn vị Unit Test", "🧱", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("Integration Test", "/ˌɪn.tɪˈɡreɪ.ʃən test/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Kiểm thử tích hợp: kiểm tra sự kết hợp và giao tiếp chính xác giữa hai hay nhiều mô-đun phần mềm khác nhau.",
     "Integration tests verify whether payment services correctly store transaction records into PostgreSQL.", "Kiểm thử tích hợp xác minh xem dịch vụ thanh toán có lưu đúng bản ghi giao dịch vào PostgreSQL.",
     "Kiểm thử tích hợp", "🔗", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("End-to-End Test (E2E)", "/end tu end test/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Kiểm thử đầu-cuối: mô phỏng hoàn chỉnh toàn bộ luồng hành trình của người dùng từ giao diện trình duyệt tới máy chủ và CSDL.",
     "Cypress and Playwright are popular tools for writing automated E2E browser tests.", "Cypress và Playwright là các công cụ phổ biến để viết kiểm thử E2E trình duyệt tự động.",
     "Kiểm thử đầu-cuối E2E", "🌐", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("Regression Testing", "/rɪˈɡreʃ.ən ˈtes.tɪŋ/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Kiểm thử hồi quy: chạy lại toàn bộ bộ kiểm thử để đảm bảo các thay đổi mã nguồn mới không làm hỏng các tính năng cũ đang chạy tốt.",
     "Automated regression testing prevents regressions from slipping into production releases.", "Kiểm thử hồi quy tự động ngăn các lỗi tái phát trượt vào bản phát hành sản xuất.",
     "Kiểm thử hồi quy Regression", "🔄", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("Smoke Testing", "/sməʊk ˈtes.tɪŋ/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Kiểm thử khói: bộ kiểm tra nhanh các chức năng sống còn cốt lõi để quyết định xem bản dựng có đủ ổn định để kiểm thử tiếp không.",
     "If the smoke test fails after deployment, the release is immediately rejected.", "Nếu kiểm thử khói thất bại sau khi triển khai, bản phát hành sẽ bị từ chối ngay lập tức.",
     "Kiểm thử nhanh Smoke Test", "💨", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("Sanity Testing", "/ˈsæn.ə.ti ˈtes.tɪŋ/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Kiểm thử tỉnh táo: kiểm tra rất nhanh và có trọng điểm sau khi sửa lỗi nhỏ để xác nhận lỗi đã được khắc phục đúng đắn.",
     "Run sanity testing on the shopping cart module after applying the discount hotfix.", "Chạy kiểm thử tỉnh táo trên mô-đun giỏ hàng sau khi áp dụng bản vá lỗi giảm giá.",
     "Kiểm thử tỉnh táo Sanity", "🧠", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("Acceptance Testing", "/əkˈsep.təns ˈtes.tɪŋ/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Kiểm thử chấp nhận: đánh giá hệ thống xem có đáp ứng đầy đủ các yêu cầu kinh doanh đã cam kết trong hợp đồng hay không.",
     "Acceptance testing must pass before management officially approves software handover.", "Kiểm thử chấp nhận phải vượt qua trước khi ban quản lý chính thức phê duyệt bàn giao phần mềm.",
     "Kiểm thử chấp nhận", "✅", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("User Acceptance Testing (UAT)", "/ˌjuː.eɪˈtiː/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Kiểm thử chấp nhận người dùng (UAT): giai đoạn người dùng thực tế cuối cùng sử dụng phần mềm thử nghiệm trước khi chính thức ra mắt.",
     "Clients conduct UAT in a dedicated staging sandbox matching production data.", "Khách hàng tiến hành UAT trong môi trường staging chuyên dụng giống hệt dữ liệu thật.",
     "Kiểm thử người dùng UAT", "👥", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("Performance Testing", "/pəˈfɔː.məns ˈtes.tɪŋ/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Kiểm thử hiệu năng: đo lường tốc độ, thời gian phản hồi, độ ổn định và tiêu thụ tài nguyên của ứng dụng dưới tải.",
     "Performance testing reveals that page load times degrade significantly with 5,000 active users.", "Kiểm thử hiệu năng cho thấy thời gian tải trang giảm đáng kể khi có 5.000 người dùng hoạt động.",
     "Kiểm thử hiệu năng", "⏱️", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Load Testing", "/ləʊd ˈtes.tɪŋ/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Kiểm thử tải: kiểm tra hành vi của hệ thống dưới mức tải dự kiến thông thường và mức tải đỉnh.",
     "K6 and JMeter simulate concurrent users during automated load testing exercises.", "K6 và JMeter mô phỏng người dùng đồng thời trong các đợt kiểm thử tải tự động.",
     "Kiểm thử tải Load Testing", "🏋️", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Stress Testing", "/stres ˈtes.tɪŋ/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Kiểm thử sức ép: đẩy tải vượt xa giới hạn chịu đựng tối đa để xem hệ thống sập như thế nào và khả năng phục hồi sau sập.",
     "Stress testing pushes servers until memory exhausts to verify graceful failure recovery.", "Kiểm thử sức ép đẩy máy chủ đến cạn RAM để kiểm tra khả năng phục hồi sự cố êm đẹp.",
     "Kiểm thử sức ép Stress Test", "💥", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Volume Testing", "/ˈvɒl.juːm ˈtes.tɪŋ/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Kiểm thử dung lượng: đưa một lượng khổng lồ dữ liệu vào cơ sở dữ liệu để kiểm tra hiệu năng khi quy mô dữ liệu phình to.",
     "Volume testing populates 100 million customer records to observe database query slowdowns.", "Kiểm thử dung lượng nạp 100 triệu bản ghi khách hàng để quan sát sự chậm lại của truy vấn CSDL.",
     "Kiểm thử dung lượng Volume", "📦", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Soak Testing (Endurance Testing)", "/səʊk ˈtes.tɪŋ/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Kiểm thử độ bền: chạy hệ thống liên tục dưới mức tải đều đặn trong thời gian dài (vài ngày) để phát hiện rò rỉ RAM.",
     "Soak testing over a 72-hour period revealed a slow memory leak in the background worker daemon.", "Kiểm thử độ bền suốt 72 giờ đã làm lộ ra rò rỉ bộ nhớ chậm trong tiến trình nền.",
     "Kiểm thử độ bền Soak Test", "⏳", "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=600&auto=format&fit=crop&q=80"),

    ("Usability Testing", "/ˌjuː.zəˈbɪl.ə.ti ˈtes.tɪŋ/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Kiểm thử khả năng sử dụng: quan sát người dùng thật sử dụng ứng dụng để xem giao diện có dễ hiểu và trực quan không.",
     "Usability testing uncovered that users struggled to find the checkout discount promo code field.", "Kiểm thử khả năng sử dụng đã phát hiện người dùng gặp khó khăn khi tìm ô mã giảm giá.",
     "Kiểm thử khả năng sử dụng", "👁️", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("A/B Testing", "/ˌeɪˈbiː ˈtes.tɪŋ/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Kiểm thử A/B: so sánh hai phiên bản (A và B) cùng hiển thị ngẫu nhiên cho người dùng để xem phiên bản nào cho tỷ lệ chuyển đổi cao hơn.",
     "A/B testing a green buy button versus a blue one resulted in a 12 percent lift in conversions.", "Kiểm thử A/B nút mua màu xanh lá với màu xanh dương đã giúp tăng 12% tỷ lệ chuyển đổi.",
     "Thử nghiệm A/B Testing", "🅰️🅱️", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Test Mock", "/test mɒk/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Đối tượng giả lập Mock: đối tượng giả mạo hành vi của thành phần phức tạp bên ngoài (như cổng thanh toán ngân hàng) trong kiểm thử.",
     "We mock the Stripe payment API in test suites to prevent real monetary credit charges.", "Chúng tôi giả lập API thanh toán Stripe trong kiểm thử để tránh trừ tiền thật của thẻ tín dụng.",
     "Đối tượng giả lập Mock", "🎭", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("Test Stub", "/test stʌb/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Đối tượng cuống Stub: đoạn mã giả lập đơn giản luôn trả về các dữ liệu tĩnh đã định trước cho các lời gọi hàm.",
     "A database stub returns canned customer JSON objects during isolated unit tests.", "Một stub cơ sở dữ liệu luôn trả về đối tượng JSON khách hàng cố định trong kiểm thử đơn vị.",
     "Đối tượng cuống Stub", "🪵", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("Test Spy", "/test spaɪ/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Đối tượng gián điệp Spy: bọc lấy hàm thực tế để ghi nhận số lần hàm được gọi, các đối số truyền vào và kết quả trả về.",
     "Use a test spy to assert that the logging function was called exactly twice.", "Dùng test spy để xác nhận rằng hàm ghi log đã được gọi chính xác hai lần.",
     "Đối tượng thám thính Spy", "🕵️", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("Test Fixture", "/test ˈfɪks.tʃər/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Môi trường cố định Fixture: thiết lập trạng thái ban đầu ổn định (dữ liệu mẫu trong RAM) trước khi chạy kiểm thử.",
     "Fixtures initialize standard database rows before every test and tear them down afterward.", "Fixture khởi tạo các dòng CSDL chuẩn trước mỗi bài kiểm thử và dọn dẹp sau khi xong.",
     "Môi trường cố định Fixture", "🎛️", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("Assertion", "/əˈsɜː.ʃən/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Khẳng định kiểm thử: mệnh đề logic kiểm tra xem kết quả thực tế có đúng bằng kết quả mong đợi hay không; nếu sai thì bài test trượt.",
     "The assertion 'expect(response.status).toBe(200)' validates successful HTTP outcomes.", "Khẳng định 'expect(response.status).toBe(200)' xác nhận kết quả HTTP thành công.",
     "Khẳng định Assertion", "⚖️", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("Code Coverage", "/kəʊd ˈkʌv.ər.ɪdʒ/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Độ bao phủ mã nguồn: tỷ lệ phần trăm số dòng mã hoặc nhánh lệnh được thực thi trong quá trình chạy kiểm thử.",
     "Our engineering standards require at least 80 percent code coverage before merging PRs.", "Tiêu chuẩn kỹ thuật của chúng tôi yêu cầu tối thiểu 80% độ bao phủ mã trước khi hợp nhất PR.",
     "Độ bao phủ mã Coverage", "📊", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Test Case", "/test keɪs/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Trường hợp kiểm thử: tập hợp điều kiện đầu vào, quy trình thực hiện và kết quả mong đợi để kiểm tra một tính năng cụ thể.",
     "Write detailed test cases covering both happy path journeys and edge-case exceptions.", "Viết các trường hợp kiểm thử chi tiết bao gồm cả luồng chuẩn lẫn các ngoại lệ biên.",
     "Trường hợp kiểm thử Test Case", "📋", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("Test Suite", "/test swiːt/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Bộ kiểm thử: tập hợp gom nhóm nhiều trường hợp kiểm thử liên quan đến nhau được thực thi cùng nhau.",
     "The entire regression test suite takes fifteen minutes to run on cloud CI servers.", "Toàn bộ bộ kiểm thử hồi quy mất mười lăm phút để chạy trên máy chủ CI đám mây.",
     "Bộ kiểm thử Test Suite", "📦", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("Test Plan", "/test plæn/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Kế hoạch kiểm thử: tài liệu mô tả chi tiết phạm vi, chiến lược, lịch trình và tài nguyên cho hoạt động kiểm thử dự án.",
     "The QA Lead presented the comprehensive test plan ahead of the major version 2.0 launch.", "Trưởng nhóm QA đã trình bày kế hoạch kiểm thử toàn diện trước khi ra mắt phiên bản 2.0.",
     "Kế hoạch kiểm thử Test Plan", "🗺️", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("Software Bug", "/ˈsɒft.weər bʌɡ/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Lỗi phần mềm: khiếm khuyết trong mã nguồn khiến phần mềm hoạt động sai hoặc tạo ra kết quả không mong đợi.",
     "A critical software bug prevented users from resetting forgotten passwords.", "Một lỗi phần mềm nghiêm trọng đã ngăn người dùng đặt lại mật khẩu bị quên.",
     "Lỗi phần mềm Bug", "🐛", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("Software Defect", "/ˈsɒft.weər ˈdiː.fekt/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Khiếm khuyết phần mềm: sự sai lệch giữa yêu cầu kỹ thuật quy định trong đặc tả và hành vi thực tế của hệ thống.",
     "The customer reported a critical defect in invoice balance calculations.", "Khách hàng đã báo cáo một khiếm khuyết nghiêm trọng trong tính toán số dư hóa đơn.",
     "Khiếm khuyết phần mềm", "⚠️", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("Bug Life Cycle", "/bʌɡ laɪf ˈsaɪ.kəl/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Vòng đời của lỗi: các trạng thái mà một lỗi trải qua từ lúc mở (New -> Assigned -> Fixed -> Verified -> Closed).",
     "Understanding the bug life cycle ensures smooth collaboration between developers and QA.", "Hiểu vòng đời của bug giúp đảm bảo việc phối hợp nhịp nhàng giữa lập trình viên và QA.",
     "Vòng đời lỗi Bug Cycle", "🔄", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("Bug Report", "/bʌɡ rɪˈpɔːt/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Báo cáo lỗi: tài liệu mô tả chi tiết lỗi gồm tóm tắt, các bước tái hiện, ảnh chụp màn hình và nhật ký lỗi.",
     "An exemplary bug report includes exact steps to reproduce and system environment logs.", "Một báo cáo lỗi mẫu mực bao gồm các bước tái hiện chính xác và nhật ký môi trường hệ thống.",
     "Báo cáo lỗi Bug Report", "📄", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("Steps to Reproduce", "/steps tu ˌriː.prəˈdjuːs/", "phrase", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Các bước tái hiện lỗi: chuỗi hành động tuần tự từng bước cần thiết để làm lỗi xuất hiện lại một cách nhất quán.",
     "Without clear steps to reproduce, engineers cannot effectively debug the issue.", "Nếu không có các bước tái hiện rõ ràng, kỹ sư không thể gỡ lỗi vấn đề một cách hiệu quả.",
     "Các bước tái hiện lỗi", "👣", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("Expected Result", "/ɪkˈspek.tɪd rɪˈzʌlt/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Kết quả mong đợi: hành vi đúng đắn mà phần mềm lẽ ra phải thực hiện theo tài liệu yêu cầu nghiệp vụ.",
     "Expected result: The modal dialog closes and a green success banner appears.", "Kết quả mong đợi: Hộp thoại modal đóng lại và biểu ngữ thành công màu xanh xuất hiện.",
     "Kết quả mong đợi", "🎯", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("Actual Result", "/ˈæk.tʃu.əl rɪˈzʌlt/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Kết quả thực tế: hành vi thực tế đang xảy ra của phần mềm (thường là lỗi sai hoặc ứng dụng bị đơ sập).",
     "Actual result: The application threw an unhandled 500 error exception.", "Kết quả thực tế: Ứng dụng đã phát sinh ngoại lệ lỗi 500 chưa được xử lý.",
     "Kết quả thực tế", "🔍", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("Bug Severity", "/bʌɡ sɪˈver.ə.ti/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Mức độ nghiêm trọng của lỗi: thước đo tác động kỹ thuật của lỗi tới hệ thống (Blocker, Critical, Major, Minor).",
     "Bug severity reflects the technical impact on functionality regardless of business timeline.", "Mức độ nghiêm trọng phản ánh tác động kỹ thuật lên tính năng bất kể tiến độ kinh doanh.",
     "Mức độ nghiêm trọng Severity", "🎚️", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("Bug Priority", "/bʌɡ praɪˈɒr.ə.ti/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Độ ưu tiên sửa lỗi: mức độ khẩn cấp về mặt kinh doanh đòi hỏi lỗi phải được sửa nhanh hay chậm.",
     "A typo on the corporate homepage has low severity but high priority for brand perception.", "Lỗi chính tả trên trang chủ có độ nghiêm trọng thấp nhưng ưu tiên sửa cao vì thương hiệu.",
     "Độ ưu tiên sửa lỗi Priority", "⭐", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("Blocker Issue", "/ˈblɒk.ər ˈɪʃ.uː/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Lỗi chặn phát hành: lỗi nghiêm trọng làm tắc nghẽn toàn bộ quá trình phát triển hoặc khiến phần mềm không thể sử dụng.",
     "The login crash was marked as a blocker issue, halting the production release.", "Lỗi sập đăng nhập bị gắn cờ lỗi chặn, làm hoãn việc phát hành sản phẩm.",
     "Lỗi chặn Blocker", "🛑", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("Critical Issue", "/ˈkrɪt.ɪ.kəl ˈɪʃ.uː/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Sự cố nghiêm trọng: lỗi gây hỏng tính năng cốt lõi hoặc gây thất thoát dữ liệu nhưng có thể có giải pháp tạm thời.",
     "Data corruption in accounting exports was declared a critical issue by the team.", "Việc hỏng dữ liệu khi xuất sổ sách kế toán bị tuyên bố là một sự cố nghiêm trọng.",
     "Sự cố nghiêm trọng Critical", "🚨", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("Workaround", "/ˈwɜːk.ə.raʊnd/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Giải pháp tạm thời: cách lách qua lỗi để hoàn thành công việc trong khi chờ đợi bản vá lỗi chính thức.",
     "Support provided a temporary workaround for users unable to export invoices directly.", "Bộ phận hỗ trợ cung cấp giải pháp tạm thời cho người dùng chưa xuất được hóa đơn trực tiếp.",
     "Giải pháp tạm thời Workaround", "🩹", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("Hotfix", "/ˈhɒt.fɪks/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Bản vá khẩn cấp: bản sửa lỗi nhanh được đẩy trực tiếp lên hệ thống sản xuất ngoài lịch phát hành thông thường.",
     "Deploying a hotfix at midnight resolved the payment processing outage immediately.", "Triển khai bản vá khẩn lúc nửa đêm đã giải quyết ngay sự cố ngừng hoạt động của cổng thanh toán.",
     "Bản vá khẩn cấp Hotfix", "🔥", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("Patch", "/pætʃ/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Bản vá phần mềm: đoạn mã bổ sung phát hành để sửa một hoặc một vài lỗi bảo mật hay chức năng cụ thể.",
     "Apply the monthly operating system security patch to protect against new CVEs.", "Cài đặt bản vá an ninh hệ điều hành hàng tháng để phòng vệ trước các mã lỗ hổng CVE mới.",
     "Bản vá phần mềm Patch", "🩹", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=80"),

    ("Release Candidate (RC)", "/rɪˈliːs ˈkæn.dɪ.dət/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Bản ứng viên phát hành: phiên bản phần mềm gần như hoàn thiện, sẵn sàng ra mắt chính thức nếu không phát hiện thêm lỗi lớn.",
     "The team tagged version 3.0.0-rc1 for final stakeholder acceptance verification.", "Nhóm gắn nhãn phiên bản 3.0.0-rc1 để các bên liên quan xác minh phê duyệt lần cuối.",
     "Bản ứng viên phát hành RC", "🏷️", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600&auto=format&fit=crop&q=80"),

    ("Agile Methodology", "/ˈædʒ.aɪl ˌmeθ.əˈdɒl.ə.dʒi/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Phương pháp luận Agile: triết lý phát triển phần mềm linh hoạt nhấn mạnh vào chu kỳ lặp ngắn, thích ứng nhanh và hợp tác.",
     "Agile methodologies prioritize working software and responding to change over rigid plans.", "Phương pháp Agile ưu tiên phần mềm chạy tốt và phản ứng với thay đổi hơn kế hoạch cứng nhắc.",
     "Phương pháp luận Agile", "🏃‍♂️", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Scrum Framework", "/skrʌm ˈfreɪm.wɜːk/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Khung làm việc Scrum: khung phát triển Agile phổ biến chia nhỏ công việc thành các khoảng thời gian cố định gọi là Sprint.",
     "Scrum relies on ceremonies like sprint planning, daily standups, reviews, and retrospectives.", "Scrum dựa trên các nghi thức như lập kế hoạch sprint, họp đứng hàng ngày, review và hồi tưởng.",
     "Khung làm việc Scrum", "🏉", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Kanban Board", "/ˈkæn.bæn bɔːd/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Bảng Kanban: công cụ quản lý công việc trực quan qua các cột (To Do -> In Progress -> Done) nhằm giới hạn việc đang làm.",
     "The Kanban board displays tasks in real time and limits Work In Progress (WIP).", "Bảng Kanban hiển thị nhiệm vụ theo thời gian thực và giới hạn lượng việc đang làm.",
     "Bảng công việc Kanban", "📋", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Sprint", "/sprɪnt/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Chu kỳ Sprint: khoảng thời gian cố định (thường 2 tuần) mà đội ngũ cam kết hoàn thành một lượng công việc cụ thể.",
     "During our two-week sprint, we delivered the new customer checkout interface.", "Trong chu kỳ sprint 2 tuần, chúng tôi đã bàn giao giao diện thanh toán mới cho khách hàng.",
     "Chu kỳ nước rút Sprint", "⏱️", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Sprint Planning", "/sprɪnt ˈplæn.ɪŋ/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Họp lập kế hoạch Sprint: cuộc họp đầu sprint nơi cả nhóm thảo luận và chọn ra các mục việc từ backlog để thực hiện.",
     "Sprint planning determines which user stories the engineering team commits to deliver.", "Buổi lập kế hoạch sprint xác định những user story mà đội kỹ sư cam kết bàn giao.",
     "Lập kế hoạch Sprint", "📅", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Daily Standup / Scrum", "/ˈdeɪ.li ˈstænd.ʌp/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Họp đứng hàng ngày: cuộc họp nhanh 15 phút đầu ngày để chia sẻ việc đã làm hôm qua, việc sẽ làm hôm nay và các vướng mắc.",
     "In the daily standup, engineers answer what they did yesterday, what they will do, and any blockers.", "Trong buổi họp đứng hàng ngày, kỹ sư chia sẻ việc đã làm, việc sẽ làm và các vướng mắc.",
     "Họp đứng hàng ngày Standup", "🧍‍♂️", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Sprint Review", "/sprɪnt rɪˈvjuː/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Họp đánh giá Sprint: buổi họp cuối sprint trình diễn demo các tính năng hoàn thành cho các bên liên quan xem xét.",
     "Stakeholders provide immediate practical feedback during the live sprint review demo.", "Các bên liên quan đưa ra phản hồi thực tế ngay trong buổi demo đánh giá sprint.",
     "Đánh giá demo Sprint Review", "👀", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Sprint Retrospective", "/sprɪnt ˌret.rəˈspek.tɪv/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Họp hồi tưởng Sprint: buổi họp nội bộ đội ngũ nhìn nhận lại những điểm làm tốt, chưa tốt và cải tiến quy trình cho sprint tới.",
     "The sprint retrospective creates a safe environment to discuss process pain points and team growth.", "Buổi hồi tưởng sprint tạo môi trường cởi mở để bàn về vướng mắc quy trình và sự phát triển của nhóm.",
     "Họp hồi tưởng Retrospective", "💭", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Product Backlog", "/ˈprɒd.ʌkt ˈbæk.lɒɡ/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Danh sách tồn đọng sản phẩm: danh sách danh mục có thứ tự ưu tiên gồm mọi tính năng, sửa lỗi và yêu cầu kỹ thuật của sản phẩm.",
     "The Product Owner regularly grooms the product backlog to keep high-value items on top.", "Product Owner định kỳ chăm sóc backlog sản phẩm để các mục giá trị cao luôn ở trên đầu.",
     "Danh sách tồn đọng Backlog", "📚", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Sprint Backlog", "/sprɪnt ˈbæk.lɒɡ/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Danh sách tồn đọng Sprint: tập hợp các hạng mục được đội ngũ lựa chọn từ product backlog để hoàn thành trong sprint hiện tại.",
     "Engineers self-assign individual tasks from the agreed sprint backlog.", "Kỹ sư tự nhận các nhiệm vụ riêng lẻ từ danh sách sprint backlog đã thống nhất.",
     "Tồn đọng Sprint Backlog", "📋", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("User Story", "/ˈjuː.zər ˈstɔː.ri/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Câu chuyện người dùng: mô tả ngắn gọn tính năng theo góc nhìn người dùng ('Là một... tôi muốn... để tôi có thể...').",
     "Format: 'As a customer, I want to filter products by price so that I can shop within my budget.'", "Định dạng: 'Là khách hàng, tôi muốn lọc sản phẩm theo giá để có thể mua sắm trong ngân sách.'",
     "Câu chuyện người dùng", "📖", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Acceptance Criteria (AC)", "/əkˈsep.təns kraɪˈtɪə.ri.ə/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Tiêu chí chấp nhận (AC): các điều kiện cụ thể bắt buộc mà một user story phải thỏa mãn để được xem là hoàn thành.",
     "QA tests the feature directly against the acceptance criteria outlined in the Jira ticket.", "QA kiểm thử tính năng trực tiếp dựa trên tiêu chí chấp nhận ghi trong thẻ Jira.",
     "Tiêu chí chấp nhận AC", "📝", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Definition of Done (DoD)", "/ˌdef.ɪˈnɪʃ.ən əv dʌn/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Định nghĩa hoàn thành (DoD): danh sách tiêu chuẩn chất lượng chung của cả nhóm (code review, test pass, deploy staging) cho mọi công việc.",
     "A story is not closed until it satisfies all conditions specified in the Definition of Done.", "Một story chưa được đóng lại cho đến khi thỏa mãn mọi điều kiện trong Định nghĩa Hoàn thành.",
     "Định nghĩa Hoàn thành DoD", "🏁", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Definition of Ready (DoR)", "/ˌdef.ɪˈnɪʃ.ən əv ˈred.i/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Định nghĩa sẵn sàng (DoR): tiêu chí quy định user story đã đủ thông tin rõ ràng và ước lượng để đưa vào sprint làm việc.",
     "The user story met the DoR because wireframes and API contracts were fully documented.", "User story đã đạt DoR vì bản vẽ giao diện và giao ước API đã được ghi chép đầy đủ.",
     "Định nghĩa Sẵn sàng DoR", "🟢", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Story Points", "/ˈstɔː.ri pɔɪnts/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Điểm câu chuyện: đơn vị đo lường tương đối dùng để ước tính độ phức tạp, rủi ro và nỗ lực của một công việc.",
     "The team estimated the database migration task at 8 story points due to technical unknowns.", "Nhóm ước lượng nhiệm vụ di chuyển CSDL ở mức 8 điểm story do có nhiều ẩn số kỹ thuật.",
     "Điểm ước lượng Story Points", "🎲", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Team Velocity", "/tiːm vəˈlɒs.ə.ti/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Vận tốc nhóm: tổng số điểm story points mà đội ngũ hoàn thành trung bình trong mỗi chu kỳ sprint.",
     "With an average velocity of 40 points, the team plans roughly 38 to 42 points per sprint.", "Với vận tốc trung bình 40 điểm, nhóm lên kế hoạch khoảng 38 đến 42 điểm mỗi sprint.",
     "Vận tốc nhóm Velocity", "⚡", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Burndown Chart", "/ˈbɜːn.daʊn tʃɑːt/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Biểu đồ tiêu hao: biểu đồ theo dõi lượng công việc còn lại từng ngày trong sprint hướng về con số 0.",
     "The burndown chart showed a steep drop on Thursday as three major pull requests merged.", "Biểu đồ tiêu hao cho thấy độ dốc giảm mạnh vào thứ Năm khi ba PR lớn được hợp nhất.",
     "Biểu đồ tiêu hao Burndown", "📉", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Epic", "/ˈep.ɪk/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Hạng mục lớn (Epic): khối công việc lớn bao quát có thể chia nhỏ thành nhiều user story thực hiện qua nhiều sprint.",
     "The 'International Payment Support' epic spans several sprints across frontend and backend squads.", "Epic 'Hỗ trợ thanh toán quốc tế' kéo dài qua nhiều sprint của cả nhóm frontend và backend.",
     "Hạng mục lớn Epic", "🏔️", "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=600&auto=format&fit=crop&q=80"),

    ("Task", "/tɑːsk/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Nhiệm vụ: đơn vị công việc kỹ thuật cụ thể cần thực hiện để hoàn thành một user story.",
     "Create a database schema migration script as a technical task under the user story.", "Tạo kịch bản di chuyển lược đồ CSDL như một nhiệm vụ kỹ thuật nằm trong user story.",
     "Nhiệm vụ Task", "📌", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Subtask", "/ˈsʌb.tɑːsk/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Nhiệm vụ con: phần chia nhỏ hơn của một nhiệm vụ để theo dõi tiến độ chi tiết từng phần việc.",
     "Unit test creation and code review are tracked as separate subtasks on Jira.", "Viết unit test và đánh giá code được theo dõi như các nhiệm vụ con riêng biệt trên Jira.",
     "Nhiệm vụ con Subtask", "🔹", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Product Roadmap", "/ˈprɒd.ʌkt ˈrəʊd.mæp/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Lộ trình sản phẩm: bản kế hoạch tầm nhìn chiến lược vạch rõ định hướng phát triển tính năng theo quý và năm.",
     "The product roadmap outlines major quarterly milestones and upcoming market releases.", "Lộ trình sản phẩm vạch ra các cột mốc quan trọng hàng quý và các bản phát hành thị trường.",
     "Lộ trình sản phẩm Roadmap", "🗺️", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Milestone", "/ˈmaɪl.stəʊn/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Cột mốc dự án: điểm mốc đánh dấu một giai đoạn quan trọng hoặc sự kiện bàn giao lớn trong vòng đời dự án.",
     "Passing internal security audits was a crucial milestone before commercial beta launch.", "Vượt qua đợt kiểm toán an ninh nội bộ là cột mốc sống còn trước khi ra mắt bản beta.",
     "Cột mốc Milestone", "🏁", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Product Manager (PM)", "/ˈprɒd.ʌkt ˈmæn.ɪ.dʒər/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Giám đốc / Quản lý sản phẩm: người chịu trách nhiệm định hình chiến lược sản phẩm, đáp ứng nhu cầu thị trường và tối ưu giá trị kinh doanh.",
     "The PM prioritizes strategic product roadmaps based on user interviews and market analytics.", "PM ưu tiên lộ trình sản phẩm chiến lược dựa trên phỏng vấn người dùng và phân tích thị trường.",
     "Quản lý sản phẩm PM", "💼", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Product Owner (PO)", "/ˈprɒd.ʌkt ˈəʊ.nər/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Chủ sở hữu sản phẩm trong Scrum: đại diện cho tiếng nói khách hàng, trực tiếp quản lý và sắp xếp độ ưu tiên của Product Backlog.",
     "The PO clarifies acceptance criteria whenever engineers need business rule details.", "PO làm rõ các tiêu chí chấp nhận mỗi khi kỹ sư cần chi tiết quy tắc nghiệp vụ.",
     "Chủ sở hữu sản phẩm PO", "👔", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Scrum Master", "/skrʌm ˈmɑː.stər/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Trọng tài Scrum Master: người điều phối hỗ trợ đội ngũ tuân thủ các nguyên tắc Scrum và loại bỏ mọi trở ngại cản trở nhóm.",
     "The Scrum Master shields the team from external distractions and facilitates sprint ceremonies.", "Scrum Master bảo vệ nhóm khỏi sự xao nhãng bên ngoài và điều phối các nghi thức sprint.",
     "Trọng tài Scrum Master", "🏉", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Tech Lead", "/tek liːd/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Trưởng nhóm kỹ thuật: kỹ sư cấp cao chịu trách nhiệm về quyết định kiến trúc, chất lượng mã nguồn và dẫn dắt kỹ thuật cho nhóm.",
     "The Tech Lead approved the microservice transition proposal after an architectural review.", "Trưởng nhóm kỹ thuật đã phê duyệt đề xuất chuyển sang vi dịch vụ sau buổi đánh giá kiến trúc.",
     "Trưởng nhóm kỹ thuật Tech Lead", "💻", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Engineering Manager (EM)", "/ˌen.dʒɪˈnɪə.rɪŋ ˈmæn.ɪ.dʒər/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Quản lý kỹ thuật: người quản lý con người, tập trung vào phát triển sự nghiệp kỹ sư, tuyển dụng và cơ cấu tổ chức nhóm.",
     "The Engineering Manager conducts one-on-ones to support engineers' professional career growth.", "Quản lý kỹ thuật tổ chức các buổi 1:1 để hỗ trợ sự phát triển nghề nghiệp của các kỹ sư.",
     "Quản lý kỹ thuật EM", "🧑‍💼", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Stakeholder", "/ˈsteɪkˌhəʊl.dər/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Bên liên quan: bất kỳ cá nhân hay tổ chức nào bị ảnh hưởng bởi kết quả của dự án (khách hàng, giám đốc, nhà đầu tư).",
     "Keep key stakeholders updated on quarterly progress to maintain alignment.", "Luôn cập nhật tiến độ hàng quý cho các bên liên quan để duy trì sự thống nhất.",
     "Bên liên quan Stakeholder", "🤝", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Deliverable", "/dɪˈlɪv.ər.ə.bəl/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Sản phẩm bàn giao: kết quả đầu ra cụ thể (tính năng phần mềm, tài liệu, báo cáo kiểm thử) phải nộp theo cam kết.",
     "The primary sprint deliverable was a documented GraphQL search service endpoint.", "Sản phẩm bàn giao chính của sprint là điểm cuối dịch vụ tìm kiếm GraphQL có tài liệu.",
     "Sản phẩm bàn giao Deliverable", "📦", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600&auto=format&fit=crop&q=80"),

    ("Project Deadline", "/ˈprɒdʒ.ekt ˈded.laɪn/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Hạn chót dự án: thời điểm cuối cùng nghiêm ngặt mà công việc hoặc dự án phải được hoàn thành.",
     "The team synchronized across time zones to meet the strict regulatory project deadline.", "Nhóm đã phối hợp qua các múi giờ để kịp hạn chót nghiêm ngặt của dự án theo quy định.",
     "Hạn chót dự án Deadline", "⏰", "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=600&auto=format&fit=crop&q=80"),

    ("Scope Creep", "/skəʊp kriːp/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Phình phạm vi dự án: hiện tượng các yêu cầu và tính năng mới liên tục được thêm vào mà không tăng thời gian hay ngân sách.",
     "Scope creep caused the mobile redesign project to overshoot its targeted launch by two months.", "Phình phạm vi dự án khiến dự án thiết kế lại app di động bị trễ 2 tháng so với kế hoạch.",
     "Phình phạm vi dự án", "🎈", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Architectural Trade-off", "/ˌɑː.kɪ.tek.tʃər.əl ˈtreɪd.ɒf/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Đánh đổi kiến trúc: sự cân nhắc được - mất giữa các yếu tố (tốc độ phát triển, độ trễ, chi phí hạ tầng, khả năng bảo trì).",
     "Choosing Redis caching involved a trade-off between sub-millisecond reads and cache complexity.", "Chọn bộ đệm Redis là sự đánh đổi giữa việc đọc dưới 1 mili-giây và độ phức tạp của bộ đệm.",
     "Đánh đổi kiến trúc Trade-off", "⚖️", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Technical Debt", "/ˈtek.nɪ.kəl det/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Nợ kỹ thuật: hệ quả tích lũy lâu dài của việc chọn giải pháp chắp vá nhanh trước mắt thay vì viết mã chuẩn chỉnh.",
     "Allocating 20 percent of every sprint to paying down technical debt keeps legacy code manageable.", "Dành 20% mỗi sprint để trả nợ kỹ thuật giúp mã nguồn cũ luôn trong tầm kiểm soát.",
     "Nợ kỹ thuật Technical Debt", "💳", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Pair Programming", "/peər ˈprəʊ.ɡræm.ɪŋ/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Lập trình cặp: hai lập trình viên cùng làm việc chung trên một máy tính (một người gõ phím Driver, một người quan sát Navigator).",
     "Pair programming accelerates onboarding and eliminates single-engineer architectural blind spots.", "Lập trình cặp tăng tốc hòa nhập nhân viên mới và loại bỏ các điểm mù kiến trúc của một cá nhân.",
     "Lập trình cặp Pair Programming", "👥", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Mob Programming", "/mɒb ˈprəʊ.ɡræm.ɪŋ/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Lập trình tập thể: toàn bộ nhóm kỹ thuật cùng ngồi lại làm việc trên một bài toán hóc búa duy nhất cùng một màn hình.",
     "The team used mob programming to debug a mysterious distributed deadlock in staging.", "Cả nhóm đã dùng lập trình tập thể để gỡ lỗi một vụ bế tắc phân tán bí ẩn trên staging.",
     "Lập trình tập thể Mob", "👨‍💻👩‍💻", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("LGTM (Looks Good To Me)", "/ˌel.dʒiː.tiːˈem/", "phrase", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Tôi thấy ổn rồi: cụm từ viết tắt phổ biến nhất trên GitHub phê duyệt pull request sẵn sàng để hợp nhất mã.",
     "The reviewer approved the pull request with a succinct 'LGTM! Great test coverage.'", "Người duyệt mã đã phê duyệt pull request với lời nhắn ngắn gọn: 'LGTM! Bao phủ test rất tốt.'",
     "Phê duyệt LGTM", "👍", "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?w=600&auto=format&fit=crop&q=80"),

    ("Peer Review", "/pɪər rɪˈvjuː/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Đánh giá đồng cấp: việc các đồng nghiệp cùng chuyên môn kiểm tra chéo công việc của nhau để đảm bảo chuẩn mực.",
     "Rigorous peer review catches security vulnerabilities and logic edge cases before shipping.", "Đánh giá đồng cấp nghiêm ngặt bắt các lỗ hổng bảo mật và trường hợp biên trước khi ra mắt.",
     "Đánh giá đồng cấp Peer Review", "👀", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("On-Call Duty", "/ɒn kɔːl ˈdjuː.ti/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Trực ca sự cố On-Call: phân công kỹ sư trực ngoài giờ để ứng cứu ngay lập tức khi hệ thống sản xuất gặp sự cố nghiêm trọng.",
     "Engineers carry the on-call pager for one week in a rotating team roster.", "Các kỹ sư giữ thiết bị trực sự cố trong một tuần theo danh sách xoay vòng của nhóm.",
     "Trực sự cố On-Call", "📟", "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=600&auto=format&fit=crop&q=80"),

    ("Incident Management", "/ˈɪn.sɪ.dənt ˈmæn.ɪdʒ.mənt/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Quản lý sự cố: quy trình điều phối và khắc phục nhằm khôi phục dịch vụ trở lại bình thường nhanh nhất khi có sự cố ngừng hoạt động.",
     "Incident management workflows assign incident commanders and communications leads during major outages.", "Quy trình quản lý sự cố phân công chỉ huy trưởng và đầu mối thông tin trong lúc sập mạng.",
     "Quản lý sự cố Incident", "🚨", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Post-Mortem", "/ˌpəʊstˈmɔː.təm/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Báo cáo mổ xẻ sự cố: buổi họp và tài liệu phân tích nguyên nhân gốc rễ sau sự cố nhằm ngăn chặn lặp lại mà không quy trách nhiệm cá nhân (blameless).",
     "A blameless post-mortem focuses on systemic architectural flaws rather than blaming human error.", "Buổi mổ xẻ không đổ lỗi tập trung vào lỗi kiến trúc hệ thống thay vì trách móc con người.",
     "Báo cáo mổ xẻ Post-Mortem", "📋", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Root Cause Analysis (RCA)", "/ruːt kɔːz əˈnæl.ə.sɪs/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Phân tích nguyên nhân gốc rễ: phương pháp dùng kỹ thuật '5 Tại sao' để tìm ra nguyên nhân sâu xa nhất gây ra sự cố hệ thống.",
     "RCA revealed that an unindexed database query exhausted the server's connection pool.", "Phân tích nguyên nhân gốc rễ đã chỉ ra câu truy vấn thiếu chỉ mục làm cạn kiệt connection pool.",
     "Nguyên nhân gốc rễ RCA", "🔍", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Knowledge Sharing", "/ˈnɒl.ɪdʒ ˈʃeə.rɪŋ/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Chia sẻ tri thức: việc phổ biến kinh nghiệm, kỹ năng và hiểu biết kỹ thuật giữa các thành viên trong tổ chức.",
     "Friday knowledge sharing sessions introduce the engineering team to new tooling and best practices.", "Buổi chia sẻ tri thức thứ Sáu giới thiệu cho nhóm kỹ sư các công cụ mới và thực hành tối ưu.",
     "Chia sẻ tri thức", "💡", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Documentation", "/ˌdɒk.jə.menˈteɪ.ʃən/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Tài liệu kỹ thuật: văn bản hướng dẫn chi tiết về cấu trúc mã nguồn, thiết kế hệ thống và cách cài đặt vận hành phần mềm.",
     "Good technical documentation reduces developer ramp-up time from weeks to days.", "Tài liệu kỹ thuật tốt rút ngắn thời gian làm quen của lập trình viên từ vài tuần xuống vài ngày.",
     "Tài liệu kỹ thuật Docs", "📚", "https://images.unsplash.com/photo-1521587760476-6c12a4b040da?w=600&auto=format&fit=crop&q=80"),

    ("Confluence", "/ˈkɒn.fluː.əns/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Nền tảng Confluence: công cụ không gian làm việc cộng tác và quản lý cơ sở tri thức kỹ thuật của Atlassian.",
     "Product specifications, architecture diagrams, and post-mortems live inside Confluence spaces.", "Thông số sản phẩm, sơ đồ kiến trúc và báo cáo mổ xẻ được lưu trong không gian Confluence.",
     "Cơ sở tri thức Confluence", "🏢", "https://images.unsplash.com/photo-1521587760476-6c12a4b040da?w=600&auto=format&fit=crop&q=80"),

    ("Jira", "/ˈdʒɪə.rə/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Phần mềm Jira: công cụ quản lý dự án và theo dõi lỗi phổ biến nhất thế giới dành cho các đội ngũ phát triển phần mềm Agile.",
     "Engineers update ticket status columns on Jira to communicate progress across departments.", "Kỹ sư cập nhật các cột trạng thái thẻ trên Jira để thông báo tiến độ giữa các phòng ban.",
     "Quản lý công việc Jira", "🎯", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("One-on-One Meeting (1:1)", "/wʌn ɒn wʌn ˈmiː.tɪŋ/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Họp 1-1: cuộc trò chuyện định kỳ trực tiếp giữa nhân viên và quản lý để trao đổi về tâm tư, định hướng sự nghiệp và phản hồi hai chiều.",
     "Weekly 1:1 meetings provide dedicated time to discuss career progression, mentorship, and roadblocks.", "Họp 1:1 hàng tuần dành thời gian riêng để bàn về thăng tiến sự nghiệp và tháo gỡ trở ngại.",
     "Họp riêng 1:1", "☕", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("All-Hands Meeting", "/ɔːl hændz ˈmiː.tɪŋ/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Họp toàn thể công ty: cuộc họp định kỳ của toàn bộ nhân viên công ty nơi ban lãnh đạo chia sẻ mục tiêu chiến lược và tài chính.",
     "The CEO announced corporate quarterly revenue achievements during the monthly all-hands meeting.", "CEO đã công bố doanh thu hàng quý của công ty trong buổi họp toàn thể hàng tháng.",
     "Họp toàn thể All-Hands", "📢", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Employee Onboarding", "/ɪmˈplɔɪ.iː ˈɒnˌbɔː.dɪŋ/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Hòa nhập nhân viên mới: quy trình đào tạo và hướng dẫn lập trình viên mới làm quen với mã nguồn, công cụ và văn hóa công ty.",
     "A clear onboarding checklist helps new engineers make their first production commit in week one.", "Bảng danh mục onboarding rõ ràng giúp kỹ sư mới có commit lên môi trường thật ngay tuần đầu.",
     "Hòa nhập nhân viên mới", "🤝", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Employee Offboarding", "/ɪmˈplɔɪ.iː ˈɒfˌbɔː.dɪŋ/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Quy trình thôi việc: thu hồi quyền truy cập hệ thống, bàn giao dự án và phỏng vấn kết thúc khi nhân viên rời tổ chức.",
     "Security policies mandate immediate revocation of VPN and GitHub permissions during offboarding.", "Chính sách bảo mật yêu cầu thu hồi ngay quyền VPN và GitHub trong quy trình bàn giao thôi việc.",
     "Quy trình thôi việc", "👋", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Sync Meeting", "/sɪŋk ˈmiː.tɪŋ/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Họp đồng bộ tiến độ: cuộc họp ngắn giữa hai hoặc nhiều bên để cập nhật tình hình công việc và thống nhất bước tiếp theo.",
     "Let's schedule a 10-minute sync meeting to clarify API contract schemas.", "Hãy lên lịch họp đồng bộ 10 phút để làm rõ cấu trúc hợp đồng API.",
     "Họp đồng bộ Sync Meeting", "🔄", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Asynchronous Communication", "/eɪˈsɪŋ.krə.nəs kəˌmjuː.nɪˈkeɪ.ʃən/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Giao tiếp bất đồng bộ: trao đổi thông tin qua văn bản (Slack, email, tài liệu) mà không đòi hỏi đối phương phải trả lời ngay tức thì.",
     "Remote companies thrive on asynchronous communication to empower global time zone flexibility.", "Công ty làm từ xa phát triển nhờ giao tiếp bất đồng bộ để linh hoạt giữa các múi giờ toàn cầu.",
     "Giao tiếp bất đồng bộ", "💬", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Team Bandwidth (Capacity)", "/tiːm ˈbænd.wɪtθ/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Khả năng gánh việc của nhóm: quỹ thời gian và năng lực thực tế mà đội ngũ có thể dành cho dự án trong một khoảng thời gian.",
     "We lack the bandwidth to take on extra feature requests this sprint without dropping existing tasks.", "Chúng tôi không còn đủ dung lượng gánh việc để nhận thêm yêu cầu mới trong sprint này.",
     "Dung lượng gánh việc Bandwidth", "🔋", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Blocked Status", "/blɒkt ˈsteɪ.təs/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Trạng thái bị tắc nghẽn: tình trạng công việc không thể tiến triển tiếp do đang phải đợi sự hỗ trợ, phê duyệt hoặc phụ thuộc bên ngoài.",
     "I am currently blocked on frontend integration pending the deployment of the auth endpoint.", "Tôi hiện đang bị tắc nghẽn ở khâu tích hợp giao diện do phải đợi điểm cuối xác thực được triển khai.",
     "Trạng thái tắc nghẽn Blocked", "🛑", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80"),

    ("Action Item", "/ˈæk.ʃən ˈaɪ.təm/", "noun", "qa_workplace", "Kiểm thử & Tiếng Anh Công sở",
     "Hạng mục hành động: đầu việc cụ thể được phân công cho người phụ trách kèm thời hạn rõ ràng rút ra sau cuộc họp.",
     "The meeting notes listed three key action items with designated owners and Friday due dates.", "Biên bản cuộc họp liệt kê ba hạng mục hành động chính kèm người phụ trách và hạn chót thứ Sáu.",
     "Hạng mục hành động", "✅", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80")
]

if __name__ == "__main__":
    print(f"Domain 10 terms count: {len(terms)}")
