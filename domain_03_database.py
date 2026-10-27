# -*- coding: utf-8 -*-
"""Domain 3: Databases & Data Engineering (100 core terms)"""

terms = [
    ("Database", "/ˈdeɪ.tə.beɪs/", "noun", "database", "Cơ sở dữ liệu",
     "Cơ sở dữ liệu: tập hợp dữ liệu có tổ chức, được lưu trữ và truy cập điện tử từ máy tính.",
     "Production databases store millions of transactional records securely.", "Cơ sở dữ liệu sản xuất lưu trữ hàng triệu bản ghi giao dịch an toàn.",
     "Cơ sở dữ liệu Database", "🗄️", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Relational Database (RDBMS)", "/rɪˈleɪ.ʃən.əl ˈdeɪ.tə.beɪs/", "noun", "database", "Cơ sở dữ liệu",
     "Hệ quản trị CSDL quan hệ: tổ chức dữ liệu thành các bảng gồm các hàng và cột có liên kết với nhau.",
     "PostgreSQL and MySQL are standard open-source relational databases.", "PostgreSQL và MySQL là các hệ quản trị CSDL quan hệ mã nguồn mở tiêu chuẩn.",
     "CSDL quan hệ RDBMS", "📊", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("NoSQL", "/ˌnəʊ ˌes.kjuːˈel/", "noun", "database", "Cơ sở dữ liệu",
     "CSDL phi quan hệ: hệ cơ sở dữ liệu phi quan hệ, phi cấu trúc được thiết kế cho việc mở rộng theo chiều ngang.",
     "NoSQL systems handle flexible unstructured documents and rapid scale.", "Hệ CSDL NoSQL xử lý tài liệu phi cấu trúc linh hoạt và mở rộng quy mô nhanh chóng.",
     "CSDL NoSQL", "🍃", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("SQL (Structured Query Language)", "/ˌes.kjuːˈel/", "noun", "database", "Cơ sở dữ liệu",
     "Ngôn ngữ truy vấn có cấu trúc chuẩn dùng để quản lý và thao tác dữ liệu trong hệ thống CSDL quan hệ.",
     "Write standard SQL to filter and aggregate revenue by quarters.", "Viết câu lệnh SQL chuẩn để lọc và tổng hợp doanh thu theo các quý.",
     "Ngôn ngữ SQL", "📜", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Table", "/ˈteɪ.bəl/", "noun", "database", "Cơ sở dữ liệu",
     "Bảng dữ liệu: tập hợp các bản ghi dữ liệu được tổ chức theo các hàng ngang và cột dọc.",
     "The orders table contains customer purchases and shipment dates.", "Bảng đơn hàng chứa các giao dịch mua của khách và ngày giao hàng.",
     "Bảng dữ liệu Table", "📋", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Record (Row)", "/ˈrek.ɔːd/", "noun", "database", "Cơ sở dữ liệu",
     "Bản ghi (Hàng): một dòng đơn lẻ trong bảng đại diện cho một thực thể dữ liệu hoàn chỉnh.",
     "Each row in the users table represents a registered account.", "Mỗi hàng trong bảng người dùng đại diện cho một tài khoản đã đăng ký.",
     "Bản ghi Row", "📄", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Field (Column)", "/fiːld/", "noun", "database", "Cơ sở dữ liệu",
     "Trường (Cột): thuộc tính dữ liệu cụ thể trong bảng mang một kiểu dữ liệu xác định.",
     "The 'created_at' column tracks the timestamp of row insertion.", "Cột 'created_at' theo dõi mốc thời gian chèn bản ghi vào bảng.",
     "Trường cột Column", "🏷️", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Schema", "/ˈskiː.mə/", "noun", "database", "Cơ sở dữ liệu",
     "Lược đồ cơ sở dữ liệu: bản vẽ cấu trúc hình thức định nghĩa các bảng, quan hệ, cột và ràng buộc.",
     "Database schema migrations must be tested before deploying to production.", "Việc di chuyển lược đồ cơ sở dữ liệu phải được kiểm thử trước khi đưa lên môi trường sản xuất.",
     "Lược đồ Schema", "📐", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Primary Key", "/ˈpraɪ.mə.ri kiː/", "noun", "database", "Cơ sở dữ liệu",
     "Khóa chính: cột hoặc nhóm cột định danh duy nhất cho mỗi bản ghi trong bảng, không được rỗng.",
     "An auto-incrementing integer or UUID typically serves as a primary key.", "Một số nguyên tự tăng hoặc chuỗi UUID thường đóng vai trò làm khóa chính.",
     "Khóa chính PK", "🔑", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Foreign Key", "/ˈfɒr.ən kiː/", "noun", "database", "Cơ sở dữ liệu",
     "Khóa ngoại: cột liên kết trỏ tới khóa chính của một bảng khác để duy trì tính toàn vẹn tham chiếu.",
     "The customer_id in orders is a foreign key referencing the users table.", "Trường customer_id trong bảng orders là khóa ngoại tham chiếu tới bảng users.",
     "Khóa ngoại FK", "🔗", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Composite Key", "/kəmˈpɒz.ɪt kiː/", "noun", "database", "Cơ sở dữ liệu",
     "Khóa kết hợp: khóa chính được cấu thành từ hai hoặc nhiều cột kết hợp lại để tạo định danh duy nhất.",
     "A student_course table uses both student_id and course_id as a composite key.", "Bảng sinh viên - khóa học dùng cả student_id và course_id làm khóa kết hợp.",
     "Khóa kết hợp", "🗝️", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Unique Constraint", "/juːˈniːk kənˈstreɪnt/", "noun", "database", "Cơ sở dữ liệu",
     "Ràng buộc duy nhất: quy tắc đảm bảo rằng tất cả các giá trị trong một cột phải phân biệt không trùng nhau.",
     "Add a unique constraint on email addresses to prevent duplicate accounts.", "Thêm ràng buộc duy nhất trên địa chỉ email để ngăn tạo tài khoản trùng lặp.",
     "Ràng buộc duy nhất", "🛡️", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Index", "/ˈɪn.deks/", "noun", "database", "Cơ sở dữ liệu",
     "Chỉ mục: cấu trúc dữ liệu bổ sung giúp tăng tốc độ tìm kiếm và trích xuất dữ liệu trên bảng.",
     "Creating an index on the user_uuid column made lookups twenty times faster.", "Việc tạo chỉ mục trên cột user_uuid giúp việc tra cứu nhanh gấp 20 lần.",
     "Chỉ mục Index", "📑", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Clustered Index", "/ˈklʌs.təd ˈɪn.deks/", "noun", "database", "Cơ sở dữ liệu",
     "Chỉ mục cụm: chỉ mục quyết định trực tiếp thứ tự sắp xếp vật lý thực tế của dữ liệu bảng trên đĩa.",
     "Each table can contain only one clustered index, usually the primary key.", "Mỗi bảng chỉ có thể chứa duy nhất một chỉ mục cụm, thường là khóa chính.",
     "Chỉ mục cụm Clustered", "🗂️", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Non-Clustered Index", "/ˌnɒnˈklʌs.təd ˈɪn.deks/", "noun", "database", "Cơ sở dữ liệu",
     "Chỉ mục phi cụm: chỉ mục lưu trữ riêng biệt cấu trúc con trỏ trỏ tới vị trí của dòng dữ liệu gốc.",
     "You can create multiple non-clustered indexes for frequently searched columns.", "Bạn có thể tạo nhiều chỉ mục phi cụm cho các cột thường xuyên được tìm kiếm.",
     "Chỉ mục phi cụm", "📑", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("B-Tree Index", "/biː triː ˈɪn.deks/", "noun", "database", "Cơ sở dữ liệu",
     "Chỉ mục cây B-Tree: cấu trúc chỉ mục phổ biến nhất hỗ trợ truy vấn so sánh bằng (=) và so sánh khoảng (<, >).",
     "B-Tree indexes maintain sorted keys to accelerate sorting and range searches.", "Chỉ mục cây B-Tree duy trì các khóa đã sắp xếp để tăng tốc sắp xếp và tìm kiếm theo khoảng.",
     "Chỉ mục B-Tree", "🌲", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("View", "/vjuː/", "noun", "database", "Cơ sở dữ liệu",
     "Khung nhìn (View): bảng ảo được định nghĩa từ kết quả của một câu truy vấn SQL đã lưu trước.",
     "Use views to present curated data without granting direct base table access.", "Dùng khung nhìn view để cung cấp dữ liệu chọn lọc mà không cấp quyền truy cập trực tiếp bảng gốc.",
     "Bảng ảo View", "👁️", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Materialized View", "/məˈtɪə.ri.ə.laɪzd vjuː/", "noun", "database", "Cơ sở dữ liệu",
     "Khung nhìn vật lý hóa: lưu trữ thực tế kết quả truy vấn vào đĩa và định kỳ làm mới lại dữ liệu.",
     "Materialized views drastically accelerate heavy analytics reporting dashboards.", "Khung nhìn vật lý hóa tăng tốc vượt trội các bảng điều khiển báo cáo phân tích nặng.",
     "Khung nhìn vật lý hóa", "💾", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Stored Procedure", "/stɔːd prəˈsiː.dʒər/", "noun", "database", "Cơ sở dữ liệu",
     "Thủ tục lưu trữ: tập hợp các câu lệnh SQL được biên dịch và lưu trữ trực tiếp trong cơ sở dữ liệu.",
     "Stored procedures execute on the database server to minimize network roundtrips.", "Thủ tục lưu trữ thực thi trực tiếp trên máy chủ CSDL để giảm thiểu số vòng truyền mạng.",
     "Thủ tục lưu trữ", "⚙️", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Database Trigger", "/ˈdeɪ.tə.beɪs ˈtrɪɡ.ər/", "noun", "database", "Cơ sở dữ liệu",
     "Trình kích hoạt: đoạn mã tự động thực thi khi xảy ra sự kiện INSERT, UPDATE hoặc DELETE trên bảng.",
     "An audit trigger writes row modifications into a history logging table.", "Một trigger kiểm toán tự động ghi lại các sửa đổi hàng vào bảng lịch sử.",
     "Trình kích hoạt Trigger", "⚡", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Database Cursor", "/ˈdeɪ.tə.beɪs ˈkɜː.sər/", "noun", "database", "Cơ sở dữ liệu",
     "Con trỏ CSDL: đối tượng cho phép duyệt tuần tự qua từng bản ghi của một tập kết quả truy vấn.",
     "Cursors should be used sparingly because row-by-row iteration hurts performance.", "Nên hạn chế dùng cursor vì việc duyệt từng hàng làm giảm hiệu năng hệ thống.",
     "Con trỏ CSDL Cursor", "👆", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Query", "/ˈkwɪə.ri/", "noun", "database", "Cơ sở dữ liệu",
     "Truy vấn: câu lệnh yêu cầu trích xuất, chèn hoặc chỉnh sửa dữ liệu gửi tới hệ thống CSDL.",
     "Optimize slow queries by reviewing indexes and join conditions.", "Tối ưu hóa các truy vấn chậm bằng cách kiểm tra lại chỉ mục và điều kiện join.",
     "Truy vấn Query", "🔍", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Subquery", "/ˈsʌbˌkwɪə.ri/", "noun", "database", "Cơ sở dữ liệu",
     "Truy vấn con: câu lệnh SELECT được lồng bên trong một câu lệnh truy vấn SQL khác.",
     "Correlated subqueries execute once for each row evaluated by the outer query.", "Truy vấn con tương quan thực thi một lần cho mỗi hàng được truy vấn bên ngoài duyệt qua.",
     "Truy vấn con Subquery", "🧩", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Join", "/dʒɔɪn/", "noun", "database", "Cơ sở dữ liệu",
     "Phép kết hợp bảng: thao tác kết hợp các bản ghi từ hai hoặc nhiều bảng dựa trên cột chung có liên quan.",
     "Joins form the relational core of normalized SQL architectures.", "Phép kết nối join tạo nên giá trị cốt lõi quan hệ trong kiến trúc SQL đã chuẩn hóa.",
     "Phép kết hợp bảng Join", "🔗", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Inner Join", "/ˈɪn.ər dʒɔɪn/", "noun", "database", "Cơ sở dữ liệu",
     "Kết hợp trong: chỉ trả về các bản ghi thỏa mãn điều kiện kết nối ở cả hai bảng tham gia.",
     "An inner join excludes customers who have never placed an order.", "Inner join loại bỏ những khách hàng chưa từng đặt bất kỳ đơn hàng nào.",
     "Phép Inner Join", "🟢", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Left Join", "/left dʒɔɪn/", "noun", "database", "Cơ sở dữ liệu",
     "Kết hợp trái: trả về tất cả các hàng từ bảng bên trái và các hàng khớp từ bảng bên phải.",
     "A left join preserves all users even if they possess no matching profiles.", "Left join giữ lại tất cả người dùng ngay cả khi họ chưa có hồ sơ tương ứng.",
     "Phép Left Join", "⬅️", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Right Join", "/raɪt dʒɔɪn/", "noun", "database", "Cơ sở dữ liệu",
     "Kết hợp phải: trả về tất cả các hàng từ bảng bên phải và các hàng khớp từ bảng bên trái.",
     "Right joins are symmetrical to left joins and used to retain right-side rows.", "Right join đối xứng với left join và dùng để giữ lại toàn bộ các hàng bên phải.",
     "Phép Right Join", "➡️", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Full Outer Join", "/fʊl ˈaʊ.tər dʒɔɪn/", "noun", "database", "Cơ sở dữ liệu",
     "Kết hợp đầy đủ ngoài: trả về tất cả các hàng khi có sự trùng khớp ở một trong hai bảng.",
     "Full outer joins combine all records from both datasets, filling gaps with NULL.", "Full outer join kết hợp mọi bản ghi từ hai tập dữ liệu và điền NULL vào các chỗ thiếu.",
     "Phép Full Outer Join", "⚪", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Cross Join", "/krɒs dʒɔɪn/", "noun", "database", "Cơ sở dữ liệu",
     "Tích đề-các: kết hợp mỗi hàng của bảng thứ nhất với tất cả các hàng của bảng thứ hai.",
     "A cross join of 10 products and 5 sizes produces 50 combinations.", "Cross join giữa 10 sản phẩm và 5 kích cỡ sẽ tạo ra 50 tổ hợp.",
     "Tích đề-các Cross Join", "✖️", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Self Join", "/self dʒɔɪn/", "noun", "database", "Cơ sở dữ liệu",
     "Tự kết hợp: phép kết hợp một bảng với chính nó để truy vấn mối quan hệ thứ bậc nội bộ.",
     "Querying an employee table with a manager_id requires a self join.", "Truy vấn bảng nhân viên có trường manager_id đòi hỏi phải thực hiện phép self join.",
     "Tự kết hợp Self Join", "🔄", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Group By", "/ɡruːp baɪ/", "phrase", "database", "Cơ sở dữ liệu",
     "Mệnh đề nhóm: gom các hàng có cùng giá trị trong các cột xác định thành các hàng tóm tắt.",
     "Group by department to calculate average employee salaries.", "Gom nhóm theo phòng ban để tính lương trung bình của nhân viên.",
     "Mệnh đề gom nhóm", "👥", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Having Clause", "/ˈhæv.ɪŋ klɔːz/", "noun", "database", "Cơ sở dữ liệu",
     "Mệnh đề Having: lọc các nhóm dữ liệu sau khi đã thực hiện gom nhóm (khác với WHERE lọc trước khi nhóm).",
     "Use HAVING COUNT(*) > 5 to filter only departments with more than five staff.", "Dùng HAVING COUNT(*) > 5 để chỉ lọc các phòng ban có trên 5 nhân sự.",
     "Mệnh đề lọc Having", "🔍", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Aggregate Function", "/ˈæɡ.rɪ.ɡət ˈfʌŋk.ʃən/", "noun", "database", "Cơ sở dữ liệu",
     "Hàm tổng hợp: hàm tính toán trên tập hợp các giá trị và trả về một giá trị duy nhất (COUNT, SUM, AVG).",
     "Aggregate functions summarize sales data across multiple regions.", "Các hàm tổng hợp tóm tắt dữ liệu bán hàng trên nhiều khu vực khác nhau.",
     "Hàm tổng hợp dữ liệu", "🧮", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Transaction", "/trænˈzæk.ʃən/", "noun", "database", "Cơ sở dữ liệu",
     "Giao dịch: chuỗi một hoặc nhiều thao tác CSDL được thực thi như một đơn vị công việc logic duy nhất.",
     "If any statement inside a transaction fails, everything rolls back.", "Nếu bất kỳ câu lệnh nào trong giao dịch thất bại, toàn bộ sẽ được khôi phục trạng thái cũ.",
     "Giao dịch Transaction", "💳", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("ACID Properties", "/ˈæs.ɪd ˈprɒp.ə.tiz/", "noun", "database", "Cơ sở dữ liệu",
     "Thuộc tính ACID: bốn tính chất cốt lõi (Nguyên tử, Nhất quán, Cô lập, Bền vững) đảm bảo độ tin cậy của giao dịch.",
     "Relational engines comply with ACID properties to safeguard bank funds.", "Các cơ chế CSDL quan hệ tuân thủ thuộc tính ACID để bảo vệ tiền tệ ngân hàng.",
     "Thuộc tính chuẩn ACID", "🏛️", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Atomicity", "/ˌæt.əˈmɪs.ə.ti/", "noun", "database", "Cơ sở dữ liệu",
     "Tính nguyên tử: nguyên lý 'tất cả hoặc không gì cả', hoặc toàn bộ giao dịch thành công, hoặc không có gì thay đổi.",
     "Atomicity ensures money transferred from account A reaches account B completely.", "Tính nguyên tử đảm bảo tiền chuyển từ tài khoản A sẽ tới trọn vẹn tài khoản B.",
     "Tính nguyên tử Atomicity", "⚛️", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Consistency", "/kənˈsɪs.tən.si/", "noun", "database", "Cơ sở dữ liệu",
     "Tính nhất quán: giao dịch chỉ có thể đưa CSDL từ trạng thái hợp lệ này sang trạng thái hợp lệ khác theo mọi ràng buộc.",
     "Consistency enforces foreign keys and schema checks across transactions.", "Tính nhất quán thực thi khóa ngoại và kiểm tra lược đồ qua mọi giao dịch.",
     "Tính nhất quán CSDL", "⚖️", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Isolation", "/ˌaɪ.səˈleɪ.ʃən/", "noun", "database", "Cơ sở dữ liệu",
     "Tính cô lập: các giao dịch đồng thời không được can thiệp hoặc nhìn thấy trạng thái trung gian chưa hoàn tất của nhau.",
     "Isolation isolates ongoing transactions until they commit successfully.", "Tính cô lập cô lập các giao dịch đang diễn ra cho đến khi chúng commit thành công.",
     "Tính cô lập Isolation", "🧱", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Durability", "/ˌdjʊə.rəˈbɪl.ə.ti/", "noun", "database", "Cơ sở dữ liệu",
     "Tính bền vững: đảm bảo dữ liệu của một giao dịch đã commit sẽ được lưu vĩnh viễn ngay cả khi mất điện đột ngột.",
     "Write-ahead logging guarantees data durability across system crashes.", "Ghi nhật ký ghi trước đảm bảo tính bền vững của dữ liệu qua các sự cố sập hệ thống.",
     "Tính bền vững Durability", "🛡️", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Dirty Read", "/ˈdɜː.ti riːd/", "noun", "database", "Cơ sở dữ liệu",
     "Đọc rác: hiện tượng một giao dịch đọc phải dữ liệu chưa được commit của một giao dịch khác mà sau đó bị hủy.",
     "Read Committed isolation prevents dirty reads from occurring.", "Mức cô lập Read Committed ngăn chặn hiện tượng đọc rác xảy ra.",
     "Đọc rác Dirty Read", "🗑️", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Non-Repeatable Read", "/ˌnɒn rɪˈpiː.tə.bəl riːd/", "noun", "database", "Cơ sở dữ liệu",
     "Đọc không lặp lại: cùng một câu lệnh đọc lại dòng dữ liệu nhưng trả về kết quả khác do giao dịch khác vừa sửa và commit.",
     "Repeatable Read level prevents non-repeatable read anomalies.", "Mức Repeatable Read ngăn chặn các bất thường đọc không lặp lại.",
     "Đọc không lặp lại", "🔄", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Phantom Read", "/ˈfæn.təm riːd/", "noun", "database", "Cơ sở dữ liệu",
     "Đọc bóng ma: hiện tượng các hàng mới xuất hiện trong một tập kết quả đọc khi một giao dịch khác vừa chèn thêm.",
     "Serializable isolation prevents phantom reads completely.", "Mức cô lập Serializable ngăn chặn hoàn toàn hiện tượng đọc bóng ma.",
     "Đọc bóng ma Phantom Read", "👻", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Isolation Level", "/ˌaɪ.səˈleɪ.ʃən ˈlev.əl/", "noun", "database", "Cơ sở dữ liệu",
     "Mức độ cô lập: cài đặt xác định mức độ bảo vệ của các giao dịch trước sự can thiệp từ giao dịch khác.",
     "Choosing the right isolation level balances performance and safety.", "Chọn đúng mức cô lập giúp cân bằng giữa hiệu năng và độ an toàn dữ liệu.",
     "Mức độ cô lập", "🎚️", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Read Committed", "/riːd kəˈmɪt.ɪd/", "noun", "database", "Cơ sở dữ liệu",
     "Mức cô lập Read Committed: chỉ cho phép đọc các dữ liệu đã được commit, là mặc định ở nhiều hệ CSDL.",
     "PostgreSQL defaults to Read Committed isolation for transactions.", "PostgreSQL mặc định dùng mức cô lập Read Committed cho các giao dịch.",
     "Mức Read Committed", "✅", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Repeatable Read", "/rɪˈpiː.tə.bəl riːd/", "noun", "database", "Cơ sở dữ liệu",
     "Mức cô lập Repeatable Read: đảm bảo dữ liệu đã đọc trong cùng một giao dịch sẽ giữ nguyên giá trị suốt quá trình.",
     "MySQL InnoDB uses Repeatable Read as its default isolation level.", "MySQL InnoDB dùng Repeatable Read làm mức cô lập mặc định.",
     "Mức Repeatable Read", "🔁", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Serializable", "/ˈsɪə.ri.ə.laɪ.zə.bəl/", "noun", "database", "Cơ sở dữ liệu",
     "Mức cô lập Serializable: mức cô lập cao nhất, thực thi các giao dịch như thể chúng diễn ra tuần tự từng cái một.",
     "Serializable guarantees absolute safety at the expense of concurrency throughput.", "Serializable đảm bảo an toàn tuyệt đối với cái giá là giảm thông lượng đồng thời.",
     "Mức Serializable", "🔒", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Database Lock", "/ˈdeɪ.tə.beɪs lɒk/", "noun", "database", "Cơ sở dữ liệu",
     "Khóa CSDL: cơ chế ngăn chặn nhiều giao dịch đồng thời sửa đổi cùng một tài nguyên dữ liệu.",
     "Row-level locks offer higher concurrency compared to table-level locks.", "Khóa ở cấp độ hàng mang lại tính đồng thời cao hơn so với khóa ở cấp độ bảng.",
     "Khóa CSDL Lock", "🔒", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Pessimistic Locking", "/ˌpes.ɪˈmɪs.tɪk ˈlɒk.ɪŋ/", "noun", "database", "Cơ sở dữ liệu",
     "Khóa bi quan: khóa dữ liệu ngay từ khi đọc để ngăn ngừa mọi can thiệp sửa đổi từ giao dịch khác.",
     "Financial balance transfers use 'SELECT FOR UPDATE' for pessimistic locking.", "Giao dịch chuyển số dư tài chính dùng 'SELECT FOR UPDATE' để khóa bi quan.",
     "Khóa bi quan Pessimistic", "🛡️", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Optimistic Locking", "/ˌɒp.tɪˈmɪs.tɪk ˈlɒk.ɪŋ/", "noun", "database", "Cơ sở dữ liệu",
     "Khóa lạc quan: không khóa dữ liệu khi đọc, mà dùng cột số phiên bản (version) để kiểm tra xung đột lúc ghi.",
     "Optimistic locking is ideal for high-throughput systems with low contention.", "Khóa lạc quan là lý tưởng cho hệ thống thông lượng cao có ít sự tranh chấp.",
     "Khóa lạc quan Optimistic", "🕊️", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Deadlock", "/ˈded.lɒk/", "noun", "database", "Cơ sở dữ liệu",
     "Bế tắc giao dịch: tình trạng hai giao dịch chờ khóa của nhau dẫn đến đình trệ vĩnh viễn nếu không can thiệp.",
     "The database deadlock detector aborts one transaction to unblock others.", "Trình phát hiện bế tắc của CSDL sẽ hủy một giao dịch để mở khóa các giao dịch khác.",
     "Bế tắc giao dịch Deadlock", "🛑", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Normalization", "/ˌnɔː.mə.laɪˈzeɪ.ʃən/", "noun", "database", "Cơ sở dữ liệu",
     "Chuẩn hóa dữ liệu: quá trình tổ chức cấu trúc bảng để giảm thiểu trùng lặp và loại bỏ dị thường khi cập nhật.",
     "Normalization eliminates redundant data by splitting records into related tables.", "Chuẩn hóa loại bỏ dữ liệu dư thừa bằng cách tách bản ghi thành các bảng có quan hệ.",
     "Chuẩn hóa dữ liệu", "📏", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("First Normal Form (1NF)", "/fɜːst ˈnɔː.məl fɔːm/", "noun", "database", "Cơ sở dữ liệu",
     "Dạng chuẩn 1: mỗi cột chỉ chứa các giá trị nguyên tử đơn lẻ và không có các nhóm lặp lại.",
     "1NF mandates that each cell contains only one atomic value.", "Dạng chuẩn 1 yêu cầu mỗi ô chỉ được chứa duy nhất một giá trị nguyên tử.",
     "Dạng chuẩn 1NF", "1️⃣", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Second Normal Form (2NF)", "/ˈsek.ənd ˈnɔː.məl fɔːm/", "noun", "database", "Cơ sở dữ liệu",
     "Dạng chuẩn 2: đạt 1NF và mọi thuộc tính không khóa đều phụ thuộc hàm đầy đủ vào khóa chính.",
     "2NF eliminates partial dependencies on composite primary keys.", "Dạng chuẩn 2 loại bỏ các phụ thuộc một phần vào khóa chính kết hợp.",
     "Dạng chuẩn 2NF", "2️⃣", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Third Normal Form (3NF)", "/θɜːd ˈnɔː.məl fɔːm/", "noun", "database", "Cơ sở dữ liệu",
     "Dạng chuẩn 3: đạt 2NF và không chứa phụ thuộc bắc cầu giữa các thuộc tính không khóa.",
     "3NF ensures no non-key field determines another non-key field.", "Dạng chuẩn 3 đảm bảo không có trường không khóa nào xác định một trường không khóa khác.",
     "Dạng chuẩn 3NF", "3️⃣", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("BCNF (Boyce-Codd Normal Form)", "/ˌbiː.siː.enˈef/", "noun", "database", "Cơ sở dữ liệu",
     "Dạng chuẩn Boyce-Codd: phiên bản chặt chẽ hơn của 3NF trong đó mọi định thức đều phải là siêu khóa.",
     "BCNF resolves anomalies arising from overlapping candidate keys.", "BCNF giải quyết các bất thường nảy sinh từ các khóa ứng viên gối nhau.",
     "Dạng chuẩn BCNF", "✨", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Denormalization", "/diːˌnɔː.mə.laɪˈzeɪ.ʃən/", "noun", "database", "Cơ sở dữ liệu",
     "Phi chuẩn hóa: chủ động thêm dữ liệu dư thừa vào bảng để giảm số phép join và tăng tốc độ đọc dữ liệu.",
     "Denormalization improves read speeds at the expense of extra storage and write complexity.", "Phi chuẩn hóa cải thiện tốc độ đọc với cái giá là tốn thêm bộ nhớ và phức tạp lúc ghi.",
     "Phi chuẩn hóa dữ liệu", "⚡", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Sharding", "/ˈʃɑː.dɪŋ/", "noun", "database", "Cơ sở dữ liệu",
     "Phân mảnh (Sharding): chia nhỏ cơ sở dữ liệu thành các phần riêng biệt đặt trên nhiều máy chủ vật lý khác nhau.",
     "Database sharding enables horizontal scaling across independent database clusters.", "Phân mảnh CSDL cho phép mở rộng quy mô theo chiều ngang trên các cụm máy chủ độc lập.",
     "Phân mảnh Sharding", "🧩", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Partitioning", "/pɑːˈtɪʃ.ən.ɪŋ/", "noun", "database", "Cơ sở dữ liệu",
     "Phân vùng bảng: chia một bảng lớn thành các phần vật lý nhỏ hơn trên cùng một máy chủ cơ sở dữ liệu.",
     "Table partitioning by year speeds up archival data lookups.", "Phân vùng bảng theo năm giúp tăng tốc tra cứu dữ liệu lưu trữ lịch sử.",
     "Phân vùng Partitioning", "🗂️", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Horizontal Partitioning", "/ˌhɒr.ɪˈzɒn.təl pɑːˈtɪʃ.ən.ɪŋ/", "noun", "database", "Cơ sở dữ liệu",
     "Phân vùng ngang: chia bảng theo các hàng, phân chia các bản ghi vào các bảng con khác nhau.",
     "Horizontal partitioning splits user records by geographical regions.", "Phân vùng ngang chia các bản ghi người dùng theo từng khu vực địa lý.",
     "Phân vùng ngang", "↔️", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Vertical Partitioning", "/ˈvɜː.tɪ.kəl pɑːˈtɪʃ.ən.ɪŋ/", "noun", "database", "Cơ sở dữ liệu",
     "Phân vùng dọc: chia bảng theo các cột, tách các cột ít dùng hoặc chứa văn bản lớn sang bảng riêng.",
     "Vertical partitioning moves large blog text columns into a separate table.", "Phân vùng dọc chuyển các cột văn bản bài viết lớn sang bảng riêng.",
     "Phân vùng dọc", "↕️", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Replication", "/ˌrep.lɪˈkeɪ.ʃən/", "noun", "database", "Cơ sở dữ liệu",
     "Sao chép dữ liệu: tự động sao chép dữ liệu từ một máy chủ CSDL sang các máy chủ khác để dự phòng.",
     "Database replication provides fault tolerance and offloads read queries.", "Sao chép CSDL mang lại khả năng chịu lỗi và giảm tải cho các truy vấn đọc.",
     "Sao chép Replication", "👯", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Master-Slave Replication", "/ˈmɑː.stər sleɪv ˌrep.lɪˈkeɪ.ʃən/", "noun", "database", "Cơ sở dữ liệu",
     "Mô hình sao chép Chính - Phụ: máy chủ chính ghi dữ liệu, các máy chủ phụ nhận bản sao để phục vụ đọc.",
     "In master-slave replication, writes go to the primary node and reads route to replicas.", "Trong mô hình chính-phụ, việc ghi gửi về nút chính còn việc đọc gửi về các bản sao.",
     "Mô hình Chính - Phụ", "👑", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Multi-Master Replication", "/ˌmʌl.ti ˈmɑː.stər/", "noun", "database", "Cơ sở dữ liệu",
     "Sao chép Đa chính: nhiều máy chủ CSDL đều có quyền tiếp nhận các thao tác ghi dữ liệu đồng thời.",
     "Multi-master replication requires robust conflict resolution strategies.", "Sao chép đa chính đòi hỏi các chiến lược giải quyết xung đột mạnh mẽ.",
     "Sao chép Đa chính", "👥", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Write-Ahead Log (WAL)", "/raɪt əˈhed lɒɡ/", "noun", "database", "Cơ sở dữ liệu",
     "Nhật ký ghi trước: kỹ thuật ghi mọi thay đổi vào nhật ký tuần tự trước khi cập nhật dữ liệu bảng trên đĩa.",
     "WAL ensures database recovery can reconstruct state after sudden crashes.", "WAL đảm bảo CSDL có thể tái dựng lại trạng thái sau khi sập máy chủ đột ngột.",
     "Nhật ký ghi trước WAL", "📜", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Connection Pool", "/kəˈnek.ʃən puːl/", "noun", "database", "Cơ sở dữ liệu",
     "Bể kết nối: bộ nhớ đệm duy trì sẵn các kết nối CSDL để tái sử dụng, tránh tốn chi phí khởi tạo liên tục.",
     "HikariCP is an ultra-fast connection pool commonly used in Java applications.", "HikariCP là một connection pool siêu nhanh thường dùng trong ứng dụng Java.",
     "Bể kết nối Connection Pool", "🏊", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("ORM (Object-Relational Mapping)", "/ˌəʊ.ɑːrˈem/", "noun", "database", "Cơ sở dữ liệu",
     "Kỹ thuật ánh xạ hướng đối tượng sang quan hệ: chuyển đổi dữ liệu giữa các bảng SQL và các đối tượng mã nguồn.",
     "Hibernate and Prisma are leading ORM libraries in web development.", "Hibernate và Prisma là các thư viện ORM hàng đầu trong phát triển web.",
     "Ánh xạ đối tượng ORM", "🔄", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Database Migration", "/ˈdeɪ.tə.beɪs maɪˈɡreɪ.ʃən/", "noun", "database", "Cơ sở dữ liệu",
     "Di chuyển CSDL: quản lý có phiên bản đối với các thay đổi cấu trúc lược đồ cơ sở dữ liệu qua thời gian.",
     "Run migrations during deployment to add new columns automatically.", "Chạy migration trong lúc triển khai để tự động bổ sung các cột mới.",
     "Di chuyển lược đồ Migration", "🚚", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Data Seeding", "/ˈdeɪ.tə siːd.ɪŋ/", "noun", "database", "Cơ sở dữ liệu",
     "Gieo mầm dữ liệu: khởi tạo dữ liệu mẫu ban đầu vào cơ sở dữ liệu phục vụ mục đích kiểm thử và phát triển.",
     "Seed scripts populate dummy users and products for development testing.", "Kịch bản gieo mầm dữ liệu tạo người dùng và sản phẩm giả để kiểm thử.",
     "Gieo mầm dữ liệu Seeding", "🌱", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Data Warehouse", "/ˈdeɪ.tə ˈweə.haʊs/", "noun", "database", "Cơ sở dữ liệu",
     "Kho dữ liệu: hệ thống CSDL tập trung tối ưu hóa cho việc phân tích dữ liệu tổng hợp từ nhiều nguồn.",
     "Snowflake and BigQuery are prominent cloud data warehouses.", "Snowflake và BigQuery là những kho dữ liệu đám mây hàng đầu.",
     "Kho dữ liệu Data Warehouse", "🏭", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Data Lake", "/ˈdeɪ.tə leɪk/", "noun", "database", "Cơ sở dữ liệu",
     "Hồ dữ liệu: kho lưu trữ tập trung chứa lượng lớn dữ liệu thô ở cả dạng có cấu trúc, bán cấu trúc và phi cấu trúc.",
     "Data lakes store clickstream logs in raw formats for future analysis.", "Hồ dữ liệu lưu trữ nhật ký lượt click ở dạng thô phục vụ phân tích sau này.",
     "Hồ dữ liệu Data Lake", "🌊", "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=600&auto=format&fit=crop&q=80"),

    ("Data Mart", "/ˈdeɪ.tə mɑːt/", "noun", "database", "Cơ sở dữ liệu",
     "Chợ dữ liệu: kho dữ liệu thu nhỏ phục vụ nhu cầu phân tích riêng cho một phòng ban cụ thể như tài chính hay tiếp thị.",
     "The marketing team accesses their dedicated data mart for campaign insights.", "Nhóm tiếp thị truy cập vào data mart chuyên dụng của họ để nắm bắt thông tin chiến dịch.",
     "Chợ dữ liệu Data Mart", "🏪", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("ETL (Extract, Transform, Load)", "/ˌiː.tiːˈel/", "noun", "database", "Cơ sở dữ liệu",
     "Quy trình trích xuất, biến đổi và nạp dữ liệu: trích xuất từ nguồn thô, làm sạch và nạp vào kho dữ liệu.",
     "ETL pipelines process overnight sales logs into clean reporting tables.", "Đường ống ETL xử lý nhật ký bán hàng qua đêm thành các bảng báo cáo sạch sẽ.",
     "Quy trình ETL", "🔄", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("ELT (Extract, Load, Transform)", "/ˌiː.elˈtiː/", "noun", "database", "Cơ sở dữ liệu",
     "Quy trình trích xuất, nạp rồi biến đổi: nạp dữ liệu thô thẳng vào kho trước rồi dùng sức mạnh của kho để biến đổi.",
     "Modern cloud platforms leverage ELT to transform data directly inside BigQuery.", "Các nền tảng đám mây hiện đại tận dụng ELT để biến đổi dữ liệu trực tiếp trong BigQuery.",
     "Quy trình ELT", "⚡", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("OLAP (Online Analytical Processing)", "/ˈoʊ.læp/", "noun", "database", "Cơ sở dữ liệu",
     "Xử lý phân tích trực tuyến: hệ thống tối ưu hóa cho các truy vấn phân tích tổng hợp phức tạp trên khối dữ liệu lớn.",
     "OLAP cubes let analysts slice and dice quarterly revenue metrics.", "Các khối OLAP cho phép chuyên viên phân tích cắt lớp số liệu doanh thu hàng quý.",
     "Xử lý phân tích OLAP", "📊", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("OLTP (Online Transaction Processing)", "/ˌoʊ.el.tiːˈpiː/", "noun", "database", "Cơ sở dữ liệu",
     "Xử lý giao dịch trực tuyến: hệ thống tối ưu cho số lượng lớn các thao tác giao dịch nhỏ, nhanh và đồng thời.",
     "E-commerce shopping carts run on high-performance OLTP engines.", "Giỏ hàng thương mại điện tử vận hành trên các bộ máy OLTP hiệu năng cao.",
     "Xử lý giao dịch OLTP", "⚡", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Star Schema", "/stɑː ˈskiː.mə/", "noun", "database", "Cơ sở dữ liệu",
     "Lược đồ hình sao: mô hình kho dữ liệu gồm một bảng sự kiện (Fact table) ở giữa và các bảng chiều (Dimension) bao quanh.",
     "Star schemas simplify business reporting queries with straightforward joins.", "Lược đồ hình sao đơn giản hóa truy vấn báo cáo với các phép join trực tiếp.",
     "Lược đồ hình sao", "⭐", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Snowflake Schema", "/ˈsnəʊ.fleɪk ˈskiː.mə/", "noun", "database", "Cơ sở dữ liệu",
     "Lược đồ bông tuyết: biến thể của lược đồ hình sao trong đó các bảng chiều được chuẩn hóa thành các bảng nhỏ hơn.",
     "Snowflake schemas reduce data redundancy across complex dimensions.", "Lược đồ bông tuyết giảm thiểu sự dư thừa dữ liệu trên các chiều phức tạp.",
     "Lược đồ bông tuyết", "❄️", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Change Data Capture (CDC)", "/tʃeɪndʒ ˈdeɪ.tə ˈkæp.tʃər/", "noun", "database", "Cơ sở dữ liệu",
     "Bắt giữ dữ liệu thay đổi: kỹ thuật tự động phát hiện và gửi đi các thay đổi (chèn, sửa, xóa) trong CSDL theo thời gian thực.",
     "Debezium is a leading CDC tool that streams database changes into Kafka.", "Debezium là công cụ CDC hàng đầu giúp truyền phát các thay đổi CSDL vào Kafka.",
     "Bắt giữ thay đổi CDC", "📡", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Document Store", "/ˈdɒk.jə.mənt stɔːr/", "noun", "database", "Cơ sở dữ liệu",
     "CSDL hướng tài liệu: hệ NoSQL lưu trữ dữ liệu dưới dạng tài liệu JSON, BSON hoặc XML.",
     "MongoDB is the most popular document store database.", "MongoDB là hệ cơ sở dữ liệu hướng tài liệu phổ biến nhất hiện nay.",
     "CSDL hướng tài liệu", "📑", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Key-Value Store", "/kiː ˈvæl.juː stɔːr/", "noun", "database", "Cơ sở dữ liệu",
     "CSDL khóa - giá trị: cơ sở dữ liệu đơn giản nhất ghép mỗi khóa định danh duy nhất với một giá trị tương ứng.",
     "Redis and DynamoDB excel as high-speed key-value stores.", "Redis và DynamoDB là những hệ lưu trữ khóa - giá trị tốc độ cao xuất sắc.",
     "CSDL Khóa - Giá trị", "🗝️", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Column-Family Database", "/ˈkɒl.əm ˈfæm.əl.i/", "noun", "database", "Cơ sở dữ liệu",
     "CSDL họ cột: lưu trữ dữ liệu theo từng nhóm cột giúp đọc siêu nhanh cho các truy vấn phân tích tổng hợp.",
     "Apache Cassandra is a distributed column-family store built for extreme write scale.", "Apache Cassandra là hệ lưu trữ họ cột phân tán được xây dựng để ghi dữ liệu cực lớn.",
     "CSDL họ cột", "🏛️", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Graph Database", "/ɡrɑːf ˈdeɪ.tə.beɪs/", "noun", "database", "Cơ sở dữ liệu",
     "CSDL đồ thị: cơ sở dữ liệu sử dụng cấu trúc đồ thị với các nút, cạnh và thuộc tính để biểu diễn dữ liệu liên kết.",
     "Neo4j stores complex fraud networks as interconnected graph nodes.", "Neo4j lưu trữ mạng lưới gian lận phức tạp dưới dạng các nút đồ thị liên kết.",
     "CSDL đồ thị Graph", "🕸️", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Time Series Database", "/taɪm ˈsɪə.riːz/", "noun", "database", "Cơ sở dữ liệu",
     "CSDL chuỗi thời gian: CSDL tối ưu hóa cho việc lưu trữ và truy vấn các chuỗi điểm dữ liệu kèm dấu thời gian.",
     "InfluxDB and TimescaleDB store IoT sensor metrics efficiently.", "InfluxDB và TimescaleDB lưu trữ số liệu cảm biến IoT rất hiệu quả.",
     "CSDL chuỗi thời gian", "⏱️", "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=600&auto=format&fit=crop&q=80"),

    ("Vector Database", "/ˈvek.tər ˈdeɪ.tə.beɪs/", "noun", "database", "Cơ sở dữ liệu",
     "CSDL véc-tơ: cơ sở dữ liệu lưu trữ các vector embedding và hỗ trợ tìm kiếm độ tương đồng cho các ứng dụng AI.",
     "Pinecone and Milvus enable fast similarity searches for LLM embeddings.", "Pinecone và Milvus cho phép tìm kiếm độ tương đồng nhanh chóng cho vector embedding của LLM.",
     "CSDL véc-tơ AI", "🎯", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("CAP Theorem", "/kæp ˈθɪə.rəm/", "noun", "database", "Cơ sở dữ liệu",
     "Định lý CAP: hệ thống phân tán chỉ có thể đảm bảo tối đa hai trong ba yếu tố: Nhất quán, Sẵn sàng và Chịu phân vùng.",
     "Under network partitions, distributed databases must choose Consistency or Availability.", "Khi mạng bị phân vùng, cơ sở dữ liệu phân tán buộc phải chọn Nhất quán hoặc Sẵn sàng.",
     "Định lý CAP phân tán", "⚖️", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("BASE Model", "/beɪs ˈmɒd.əl/", "noun", "database", "Cơ sở dữ liệu",
     "Mô hình BASE (Basically Available, Soft state, Eventual consistency): mô hình thay thế ACID cho hệ phân tán.",
     "NoSQL systems often favor BASE over ACID for horizontal scalability.", "Các hệ NoSQL thường chuộng mô hình BASE hơn ACID để đạt khả năng mở rộng ngang.",
     "Mô hình BASE", "🌐", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Eventual Consistency", "/ɪˈven.tʃu.əl kənˈsɪs.tən.si/", "noun", "database", "Cơ sở dữ liệu",
     "Tính nhất quán cuối cùng: mô hình đảm bảo nếu không có cập nhật mới, mọi bản sao dữ liệu cuối cùng sẽ đồng nhất.",
     "Social media like counters often rely on eventual consistency.", "Bộ đếm lượt thích trên mạng xã hội thường dựa vào tính nhất quán cuối cùng.",
     "Tính nhất quán cuối cùng", "🔄", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Query Execution Plan", "/ˈkwɪə.ri ˌek.sɪˈkjuː.ʃən plæn/", "noun", "database", "Cơ sở dữ liệu",
     "Kế hoạch thực thi truy vấn: chuỗi các bước chi tiết mà bộ tối ưu hóa CSDL chọn để thực hiện một truy vấn SQL.",
     "Examine the query execution plan to diagnose expensive table scans.", "Kiểm tra kế hoạch thực thi truy vấn để chẩn đoán các thao tác quét bảng tốn kém.",
     "Kế hoạch thực thi truy vấn", "🗺️", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Index Scan", "/ˈɪn.deks skæn/", "noun", "database", "Cơ sở dữ liệu",
     "Quét chỉ mục: việc duyệt qua các phần tử của cây chỉ mục để lọc các hàng phù hợp.",
     "An index scan reads all index nodes when filter criteria lack high selectivity.", "Quét chỉ mục sẽ đọc tất cả các nút chỉ mục khi tiêu chí lọc không có tính chọn lọc cao.",
     "Quét chỉ mục Index Scan", "🔍", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Index Seek", "/ˈɪn.deks siːk/", "noun", "database", "Cơ sở dữ liệu",
     "Tìm kiếm theo chỉ mục: điều hướng trực tiếp bằng cây B-tree đến đúng hàng cần tìm, nhanh nhất có thể.",
     "An index seek provides the fastest lookup performance for equality filters.", "Tìm kiếm chỉ mục mang lại hiệu năng tra cứu nhanh nhất cho bộ lọc so sánh bằng.",
     "Tìm kiếm chỉ mục Seek", "🎯", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Full Table Scan", "/fʊl ˈteɪ.bəl skæn/", "noun", "database", "Cơ sở dữ liệu",
     "Quét toàn bộ bảng: đọc từng dòng dữ liệu từ đầu đến cuối bảng vì không có chỉ mục phù hợp.",
     "A full table scan on a 50-million-row table causes severe I/O bottlenecks.", "Quét toàn bộ bảng trên bảng 50 triệu hàng gây nghẽn nghiêm trọng cổng vào ra đĩa.",
     "Quét toàn bảng Table Scan", "🐢", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Explain Plan", "/ɪkˈspleɪn plæn/", "noun", "database", "Cơ sở dữ liệu",
     "Lệnh giải trình: câu lệnh EXPLAIN phân tích chi phí và chỉ ra cách CSDL sẽ chạy truy vấn SQL.",
     "Running 'EXPLAIN ANALYZE' reveals the actual runtime of each query node.", "Chạy lệnh 'EXPLAIN ANALYZE' hiển thị thời gian thực tế của từng nút truy vấn.",
     "Lệnh giải trình Explain", "📋", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Database Backup / Dump", "/ˈdeɪ.tə.beɪs ˈbæk.ʌp/", "noun", "database", "Cơ sở dữ liệu",
     "Sao lưu CSDL: tạo bản sao lưu toàn bộ dữ liệu hoặc lược đồ vào một tệp để khôi phục khi có thảm họa.",
     "Execute nightly pg_dump commands to back up production PostgreSQL data.", "Chạy lệnh pg_dump mỗi đêm để sao lưu dữ liệu PostgreSQL sản xuất.",
     "Sao lưu CSDL Backup", "💾", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Point-in-Time Recovery (PITR)", "/pɔɪnt ɪn taɪm rɪˈkʌv.ər.i/", "noun", "database", "Cơ sở dữ liệu",
     "Khôi phục tại thời điểm: khả năng phục hồi dữ liệu về chính xác một giây cụ thể trong quá khứ nhờ WAL log.",
     "PITR allows reverting database state back to right before an accidental table drop.", "PITR cho phép khôi phục dữ liệu về đúng thời điểm ngay trước khi lỡ xóa nhầm bảng.",
     "Khôi phục tại thời điểm", "⏰", "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=600&auto=format&fit=crop&q=80"),

    ("In-Memory Database", "/ɪn ˈmem.ər.i ˈdeɪ.tə.beɪs/", "noun", "database", "Cơ sở dữ liệu",
     "CSDL trong bộ nhớ RAM: lưu trữ toàn bộ dữ liệu trên RAM để đạt tốc độ truy xuất cực nhanh với độ trễ micro-giây.",
     "Redis serves as an in-memory database to deliver sub-millisecond responses.", "Redis đóng vai trò cơ sở dữ liệu trong RAM giúp phản hồi dưới một mili-giây.",
     "CSDL trong RAM", "⚡", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Cache Invalidation", "/kæʃ ɪnˌvæl.ɪˈdeɪ.ʃən/", "noun", "database", "Cơ sở dữ liệu",
     "Xóa bỏ bộ nhớ đệm: quá trình xóa hoặc cập nhật dữ liệu lưu đệm khi dữ liệu gốc trong CSDL đã bị sửa.",
     "Cache invalidation is notoriously one of the hardest problems in computer science.", "Xóa bỏ bộ nhớ đệm nổi tiếng là một trong những bài toán khó nhất của khoa học máy tính.",
     "Xóa bộ nhớ đệm", "🧹", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Redis", "/ˈred.ɪs/", "noun", "database", "Cơ sở dữ liệu",
     "Redis: hệ thống lưu trữ cấu trúc dữ liệu trong bộ nhớ mã nguồn mở, dùng làm CSDL, bộ nhớ đệm và môi giới tin nhắn.",
     "Use Redis to cache session tokens and enforce rate limiting per user.", "Dùng Redis để lưu đệm mã token phiên và thực thi giới hạn tần suất yêu cầu người dùng.",
     "Hệ thống Redis Cache", "🔴", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Query Optimization", "/ˈkwɪə.ri ˌɒp.tɪ.maɪˈzeɪ.ʃən/", "noun", "database", "Cơ sở dữ liệu",
     "Tối ưu hóa truy vấn: quá trình chọn lựa kế hoạch thực thi tốn ít tài nguyên và thời gian nhất để chạy một câu lệnh SQL.",
     "Proper query optimization reduced database CPU utilization by 40 percent.", "Việc tối ưu hóa truy vấn đúng đắn đã giảm 40% tải CPU của cơ sở dữ liệu.",
     "Tối ưu hóa truy vấn", "🚀", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Upsert", "/ˈʌp.sɜːt/", "verb", "database", "Cơ sở dữ liệu",
     "Chèn hoặc cập nhật: thao tác chèn bản ghi mới nếu chưa có, hoặc cập nhật bản ghi cũ nếu đã tồn tại khóa.",
     "The ON CONFLICT DO UPDATE clause in PostgreSQL performs an atomic upsert.", "Mệnh đề ON CONFLICT DO UPDATE trong PostgreSQL thực hiện thao tác upsert nguyên tử.",
     "Thao tác Upsert", "🔄", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Write Amplification", "/raɪt ˌæm.plɪ.fɪˈkeɪ.ʃən/", "noun", "database", "Cơ sở dữ liệu",
     "Khuếch đại ghi: hiện tượng lượng dữ liệu ghi vật lý vào ổ đĩa lớn hơn nhiều so với lượng dữ liệu thực tế do phần mềm yêu cầu.",
     "Excessive non-clustered indexes increase write amplification on frequent updates.", "Quá nhiều chỉ mục phi cụm làm gia tăng hiện tượng khuếch đại ghi khi cập nhật dữ liệu liên tục.",
     "Khuếch đại ghi đĩa", "📈", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80")
]

if __name__ == "__main__":
    print(f"Domain 3 terms count: {len(terms)}")
