# -*- coding: utf-8 -*-
"""Domain 8: Web, API & Mobile Engineering (100 core terms)"""

terms = [
    ("Frontend Development", "/ˌfrʌnt.end dɪˈvel.əp.mənt/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Phát triển giao diện: xây dựng phần nhìn thấy và tương tác trực tiếp của người dùng trên trang web hoặc ứng dụng.",
     "Frontend development requires mastery of HTML, CSS, JavaScript, and user experience.", "Phát triển frontend đòi hỏi phải thành thạo HTML, CSS, JavaScript và trải nghiệm người dùng.",
     "Phát triển giao diện Frontend", "🎨", "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=600&auto=format&fit=crop&q=80"),

    ("Backend Development", "/ˌbæk.end dɪˈvel.əp.mənt/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Phát triển phía máy chủ: xây dựng logic nghiệp vụ, xử lý dữ liệu, API và tích hợp cơ sở dữ liệu trên máy chủ.",
     "Backend developers focus on database queries, authentication, and API scalability.", "Lập trình viên backend tập trung vào truy vấn CSDL, xác thực và khả năng mở rộng API.",
     "Phát triển máy chủ Backend", "⚙️", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Full Stack Development", "/fʊl stæk dɪˈvel.əp.mənt/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Phát triển toàn diện Full Stack: khả năng làm việc thành thạo trên cả hai tầng frontend giao diện và backend máy chủ.",
     "Full stack engineers can prototype complete end-to-end web applications independently.", "Kỹ sư full stack có thể tự mình tạo nguyên mẫu hoàn chỉnh ứng dụng web từ đầu đến cuối.",
     "Lập trình toàn diện Full Stack", "🥞", "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    ("HTML (HyperText Markup Language)", "/ˌeɪtʃ.tiː.emˈel/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Ngôn ngữ đánh dấu siêu văn bản: ngôn ngữ tiêu chuẩn định hình cấu trúc và nội dung ngữ nghĩa của các trang web.",
     "HTML5 introduces semantic tags like header, article, section, and footer.", "HTML5 giới thiệu các thẻ ngữ nghĩa như header, article, section và footer.",
     "Ngôn ngữ cấu trúc HTML", "🌐", "https://images.unsplash.com/photo-1542838132-92c53300491e?w=600&auto=format&fit=crop&q=80"),

    ("CSS (Cascading Style Sheets)", "/ˌsiː.esˈes/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Bảng kiểu định dạng tầng: ngôn ngữ quy định cách trình bày trực quan, màu sắc, phông chữ và bố cục của tài liệu HTML.",
     "CSS transforms raw HTML markup into beautiful, styled web layouts.", "CSS biến đổi mã HTML thô thành các giao diện web đẹp mắt và có phong cách.",
     "Định dạng giao diện CSS", "🎨", "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=600&auto=format&fit=crop&q=80"),

    ("JavaScript", "/ˈdʒɑː.və.skrɪpt/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Ngôn ngữ JavaScript: ngôn ngữ lập trình kịch bản thông dịch năng động đem lại tính tương tác cho trình duyệt web.",
     "Modern JavaScript engines like V8 compile script code into native machine instructions.", "Các công cụ JavaScript hiện đại như V8 biên dịch mã kịch bản thành chỉ lệnh máy gốc.",
     "Ngôn ngữ JavaScript", "💛", "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    ("TypeScript", "/ˈtaɪp.skrɪpt/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Ngôn ngữ TypeScript: phần mở rộng cú pháp của JavaScript do Microsoft phát triển bổ sung kiểm tra kiểu tĩnh an toàn.",
     "TypeScript catches runtime type errors during development before compilation.", "TypeScript bắt các lỗi kiểu dữ liệu lúc chạy ngay trong quá trình phát triển trước khi biên dịch.",
     "Ngôn ngữ TypeScript", "🔷", "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    ("DOM (Document Object Model)", "/dɒm/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Mô hình đối tượng tài liệu: biểu diễn dạng cây của tài liệu HTML cho phép JavaScript truy cập và chỉnh sửa giao diện động.",
     "JavaScript manipulates DOM nodes to update user interface contents dynamically.", "JavaScript thao tác trên các nút DOM để cập nhật nội dung giao diện người dùng động.",
     "Mô hình cây DOM", "🌳", "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    ("Virtual DOM", "/ˈvɜː.tʃu.əl dɒm/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "DOM ảo: bản sao nhẹ của DOM thực tế lưu trong bộ nhớ giúp các thư viện như React tối ưu việc kết xuất lại giao diện.",
     "The virtual DOM computes minimal diffs to update real browser elements efficiently.", "DOM ảo tính toán chênh lệch tối thiểu để cập nhật phần tử trình duyệt thực hiệu quả.",
     "Mô hình DOM ảo", "⚡", "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    ("Responsive Web Design", "/rɪˈspɒn.sɪv ˈweb dɪˈzaɪn/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Thiết kế web đáp ứng: phương pháp thiết kế giúp trang web tự động thích ứng hoàn hảo với mọi kích thước màn hình.",
     "Responsive web design uses CSS media queries and fluid grids to support smartphones.", "Thiết kế web đáp ứng dùng truy vấn media CSS và lưới linh hoạt để hỗ trợ smartphone.",
     "Thiết kế web đáp ứng RWD", "📱", "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=600&auto=format&fit=crop&q=80"),

    ("CSS Grid", "/ˌsiː.esˈes ɡrɪd/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Bố cục lưới CSS Grid: hệ thống bố cục hai chiều (hàng và cột) mạnh mẽ cho phép thiết kế giao diện web phức tạp.",
     "CSS Grid simplifies building complex dashboard layouts without extra div wrappers.", "CSS Grid đơn giản hóa việc xây dựng bố cục dashboard phức tạp mà không cần nhiều thẻ div bọc.",
     "Bố cục lưới CSS Grid", "📐", "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=600&auto=format&fit=crop&q=80"),

    ("Flexbox", "/ˈfleks.bɒks/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Mô hình Flexbox: mô hình bố cục một chiều (theo hàng hoặc cột) giúp căn chỉnh và phân bổ không gian giữa các phần tử.",
     "Use Flexbox to center elements both vertically and horizontally in one line of CSS.", "Dùng Flexbox để căn giữa phần tử cả chiều dọc và ngang chỉ với một dòng mã CSS.",
     "Mô hình hộp linh hoạt Flexbox", "📦", "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=600&auto=format&fit=crop&q=80"),

    ("Tailwind CSS", "/ˈteɪl.wɪnd ˌsiː.esˈes/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Khung tiện ích Tailwind CSS: khung giao diện hướng tiện ích cung cấp hàng ngàn lớp CSS nhỏ để tạo giao diện nhanh chóng.",
     "Tailwind CSS accelerates UI styling without writing custom stylesheet files.", "Tailwind CSS tăng tốc thiết kế UI mà không cần viết các tệp định dạng tùy biến riêng.",
     "Khung giao diện Tailwind CSS", "🌊", "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=600&auto=format&fit=crop&q=80"),

    ("Bootstrap", "/ˈbuːt.stræp/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Khung giao diện Bootstrap: bộ khung thành phần HTML, CSS, JS mã nguồn mở kinh điển do Twitter xây dựng.",
     "Bootstrap provides ready-made modals, navbars, and buttons for rapid prototyping.", "Bootstrap cung cấp sẵn hộp thoại modal, thanh điều hướng và nút bấm để tạo nguyên mẫu nhanh.",
     "Khung giao diện Bootstrap", "🥾", "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=600&auto=format&fit=crop&q=80"),

    ("Sass / SCSS", "/sæs/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Trình tiền xử lý Sass: ngôn ngữ mở rộng của CSS bổ sung biến số, lồng khối, mixin và hàm tái sử dụng.",
     "SCSS variables help maintain consistent brand colors across extensive style sheets.", "Biến SCSS giúp duy trì màu sắc thương hiệu nhất quán qua các bảng định dạng lớn.",
     "Tiền xử lý kiểu dáng Sass", "💅", "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=600&auto=format&fit=crop&q=80"),

    ("Webpack", "/ˈweb.pæk/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Công cụ đóng gói Webpack: trình đóng gói mô-đun tĩnh cho các ứng dụng JavaScript hiện đại.",
     "Webpack bundles JavaScript modules, CSS assets, and images into optimized bundles.", "Webpack đóng gói các mô-đun JavaScript, tài nguyên CSS và hình ảnh thành các gói tối ưu.",
     "Công cụ đóng gói Webpack", "📦", "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    ("Vite", "/viːt/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Công cụ dựng Vite: công cụ xây dựng frontend thế hệ mới cực nhanh tận dụng các mô-đun ESM bản địa của trình duyệt.",
     "Vite provides near-instantaneous Hot Module Replacement (HMR) during frontend development.", "Vite mang lại khả năng thay thế mô-đun nóng (HMR) gần như tức thì khi phát triển frontend.",
     "Công cụ dựng siêu tốc Vite", "⚡", "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    ("Babel", "/ˈbeɪ.bəl/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Trình chuyển đổi Babel: trình chuyển đổi mã JavaScript thế hệ mới (ES6+) thành mã tương thích với các trình duyệt cũ.",
     "Babel transforms modern ECMAScript syntax and JSX into cross-browser JavaScript.", "Babel chuyển đổi cú pháp ECMAScript hiện đại và JSX thành JavaScript tương thích mọi trình duyệt.",
     "Trình chuyển đổi Babel", "🔄", "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    ("Module Bundler", "/ˈmɒdʒ.uːl ˈbʌn.dlər/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Trình đóng gói mô-đun: công cụ phân tích đồ thị phụ thuộc mã nguồn và gom các tệp lại thành các gói nhỏ gọn gửi tới client.",
     "Module bundlers perform tree-shaking to eliminate dead, unused code from outputs.", "Trình đóng gói mô-đun thực hiện rung cây (tree-shaking) để loại bỏ mã thừa không dùng.",
     "Trình đóng gói mô-đun", "📦", "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    ("Single Page Application (SPA)", "/ˈsɪŋ.ɡəl peɪdʒ/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Ứng dụng một trang (SPA): ứng dụng web tải một trang HTML duy nhất và cập nhật nội dung động mà không tải lại toàn trang.",
     "React and Vue are commonly used to develop highly interactive SPAs.", "React và Vue thường được dùng để phát triển các ứng dụng một trang SPA tương tác cao.",
     "Ứng dụng một trang SPA", "📄", "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=600&auto=format&fit=crop&q=80"),

    ("Multi-Page Application (MPA)", "/ˈmʌl.ti peɪdʒ/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Ứng dụng nhiều trang (MPA): ứng dụng web truyền thống trong đó mỗi thao tác chuyển trang đều yêu cầu máy chủ trả về trang HTML mới.",
     "Traditional e-commerce websites often use an MPA structure for maximum search SEO visibility.", "Các trang thương mại điện tử truyền thống thường dùng cấu trúc MPA để tối ưu hóa SEO tìm kiếm.",
     "Ứng dụng nhiều trang MPA", "📑", "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=600&auto=format&fit=crop&q=80"),

    ("Server-Side Rendering (SSR)", "/ˈsɜː.vər saɪd ˈren.dər.ɪŋ/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Kết xuất phía máy chủ (SSR): máy chủ kết xuất sẵn mã HTML hoàn chỉnh và gửi tới trình duyệt để tăng tốc tải trang và SEO.",
     "Next.js provides built-in server-side rendering to boost SEO indexing rankings.", "Next.js cung cấp tính năng kết xuất phía máy chủ tích hợp sẵn để tăng thứ hạng SEO.",
     "Kết xuất máy chủ SSR", "🖥️", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Static Site Generation (SSG)", "/ˈstæt.ɪk saɪt ˌdʒen.əˈreɪ.ʃən/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Tạo trang tĩnh (SSG): tạo trước tất cả các trang HTML tĩnh ngay tại thời điểm xây dựng bản dựng (build-time).",
     "Documentation portals use SSG to deliver lightning-fast static pages via CDN.", "Các cổng tài liệu dùng SSG để cung cấp các trang tĩnh nhanh như chớp qua CDN.",
     "Tạo trang tĩnh SSG", "⚡", "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=600&auto=format&fit=crop&q=80"),

    ("Incremental Static Regeneration (ISR)", "/ˌɪŋ.krəˈmen.təl/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Tái tạo tĩnh gia tăng (ISR): cho phép cập nhật từng trang tĩnh riêng biệt ở chế độ nền mà không cần xây dựng lại toàn bộ trang web.",
     "ISR updates product catalog pages on-demand without rebuilding thousands of static files.", "ISR cập nhật các trang danh mục sản phẩm theo yêu cầu mà không cần build lại hàng ngàn tệp.",
     "Tái tạo tĩnh gia tăng ISR", "🔄", "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=600&auto=format&fit=crop&q=80"),

    ("Client-Side Rendering (CSR)", "/ˈklaɪ.ənt saɪd ˈren.dər.ɪŋ/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Kết xuất phía máy khách (CSR): trình duyệt tải trang HTML rỗng và mã JavaScript để tự kết xuất toàn bộ giao diện phía người dùng.",
     "CSR offloads rendering work to the user's browser but can suffer slower initial loads.", "CSR giảm tải việc kết xuất cho máy chủ nhưng có thể tải trang lần đầu chậm hơn.",
     "Kết xuất máy khách CSR", "💻", "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=600&auto=format&fit=crop&q=80"),

    ("Hydration", "/haɪˈdreɪ.ʃən/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Bù ẩm dữ liệu: quá trình JavaScript phía trình duyệt gắn các trình xử lý sự kiện vào mã HTML tĩnh do máy chủ gửi sang.",
     "React hydration makes the server-rendered HTML interactive inside the browser.", "Quá trình hydration trong React biến mã HTML do máy chủ kết xuất thành giao diện có thể tương tác.",
     "Bù ẩm giao diện Hydration", "💧", "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=600&auto=format&fit=crop&q=80"),

    ("Progressive Web App (PWA)", "/prəˈɡres.ɪv web æp/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Ứng dụng web cấp tiến (PWA): trang web mang lại trải nghiệm cài đặt, thông báo đẩy và chạy ngoại tuyến như ứng dụng di động bản địa.",
     "PWAs let mobile users install websites directly to their phone home screens.", "PWA cho phép người dùng di động cài đặt trang web trực tiếp lên màn hình chính.",
     "Ứng dụng web cấp tiến PWA", "📱", "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=600&auto=format&fit=crop&q=80"),

    ("Service Worker", "/ˈsɜː.vɪs ˈwɜː.kər/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Tiến trình dịch vụ Service Worker: kịch bản JavaScript chạy ngầm riêng biệt với trang web, cho phép lưu đệm ngoại tuyến và thông báo đẩy.",
     "The service worker intercepts network requests to serve cached assets when offline.", "Service worker chặn các yêu cầu mạng để phục vụ tài nguyên lưu đệm khi mất mạng.",
     "Tiến trình Service Worker", "🛠️", "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=600&auto=format&fit=crop&q=80"),

    ("Web App Manifest", "/web æp ˈmæn.ɪ.fest/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Tệp manifest ứng dụng web: tệp JSON chứa siêu dữ liệu (tên app, biểu tượng icon, màu sắc) phục vụ việc cài đặt PWA.",
     "The manifest.json file tells the mobile OS how to display the installed web application.", "Tệp manifest.json chỉ dẫn cho hệ điều hành di động cách hiển thị ứng dụng web đã cài đặt.",
     "Tệp cấu hình Web Manifest", "📋", "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=600&auto=format&fit=crop&q=80"),

    ("LocalStorage", "/ˈləʊ.kəl ˈstɔː.rɪdʒ/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Bộ nhớ cục bộ: cơ chế lưu trữ cặp khóa - giá trị vĩnh viễn trên trình duyệt của người dùng (dung lượng khoảng 5-10MB).",
     "Persist dark theme user preferences inside the browser's localStorage.", "Lưu giữ tùy chọn chế độ nền tối của người dùng bên trong bộ nhớ localStorage.",
     "Bộ nhớ cục bộ LocalStorage", "💾", "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=600&auto=format&fit=crop&q=80"),

    ("SessionStorage", "/ˈseʃ.ən ˈstɔː.rɪdʒ/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Bộ nhớ phiên: lưu trữ cặp khóa - giá trị chỉ tồn tại trong suốt thời gian mở thẻ duyệt web hiện tại.",
     "SessionStorage clears all preserved checkout form data when the user closes the tab.", "SessionStorage xóa sạch toàn bộ dữ liệu đơn hàng khi người dùng đóng thẻ trình duyệt.",
     "Bộ nhớ phiên SessionStorage", "⏱️", "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=600&auto=format&fit=crop&q=80"),

    ("IndexedDB", "/ˈɪn.dekst ˌdiːˈbiː/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Cơ sở dữ liệu IndexedDB: CSDL NoSQL giao dịch tích hợp sẵn trong trình duyệt để lưu trữ lượng lớn dữ liệu có cấu trúc ngoại tuyến.",
     "Offline web apps store hundreds of downloaded documents locally using IndexedDB.", "Ứng dụng web ngoại tuyến lưu trữ hàng trăm tài liệu tải về bằng IndexedDB.",
     "CSDL trình duyệt IndexedDB", "🗄️", "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=600&auto=format&fit=crop&q=80"),

    ("HTTP Cookie", "/ˌeɪtʃ.tiː.tiːˈpiː ˈkʊk.i/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Cookie HTTP: mẩu dữ liệu nhỏ do máy chủ gửi và lưu trên trình duyệt, tự động đính kèm theo mỗi yêu cầu tiếp theo.",
     "Secure HTTP-only cookies prevent JavaScript from accessing sensitive session IDs.", "Cookie bảo mật HTTP-only ngăn JavaScript truy cập vào mã định danh phiên nhạy cảm.",
     "Bánh quy Cookie HTTP", "🍪", "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=600&auto=format&fit=crop&q=80"),

    ("SameSite Cookie", "/seɪm saɪt ˈkʊk.i/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Thuộc tính SameSite: cờ bảo mật của cookie quy định cookie có được gửi kèm trong các yêu cầu chéo trang hay không.",
     "Setting SameSite=Lax defends user authentication cookies against CSRF attacks.", "Thiết lập SameSite=Lax bảo vệ cookie xác thực người dùng khỏi các cuộc tấn công CSRF.",
     "Cờ bảo mật SameSite", "🛡️", "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=600&auto=format&fit=crop&q=80"),

    ("REST (Representational State Transfer)", "/rest/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Kiến trúc REST: phong cách kiến trúc phần mềm tiêu chuẩn cho hệ thống phân tán sử dụng các phương thức HTTP phi trạng thái.",
     "REST principles mandate stateless client-server interactions using standard HTTP verbs.", "Các nguyên lý REST quy định giao tiếp phi trạng thái giữa client và server dùng động từ HTTP.",
     "Kiến trúc REST", "🏛️", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("RESTful API", "/ˈrest.fʊl ˌeɪ.piːˈaɪ/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Giao diện RESTful API: giao diện API tuân thủ đầy đủ các ràng buộc thiết kế của kiến trúc REST.",
     "Our mobile application consumes a RESTful API to synchronize user data with the cloud.", "Ứng dụng di động của chúng tôi sử dụng API RESTful để đồng bộ dữ liệu người dùng lên mây.",
     "Giao diện RESTful API", "🔌", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("API Endpoint", "/ˌeɪ.piːˈaɪ ˈend.pɔɪnt/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Điểm cuối API: địa chỉ URL cụ thể trên máy chủ nơi ứng dụng khách gửi yêu cầu để thực hiện một hành động.",
     "The '/api/v1/users' endpoint returns a JSON list of registered profiles.", "Điểm cuối '/api/v1/users' trả về danh sách hồ sơ đã đăng ký dưới dạng JSON.",
     "Điểm cuối API Endpoint", "📍", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("HTTP Methods", "/ˌeɪtʃ.tiː.tiːˈpiː ˈmeθ.ədz/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Phương thức HTTP: tập hợp các động từ chỉ rõ hành động mong muốn được thực thi trên tài nguyên (GET, POST, PUT, DELETE).",
     "Standard HTTP methods clarify whether an API request is fetching, modifying, or creating data.", "Các phương thức HTTP tiêu chuẩn làm rõ yêu cầu API là lấy, sửa hay tạo mới dữ liệu.",
     "Phương thức HTTP", "🔤", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("GET Request", "/ɡet rɪˈkwest/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Yêu cầu GET: phương thức an toàn dùng để trích xuất dữ liệu từ máy chủ mà không làm thay đổi trạng thái tài nguyên.",
     "Browsers issue GET requests when navigating to web links.", "Trình duyệt phát ra các yêu cầu GET khi người dùng chuyển hướng tới các liên kết web.",
     "Yêu cầu GET", "📥", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("POST Request", "/pəʊst rɪˈkwest/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Yêu cầu POST: phương thức gửi dữ liệu trong thân yêu cầu (body) lên máy chủ để tạo mới tài nguyên hoặc xử lý biểu mẫu.",
     "Submitting the registration form fires an HTTP POST request carrying the user data.", "Gửi biểu mẫu đăng ký sẽ kích hoạt yêu cầu HTTP POST mang theo dữ liệu người dùng.",
     "Yêu cầu tạo mới POST", "📤", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("PUT Request", "/pʊt rɪˈkwest/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Yêu cầu PUT: phương thức thay thế toàn bộ tài nguyên hiện có bằng dữ liệu gửi kèm (hoặc tạo mới nếu chưa tồn tại).",
     "A PUT request replaces the complete target document with the submitted payload.", "Yêu cầu PUT thay thế hoàn toàn tài nguyên mục tiêu bằng dữ liệu tải trọng vừa gửi.",
     "Yêu cầu thay thế PUT", "🔄", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("PATCH Request", "/pætʃ rɪˈkwest/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Yêu cầu PATCH: phương thức áp dụng các chỉnh sửa từng phần đối với tài nguyên mà không cần gửi lại toàn bộ dữ liệu.",
     "Use a PATCH request to modify only the user's phone number without altering other fields.", "Dùng yêu cầu PATCH để chỉ sửa số điện thoại mà không làm thay đổi các trường dữ liệu khác.",
     "Yêu cầu sửa đổi PATCH", "🩹", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("DELETE Request", "/dɪˈliːt rɪˈkwest/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Yêu cầu DELETE: phương thức yêu cầu máy chủ xóa bỏ tài nguyên được chỉ định.",
     "Clicking the remove button triggers an HTTP DELETE request to delete the post.", "Nhấp vào nút xóa sẽ kích hoạt yêu cầu HTTP DELETE để xóa bài đăng.",
     "Yêu cầu xóa DELETE", "🗑️", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("HTTP Status Codes", "/ˌeɪtʃ.tiː.tiːˈpiː ˈsteɪ.təs kəʊdz/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Mã trạng thái HTTP: mã số 3 chữ số do máy chủ trả về cho biết kết quả thành công hay thất bại của yêu cầu HTTP.",
     "HTTP status codes are categorized into informational, success, redirection, client, and server errors.", "Mã trạng thái HTTP phân thành các nhóm: thông tin, thành công, chuyển hướng, lỗi client và lỗi máy chủ.",
     "Mã trạng thái HTTP", "🔢", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("200 OK", "/tuː ˈhʌn.drəd əʊˈkeɪ/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Mã 200 OK: mã trạng thái tiêu chuẩn báo hiệu yêu cầu HTTP đã được xử lý hoàn toàn thành công.",
     "The API returns 200 OK accompanied by the requested JSON payload.", "API trả về mã 200 OK kèm theo dữ liệu JSON được yêu cầu.",
     "Thành công 200 OK", "✅", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("201 Created", "/tuː ˈhʌn.drəd wʌn/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Mã 201 Created: báo hiệu yêu cầu đã thành công và một tài nguyên mới đã được tạo ra thành công trên máy chủ.",
     "Successful POST requests registering new accounts should respond with 201 Created.", "Yêu cầu POST đăng ký tài khoản mới thành công nên phản hồi mã 201 Created.",
     "Đã tạo mới 201 Created", "✨", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("204 No Content", "/tuː ˈhʌn.drəd fɔːr/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Mã 204 No Content: yêu cầu thành công nhưng máy chủ không cần trả về bất kỳ nội dung nào trong phần thân (body).",
     "Successful DELETE operations conventionally return 204 No Content.", "Các thao tác xóa DELETE thành công theo quy ước sẽ trả về mã 204 No Content.",
     "Không nội dung 204 No Content", "📭", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("400 Bad Request", "/fɔː ˈhʌn.drəd/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Mã 400 Bad Request: máy chủ không thể hiểu hoặc xử lý yêu cầu do lỗi cú pháp hoặc dữ liệu gửi lên không hợp lệ.",
     "Submitting a malformed JSON body results in a 400 Bad Request response.", "Gửi phần thân JSON sai định dạng cú pháp dẫn tới phản hồi lỗi 400 Bad Request.",
     "Lỗi yêu cầu 400 Bad Request", "⚠️", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("401 Unauthorized", "/fɔː ˈhʌn.drəd wʌn/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Mã 401 Chưa xác thực: yêu cầu bị từ chối do thiếu thông tin xác thực danh tính hợp lệ hoặc token đã hết hạn.",
     "Requests lacking an Authorization bearer header receive a 401 Unauthorized status.", "Các yêu cầu thiếu tiêu đề Authorization bearer sẽ nhận mã trạng thái 401 Unauthorized.",
     "Chưa xác thực 401 Unauthorized", "🚫", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("403 Forbidden", "/fɔː ˈhʌn.drəd θriː/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Mã 403 Bị cấm: máy chủ hiểu danh tính của người dùng nhưng từ chối cấp quyền truy cập tài nguyên được yêu cầu.",
     "A non-admin user attempting to access administrative dashboards receives a 403 Forbidden.", "Người dùng không phải quản trị viên cố truy cập dashboard quản trị sẽ nhận mã 403 Forbidden.",
     "Bị cấm quyền 403 Forbidden", "⛔", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("404 Not Found", "/fɔː ˈhʌn.drəd fɔːr/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Mã 404 Không tìm thấy: máy chủ không thể tìm thấy tài nguyên tương ứng với đường dẫn URL được yêu cầu.",
     "Typing an incorrect webpage URL in the browser triggers a 404 Not Found error page.", "Gõ sai địa chỉ URL trang web trong trình duyệt sẽ kích hoạt trang lỗi 404 Not Found.",
     "Không tìm thấy 404 Not Found", "🔍", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("500 Internal Server Error", "/faɪv ˈhʌn.drəd/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Mã 500 Lỗi nội bộ máy chủ: máy chủ gặp sự cố bất ngờ hoặc ngoại lệ chưa được xử lý trong mã nguồn backend.",
     "Uncaught backend exceptions trigger a 500 Internal Server Error response.", "Ngoại lệ phía backend không được bắt sẽ gây ra phản hồi lỗi 500 Internal Server Error.",
     "Lỗi máy chủ 500 Error", "💥", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("502 Bad Gateway", "/faɪv ˈhʌn.drəd tuː/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Mã 502 Cổng trung gian lỗi: máy chủ proxy hoặc load balancer nhận phản hồi không hợp lệ từ máy chủ backend phía sau.",
     "When Node.js backend processes crash, Nginx reverse proxy returns a 502 Bad Gateway.", "Khi tiến trình backend Node.js bị sập, proxy Nginx trả về lỗi 502 Bad Gateway.",
     "Cổng trung gian lỗi 502", "🚪", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("503 Service Unavailable", "/faɪv ˈhʌn.drəd θriː/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Mã 503 Dịch vụ không khả dụng: máy chủ tạm thời không thể tiếp nhận yêu cầu do đang quá tải hoặc bảo trì.",
     "Deploying maintenance mode displays a friendly 503 Service Unavailable notice.", "Bật chế độ bảo trì sẽ hiển thị thông báo thân thiện 503 Service Unavailable.",
     "Dịch vụ quá tải 503", "🚧", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("504 Gateway Timeout", "/faɪv ˈhʌn.drəd fɔːr/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Mã 504 Hết thời gian chờ: máy chủ proxy không nhận được phản hồi kịp thời từ máy chủ cấp cao hơn.",
     "A slow SQL query running over 60 seconds triggered a 504 Gateway Timeout.", "Câu truy vấn SQL chậm chạy quá 60 giây đã kích hoạt lỗi 504 Gateway Timeout.",
     "Hết thời gian chờ 504", "⏰", "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=600&auto=format&fit=crop&q=80"),

    ("GraphQL", "/ˌɡræf.kjuːˈel/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Ngôn ngữ truy vấn GraphQL: cho phép client yêu cầu chính xác những trường dữ liệu mình cần, tránh thừa hoặc thiếu dữ liệu.",
     "GraphQL solves over-fetching and under-fetching common in REST API architectures.", "GraphQL giải quyết triệt để tình trạng lấy thừa hoặc thiếu dữ liệu thường gặp trong REST.",
     "Ngôn ngữ truy vấn GraphQL", "🕸️", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("GraphQL Schema", "/ˌɡræf.kjuːˈel ˈskiː.mə/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Lược đồ GraphQL: bản hợp đồng định nghĩa chặt chẽ tất cả các kiểu dữ liệu, trường, truy vấn và mutation khả dụng.",
     "The GraphQL schema clearly documents the exact shapes of accessible API objects.", "Lược đồ GraphQL ghi lại chính xác cấu trúc hình dạng của các đối tượng API truy cập được.",
     "Lược đồ GraphQL Schema", "📐", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("GraphQL Query", "/ˌɡræf.kjuːˈel ˈkwɪə.ri/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Truy vấn GraphQL: thao tác chỉ đọc dùng để trích xuất dữ liệu từ máy chủ theo cấu trúc chính xác do client định nghĩa.",
     "Clients submit a single GraphQL query to retrieve user details along with recent orders.", "Client gửi một truy vấn GraphQL duy nhất để lấy thông tin người dùng kèm đơn hàng gần đây.",
     "Truy vấn GraphQL Query", "🔍", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("GraphQL Mutation", "/ˌɡræf.kjuːˈel mjuːˈteɪ.ʃən/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Thao tác biến đổi GraphQL: thao tác tạo mới, cập nhật hoặc xóa dữ liệu trên máy chủ trong GraphQL.",
     "Execute a GraphQL mutation to update a customer's shipping address.", "Thực thi mutation GraphQL để cập nhật địa chỉ giao hàng của khách.",
     "Biến đổi dữ liệu Mutation", "✏️", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("GraphQL Resolver", "/ˌɡræf.kjuːˈel rɪˈzɒl.vər/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Hàm xử lý GraphQL: hàm phía máy chủ chịu trách nhiệm nạp và trả về dữ liệu cho một trường cụ thể trong lược đồ.",
     "Resolvers query databases or third-party APIs to populate GraphQL schema fields.", "Các hàm resolver truy vấn CSDL hoặc API bên thứ ba để điền dữ liệu cho trường GraphQL.",
     "Hàm giải quyết Resolver", "⚙️", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("GraphQL Subscription", "/ˌɡræf.kjuːˈel səbˈskrɪp.ʃən/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Đăng ký thời gian thực GraphQL: duy trì kết nối WebSocket để máy chủ tự động đẩy dữ liệu mới về client khi có sự kiện.",
     "Live chat applications rely on GraphQL subscriptions to stream messages instantly.", "Ứng dụng chat trực tiếp dựa vào GraphQL subscription để truyền tin nhắn tức thì.",
     "Đăng ký nhận tin Subscription", "📡", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("gRPC", "/ˌdʒiː.ɑːr.piːˈsiː/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Khung gRPC: khung gọi thủ tục từ xa hiệu năng cao của Google chạy trên HTTP/2 và mã hóa nhị phân Protocol Buffers.",
     "Microservices use gRPC for ultra-fast, low-overhead inter-service communications.", "Các vi dịch vụ dùng gRPC để truyền thông giữa các dịch vụ siêu nhanh và ít tốn phụ phí.",
     "Khung gọi từ xa gRPC", "🚀", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Protocol Buffers (Protobuf)", "/ˈprəʊ.tə.kɒl ˈbʌf.ərz/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Bộ đệm giao thức Protobuf: cơ chế tuần tự hóa dữ liệu có cấu trúc dạng nhị phân nhỏ gọn và nhanh hơn nhiều so với JSON hay XML.",
     "Protobuf binary payloads are dramatically smaller than comparable JSON payloads.", "Tải trọng nhị phân Protobuf nhỏ hơn rất nhiều so với tải trọng JSON tương đương.",
     "Bộ đệm giao thức Protobuf", "📦", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Server-Sent Events (SSE)", "/ˈsɜː.vər sent ɪˈvents/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Sự kiện gửi từ máy chủ (SSE): công nghệ cho phép máy chủ đơn phương truyền dữ liệu một chiều liên tục về trình duyệt qua HTTP.",
     "LLM chat interfaces use Server-Sent Events to stream generated tokens in real time.", "Giao diện chat LLM dùng Server-Sent Events để truyền các token theo thời gian thực.",
     "Sự kiện từ máy chủ SSE", "🌊", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Cross-Origin Resource Sharing (CORS)", "/kɔːz/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Cơ chế chia sẻ tài nguyên nguồn gốc chéo CORS: tiêu chuẩn an ninh của trình duyệt kiểm soát việc trang web truy cập tài nguyên từ miền khác.",
     "Configure backend CORS headers to permit API requests originating from our frontend domain.", "Cấu hình tiêu đề CORS ở backend để cho phép các yêu cầu API từ tên miền frontend.",
     "Cơ chế chia sẻ chéo CORS", "🌐", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("CORS Preflight Request", "/kɔːz ˈpriː.flaɪt/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Yêu cầu tiền kiểm Preflight: trình duyệt tự động gửi yêu cầu HTTP OPTIONS trước để hỏi máy chủ có chấp thuận phương thức đó không.",
     "Browsers send an OPTIONS preflight request before complex POST or DELETE operations.", "Trình duyệt gửi yêu cầu tiền kiểm OPTIONS trước các thao tác phức tạp như POST hoặc DELETE.",
     "Yêu cầu tiền kiểm Preflight", "✈️", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Content-Type Header", "/ˈkɒn.tent taɪp ˈhed.ər/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Tiêu đề Content-Type: tiêu đề HTTP chỉ rõ định dạng MIME của dữ liệu truyền đi (ví dụ: application/json).",
     "Set Content-Type to 'application/json' when transmitting structured JSON payloads.", "Đặt Content-Type thành 'application/json' khi truyền dữ liệu JSON có cấu trúc.",
     "Tiêu đề Content-Type", "📋", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Bearer Token Authentication", "/ˈbeə.rər ˈtəʊ.kən/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Xác thực mã Bearer Token: mô hình xác thực trong đó người nắm giữ chuỗi token sẽ được cấp quyền truy cập tài nguyên API.",
     "Pass the JWT inside the 'Authorization: Bearer <token>' header for API requests.", "Truyền mã JWT vào tiêu đề 'Authorization: Bearer <token>' khi gọi API.",
     "Xác thực mã Bearer Token", "🎟️", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("API Rate Limiting", "/ˌeɪ.piːˈaɪ reɪt ˈlɪm.ɪ.tɪŋ/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Giới hạn tần suất gọi API: kiểm soát số lượng cuộc gọi API tối đa mà một người dùng hay IP có thể thực hiện trong một khoảng thời gian.",
     "API rate limiting enforces a maximum of 100 requests per minute per IP address.", "Giới hạn tần suất gọi API áp đặt tối đa 100 yêu cầu mỗi phút cho mỗi địa chỉ IP.",
     "Giới hạn tần suất Rate Limiting", "🚦", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("API Throttling", "/ˌeɪ.piːˈaɪ ˈθrɒt.lɪŋ/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Tiết lưu API: làm chậm tốc độ xử lý hoặc trì hoãn các yêu cầu khi hệ thống máy chủ có dấu hiệu quá tải.",
     "Throttling slows down excessive requests to prevent service failure under extreme load.", "Tiết lưu làm chậm các yêu cầu quá mức để ngăn sập dịch vụ khi tải tăng quá cao.",
     "Tiết lưu yêu cầu Throttling", "🛑", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("WebAssembly (Wasm)", "/ˈweb.əˌsem.bli/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Mã nhị phân WebAssembly: định dạng mã nhị phân hiệu năng gần bằng mã máy gốc chạy bên trong các trình duyệt hiện đại.",
     "Figma uses WebAssembly with C++ to render smooth 60 FPS graphics inside browsers.", "Figma sử dụng WebAssembly viết bằng C++ để kết xuất đồ họa 60 FPS mượt mà trên web.",
     "Mã nhị phân WebAssembly", "⚡", "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    ("Mobile Application", "/ˈməʊ.baɪl ˌæp.lɪˈkeɪ.ʃən/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Ứng dụng di động: phần mềm ứng dụng được thiết kế chuyên biệt để chạy trên các thiết bị như điện thoại thông minh và máy tính bảng.",
     "Mobile applications account for the majority of global consumer internet engagement.", "Ứng dụng di động chiếm phần lớn thời lượng tương tác Internet của người dùng toàn cầu.",
     "Ứng dụng di động Mobile App", "📱", "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=600&auto=format&fit=crop&q=80"),

    ("Native App", "/ˈneɪ.tɪv æp/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Ứng dụng bản địa: ứng dụng được viết riêng cho một hệ điều hành cụ thể (Swift cho iOS, Kotlin cho Android) để tối ưu hiệu năng cao nhất.",
     "Native apps offer the smoothest 120Hz animations and full access to camera hardware.", "Ứng dụng bản địa mang lại hoạt ảnh 120Hz mượt nhất và toàn quyền truy cập phần cứng camera.",
     "Ứng dụng bản địa Native App", "🍎", "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=600&auto=format&fit=crop&q=80"),

    ("Hybrid App", "/ˈhaɪ.brɪd æp/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Ứng dụng lai: ứng dụng kết hợp mã nguồn web (HTML, CSS, JS) được bọc bên trong một khung ứng dụng bản địa có WebView.",
     "Hybrid apps reduce initial development costs by reusing web code across platforms.", "Ứng dụng lai giảm chi phí phát triển ban đầu bằng cách tái sử dụng mã web cho mọi nền tảng.",
     "Ứng dụng lai Hybrid App", "🔄", "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=600&auto=format&fit=crop&q=80"),

    ("Cross-Platform Framework", "/krɒs ˈplæt.fɔːm ˈfreɪm.wɜːk/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Khung phát triển đa nền tảng: cho phép viết mã một lần duy nhất và xuất bản ứng dụng chạy được trên cả iOS lẫn Android.",
     "Cross-platform frameworks let engineering teams maintain a unified codebase.", "Các khung đa nền tảng giúp các nhóm kỹ sư duy trì một cơ sở mã nguồn thống nhất.",
     "Khung đa nền tảng", "🌐", "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=600&auto=format&fit=crop&q=80"),

    ("React Native", "/riˈækt ˈneɪ.tɪv/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Nền tảng React Native: khung phát triển di động đa nền tảng của Meta dùng JavaScript và React kết xuất thành các thành phần bản địa.",
     "React Native compiles JSX components into native Android and iOS view elements.", "React Native biên dịch các thành phần JSX thành các thành phần hiển thị bản địa của Android và iOS.",
     "Khung React Native", "⚛️", "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=600&auto=format&fit=crop&q=80"),

    ("Flutter", "/ˈflʌt.ər/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Bộ công cụ Flutter: khung phát triển giao diện mã nguồn mở của Google viết bằng ngôn ngữ Dart tự vẽ mọi pixel bằng engine Skia.",
     "Flutter renders beautiful custom UI widgets at 60 FPS on both mobile platforms.", "Flutter kết xuất các widget UI đẹp mắt ở tốc độ 60 FPS trên cả hai nền tảng di động.",
     "Bộ công cụ Flutter", "🦋", "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=600&auto=format&fit=crop&q=80"),

    ("Dart", "/dɑːt/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Ngôn ngữ lập trình Dart: ngôn ngữ hướng đối tượng định kiểu mạnh do Google phát triển tối ưu cho phát triển giao diện Flutter.",
     "Dart supports both Just-In-Time (JIT) compilation for hot reload and Ahead-Of-Time (AOT) for release.", "Dart hỗ trợ cả biên dịch JIT cho hot reload và biên dịch AOT cho bản phát hành.",
     "Ngôn ngữ Dart", "🎯", "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    ("Swift", "/swɪft/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Ngôn ngữ lập trình Swift: ngôn ngữ mã nguồn mở hiện đại, an toàn và trực quan do Apple phát triển cho iOS, macOS và watchOS.",
     "Swift offers expressive modern syntax and robust memory safety features.", "Swift mang lại cú pháp hiện đại giàu biểu cảm và các tính năng an toàn bộ nhớ mạnh mẽ.",
     "Ngôn ngữ Apple Swift", "🦅", "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=600&auto=format&fit=crop&q=80"),

    ("SwiftUI", "/swɪft ˌjuːˈaɪ/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Khung khai báo SwiftUI: khung phát triển giao diện người dùng theo phong cách khai báo hiện đại của Apple trên tất cả hệ sinh thái.",
     "SwiftUI allows developers to construct iOS views with concise declarative Swift code.", "SwiftUI cho phép lập trình viên tạo giao diện iOS bằng mã Swift khai báo súc tích.",
     "Khung giao diện SwiftUI", "🍎", "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=600&auto=format&fit=crop&q=80"),

    ("Kotlin", "/ˈkɒt.lɪn/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Ngôn ngữ lập trình Kotlin: ngôn ngữ tĩnh chạy trên JVM do JetBrains phát triển và được Google chọn làm ngôn ngữ ưu tiên hàng đầu cho Android.",
     "Kotlin eliminates null pointer exceptions through first-class nullable types.", "Kotlin loại bỏ lỗi con trỏ null nhờ hỗ trợ sẵn kiểu dữ liệu nullable.",
     "Ngôn ngữ Android Kotlin", "🟣", "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=600&auto=format&fit=crop&q=80"),

    ("Jetpack Compose", "/ˈdʒet.pæk kəmˈpəʊz/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Bộ công cụ Jetpack Compose: bộ công cụ phát triển giao diện khai báo hiện đại chính thức của Google cho Android.",
     "Jetpack Compose simplifies Android UI development with reactive state observables.", "Jetpack Compose đơn giản hóa phát triển UI Android bằng các trạng thái phản ứng quan sát được.",
     "Khung giao diện Jetpack Compose", "🤖", "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=600&auto=format&fit=crop&q=80"),

    ("Android SDK", "/ˈæn.drɔɪd ˌes.diːˈkeɪ/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Bộ phát triển phần mềm Android SDK: bộ công cụ, trình giả lập và thư viện API chính thức để xây dựng ứng dụng Android.",
     "Update the Android SDK to target the latest Android platform API levels.", "Cập nhật Android SDK để nhắm tới các cấp độ API mới nhất của nền tảng Android.",
     "Bộ công cụ Android SDK", "🧰", "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=600&auto=format&fit=crop&q=80"),

    ("iOS SDK", "/ˌaɪ.oʊˈes ˌes.diːˈkeɪ/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Bộ phát triển phần mềm iOS SDK: bộ công cụ và framework chính thức của Apple (UIKit, CoreData, ARKit) cho thiết bị iOS.",
     "The iOS SDK gives developers access to device sensors, biometric cameras, and Apple Pay.", "iOS SDK cung cấp quyền truy cập vào cảm biến, camera sinh trắc học và Apple Pay.",
     "Bộ công cụ iOS SDK", "🧰", "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=600&auto=format&fit=crop&q=80"),

    ("Xcode", "/ˈeks.kəʊd/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Môi trường phát triển Xcode: môi trường IDE chính thức của Apple dùng để phát triển, biên dịch và gỡ lỗi phần mềm Apple.",
     "Build and profile iOS applications using Apple's integrated Xcode IDE.", "Xây dựng và đánh giá hiệu năng ứng dụng iOS bằng môi trường tích hợp Xcode của Apple.",
     "Môi trường phát triển Xcode", "🛠️", "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=600&auto=format&fit=crop&q=80"),

    ("Android Studio", "/ˈæn.drɔɪd ˈstjuː.di.əʊ/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Môi trường phát triển Android Studio: IDE chính thức của Google dựa trên IntelliJ IDEA dành riêng cho phát triển ứng dụng Android.",
     "Android Studio includes intelligent code completion and an integrated Android emulator.", "Android Studio tích hợp gợi ý mã thông minh và trình giả lập Android sẵn có.",
     "Môi trường Android Studio", "💻", "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=600&auto=format&fit=crop&q=80"),

    ("APK (Android Package)", "/ˌeɪ.piːˈkeɪ/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Gói ứng dụng Android APK: định dạng tệp gói nén dùng để phân phối và cài đặt ứng dụng trên hệ điều hành Android.",
     "Users can sideload test APK files onto their Android phones directly.", "Người dùng có thể cài đặt trực tiếp tệp APK kiểm thử lên điện thoại Android.",
     "Gói cài đặt Android APK", "📦", "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=600&auto=format&fit=crop&q=80"),

    ("AAB (Android App Bundle)", "/ˌeɪ.eɪˈbiː/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Định dạng gói phân phối Google AAB: chuẩn phát hành mới của Google Play tự động tối ưu hóa kích thước cài đặt cho từng thiết bị.",
     "Publishing an Android App Bundle reduces download sizes for end users by 15 percent.", "Phát hành Android App Bundle giúp giảm 15% dung lượng tải xuống cho người dùng cuối.",
     "Gói phát hành AAB", "🎁", "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=600&auto=format&fit=crop&q=80"),

    ("IPA (iOS App Store Package)", "/ˌaɪ.piːˈeɪ/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Gói cài đặt iOS IPA: định dạng tệp lưu trữ nén của ứng dụng iOS chứa mã nhị phân và tài nguyên sẵn sàng cài đặt trên thiết bị Apple.",
     "Distribute enterprise IPA packages to internal testing teams using Apple TestFlight.", "Phân phối các gói IPA doanh nghiệp cho nhóm kiểm thử nội bộ bằng Apple TestFlight.",
     "Gói cài đặt iOS IPA", "📦", "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=600&auto=format&fit=crop&q=80"),

    ("Google Play Store", "/ˈɡuː.ɡəl pleɪ stɔːr/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Cửa hàng Google Play: chợ phân phối ứng dụng kỹ thuật số chính thức lớn nhất cho hệ điều hành Android.",
     "Submit new app releases to the Google Play Store Console for automated security review.", "Nộp các bản phát hành app mới lên Google Play Store Console để duyệt an ninh tự động.",
     "Cửa hàng Google Play", "🏬", "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=600&auto=format&fit=crop&q=80"),

    ("Apple App Store", "/ˈæp.əl æp stɔːr/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Cửa hàng ứng dụng Apple: nền tảng phân phối ứng dụng di động độc quyền của Apple với quy trình kiểm duyệt chất lượng khắt khe.",
     "The Apple App Store review team verifies that apps strictly follow privacy guidelines.", "Đội ngũ duyệt Apple App Store xác minh ứng dụng tuân thủ nghiêm ngặt hướng dẫn quyền riêng tư.",
     "Cửa hàng Apple App Store", "🏬", "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=600&auto=format&fit=crop&q=80"),

    ("Push Notifications", "/pʊʃ ˌnəʊ.tɪ.fɪˈkeɪ.ʃənz/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Thông báo đẩy: thông điệp tự động bật lên màn hình khóa của thiết bị di động gửi từ máy chủ thông qua APNs hoặc FCM.",
     "Firebase Cloud Messaging (FCM) delivers personalized push notifications to millions of mobile users.", "Firebase Cloud Messaging (FCM) gửi thông báo đẩy cá nhân hóa tới hàng triệu người dùng.",
     "Thông báo đẩy Push Notification", "🔔", "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=600&auto=format&fit=crop&q=80"),

    ("Deep Linking", "/diːp ˈlɪŋk.ɪŋ/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Liên kết sâu: liên kết URL trực tiếp đưa người dùng tới thẳng một màn hình nội dung cụ thể bên trong ứng dụng di động.",
     "Deep linking allows promotional email links to open specific product pages inside the app.", "Liên kết sâu cho phép liên kết email quảng cáo mở thẳng trang chi tiết sản phẩm trong app.",
     "Liên kết sâu Deep Linking", "🔗", "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=600&auto=format&fit=crop&q=80"),

    ("Universal Links", "/ˌjuː.nɪˈvɜː.səl lɪŋks/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Liên kết vạn năng: chuẩn liên kết của Apple kết nối an toàn URL trang web tiêu chuẩn với ứng dụng iOS.",
     "Universal links open seamlessly in the native iOS app without bouncing through Safari.", "Liên kết vạn năng mở mượt mà trong ứng dụng iOS bản địa mà không bị bật qua Safari.",
     "Liên kết vạn năng Universal Links", "🌐", "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=600&auto=format&fit=crop&q=80"),

    ("Mobile WebView", "/ˈməʊ.baɪl ˈweb.vjuː/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Khung hiển thị web trong app: thành phần giao diện cho phép nhúng trực tiếp trang web chạy bên trong ứng dụng di động bản địa.",
     "In-app payments often render checkout flows inside a secure mobile WebView.", "Thanh toán trong app thường hiển thị quy trình thanh toán bên trong một WebView an toàn.",
     "Khung hiển thị WebView", "🪟", "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=600&auto=format&fit=crop&q=80"),

    ("State Management", "/steɪt ˈmæn.ɪdʒ.mənt/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Quản lý trạng thái: kiến trúc và thư viện dùng để theo dõi và đồng bộ hóa trạng thái dữ liệu qua các thành phần UI.",
     "Centralized state management avoids prop drilling down deep component hierarchies.", "Quản lý trạng thái tập trung giúp tránh việc truyền dữ liệu qua quá nhiều cấp thành phần.",
     "Quản lý trạng thái State Management", "🎛️", "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=600&auto=format&fit=crop&q=80"),

    ("Redux", "/ˈriː.dʌks/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Thư viện Redux: thư viện quản lý trạng thái có thể dự đoán dựa trên mô hình luồng dữ liệu một chiều (Store, Action, Reducer).",
     "Redux enforces immutable state updates through dispatched pure reducer actions.", "Redux thực thi cập nhật trạng thái bất biến thông qua các action reducer thuần khiết.",
     "Thư viện quản lý Redux", "🔄", "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=600&auto=format&fit=crop&q=80"),

    ("React Context API", "/riˈækt ˈkɒn.tekst ˌeɪ.piːˈaɪ/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Cơ chế Context của React: giải pháp tích hợp sẵn trong React để chia sẻ dữ liệu toàn cục (như theme, user) không cần prop drilling.",
     "Use React Context API for lightweight global state sharing like user auth status.", "Dùng React Context API cho việc chia sẻ trạng thái toàn cục nhẹ như trạng thái đăng nhập.",
     "Cơ chế React Context", "🌐", "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=600&auto=format&fit=crop&q=80"),

    ("Server-Driven UI", "/ˈsɜː.vər ˌdrɪv.ən ˌjuːˈaɪ/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Giao diện do máy chủ điều khiển: kiến trúc trong đó máy chủ gửi cấu trúc và bố cục JSON để app di động tự vẽ lại mà không cần cập nhật bản phát hành app.",
     "Server-driven UI lets marketing teams change app home screen layouts instantly without App Store approval.", "Giao diện do máy chủ điều khiển giúp thay đổi bố cục màn hình chính ngay lập tức mà không cần duyệt App Store.",
     "Giao diện máy chủ điều khiển", "🎛️", "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=600&auto=format&fit=crop&q=80"),

    ("Component Lifecycle", "/kəmˈpəʊ.nənt ˈlaɪfˌsaɪ.kəl/", "noun", "web_mobile", "Web & Ứng dụng Di động",
     "Vòng đời thành phần: chuỗi các giai đoạn (khởi tạo, gắn kết mount, cập nhật và hủy unmount) mà một thành phần giao diện trải qua.",
     "Clean up intervals and active WebSocket connections inside the unmount component lifecycle phase.", "Dọn dẹp các bộ đếm thời gian và kết nối WebSocket trong giai đoạn hủy unmount của vòng đời thành phần.",
     "Vòng đời thành phần Lifecycle", "🔄", "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=600&auto=format&fit=crop&q=80")
]

if __name__ == "__main__":
    print(f"Domain 8 terms count: {len(terms)}")
