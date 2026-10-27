# -*- coding: utf-8 -*-
"""Domain 1: Programming & Software Engineering (100 core terms)"""

terms = [
    ("Algorithm", "/ˈæl.ɡə.rɪ.ðəm/", "noun", "programming", "Lập trình",
     "Thuật toán: tập hợp chỉ dẫn từng bước rõ ràng để giải quyết một bài toán cụ thể.",
     "The sorting algorithm reorders elements in ascending order.", "Thuật toán sắp xếp sắp xếp lại các phần tử theo thứ tự tăng dần.",
     "Thuật toán xử lý", "⚙️", "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    ("Refactor", "/ˌriːˈfæk.tər/", "verb", "programming", "Lập trình",
     "Tái cấu trúc mã nguồn: cải thiện cấu trúc bên trong của mã mà không làm thay đổi hành vi bên ngoài.",
     "We should refactor the billing module to eliminate code duplication.", "Chúng ta nên tái cấu trúc mô-đun thanh toán để loại bỏ việc trùng lặp mã.",
     "Tái cấu trúc mã", "🔄", "https://images.unsplash.com/photo-1542838132-92c53300491e?w=600&auto=format&fit=crop&q=80"),

    ("Repository", "/rɪˈpɒz.ɪ.tər.i/", "noun", "programming", "Lập trình",
     "Kho lưu trữ: nơi lưu giữ mã nguồn và lịch sử các phiên bản trong hệ thống Git.",
     "Initialize a local git repository using 'git init'.", "Khởi tạo kho lưu trữ git cục bộ bằng lệnh 'git init'.",
     "Kho lưu trữ Git", "📦", "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?w=600&auto=format&fit=crop&q=80"),

    ("Deploy", "/dɪˈplɔɪ/", "verb", "programming", "Lập trình",
     "Triển khai: đưa ứng dụng lên máy chủ sản xuất để phục vụ người dùng cuối.",
     "We deploy our production releases every Tuesday morning.", "Chúng tôi triển khai các bản phát hành sản xuất vào mỗi sáng thứ Ba.",
     "Triển khai máy chủ", "🚀", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600&auto=format&fit=crop&q=80"),

    ("Debug", "/diːˈbʌɡ/", "verb", "programming", "Lập trình",
     "Gỡ lỗi: tìm kiếm, phân tích và sửa chữa các lỗi logic hoặc lỗi cú pháp trong phần mềm.",
     "Use interactive debuggers to inspect variables during runtime.", "Sử dụng trình gỡ lỗi tương tác để kiểm tra giá trị các biến lúc chạy.",
     "Gỡ lỗi phần mềm", "🐛", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Compiler", "/kəmˈpaɪ.lər/", "noun", "programming", "Lập trình",
     "Trình biên dịch: dịch toàn bộ mã nguồn bậc cao thành mã máy nhị phân có thể thực thi trực tiếp.",
     "The C++ compiler outputs an executable binary file upon success.", "Trình biên dịch C++ xuất ra một tệp nhị phân thực thi được khi thành công.",
     "Trình biên dịch mã", "⚙️", "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    ("Interpreter", "/ɪnˈtɜː.prə.tər/", "noun", "programming", "Lập trình",
     "Trình thông dịch: phần mềm đọc và thực thi từng câu lệnh mã nguồn trực tiếp mà không cần biên dịch trước.",
     "Node.js uses the V8 engine as an interpreter and JIT compiler.", "Node.js sử dụng công cụ V8 như một trình thông dịch và biên dịch JIT.",
     "Trình thông dịch", "📜", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Syntax", "/ˈsɪn.tæks/", "noun", "programming", "Lập trình",
     "Cú pháp: tập hợp các quy tắc định dạng hợp lệ của các câu lệnh trong ngôn ngữ lập trình.",
     "Python emphasizes clean indentation syntax over curly braces.", "Python nhấn mạnh cú pháp thụt lề sạch sẽ thay vì dùng dấu ngoặc nhọn.",
     "Cú pháp ngôn ngữ", "📝", "https://images.unsplash.com/photo-1542838132-92c53300491e?w=600&auto=format&fit=crop&q=80"),

    ("Variable", "/ˈveə.ri.ə.bəl/", "noun", "programming", "Lập trình",
     "Biến số: định danh đại diện cho một ô nhớ lưu trữ dữ liệu có thể thay đổi trong quá trình chạy.",
     "Global variables should be minimized to avoid state collisions.", "Nên hạn chế biến toàn cục để tránh xung đột trạng thái ngoài ý muốn.",
     "Biến số lưu trữ", "🏷️", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Constant", "/ˈkɒn.stənt/", "noun", "programming", "Lập trình",
     "Hằng số: đại lượng lưu trữ giá trị cố định và không thể thay đổi sau khi đã khởi tạo.",
     "Declare immutable configuration values using the 'const' keyword.", "Khai báo các giá trị cấu hình bất biến bằng từ khóa 'const'.",
     "Hằng số bất biến", "🔒", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Function", "/ˈfʌŋk.ʃən/", "noun", "programming", "Lập trình",
     "Hàm: khối lệnh có thể tái sử dụng, nhận đầu vào, thực hiện xử lý và có thể trả về giá trị đầu ra.",
     "Keep functions small and focused on a single responsibility.", "Giữ cho các hàm ngắn gọn và chỉ tập trung vào một nhiệm vụ duy nhất.",
     "Hàm thực thi", "🧩", "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    ("Parameter", "/pəˈræm.ɪ.tər/", "noun", "programming", "Lập trình",
     "Tham số: biến được định nghĩa trong khai báo của hàm để nhận giá trị truyền vào.",
     "The function signature defines two numeric parameters.", "Chữ ký hàm định nghĩa hai tham số kiểu số.",
     "Tham số khai báo", "📥", "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    ("Argument", "/ˈɑːɡ.jə.mənt/", "noun", "programming", "Lập trình",
     "Đối số: giá trị thực tế được truyền vào hàm khi thực hiện lời gọi hàm.",
     "Pass the user ID as an argument to fetch user profile data.", "Truyền mã người dùng làm đối số để lấy dữ liệu hồ sơ người dùng.",
     "Đối số truyền vào", "📤", "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    ("Return", "/rɪˈtɜːn/", "verb", "programming", "Lập trình",
     "Trả về giá trị: kết thúc việc thực thi hàm và gửi kết quả tính toán lại nơi đã gọi.",
     "If validation fails, the function should return null immediately.", "Nếu kiểm tra dữ liệu thất bại, hàm cần trả về null ngay lập tức.",
     "Trả về giá trị", "🔙", "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    ("Scope", "/skəʊp/", "noun", "programming", "Lập trình",
     "Phạm vi biến: vùng không gian mã nguồn nơi một biến số hoặc định danh có thể truy cập được.",
     "Variables declared inside a block have block-level scope.", "Biến được khai báo bên trong một khối có phạm vi ở cấp độ khối.",
     "Phạm vi truy cập", "🔭", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Recursion", "/rɪˈkɜː.ʃən/", "noun", "programming", "Lập trình",
     "Đệ quy: kỹ thuật trong đó một hàm tự gọi lại chính nó để giải bài toán nhỏ hơn.",
     "Every recursion must have a well-defined base case to terminate.", "Mọi hàm đệ quy đều phải có trường hợp cơ sở rõ ràng để dừng lại.",
     "Hàm đệ quy", "🌀", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Callback", "/ˈkɑːl.bæk/", "noun", "programming", "Lập trình",
     "Hàm gọi lại: hàm được truyền như đối số vào hàm khác để được gọi khi hoàn thành tác vụ.",
     "Provide an error-first callback to handle asynchronous disk reads.", "Cung cấp hàm callback ưu tiên lỗi để xử lý việc đọc đĩa bất đồng bộ.",
     "Hàm gọi lại Callback", "📞", "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    ("Closure", "/ˈkləʊ.ʒər/", "noun", "programming", "Lập trình",
     "Bao đóng (Closure): hàm ghi nhớ và có thể truy cập các biến từ phạm vi bên ngoài ngay cả khi phạm vi đó đã thoát.",
     "Closures are widely used in JavaScript to create private state.", "Closure được sử dụng rộng rãi trong JavaScript để tạo biến trạng thái riêng tư.",
     "Bao đóng Closure", "🎒", "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    ("Promise", "/ˈprɒm.ɪs/", "noun", "programming", "Lập trình",
     "Đối tượng đại diện cho kết quả hoàn thành hoặc thất bại trong tương lai của một tác vụ bất đồng bộ.",
     "Promises prevent deep nesting known as callback hell.", "Promise giúp ngăn chặn tình trạng lồng hàm quá sâu gọi là callback hell.",
     "Lời hứa Promise", "🤝", "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    ("Async/Await", "/eɪˈsɪŋk əˈweɪt/", "phrase", "programming", "Lập trình",
     "Cú pháp giúp viết mã bất đồng bộ trông giống như mã đồng bộ tuần tự, dễ đọc hơn.",
     "Using async/await makes asynchronous network calls intuitive.", "Sử dụng cú pháp async/await giúp các cuộc gọi mạng bất đồng bộ trở nên trực quan.",
     "Bất đồng bộ Async/Await", "⏳", "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=600&auto=format&fit=crop&q=80"),

    ("Object-Oriented Programming (OOP)", "/ˈɒb.dʒɪkt ˈɔː.ri.en.tɪd/", "noun", "programming", "Lập trình",
     "Lập trình hướng đối tượng: mô hình lập trình dựa trên khái niệm các đối tượng chứa dữ liệu và hành vi.",
     "OOP relies on four pillars: encapsulation, inheritance, polymorphism, and abstraction.", "OOP dựa trên bốn trụ cột: đóng gói, kế thừa, đa hình và trừu tượng.",
     "Lập trình hướng đối tượng", "🏛️", "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    ("Class", "/klɑːs/", "noun", "programming", "Lập trình",
     "Lớp: bản thiết kế hoặc khuôn mẫu định nghĩa các thuộc tính và phương thức cho các đối tượng.",
     "Define a User class with properties like name, email, and password.", "Định nghĩa lớp User với các thuộc tính như tên, email và mật khẩu.",
     "Lớp khuôn mẫu Class", "📐", "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    ("Object", "/ˈɒb.dʒɪkt/", "noun", "programming", "Lập trình",
     "Đối tượng: thực thể cụ thể chứa dữ liệu (trạng thái) và hành vi được tạo ra từ một lớp.",
     "Each customer in memory is represented as an instance object.", "Mỗi khách hàng trong bộ nhớ được biểu diễn dưới dạng một đối tượng.",
     "Đối tượng cụ thể", "🧱", "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    ("Instance", "/ˈɪn.stəns/", "noun", "programming", "Lập trình",
     "Bản thể / Thể hiện: đối tượng cụ thể được cấp phát trong bộ nhớ tạo ra từ một lớp.",
     "We instantiate a new instance of the database connection manager.", "Chúng tôi khởi tạo một thể hiện mới của trình quản lý kết nối cơ sở dữ liệu.",
     "Thể hiện đối tượng", "✨", "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    ("Method", "/ˈmeθ.əd/", "noun", "programming", "Lập trình",
     "Phương thức: hàm được gắn liền với một lớp hoặc một đối tượng để thực thi hành vi.",
     "Invoke the calculateTotal() method on the ShoppingCart instance.", "Gọi phương thức calculateTotal() trên thể hiện của ShoppingCart.",
     "Phương thức đối tượng", "⚙️", "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    ("Inheritance", "/ɪnˈher.ɪ.təns/", "noun", "programming", "Lập trình",
     "Kế thừa: cơ chế cho phép một lớp con tái sử dụng và mở rộng thuộc tính, phương thức của lớp cha.",
     "The Dog class gains movement methods via inheritance from Animal.", "Lớp Dog có được các phương thức di chuyển thông qua sự kế thừa từ lớp Animal.",
     "Kế thừa lớp", "🌳", "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    ("Polymorphism", "/ˌpɒl.iˈmɔː.fɪ.zəm/", "noun", "programming", "Lập trình",
     "Tính đa hình: khả năng các đối tượng khác nhau phản hồi theo cách riêng với cùng một thông điệp hoặc phương thức.",
     "Polymorphism allows treating both Circle and Square as Shape instances.", "Tính đa hình cho phép xử lý cả Circle và Square như là đối tượng Shape.",
     "Tính đa hình OOP", "🎭", "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    ("Encapsulation", "/ɪnˌkæp.sjəˈleɪ.ʃən/", "noun", "programming", "Lập trình",
     "Tính đóng gói: kỹ thuật ẩn giấu dữ liệu nội bộ bên trong đối tượng và chỉ cung cấp giao diện truy cập công khai.",
     "Encapsulation protects private fields from direct external manipulation.", "Tính đóng gói bảo vệ các trường dữ liệu riêng tư khỏi sự can thiệp trực tiếp từ bên ngoài.",
     "Tính đóng gói dữ liệu", "💊", "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    ("Abstraction", "/æbˈstræk.ʃən/", "noun", "programming", "Lập trình",
     "Tính trừu tượng: việc chỉ hiển thị các chi tiết thiết yếu cho người dùng và ẩn đi sự phức tạp cài đặt bên trong.",
     "Abstraction hides the low-level SQL queries behind high-level repository methods.", "Tính trừu tượng ẩn các câu lệnh SQL cấp thấp đằng sau các phương thức kho lưu trữ cấp cao.",
     "Tính trừu tượng hóa", "🎨", "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    ("Interface", "/ˈɪn.tə.feɪs/", "noun", "programming", "Lập trình",
     "Giao diện: hợp đồng định nghĩa danh sách các phương thức mà một lớp phải triển khai.",
     "Classes that implement the PaymentGateway interface must implement charge().", "Các lớp triển khai giao diện PaymentGateway bắt buộc phải có phương thức charge().",
     "Giao diện hợp đồng", "📑", "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    ("Abstract Class", "/ˈæb.strækt klɑːs/", "noun", "programming", "Lập trình",
     "Lớp trừu tượng: lớp không thể trực tiếp khởi tạo thành đối tượng, dùng làm lớp nền tảng cho lớp con.",
     "An abstract class can contain both concrete methods and abstract method signatures.", "Lớp trừu tượng có thể chứa cả phương thức cụ thể lẫn chữ ký phương thức trừu tượng.",
     "Lớp trừu tượng", "📐", "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    ("Constructor", "/kənˈstrʌk.tər/", "noun", "programming", "Lập trình",
     "Hàm khởi tạo: phương thức đặc biệt tự động chạy khi một đối tượng mới được tạo ra từ lớp.",
     "Initialize member properties inside the class constructor.", "Khởi tạo các thuộc tính thành viên bên trong hàm khởi tạo của lớp.",
     "Hàm khởi tạo Constructor", "🏗️", "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    ("Destructor", "/dɪˈstrʌk.tər/", "noun", "programming", "Lập trình",
     "Hàm hủy: phương thức tự động chạy khi một đối tượng bị giải phóng bộ nhớ.",
     "The destructor closes file handles and releases unmanaged resources.", "Hàm hủy đóng các con trỏ tệp và giải phóng tài nguyên không quản lý.",
     "Hàm hủy Destructor", "🧹", "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    ("Exception", "/ɪkˈsep.ʃən/", "noun", "programming", "Lập trình",
     "Ngoại lệ: sự kiện bất thường làm gián đoạn luồng thực thi thông thường của chương trình.",
     "Throwing an exception signals that an unrecoverable error occurred.", "Ném ra ngoại lệ báo hiệu một lỗi không thể phục hồi đã xảy ra.",
     "Ngoại lệ Exception", "⚠️", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Try-Catch", "/traɪ kætʃ/", "noun", "programming", "Lập trình",
     "Khối bắt ngoại lệ: cấu trúc lệnh kiểm soát lỗi giúp ứng dụng không bị sập khi gặp lỗi.",
     "Wrap risky network operations inside a try-catch block.", "Bọc các thao tác mạng có rủi ro bên trong khối try-catch.",
     "Khối bắt lỗi Try-Catch", "🛡️", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Stack Trace", "/stæk treɪs/", "noun", "programming", "Lập trình",
     "Dấu vết ngăn xếp: báo cáo danh sách các lệnh gọi hàm đang hoạt động khi xảy ra lỗi.",
     "Read the top lines of the stack trace to locate the file and line number.", "Đọc các dòng đầu tiên của dấu vết ngăn xếp để xác định tệp và số dòng gây lỗi.",
     "Dấu vết lỗi Stack Trace", "📜", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Thread", "/θred/", "noun", "programming", "Lập trình",
     "Luồng thực thi: đơn vị xử lý nhỏ nhất mà hệ điều hành có thể phân phối thời gian CPU.",
     "Spawn a background worker thread to process image resizing.", "Tạo một luồng chạy ngầm để xử lý việc thay đổi kích thước ảnh.",
     "Luồng xử lý Thread", "🧵", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Concurrency", "/kənˈkʌr.ən.si/", "noun", "programming", "Lập trình",
     "Đồng thời: khả năng xử lý nhiều tác vụ cùng một lúc trong các khoảng thời gian xen kẽ.",
     "Concurrency allows a web server to handle thousands of requests seamlessly.", "Tính đồng thời cho phép máy chủ web xử lý hàng ngàn yêu cầu mà không bị gián đoạn.",
     "Xử lý đồng thời", "🔀", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Parallelism", "/ˈpær.ə.lel.ɪ.zəm/", "noun", "programming", "Lập trình",
     "Song song: việc thực thi nhiều phép tính chính xác tại cùng một thời điểm trên nhiều lõi CPU.",
     "Parallelism requires multi-core hardware to execute simultaneously.", "Xử lý song song đòi hỏi phần cứng đa lõi để thực thi đồng thời.",
     "Xử lý song song", "⚡", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Synchronous", "/ˈsɪŋ.krə.nəs/", "adjective", "programming", "Lập trình",
     "Đồng bộ: mô hình thực thi trong đó mỗi câu lệnh phải đợi lệnh trước hoàn thành mới được chạy.",
     "Synchronous file I/O blocks the main thread until reading finishes.", "Thao tác vào ra tệp đồng bộ sẽ chặn luồng chính cho tới khi đọc xong.",
     "Xử lý đồng bộ", "⏱️", "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=600&auto=format&fit=crop&q=80"),

    ("Asynchronous", "/eɪˈsɪŋ.krə.nəs/", "adjective", "programming", "Lập trình",
     "Bất đồng bộ: mô hình cho phép chương trình tiếp tục chạy các lệnh khác trong khi chờ tác vụ tốn thời gian hoàn tất.",
     "Asynchronous messaging prevents user interfaces from freezing.", "Nhắn tin bất đồng bộ ngăn giao diện người dùng bị đơ cứng.",
     "Xử lý bất đồng bộ", "🔄", "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=600&auto=format&fit=crop&q=80"),

    ("Deadlock", "/ˈded.lɒk/", "noun", "programming", "Lập trình",
     "Bế tắc (Deadlock): trạng thái hai hoặc nhiều tiến trình vĩnh viễn bị chặn vì cùng chờ tài nguyên của nhau.",
     "Careful resource ordering prevents system deadlocks.", "Việc sắp xếp thứ tự tài nguyên cẩn thận giúp ngăn chặn tình trạng bế tắc hệ thống.",
     "Bế tắc Deadlock", "🛑", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Race Condition", "/reɪs kənˈdɪʃ.ən/", "noun", "programming", "Lập trình",
     "Điều kiện tranh chấp: lỗi xảy ra khi hai luồng truy cập và sửa đổi dữ liệu dùng chung cùng một lúc.",
     "A race condition caused account balances to decrement incorrectly.", "Điều kiện tranh chấp đã khiến số dư tài khoản bị trừ không chính xác.",
     "Tranh chấp dữ liệu", "🏁", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Mutex", "/ˈmjuː.teks/", "noun", "programming", "Lập trình",
     "Khóa loại trừ tương hỗ: cơ chế đồng bộ đảm bảo chỉ một luồng duy nhất được vào vùng tài nguyên găng tại một thời điểm.",
     "Acquire the mutex before modifying the shared counter.", "Chiếm giữ khóa mutex trước khi chỉnh sửa bộ đếm dùng chung.",
     "Khóa Mutex", "🔑", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Semaphore", "/ˈsem.ə.fɔːr/", "noun", "programming", "Lập trình",
     "Biến cờ hiệu: biến kiểm soát truy cập đồng thời của nhiều luồng tới một số lượng tài nguyên giới hạn.",
     "A counting semaphore limits database connections to twenty.", "Một semaphore đếm giới hạn số kết nối cơ sở dữ liệu ở mức hai mươi.",
     "Cờ hiệu Semaphore", "🚦", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Garbage Collection", "/ˈɡɑː.bɪdʒ kəˈlek.ʃən/", "noun", "programming", "Lập trình",
     "Thu gom rác tự động: cơ chế tự động tìm kiếm và thu hồi bộ nhớ của các đối tượng không còn được sử dụng.",
     "Java relies on automated garbage collection to manage heap memory.", "Java dựa vào việc thu gom rác tự động để quản lý bộ nhớ heap.",
     "Thu gom rác bộ nhớ", "♻️", "https://images.unsplash.com/photo-1532996122724-e3c354a0b15b?w=600&auto=format&fit=crop&q=80"),

    ("Memory Leak", "/ˈmem.ər.i liːk/", "noun", "programming", "Lập trình",
     "Rò rỉ bộ nhớ: hiện tượng chương trình không giải phóng bộ nhớ không còn dùng, khiến RAM cạn kiệt dần.",
     "Unremoved event listeners are a frequent source of memory leaks.", "Các trình lắng nghe sự kiện không được gỡ bỏ là nguồn gây rò rỉ bộ nhớ phổ biến.",
     "Rò rỉ bộ nhớ RAM", "💧", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Pointer", "/ˈpɔɪn.tər/", "noun", "programming", "Lập trình",
     "Con trỏ: biến lưu trữ địa chỉ ô nhớ trực tiếp của một biến hoặc đối tượng khác.",
     "Pointers allow direct hardware manipulation in C programs.", "Con trỏ cho phép can thiệp trực tiếp vào phần cứng trong các chương trình C.",
     "Con trỏ ô nhớ", "👉", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Reference", "/ˈref.ər.əns/", "noun", "programming", "Lập trình",
     "Tham chiếu: biệt danh hoặc chỉ mục an toàn trỏ tới vị trí của một đối tượng trong bộ nhớ.",
     "Objects in Python are passed by reference rather than copied.", "Các đối tượng trong Python được truyền bằng tham chiếu thay vì sao chép.",
     "Tham chiếu đối tượng", "🔗", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Buffer Overflow", "/ˈbʌf.ər ˈoʊ.vərˌfloʊ/", "noun", "programming", "Lập trình",
     "Tràn bộ đệm: lỗi bảo mật xảy ra khi dữ liệu ghi vượt quá dung lượng cấp phát của bộ nhớ đệm.",
     "Modern compilers insert canaries to detect buffer overflow attacks.", "Các trình biên dịch hiện đại gắn các canary để phát hiện tấn công tràn bộ đệm.",
     "Tràn bộ đệm nhớ", "💥", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Type Safety", "/taɪp ˈseɪf.ti/", "noun", "programming", "Lập trình",
     "An toàn kiểu: mức độ mà ngôn ngữ ngăn chặn việc thao tác dữ liệu sai kiểu gây lỗi lúc chạy.",
     "Type safety in Rust prevents memory crashes at compile time.", "An toàn kiểu trong Rust ngăn chặn sập bộ nhớ ngay tại thời điểm biên dịch.",
     "An toàn kiểu dữ liệu", "🛡️", "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    ("Static Typing", "/ˈstæt.ɪk ˈtaɪ.pɪŋ/", "noun", "programming", "Lập trình",
     "Định kiểu tĩnh: kiểu dữ liệu của biến được xác định và kiểm tra ngay từ thời điểm biên dịch mã.",
     "Static typing catches typo bugs before you push code to GitHub.", "Định kiểu tĩnh bắt các lỗi gõ sai trước khi bạn đẩy mã nguồn lên GitHub.",
     "Định kiểu tĩnh", "🔒", "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    ("Dynamic Typing", "/daɪˈnæm.ɪk ˈtaɪ.pɪŋ/", "noun", "programming", "Lập trình",
     "Định kiểu động: kiểu dữ liệu của biến được quyết định và kiểm tra lúc chương trình đang chạy.",
     "Dynamic typing allows fast prototyping in languages like JavaScript and Python.", "Định kiểu động cho phép tạo nguyên mẫu nhanh chóng trong JavaScript và Python.",
     "Định kiểu động", "🌊", "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    ("Type Inference", "/taɪp ˈɪn.fər.əns/", "noun", "programming", "Lập trình",
     "Suy luận kiểu: khả năng trình biên dịch tự suy ra kiểu dữ liệu mà lập trình viên không cần khai báo rõ.",
     "TypeScript automatically performs type inference from variable assignments.", "TypeScript tự động suy luận kiểu từ các phép gán biến ban đầu.",
     "Suy luận kiểu tự động", "💡", "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    ("Generics", "/dʒəˈner.ɪks/", "noun", "programming", "Lập trình",
     "Tham số kiểu tổng quát: cơ chế cho phép viết hàm hoặc lớp hoạt động được với nhiều kiểu dữ liệu khác nhau.",
     "Generics allow creating type-safe collections in Java and C#.", "Generics cho phép tạo các tập hợp an toàn kiểu trong Java và C#.",
     "Kiểu tổng quát Generics", "🧩", "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    ("Lambda Function", "/ˈlæm.də ˈfʌŋk.ʃən/", "noun", "programming", "Lập trình",
     "Hàm vô danh (Lambda): hàm ngắn gọn không có tên thường dùng làm đối số cho các hàm bậc cao.",
     "We passed a lambda function to filter even numbers from the list.", "Chúng tôi đã truyền một hàm lambda để lọc các số chẵn từ danh sách.",
     "Hàm ẩn danh Lambda", "λ", "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    ("Higher-Order Function", "/ˌhaɪ.ər ˈɔː.dər ˈfʌŋk.ʃən/", "noun", "programming", "Lập trình",
     "Hàm bậc cao: hàm nhận hàm khác làm đối số hoặc trả về một hàm làm kết quả đầu ra.",
     "Map, filter, and reduce are classic examples of higher-order functions.", "Map, filter và reduce là những ví dụ kinh điển về hàm bậc cao.",
     "Hàm bậc cao", "🪜", "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    ("Pure Function", "/pjʊər ˈfʌŋk.ʃən/", "noun", "programming", "Lập trình",
     "Hàm thuần khiết: hàm luôn trả về cùng kết quả với cùng đầu vào và không gây tác dụng phụ ra bên ngoài.",
     "Pure functions make code predictable and effortless to unit test.", "Các hàm thuần khiết giúp mã có thể dự đoán được và rất dễ viết kiểm thử đơn vị.",
     "Hàm thuần khiết", "✨", "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    ("Immutability", "/ɪˌmjuː.təˈbɪl.ə.ti/", "noun", "programming", "Lập trình",
     "Tính bất biến: thuộc tính của một đối tượng mà giá trị không thể bị thay đổi sau khi được tạo ra.",
     "Functional programming advocates immutability to prevent concurrency bugs.", "Lập trình hàm khuyến khích tính bất biến để ngăn chặn các lỗi đồng thời.",
     "Tính bất biến", "💎", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Side Effect", "/saɪd ɪˈfekt/", "noun", "programming", "Lập trình",
     "Tác dụng phụ: việc hàm làm thay đổi trạng thái bên ngoài phạm vi của nó như sửa biến toàn cục hoặc ghi đĩa.",
     "Avoid hidden side effects when computing numerical transformations.", "Tránh các tác dụng phụ tiềm ẩn khi tính toán các phép biến đổi số học.",
     "Tác dụng phụ Side Effect", "⚠️", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Currying", "/ˈkʌr.i.ɪŋ/", "noun", "programming", "Lập trình",
     "Kỹ thuật biến đổi một hàm nhận nhiều đối số thành chuỗi các hàm mỗi hàm chỉ nhận một đối số duy nhất.",
     "Currying enables partial application of configuration arguments.", "Currying cho phép áp dụng từng phần các đối số cấu hình.",
     "Kỹ thuật Currying", "🍛", "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    ("Module", "/ˈmɒdʒ.uːl/", "noun", "programming", "Lập trình",
     "Mô-đun: đơn vị mã nguồn độc lập đóng gói các tính năng liên quan để dễ quản lý và tái sử dụng.",
     "Export functions clearly from the authentication module.", "Xuất khẩu các hàm một cách rõ ràng từ mô-đun xác thực.",
     "Mô-đun mã nguồn", "📦", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Package", "/ˈpæk.ɪdʒ/", "noun", "programming", "Lập trình",
     "Gói phần mềm: tập hợp các mô-đun được đóng gói kèm siêu dữ liệu để phân phối qua kho quản lý gói.",
     "Install the security package using npm or yarn.", "Cài đặt gói bảo mật bằng trình quản lý gói npm hoặc yarn.",
     "Gói phần mềm Package", "🎁", "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?w=600&auto=format&fit=crop&q=80"),

    ("Library", "/ˈlaɪ.brər.i/", "noun", "programming", "Lập trình",
     "Thư viện phần mềm: tập hợp các hàm và lớp được viết sẵn mà lập trình viên chủ động gọi khi cần.",
     "Lodash is a popular utility library in modern JavaScript.", "Lodash là một thư viện tiện ích phổ biến trong lập trình JavaScript hiện đại.",
     "Thư viện mã nguồn", "📚", "https://images.unsplash.com/photo-1521587760476-6c12a4b040da?w=600&auto=format&fit=crop&q=80"),

    ("Framework", "/ˈfreɪm.wɜːk/", "noun", "programming", "Lập trình",
     "Bộ khung kiến trúc: khung cấu trúc phần mềm định sẵn quy tắc và luồng kiểm soát điều khiển ứng dụng.",
     "Django is a full-featured web framework built for Python developers.", "Django là một khung phát triển web đầy đủ tính năng dành cho lập trình viên Python.",
     "Bộ khung Framework", "🏗️", "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    ("SDK (Software Development Kit)", "/ˌes.diːˈkeɪ/", "noun", "programming", "Lập trình",
     "Bộ công cụ phát triển phần mềm: bộ công cụ, tài liệu, thư viện và ví dụ giúp xây dựng ứng dụng cho một nền tảng.",
     "Download the Android SDK to compile mobile application packages.", "Tải xuống bộ Android SDK để biên dịch các gói ứng dụng di động.",
     "Bộ công cụ phát triển SDK", "🧰", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("API (Application Programming Interface)", "/ˌeɪ.piːˈaɪ/", "noun", "programming", "Lập trình",
     "Giao diện lập trình ứng dụng: tập hợp các quy tắc định nghĩa cách các hệ thống phần mềm giao tiếp với nhau.",
     "The payment API responds with JSON data for each transaction.", "API thanh toán phản hồi dữ liệu định dạng JSON cho mỗi giao dịch.",
     "Giao diện API", "🔌", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Dependency", "/dɪˈpen.dən.si/", "noun", "programming", "Lập trình",
     "Phụ thuộc: một thư viện hoặc gói phần mềm bên ngoài mà ứng dụng của bạn cần để hoạt động.",
     "Audit third-party dependencies regularly for known vulnerabilities.", "Kiểm tra định kỳ các phần phụ thuộc của bên thứ ba để tìm lỗi bảo mật.",
     "Sự phụ thuộc Dependency", "🔗", "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?w=600&auto=format&fit=crop&q=80"),

    ("Dependency Injection (DI)", "/dɪˌpen.dən.si ɪnˈdʒek.ʃən/", "noun", "programming", "Lập trình",
     "Tiêm phụ thuộc: mẫu thiết kế trong đó một đối tượng nhận các đối tượng phụ thuộc từ bên ngoài thay vì tự khởi tạo.",
     "Dependency injection makes components loose-coupled and testable.", "Kỹ thuật tiêm phụ thuộc giúp các thành phần lỏng lẻo và dễ kiểm thử.",
     "Tiêm phụ thuộc DI", "💉", "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    ("Inversion of Control (IoC)", "/ɪnˈvɜː.ʒən əv kənˈtroʊl/", "noun", "programming", "Lập trình",
     "Đảo ngược điều khiển: nguyên lý phần mềm chuyển giao quyền điều khiển luồng thực thi cho khung cấu trúc hoặc thùng chứa.",
     "Spring container applies Inversion of Control to manage bean lifecycles.", "Bộ chứa Spring áp dụng Đảo ngược điều khiển để quản lý vòng đời của bean.",
     "Đảo ngược điều khiển IoC", "🔄", "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    ("Transpiler", "/trænzˈpaɪ.lər/", "noun", "programming", "Lập trình",
     "Trình biên dịch mã nguồn sang mã nguồn: dịch mã từ ngôn ngữ này sang ngôn ngữ khác ở cùng bậc trừu tượng.",
     "Babel is a famous JavaScript transpiler converting ES6 to ES5.", "Babel là một trình transpiler nổi tiếng chuyển đổi mã ES6 sang chuẩn ES5.",
     "Trình dịch mã Transpiler", "🔄", "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    ("Runtime Environment", "/ˈrʌn.taɪm ɪnˈvaɪ.rən.mənt/", "noun", "programming", "Lập trình",
     "Môi trường thực thi: hệ sinh thái phần mềm cung cấp các dịch vụ cần thiết để ứng dụng chạy.",
     "Node.js provides a JavaScript runtime environment outside the browser.", "Node.js cung cấp môi trường thực thi JavaScript bên ngoài trình duyệt web.",
     "Môi trường thực thi", "⚙️", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Design Pattern", "/dɪˈzaɪn ˈpæt.ən/", "noun", "programming", "Lập trình",
     "Mẫu thiết kế: giải pháp tổng quát có thể tái sử dụng cho các vấn đề thường gặp trong kiến trúc phần mềm.",
     "Design patterns provide proven vocabularies for engineering teams.", "Các mẫu thiết kế cung cấp ngôn ngữ chung đã được kiểm chứng cho các đội ngũ kỹ sư.",
     "Mẫu thiết kế phần mềm", "📐", "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    ("Singleton Pattern", "/ˈsɪŋ.ɡəl.tən ˈpæt.ən/", "noun", "programming", "Lập trình",
     "Mẫu thiết kế Singleton: đảm bảo một lớp chỉ có đúng một thể hiện duy nhất và cung cấp điểm truy cập toàn cục.",
     "Use Singleton for database connection pools and logging systems.", "Dùng mẫu Singleton cho nhóm kết nối cơ sở dữ liệu và hệ thống ghi nhật ký.",
     "Mẫu Singleton", "☝️", "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    ("Factory Pattern", "/ˈfæk.tər.i ˈpæt.ən/", "noun", "programming", "Lập trình",
     "Mẫu thiết kế Factory: định nghĩa giao diện tạo đối tượng nhưng để lớp con quyết định loại đối tượng nào được tạo.",
     "The notification factory returns email, SMS, or push sender objects.", "Factory thông báo sẽ trả về đối tượng gửi email, tin nhắn SMS hoặc thông báo đẩy.",
     "Mẫu Factory", "🏭", "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    ("Observer Pattern", "/əbˈzɜː.vər ˈpæt.ən/", "noun", "programming", "Lập trình",
     "Mẫu thiết kế Observer: mô hình xuất bản - đăng ký trong đó đối tượng tự động thông báo cho các người theo dõi khi thay đổi trạng thái.",
     "UI buttons use the observer pattern to notify registered event handlers.", "Các nút giao diện dùng mẫu quan sát observer để thông báo cho các bộ xử lý sự kiện đã đăng ký.",
     "Mẫu quan sát Observer", "👀", "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    ("Strategy Pattern", "/ˈstræt.ə.dʒi ˈpæt.ən/", "noun", "programming", "Lập trình",
     "Mẫu thiết kế Chiến lược: cho phép định nghĩa một tập hợp thuật toán và hoán đổi chúng linh hoạt lúc chạy.",
     "Payment processing uses Strategy pattern to switch between PayPal and Stripe.", "Xử lý thanh toán dùng mẫu Strategy để chuyển đổi linh hoạt giữa PayPal và Stripe.",
     "Mẫu chiến lược Strategy", "♟️", "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    ("Decorator Pattern", "/ˈdek.ə.reɪ.tər ˈpæt.ən/", "noun", "programming", "Lập trình",
     "Mẫu thiết kế Decorator: cho phép gắn thêm các hành vi mới vào đối tượng một cách linh hoạt mà không cần sửa lớp gốc.",
     "Python decorators wrap functions to add logging or authentication.", "Các decorator trong Python bao bọc hàm để bổ sung ghi log hoặc xác thực quyền.",
     "Mẫu trang trí Decorator", "🎀", "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    ("Adapter Pattern", "/əˈdæp.tər ˈpæt.ən/", "noun", "programming", "Lập trình",
     "Mẫu thiết kế Adapter: chuyển đổi giao diện của một lớp thành giao diện khác mà khách hàng mong đợi.",
     "The legacy API adapter translates XML responses into modern JSON.", "Bộ chuyển đổi API cũ dịch các phản hồi XML thành định dạng JSON hiện đại.",
     "Mẫu chuyển đổi Adapter", "🔌", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&auto=format&fit=crop&q=80"),

    ("Facade Pattern", "/fəˈsɑːd ˈpæt.ən/", "noun", "programming", "Lập trình",
     "Mẫu thiết kế Facade: cung cấp giao diện đơn giản hóa cấp cao cho một hệ thống con phức tạp bên dưới.",
     "A checkout facade conceals inventory, payment, and shipping subsystems.", "Giao diện mặt tiền thanh toán che giấu các hệ thống con tồn kho, thanh toán và vận chuyển.",
     "Mẫu mặt tiền Facade", "🏛️", "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    ("MVC (Model-View-Controller)", "/ˌem.viːˈsiː/", "noun", "programming", "Lập trình",
     "Mô hình MVC: kiến trúc phân chia ứng dụng thành ba phần: dữ liệu (Model), giao diện (View) và điều khiển (Controller).",
     "MVC separates business logic from presentation concerns.", "MVC tách biệt rõ ràng giữa logic nghiệp vụ và giao diện trình bày.",
     "Mô hình kiến trúc MVC", "📐", "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    ("MVVM (Model-View-ViewModel)", "/ˌem.viː.viːˈem/", "noun", "programming", "Lập trình",
     "Mô hình kiến trúc phần mềm tách biệt việc phát triển giao diện đồ họa thông qua cơ chế ràng buộc dữ liệu.",
     "Modern Android apps leverage MVVM with observable LiveData.", "Các ứng dụng Android hiện đại tận dụng mô hình MVVM với LiveData quan sát được.",
     "Mô hình MVVM", "📱", "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=600&auto=format&fit=crop&q=80"),

    ("Microservices", "/ˈmaɪ.krəʊˌsɜː.vɪ.sɪz/", "noun", "programming", "Lập trình",
     "Kiến trúc vi dịch vụ: thiết kế hệ thống thành một bộ các dịch vụ nhỏ, triển khai độc lập và giao tiếp qua mạng.",
     "Microservices allow individual teams to deploy changes independently.", "Kiến trúc vi dịch vụ cho phép các nhóm riêng biệt triển khai tính năng độc lập.",
     "Kiến trúc vi dịch vụ", "🌐", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Monolithic Architecture", "/ˌmɒn.əˈlɪθ.ɪk ˌɑː.kɪ.tek.tʃər/", "noun", "programming", "Lập trình",
     "Kiến trúc nguyên khối: hệ thống phần mềm mà mọi chức năng được đóng gói và triển khai thành một khối duy nhất.",
     "Startups often launch with a monolithic architecture for speed.", "Các công ty khởi nghiệp thường bắt đầu với kiến trúc nguyên khối để tối ưu tốc độ.",
     "Kiến trúc nguyên khối", "🏢", "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=600&auto=format&fit=crop&q=80"),

    ("Event-Driven Architecture", "/ɪˈvent ˌdrɪv.ən ˌɑː.kɪ.tek.tʃər/", "noun", "programming", "Lập trình",
     "Kiến trúc hướng sự kiện: mô hình phần mềm trong đó các hành vi được kích hoạt khi phát hiện các sự kiện hệ thống.",
     "Event-driven architecture decouples producers from consumers using Kafka.", "Kiến trúc hướng sự kiện tách biệt nơi sản xuất và nơi tiêu thụ thông qua Kafka.",
     "Kiến trúc hướng sự kiện", "⚡", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Domain-Driven Design (DDD)", "/dəʊˈmeɪn ˈdrɪv.ən dɪˈzaɪn/", "noun", "programming", "Lập trình",
     "Thiết kế hướng miền: phương pháp thiết kế phần mềm xoay quanh mô hình nghiệp vụ cốt lõi và thuật ngữ chuyên ngành.",
     "DDD establishes an ubiquitous language between engineers and domain experts.", "DDD thiết lập một ngôn ngữ thống nhất chung giữa kỹ sư và chuyên gia nghiệp vụ.",
     "Thiết kế hướng miền DDD", "🎯", "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    ("Clean Architecture", "/kliːn ˌɑː.kɪ.tek.tʃər/", "noun", "programming", "Lập trình",
     "Kiến trúc sạch: mô hình kiến trúc phân lớp đặt logic nghiệp vụ ở trung tâm, không bị phụ thuộc vào khung hay cơ sở dữ liệu.",
     "Clean Architecture isolates domain rules from database and UI frameworks.", "Kiến trúc sạch cô lập các quy tắc nghiệp vụ khỏi cơ sở dữ liệu và giao diện.",
     "Kiến trúc sạch Clean", "🧼", "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    ("Git Commit", "/ɡɪt kəˈmɪt/", "noun", "programming", "Lập trình",
     "Bản lưu trạng thái Git: ghi lại ảnh chụp các thay đổi mã nguồn vào lịch sử kho lưu trữ kèm thông điệp giải thích.",
     "Write atomic git commits with clear and concise descriptive messages.", "Hãy tạo các commit nhỏ gọn kèm thông điệp mô tả rõ ràng và súc tích.",
     "Lưu trạng thái Git Commit", "💾", "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?w=600&auto=format&fit=crop&q=80"),

    ("Git Branch", "/ɡɪt brɑːntʃ/", "noun", "programming", "Lập trình",
     "Nhánh Git: không gian làm việc song song cho phép phát triển tính năng mới mà không ảnh hưởng nhánh chính.",
     "Create a feature branch before developing the payment gateway integration.", "Tạo một nhánh tính năng mới trước khi phát triển tích hợp cổng thanh toán.",
     "Nhánh mã nguồn Git", "🌿", "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?w=600&auto=format&fit=crop&q=80"),

    ("Merge", "/mɜːdʒ/", "verb", "programming", "Lập trình",
     "Hợp nhất: kết hợp các thay đổi lịch sử từ một nhánh này vào một nhánh khác trong Git.",
     "Merge the pull request after all automated CI tests pass.", "Hợp nhất pull request sau khi tất cả các kiểm thử CI tự động đều vượt qua.",
     "Hợp nhất nhánh Git", "🔀", "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?w=600&auto=format&fit=crop&q=80"),

    ("Rebase", "/ˌriːˈbeɪs/", "verb", "programming", "Lập trình",
     "Đặt lại gốc: chuyển đổi hoặc áp dụng lại các commit của một nhánh lên trên đầu commit mới nhất của nhánh đích.",
     "Rebase your feature branch onto main to keep a clean, linear history.", "Rebase nhánh tính năng của bạn lên nhánh chính để giữ lịch sử commit thẳng thớm.",
     "Đặt lại gốc Git Rebase", "📏", "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?w=600&auto=format&fit=crop&q=80"),

    ("Pull Request (PR)", "/pʊl rɪˈkwest/", "noun", "programming", "Lập trình",
     "Yêu cầu hợp nhất: đề xuất đưa các thay đổi từ nhánh của bạn vào nhánh mã nguồn chung để đội ngũ xem xét.",
     "Reviewers requested changes on the pull request regarding error handling.", "Những người duyệt mã đã yêu cầu sửa lại pull request liên quan đến việc xử lý lỗi.",
     "Yêu cầu duyệt mã PR", "📬", "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?w=600&auto=format&fit=crop&q=80"),

    ("Code Review", "/kəʊd rɪˈvjuː/", "noun", "programming", "Lập trình",
     "Đánh giá mã nguồn: quá trình các kỹ sư đồng nghiệp kiểm tra mã của nhau để tìm lỗi và nâng cao chất lượng.",
     "Constructive code reviews foster mentorship and prevent system defects.", "Việc đánh giá mã nguồn mang tính xây dựng giúp bồi dưỡng kỹ năng và ngăn ngừa lỗi hệ thống.",
     "Đánh giá mã Code Review", "👀", "https://images.unsplash.com/photo-1542838132-92c53300491e?w=600&auto=format&fit=crop&q=80"),

    ("Boilerplate", "/ˈbɔɪ.lə.pleɪt/", "noun", "programming", "Lập trình",
     "Mã mẫu rập khuôn: đoạn mã tiêu chuẩn cần lặp lại ở nhiều nơi mà ít hoặc không có sự thay đổi.",
     "Lombok annotations reduce getter and setter boilerplate in Java codebases.", "Các chú thích Lombok giúp giảm bớt mã boilerplate getter và setter trong Java.",
     "Mã mẫu rập khuôn", "📋", "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&auto=format&fit=crop&q=80"),

    ("Deprecated", "/ˈdep.rə.keɪ.tɪd/", "adjective", "programming", "Lập trình",
     "Không còn khuyên dùng: tính năng hoặc hàm cũ vẫn tồn tại nhưng sắp bị xóa bỏ trong các phiên bản tới.",
     "The legacy encryption method is deprecated and should not be used in new projects.", "Phương thức mã hóa cũ đã bị ngừng khuyên dùng và không nên dùng cho dự án mới.",
     "Không còn khuyên dùng", "⚠️", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Legacy Code", "/ˈleɡ.ə.si kəʊd/", "noun", "programming", "Lập trình",
     "Mã nguồn cũ: mã kế thừa từ các phiên bản trước thường thiếu tài liệu và khó kiểm thử tự động.",
     "Refactoring legacy code requires thorough integration test coverage first.", "Tái cấu trúc mã nguồn cũ đòi hỏi phải có kiểm thử tích hợp bao phủ trước.",
     "Mã nguồn kế thừa", "🏛️", "https://images.unsplash.com/photo-1542838132-92c53300491e?w=600&auto=format&fit=crop&q=80"),

    ("Semantic Versioning (SemVer)", "/sɪˈmæn.tɪk ˈvɜː.ʃən.ɪŋ/", "noun", "programming", "Lập trình",
     "Quy tắc đánh số phiên bản ngữ nghĩa (MAJOR.MINOR.PATCH) phản ánh mức độ thay đổi của phần mềm.",
     "Incrementing MAJOR in SemVer communicates breaking API changes to clients.", "Việc tăng số MAJOR trong SemVer thông báo thay đổi phá vỡ tương thích tới client.",
     "Quy chuẩn phiên bản SemVer", "🏷️", "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?w=600&auto=format&fit=crop&q=80"),

    ("Monorepo", "/ˈmɒn.əʊˌriː.pəʊ/", "noun", "programming", "Lập trình",
     "Kho chứa đơn: chiến lược quản trị mã nguồn lưu trữ toàn bộ các dự án và dịch vụ của tổ chức trong một repo duy nhất.",
     "Google and Meta use a monorepo setup to simplify cross-project refactoring.", "Google và Meta sử dụng monorepo để đơn giản hóa việc tái cấu trúc mã giữa các dự án.",
     "Kho chứa đơn Monorepo", "📦", "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?w=600&auto=format&fit=crop&q=80"),

    ("Idempotence", "/aɪˈdem.pəʊ.təns/", "noun", "programming", "Lập trình",
     "Tính lũy đẳng: tính chất một thao tác khi thực hiện nhiều lần vẫn đem lại kết quả giống hệt thực hiện một lần.",
     "HTTP PUT and DELETE requests are designed to have idempotence.", "Các yêu cầu HTTP PUT và DELETE được thiết kế để có tính chất lũy đẳng.",
     "Tính lũy đẳng Idempotence", "🔄", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Linter", "/ˈlɪn.tər/", "noun", "programming", "Lập trình",
     "Trình phân tích tĩnh (Linter): công cụ tự động quét mã nguồn để gắn cờ các lỗi cú pháp, quy ước và bug tiềm ẩn.",
     "ESLint is a standard linter used by modern JavaScript engineering teams.", "ESLint là công cụ linter tiêu chuẩn được các nhóm kỹ sư JavaScript hiện đại sử dụng.",
     "Trình phân tích Linter", "🔍", "https://images.unsplash.com/photo-1542838132-92c53300491e?w=600&auto=format&fit=crop&q=80")
]

if __name__ == "__main__":
    print(f"Domain 1 terms count: {len(terms)}")
