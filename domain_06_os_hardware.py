# -*- coding: utf-8 -*-
"""Domain 6: Operating Systems & Computer Hardware (100 core terms)"""

terms = [
    ("Operating System (OS)", "/ˈɒp.ər.eɪ.tɪŋ ˈsɪs.təm/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Hệ điều hành: phần mềm hệ thống quản lý tài nguyên phần cứng và cung cấp các dịch vụ dùng chung cho các ứng dụng.",
     "Linux is the dominant operating system for high-performance cloud servers.", "Linux là hệ điều hành thống trị dành cho các máy chủ đám mây hiệu năng cao.",
     "Hệ điều hành OS", "💻", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Kernel", "/ˈkɜː.nəl/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Hạt nhân hệ điều hành: lõi cốt lõi của OS có toàn quyền kiểm soát mọi thứ trong hệ thống máy tính.",
     "The Linux kernel directly schedules CPU processes and allocates physical RAM.", "Hạt nhân Linux trực tiếp lập lịch tiến trình CPU và cấp phát bộ nhớ RAM vật lý.",
     "Hạt nhân Kernel", "🧠", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Monolithic Kernel", "/ˌmɒn.əˈlɪθ.ɪk ˈkɜː.nəl/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Hạt nhân nguyên khối: toàn bộ các dịch vụ hệ điều hành (trình điều khiển, hệ thống tệp, bộ nhớ) chạy chung trong không gian hạt nhân.",
     "Monolithic kernels offer high execution speed due to zero context switching overhead.", "Hạt nhân nguyên khối mang lại tốc độ thực thi cao do không tốn phụ phí chuyển ngữ cảnh.",
     "Hạt nhân nguyên khối", "🏛️", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Microkernel", "/ˈmaɪ.krəʊˌkɜː.nəl/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Vi hạt nhân: chỉ giữ các cơ chế tối thiểu trong kernel, các dịch vụ khác chạy ngoài không gian người dùng.",
     "Microkernels isolate drivers in user space to prevent driver bugs from crashing the OS.", "Vi hạt nhân cô lập trình điều khiển trong không gian người dùng để ngăn lỗi làm sập OS.",
     "Vi hạt nhân Microkernel", "🔬", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("User Space", "/ˈjuː.zər speɪs/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Không gian người dùng: vùng bộ nhớ bị giới hạn đặc quyền nơi các chương trình ứng dụng thông thường hoạt động.",
     "User space applications cannot execute privileged CPU instructions directly.", "Ứng dụng trong không gian người dùng không thể thực thi trực tiếp các chỉ lệnh CPU đặc quyền.",
     "Không gian người dùng", "👤", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Kernel Space", "/ˈkɜː.nəl speɪs/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Không gian hạt nhân: vùng bộ nhớ được bảo vệ cao nhất dành riêng cho việc thực thi nhân hệ điều hành.",
     "Device drivers execute within kernel space with full hardware device access.", "Trình điều khiển thiết bị thực thi bên trong không gian hạt nhân với toàn quyền truy cập phần cứng.",
     "Không gian hạt nhân", "👑", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("System Call (Syscall)", "/ˈsɪs.təm kɔːl/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Lời gọi hệ thống: giao diện có lập trình cho phép ứng dụng người dùng yêu cầu dịch vụ từ hạt nhân hệ điều hành.",
     "Functions like open() and read() trigger system calls into kernel space.", "Các hàm như open() và read() kích hoạt các lời gọi hệ thống vào không gian hạt nhân.",
     "Lời gọi hệ thống Syscall", "📞", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Process", "/ˈprəʊ.ses/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Tiến trình: một chương trình đang trong trạng thái được nạp vào bộ nhớ và thực thi bởi hệ điều hành.",
     "Each running process has its own isolated memory address space.", "Mỗi tiến trình đang chạy sở hữu một không gian địa chỉ bộ nhớ cô lập riêng biệt.",
     "Tiến trình Process", "⚙️", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Process ID (PID)", "/ˌpiː.aɪˈdiː/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Mã định danh tiến trình: số nguyên dương duy nhất được hệ điều hành gán để phân biệt mỗi tiến trình.",
     "Use 'kill -9 1234' where 1234 represents the PID of the stuck process.", "Dùng lệnh 'kill -9 1234' trong đó 1234 đại diện cho PID của tiến trình bị treo.",
     "Mã tiến trình PID", "🔢", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Thread", "/θred/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Luồng thực thi: đơn vị thực thi nhỏ nhất bên trong một tiến trình, chia sẻ chung không gian bộ nhớ của tiến trình đó.",
     "Multiple threads inside the same process can communicate directly via shared memory.", "Nhiều luồng trong cùng một tiến trình có thể trao đổi trực tiếp qua bộ nhớ chung.",
     "Luồng xử lý Thread", "🧵", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Multithreading", "/ˌmʌl.tiˈθred.ɪŋ/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Đa luồng: kỹ thuật cho phép một tiến trình thực thi đồng thời nhiều luồng công việc khác nhau.",
     "Multithreading keeps the user interface responsive during heavy file downloading.", "Đa luồng giúp giao diện người dùng luôn phản hồi mượt mà trong khi đang tải tệp nặng.",
     "Xử lý đa luồng", "🔀", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Multiprocessing", "/ˌmʌl.tiˈprəʊ.ses.ɪŋ/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Đa xử lý: việc sử dụng hai hay nhiều bộ xử lý CPU vật lý để đồng thời thực thi các tiến trình khác nhau.",
     "Multiprocessing overcomes Python's Global Interpreter Lock (GIL) limitations.", "Kỹ thuật đa xử lý khắc phục được giới hạn khóa GIL của ngôn ngữ Python.",
     "Đa xử lý Multiprocessing", "⚡", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("CPU Scheduling", "/ˌsiː.piːˈjuː ˈskedʒ.uː.lɪŋ/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Lập lịch CPU: thuật toán của hệ điều hành quyết định tiến trình nào được cấp phát CPU và trong bao lâu.",
     "The Linux Completely Fair Scheduler (CFS) provides optimal CPU scheduling.", "Bộ lập lịch hoàn toàn công bằng (CFS) của Linux mang lại khả năng lập lịch CPU tối ưu.",
     "Lập lịch CPU", "📅", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Context Switch", "/ˈkɒn.tekst swɪtʃ/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Chuyển đổi ngữ cảnh: quá trình lưu lại trạng thái tiến trình hiện tại và nạp trạng thái tiến trình khác để chạy.",
     "Excessive context switches cause performance overhead and waste CPU cycles.", "Chuyển đổi ngữ cảnh quá nhiều gây ra phụ phí hiệu năng và lãng phí chu kỳ CPU.",
     "Chuyển ngữ cảnh", "🔄", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Interrupt", "/ˈɪn.tə.rʌpt/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Ngắt: tín hiệu từ phần cứng hoặc phần mềm thông báo cho CPU tạm dừng việc hiện tại để xử lý sự kiện khẩn.",
     "A keyboard keystroke generates a hardware interrupt to process the key press.", "Thao tác gõ phím tạo ra một ngắt phần cứng để xử lý ký tự vừa nhấn.",
     "Tín hiệu ngắt Interrupt", "⚡", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Interrupt Handler (ISR)", "/ˈɪn.tə.rʌpt ˈhænd.lər/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Trình xử lý ngắt: đoạn mã chuyên biệt trong kernel tự động được triệu hồi khi xảy ra một tín hiệu ngắt xác định.",
     "The ISR reads incoming network bytes from the NIC buffer into main memory.", "Trình xử lý ngắt ISR đọc các byte mạng từ bộ đệm của card mạng vào bộ nhớ chính.",
     "Trình xử lý ngắt ISR", "🛠️", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("CPU (Central Processing Unit)", "/ˌsiː.piːˈjuː/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Bộ vi xử lý trung tâm: bộ não chính của máy tính thực thi các chỉ lệnh của chương trình và điều khiển mọi linh kiện.",
     "Modern desktop CPUs contain billions of nanoscale transistors.", "Các bộ vi xử lý máy tính hiện đại chứa hàng tỷ bóng bán dẫn kích thước nano.",
     "Bộ vi xử lý CPU", "💻", "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=600&auto=format&fit=crop&q=80"),

    ("Multi-Core Processor", "/ˌmʌl.ti kɔːr ˈprəʊ.ses.ər/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Bộ xử lý đa lõi: chip CPU tích hợp nhiều lõi tính toán độc lập trên cùng một khuôn bán dẫn.",
     "Multi-core processors allow parallel execution of video rendering tasks.", "Bộ xử lý đa lõi cho phép thực thi song song các tác vụ kết xuất video.",
     "Bộ xử lý đa lõi", "🔲", "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=600&auto=format&fit=crop&q=80"),

    ("Clock Speed", "/klɒk spiːd/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Tốc độ xung nhịp: tần số nhịp xung mà CPU thực hiện các chu kỳ chỉ lệnh trong mỗi giây (đo bằng GHz).",
     "A clock speed of 4.5 GHz means 4.5 billion clock cycles every second.", "Tốc độ xung nhịp 4.5 GHz có nghĩa là 4,5 tỷ chu kỳ xung nhịp diễn ra mỗi giây.",
     "Tốc độ xung nhịp", "⏱️", "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=600&auto=format&fit=crop&q=80"),

    ("Overclocking", "/ˈəʊ.və.klɒk.ɪŋ/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Ép xung: điều chỉnh xung nhịp phần cứng vượt quá thông số tiêu chuẩn của nhà sản xuất để tăng hiệu năng.",
     "Overclocking increases gaming frame rates but demands powerful cooling solutions.", "Ép xung tăng tốc độ khung hình khi chơi game nhưng đòi hỏi giải pháp tản nhiệt mạnh mẽ.",
     "Ép xung Overclocking", "🔥", "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=600&auto=format&fit=crop&q=80"),

    ("ALU (Arithmetic Logic Unit)", "/ˌeɪ.elˈjuː/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Đơn vị số học và logic: mạch điện tử bên trong CPU chịu trách nhiệm thực hiện các phép toán cộng trừ và logic AND, OR.",
     "The ALU performs fundamental binary arithmetic calculations.", "ALU thực hiện các phép tính toán số học nhị phân cơ bản.",
     "Khối tính toán ALU", "🧮", "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=600&auto=format&fit=crop&q=80"),

    ("CPU Register", "/ˌsiː.piːˈjuː ˈredʒ.ɪ.stər/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Thanh ghi CPU: ô nhớ tốc độ cực nhanh tích hợp trực tiếp bên trong nhân CPU để lưu dữ liệu tức thì.",
     "Registers provide near-instantaneous single-cycle data access for instructions.", "Thanh ghi cung cấp khả năng truy xuất dữ liệu gần như tức thì trong một chu kỳ xung nhịp.",
     "Thanh ghi CPU", "⚡", "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=600&auto=format&fit=crop&q=80"),

    ("Program Counter (PC)", "/ˈprəʊ.ɡræm ˈkaʊn.tər/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Bộ đếm chương trình: thanh ghi đặc biệt lưu địa chỉ ô nhớ của chỉ lệnh tiếp theo chuẩn bị được nạp vào CPU.",
     "Branch instructions alter the Program Counter to jump to a different code path.", "Lệnh rẽ nhánh làm thay đổi bộ đếm chương trình để nhảy tới đường dẫn mã khác.",
     "Bộ đếm chương trình PC", "📍", "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=600&auto=format&fit=crop&q=80"),

    ("CPU Cache", "/ˌsiː.piːˈjuː kæʃ/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Bộ nhớ đệm CPU: bộ nhớ SRAM siêu nhanh nằm gần nhân xử lý giúp giảm thiểu thời gian chờ đọc dữ liệu từ RAM.",
     "CPU caches bridge the vast speed discrepancy between processors and DRAM.", "Bộ nhớ đệm CPU thu hẹp độ chênh lệch tốc độ khổng lồ giữa vi xử lý và bộ nhớ RAM.",
     "Bộ đệm CPU Cache", "⚡", "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=600&auto=format&fit=crop&q=80"),

    ("L1 Cache", "/ˌelˈwʌn kæʃ/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Bộ đệm L1: bộ nhớ đệm cấp cao nhất, nằm ngay trong từng lõi CPU, dung lượng nhỏ nhưng có độ trễ thấp nhất.",
     "L1 cache latency is measured in only a few CPU clock cycles.", "Độ trễ của bộ nhớ đệm L1 chỉ được tính bằng vài chu kỳ xung nhịp CPU.",
     "Bộ nhớ đệm L1", "🥇", "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=600&auto=format&fit=crop&q=80"),

    ("L2 Cache", "/ˌelˈtuː kæʃ/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Bộ đệm L2: bộ nhớ đệm cấp hai, dung lượng lớn hơn L1 nhưng chậm hơn một chút, thường gắn riêng cho từng lõi.",
     "L2 cache stores instructions and data missed by the smaller L1 cache.", "Bộ nhớ đệm L2 lưu trữ các chỉ lệnh và dữ liệu bị trượt khỏi bộ đệm L1 nhỏ hơn.",
     "Bộ nhớ đệm L2", "🥈", "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=600&auto=format&fit=crop&q=80"),

    ("L3 Cache", "/ˌelˈθriː kæʃ/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Bộ đệm L3: bộ nhớ đệm cấp ba lớn nhất (hàng chục đến hàng trăm MB) được chia sẻ chung giữa tất cả các lõi CPU.",
     "Modern gaming CPUs feature massive 3D V-Cache L3 pools to prevent memory stalls.", "CPU chơi game hiện đại trang bị cụm L3 3D V-Cache cực lớn để ngăn nghẽn bộ nhớ.",
     "Bộ nhớ đệm L3", "🥉", "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=600&auto=format&fit=crop&q=80"),

    ("Cache Hit", "/kæʃ hɪt/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Đạt bộ đệm: trạng thái dữ liệu CPU yêu cầu có sẵn ngay trong bộ nhớ đệm cache, giúp truy xuất tức thì.",
     "High cache hit rates keep CPU cores fed with instructions without stalling.", "Tỷ lệ đạt bộ nhớ đệm cao giúp các lõi CPU luôn được cung cấp dữ liệu mà không bị treo chờ.",
     "Đạt bộ đệm Cache Hit", "🎯", "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=600&auto=format&fit=crop&q=80"),

    ("Cache Miss", "/kæʃ mɪs/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Trượt bộ đệm: trạng thái dữ liệu yêu cầu không có trong cache, buộc CPU phải mất thời gian nạp từ RAM chính.",
     "A cache miss forces the CPU to wait hundreds of cycles for main DRAM retrieval.", "Hiện tượng trượt bộ đệm buộc CPU phải đợi hàng trăm chu kỳ để nạp từ DRAM chính.",
     "Trượt bộ đệm Cache Miss", "❌", "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=600&auto=format&fit=crop&q=80"),

    ("Cache Coherency", "/kæʃ kəʊˈhɪə.rən.si/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Tính nhất quán bộ đệm: giao thức đảm bảo mọi bản sao dữ liệu trong các cache riêng của các lõi đều đồng nhất.",
     "MESI protocol enforces cache coherency across multi-core processors.", "Giao thức MESI thực thi tính nhất quán bộ nhớ đệm trên các bộ xử lý đa lõi.",
     "Tính nhất quán bộ đệm", "🔄", "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=600&auto=format&fit=crop&q=80"),

    ("RAM (Random Access Memory)", "/ræm/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Bộ nhớ truy cập ngẫu nhiên: bộ nhớ chính khả biến tốc độ cao lưu trữ dữ liệu và chương trình đang chạy.",
     "DDR5 RAM delivers extreme bandwidth for memory-intensive machine learning workloads.", "RAM DDR5 mang lại băng thông cực lớn cho các tác vụ học máy tiêu tốn nhiều bộ nhớ.",
     "Bộ nhớ chính RAM", "💾", "https://images.unsplash.com/photo-1544652478-6653e09f18a2?w=600&auto=format&fit=crop&q=80"),

    ("ROM (Read-Only Memory)", "/rɒm/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Bộ nhớ chỉ đọc: bộ nhớ bất biến lưu trữ vĩnh viễn các chỉ dẫn khởi động cơ bản của hệ thống máy tính.",
     "Motherboard firmware is stored securely inside a flash ROM chip.", "Firmware của bo mạch chủ được lưu trữ an toàn bên trong chip flash ROM.",
     "Bộ nhớ chỉ đọc ROM", "🔒", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Virtual Memory", "/ˈvɜː.tʃu.əl ˈmem.ər.i/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Bộ nhớ ảo: kỹ thuật quản lý bộ nhớ tạo ảo giác về một không gian RAM liên tục lớn hơn RAM vật lý thực tế.",
     "Virtual memory isolates application spaces and prevents memory starvation.", "Bộ nhớ ảo cô lập các không gian ứng dụng và ngăn ngừa cạn kiệt bộ nhớ.",
     "Bộ nhớ ảo Virtual Memory", "🌐", "https://images.unsplash.com/photo-1544652478-6653e09f18a2?w=600&auto=format&fit=crop&q=80"),

    ("Paging", "/ˈpeɪ.dʒɪŋ/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Phân trang bộ nhớ: cơ chế chia bộ nhớ ảo và bộ nhớ vật lý thành các khối kích thước cố định gọi là trang (page).",
     "Standard memory paging uses 4KB block allocations across virtual addresses.", "Cơ chế phân trang tiêu chuẩn cấp phát các khối kích thước 4KB qua các địa chỉ ảo.",
     "Phân trang bộ nhớ", "📄", "https://images.unsplash.com/photo-1544652478-6653e09f18a2?w=600&auto=format&fit=crop&q=80"),

    ("Page Table", "/peɪdʒ ˈteɪ.bəl/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Bảng trang: cấu trúc dữ liệu do hệ điều hành duy trì để ánh xạ địa chỉ bộ nhớ ảo sang địa chỉ bộ nhớ vật lý.",
     "The MMU walks the page table to resolve physical RAM addresses.", "Khối MMU duyệt qua bảng trang để giải quyết địa chỉ RAM vật lý thực tế.",
     "Bảng trang Page Table", "📋", "https://images.unsplash.com/photo-1544652478-6653e09f18a2?w=600&auto=format&fit=crop&q=80"),

    ("Page Fault", "/peɪdʒ fɒlt/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Lỗi trang: ngoại lệ xảy ra khi một chương trình truy cập vào trang bộ nhớ chưa được nạp vào RAM vật lý.",
     "Major page faults incur slow disk reads to bring swapped pages back to RAM.", "Lỗi trang nghiêm trọng buộc phải đọc ổ đĩa chậm để nạp lại các trang bị hoán đổi về RAM.",
     "Lỗi trang Page Fault", "⚠️", "https://images.unsplash.com/photo-1544652478-6653e09f18a2?w=600&auto=format&fit=crop&q=80"),

    ("TLB (Translation Lookaside Buffer)", "/ˌtiː.elˈbiː/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Bộ đệm dịch địa chỉ: bộ nhớ đệm phần cứng lưu các phép dịch địa chỉ gần nhất từ ảo sang vật lý.",
     "A TLB hit bypasses expensive multi-level page table walks.", "Đạt bộ đệm TLB giúp bỏ qua việc duyệt bảng trang nhiều cấp tốn kém.",
     "Bộ đệm dịch địa chỉ TLB", "⚡", "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=600&auto=format&fit=crop&q=80"),

    ("Swapping", "/ˈswɒp.ɪŋ/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Hoán đổi bộ nhớ: chuyển các trang dữ liệu không dùng trong RAM ra vùng không gian swap trên ổ cứng.",
     "Excessive swapping slows down system responsiveness into unusable thrashing.", "Hoán đổi bộ nhớ quá mức làm chậm phản hồi hệ thống dẫn tới tình trạng giật cục.",
     "Hoán đổi đĩa Swapping", "🔄", "https://images.unsplash.com/photo-1544652478-6653e09f18a2?w=600&auto=format&fit=crop&q=80"),

    ("MMU (Memory Management Unit)", "/ˌem.emˈjuː/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Khối quản lý bộ nhớ: thành phần phần cứng máy tính xử lý mọi thao tác dịch địa chỉ và bảo vệ bộ nhớ.",
     "The MMU raises hardware segmentation faults when programs access illegal addresses.", "MMU phát sinh lỗi phân đoạn phần cứng khi chương trình truy cập địa chỉ trái phép.",
     "Khối quản lý bộ nhớ MMU", "⚙️", "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=600&auto=format&fit=crop&q=80"),

    ("Disk Fragmentation", "/dɪsk ˌfræɡ.mənˈteɪ.ʃən/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Phân mảnh đĩa: tình trạng các mảnh của cùng một tệp nằm rải rác không liên tục trên đĩa cơ học.",
     "Disk defragmentation reassembles scattered files on traditional magnetic hard drives.", "Chống phân mảnh đĩa gom lại các tệp nằm rải rác trên ổ đĩa từ truyền thống.",
     "Phân mảnh đĩa", "🧩", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("SSD (Solid-State Drive)", "/ˌes.esˈdiː/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Ổ lưu trữ thể rắn: thiết bị lưu trữ dùng bộ nhớ flash không cơ học, đem lại tốc độ đọc ghi vượt trội so với HDD.",
     "Upgrading a laptop to an SSD dramatically cuts boot times from minutes to seconds.", "Nâng cấp laptop lên ổ SSD giúp rút ngắn thời gian khởi động từ vài phút xuống vài giây.",
     "Ổ cứng thể rắn SSD", "⚡", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("HDD (Hard Disk Drive)", "/ˌeɪtʃ.diːˈdiː/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Ổ đĩa cứng cơ học: thiết bị lưu trữ dữ liệu từ tính truyền thống dùng các đĩa quay và đầu đọc cơ học.",
     "Mechanical HDDs provide economical massive storage capacity for cold data backups.", "Ổ cứng HDD cơ học mang lại dung lượng lưu trữ khổng lồ tiết kiệm cho sao lưu lạnh.",
     "Ổ đĩa cứng HDD", "💽", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("NVMe (Non-Volatile Memory Express)", "/ˌen.viː.emˈiː/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Giao thức NVMe: chuẩn giao tiếp tốc độ cực cao kết nối trực tiếp ổ SSD với khe cắm PCIe của bo mạch chủ.",
     "NVMe drives achieve sequential read throughput exceeding 7000 MB per second.", "Ổ đĩa NVMe đạt thông lượng đọc tuần tự vượt mốc 7000 MB mỗi giây.",
     "Chuẩn lưu trữ NVMe", "🚀", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("SATA", "/ˈsɑː.tə/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Chuẩn giao tiếp SATA: chuẩn kết nối cáp dữ liệu thông dụng cho các ổ đĩa quang và ổ cứng với tốc độ tối đa 6 Gbps.",
     "SATA III interfaces are capped at a maximum throughput of 600 MB/s.", "Giao diện SATA III bị giới hạn ở mức thông lượng tối đa khoảng 600 MB/s.",
     "Chuẩn kết nối SATA", "🔌", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("PCIe (PCI Express)", "/ˌpiː.siː.aɪ ɪkˈspres/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Bus mở rộng PCIe: giao diện bus mở rộng tốc độ cao trên bo mạch chủ dùng cắm card đồ họa và ổ NVMe.",
     "Graphics cards plug into high-speed PCIe x16 slots for maximum bandwidth.", "Card màn hình cắm vào các khe PCIe x16 tốc độ cao để đạt băng thông tối đa.",
     "Giao diện mở rộng PCIe", "💳", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Motherboard", "/ˈmʌð.ə.bɔːd/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Bo mạch chủ: bảng mạch in chính liên kết CPU, RAM, ổ lưu trữ và các thiết bị ngoại vi vào hệ thống.",
     "The motherboard houses the CPU socket, RAM slots, and power regulators.", "Bo mạch chủ chứa đế cắm CPU, khe cắm RAM và các mạch cấp nguồn.",
     "Bo mạch chủ Motherboard", "🎛️", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Chipset", "/ˈtʃɪp.set/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Bộ mạch tích hợp Chipset: mạch điều khiển trung tâm trên bo mạch chủ quản lý việc truyền dữ liệu giữa CPU và ngoại vi.",
     "The motherboard chipset dictates PCIe lane allocations and USB port counts.", "Chipset bo mạch chủ quyết định số đường PCIe và số lượng cổng USB hỗ trợ.",
     "Bộ vi mạch Chipset", "⚙️", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("BIOS", "/ˈbaɪ.ɒs/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Hệ thống nhập xuất cơ bản BIOS: phần sụn cổ điển thực hiện kiểm tra phần cứng POST và khởi động hệ điều hành.",
     "Users press Del or F2 during power-on to configure BIOS hardware settings.", "Người dùng nhấn phím Del hoặc F2 lúc bật máy để cấu hình cài đặt phần cứng trong BIOS.",
     "Phần sụn BIOS cũ", "📟", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("UEFI", "/ˌjuː.iː.efˈaɪ/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Giao diện phần sụn mở rộng hợp nhất UEFI: chuẩn thay thế hiện đại cho BIOS với giao diện đồ họa và Secure Boot.",
     "UEFI supports partition tables beyond 2 Terabytes via the GPT standard.", "UEFI hỗ trợ bảng phân vùng lớn hơn 2 Terabyte thông qua tiêu chuẩn GPT.",
     "Chuẩn phần sụn UEFI", "🖥️", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Bootloader", "/ˈbuːtˌləʊ.dər/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Trình nạp khởi động: chương trình nhỏ nạp ảnh nhân hệ điều hành từ ổ cứng vào bộ nhớ RAM khi mở máy tính.",
     "The bootloader initializes essential registers before transferring control to the kernel.", "Bootloader khởi tạo các thanh ghi thiết yếu trước khi bàn giao quyền kiểm soát cho kernel.",
     "Trình khởi động Bootloader", "🚀", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("GRUB", "/ɡrʌb/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Trình khởi động GRUB: trình nạp khởi động chuẩn trên hệ điều hành Linux cho phép chọn phiên bản hạt nhân hoặc OS khác.",
     "Edit /etc/default/grub to change boot timeout and kernel parameters.", "Chỉnh sửa tệp /etc/default/grub để thay đổi thời gian chờ khởi động và tham số kernel.",
     "Trình khởi động Linux GRUB", "🐧", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Starvation", "/stɑːˈveɪ.ʃən/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Hiện tượng đói tài nguyên: tiến trình vĩnh viễn không được cấp phát CPU hay tài nguyên do các tiến trình ưu tiên cao chiếm giữ liên tục.",
     "Aging techniques gradually increase process priority to eliminate starvation.", "Kỹ thuật lão hóa tăng dần độ ưu tiên của tiến trình để loại bỏ tình trạng đói tài nguyên.",
     "Đói tài nguyên Starvation", "⌛", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Critical Section", "/ˈkrɪt.ɪ.kəl ˈsek.ʃən/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Vùng găng: đoạn mã truy cập vào tài nguyên dùng chung mà tại một thời điểm chỉ cho phép một luồng duy nhất thực thi.",
     "Mutex locks protect critical sections against concurrent thread corruption.", "Khóa mutex bảo vệ vùng găng khỏi việc bị làm hỏng dữ liệu khi nhiều luồng cùng chạy.",
     "Vùng găng Critical Section", "🛑", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("File System", "/faɪl ˈsɪs.təm/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Hệ thống tệp: phương pháp và cấu trúc dữ liệu mà hệ điều hành dùng để kiểm soát việc lưu trữ và truy xuất tệp trên đĩa.",
     "Different file systems optimize for speed, journaling, or snapshot capability.", "Các hệ thống tệp khác nhau tối ưu cho tốc độ, ghi nhật ký hoặc khả năng chụp nhanh snapshot.",
     "Hệ thống tệp File System", "📂", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Ext4", "/ˌekstˈfɔːr/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Hệ thống tệp Ext4: hệ thống tệp ghi nhật ký tiêu chuẩn và phổ biến nhất trên hầu hết các bản phân phối Linux.",
     "Ext4 delivers excellent stability and supports files up to 16 Terabytes in size.", "Ext4 mang lại độ ổn định tuyệt vời và hỗ trợ kích thước tệp đơn lẻ lên tới 16 Terabyte.",
     "Hệ thống tệp Linux Ext4", "🐧", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("NTFS", "/ˌen.tiː.efˈes/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Hệ thống tệp NTFS: hệ thống tệp tiêu chuẩn mặc định của hệ điều hành Microsoft Windows có hỗ trợ phân quyền và nén.",
     "Windows installs onto an NTFS partition by default for file-level permissions.", "Windows cài đặt mặc định trên phân vùng NTFS để hỗ trợ phân quyền cấp độ tệp tin.",
     "Hệ thống tệp Windows NTFS", "🪟", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("APFS", "/ˌeɪ.piː.efˈes/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Hệ thống tệp Apple APFS: hệ thống tệp hiện đại tối ưu cho ổ SSD và bộ nhớ flash dùng trên macOS và iOS.",
     "APFS enables instantaneous file cloning and robust native disk encryption.", "APFS cho phép nhân bản tệp tức thì và tích hợp mã hóa đĩa gốc mạnh mẽ.",
     "Hệ thống tệp Apple APFS", "🍎", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("ZFS", "/ˌzed.efˈes/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Hệ thống tệp ZFS: hệ thống tệp kết hợp quản lý ổ đĩa dung lượng khổng lồ với khả năng tự sửa lỗi dữ liệu (self-healing).",
     "Storage servers use ZFS RAIDZ pools to protect petabytes of media archives.", "Máy chủ lưu trữ dùng cụm ZFS RAIDZ để bảo vệ hàng petabyte dữ liệu truyền thông.",
     "Hệ thống tệp tự sửa ZFS", "🛡️", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("Inode", "/ˈaɪ.nəʊd/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Nút chỉ mục Inode: cấu trúc dữ liệu trên Unix/Linux lưu siêu dữ liệu (metadata) của tệp như kích thước, quyền, ngày tạo.",
     "A disk running out of free inodes cannot create new files even with empty space.", "Ổ đĩa hết inode trống sẽ không thể tạo tệp mới ngay cả khi còn dung lượng đĩa.",
     "Chỉ mục tệp Inode", "📋", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("File Descriptor", "/faɪl dɪˈskrɪp.tər/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Mô tả tệp: số nguyên không âm trừu tượng đại diện cho một tệp hoặc socket mạng đang mở trong Unix.",
     "Standard streams stdin, stdout, and stderr map to file descriptors 0, 1, and 2.", "Các luồng chuẩn stdin, stdout và stderr tương ứng với các mô tả tệp số 0, 1 và 2.",
     "Bộ mô tả tệp", "🔢", "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&auto=format&fit=crop&q=80"),

    ("POSIX", "/ˈpɒz.ɪks/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Chuẩn tương thích POSIX: bộ tiêu chuẩn quốc tế IEEE đảm bảo tính tương thích phần mềm giữa các hệ điều hành họ Unix.",
     "Writing POSIX-compliant C code ensures seamless portability across Linux and macOS.", "Viết mã C tuân thủ chuẩn POSIX đảm bảo chạy được mượt mà trên cả Linux và macOS.",
     "Chuẩn tương thích POSIX", "📜", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Shell", "/ʃel/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Vỏ dòng lệnh Shell: chương trình thông dịch lệnh cho phép người dùng giao tiếp và ra lệnh cho hệ điều hành.",
     "The shell accepts commands typed into the terminal and launches corresponding binaries.", "Shell nhận các lệnh gõ vào cửa sổ terminal và khởi chạy các tệp nhị phân tương ứng.",
     "Vỏ dòng lệnh Shell", "🐚", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Bash", "/bæʃ/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Trình thông dịch Bash: vỏ dòng lệnh và ngôn ngữ kịch bản mặc định kinh điển trên hầu hết các hệ thống Linux.",
     "Write automated system administration scripts in Bash.", "Viết các kịch bản tự động hóa quản trị hệ thống bằng ngôn ngữ kịch bản Bash.",
     "Trình dòng lệnh Bash", "💻", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Zsh", "/ˌzed.esˈeɪtʃ/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Trình thông dịch Zsh: phiên bản vỏ lệnh nâng cao hỗ trợ tự động hoàn thành thông minh và tùy biến giao diện mạnh mẽ.",
     "macOS uses Zsh as its default interactive shell since macOS Catalina.", "macOS sử dụng Zsh làm vỏ dòng lệnh tương tác mặc định kể từ bản macOS Catalina.",
     "Trình dòng lệnh Zsh", "⚡", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Terminal", "/ˈtɜː.mɪ.nəl/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Cửa sổ dòng lệnh Terminal: chương trình giả lập môi trường văn bản cho phép tương tác trực tiếp với shell.",
     "Developers spend much of their day running git and docker commands inside the terminal.", "Lập trình viên dành nhiều thời gian chạy lệnh git và docker bên trong cửa sổ terminal.",
     "Cửa sổ lệnh Terminal", "🖥️", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Command Line Interface (CLI)", "/kəˌmɑːnd laɪn ˈɪn.tə.feɪs/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Giao diện dòng lệnh CLI: cơ chế tương tác với phần mềm bằng các dòng văn bản lệnh thay vì bấm nút đồ họa.",
     "The AWS CLI lets administrators provision cloud infrastructure via terminal commands.", "AWS CLI cho phép người quản trị khởi tạo hạ tầng đám mây qua lệnh dòng lệnh.",
     "Giao diện dòng lệnh CLI", "⌨️", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80"),

    ("Graphical User Interface (GUI)", "/ˌdʒiː.juːˈaɪ/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Giao diện người dùng đồ họa: giao diện tương tác trực quan qua các cửa sổ, biểu tượng icon, chuột và nút bấm.",
     "GUIs provide an intuitive visual visual experience for non-technical users.", "Giao diện GUI mang lại trải nghiệm trực quan thân thiện cho người dùng thông thường.",
     "Giao diện đồ họa GUI", "🖼️", "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    ("Environment Variable", "/ɪnˈvaɪ.rən.mənt ˈveə.ri.ə.bəl/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Biến môi trường: giá trị động được thiết lập trong hệ điều hành ảnh hưởng tới hành vi của các tiến trình đang chạy.",
     "Store database secrets in the DATABASE_URL environment variable rather than hardcoding them.", "Lưu mật mã CSDL trong biến môi trường DATABASE_URL thay vì gắn cứng vào mã nguồn.",
     "Biến môi trường", "🌐", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Daemon", "/ˈdiː.mən/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Tiến trình nền ẩn: tiến trình chạy ngầm liên tục dưới nền của hệ điều hành mà không cần giao diện người dùng trực tiếp.",
     "Web server daemons listen continuously in the background for incoming client connections.", "Các tiến trình nền máy chủ web lắng nghe liên tục dưới nền để đón kết nối máy khách.",
     "Tiến trình chạy ngầm Daemon", "👻", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("System Service", "/ˈsɪs.təm ˈsɜː.vɪs/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Dịch vụ hệ thống: chương trình cung cấp chức năng quan trọng cho OS như mạng, in ấn, tường lửa hoặc CSDL.",
     "Restart the SSH system service using the command 'systemctl restart sshd'.", "Khởi động lại dịch vụ hệ thống SSH bằng lệnh 'systemctl restart sshd'.",
     "Dịch vụ hệ thống Service", "⚙️", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Systemd", "/ˈsɪs.təm.diː/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Hệ thống quản lý khởi động Systemd: bộ quản lý dịch vụ và khởi tạo tiến trình (PID 1) chuẩn trên hầu hết Linux hiện đại.",
     "Systemd unit files configure automatic restarts for crashed application services.", "Tệp cấu hình systemd thiết lập việc tự động khởi động lại khi dịch vụ ứng dụng bị sập.",
     "Trình quản lý Systemd", "🎛️", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Cron Job", "/krɒn dʒɒb/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Tác vụ định kỳ Cron: tiện ích lập lịch chạy các lệnh hoặc kịch bản tự động theo khoảng thời gian cố định trên Unix.",
     "A nightly cron job executes database backups every night at 2:00 AM.", "Một tác vụ cron chạy định kỳ sao lưu cơ sở dữ liệu vào 2 giờ sáng mỗi đêm.",
     "Tác vụ định kỳ Cron", "⏰", "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=600&auto=format&fit=crop&q=80"),

    ("Pipe (Unix Pipe)", "/paɪp/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Đường ống lệnh (Pipe |): kỹ thuật chuyển trực tiếp đầu ra (stdout) của lệnh trước làm đầu vào (stdin) cho lệnh sau.",
     "Chaining commands with a pipe like 'cat log.txt | grep error' filters output cleanly.", "Ghép nối lệnh bằng đường ống như 'cat log.txt | grep error' lọc dữ liệu rất gọn.",
     "Đường ống lệnh Pipe", "🚰", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Standard Input (stdin)", "/ˈstæn.dəd ˈɪn.pʊt/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Luồng đầu vào chuẩn: kênh dữ liệu mặc định mà chương trình nhận văn bản đầu vào (thường từ bàn phím).",
     "The command reads data from standard input when no filename argument is specified.", "Câu lệnh đọc dữ liệu từ luồng đầu vào chuẩn khi không có tham số tên tệp được chỉ định.",
     "Đầu vào chuẩn stdin", "📥", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Standard Output (stdout)", "/ˈstæn.dəd ˈaʊt.pʊt/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Luồng đầu ra chuẩn: kênh dữ liệu mặc định nơi chương trình ghi kết quả văn bản (thường hiển thị ra màn hình terminal).",
     "Redirect standard output into a text file using the '>' redirection operator.", "Chuyển hướng đầu ra chuẩn vào tệp văn bản bằng toán tử '>'.",
     "Đầu ra chuẩn stdout", "📤", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Standard Error (stderr)", "/ˈstæn.dəd ˈer.ər/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Luồng lỗi chuẩn: kênh dữ liệu riêng biệt dành riêng cho việc xuất thông báo lỗi hoặc chẩn đoán sự cố.",
     "Separate stderr from stdout to keep error logs isolated from standard application outputs.", "Tách stderr khỏi stdout để giữ nhật ký lỗi riêng biệt với kết quả thông thường của ứng dụng.",
     "Đầu ra lỗi chuẩn stderr", "⚠️", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Signal", "/ˈsɪɡ.nəl/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Tín hiệu hệ điều hành: thông báo bất đồng bộ gửi tới tiến trình để báo hiệu một sự kiện vừa xảy ra.",
     "Processes can catch and handle incoming signals like SIGHUP to reload configs.", "Tiến trình có thể bắt và xử lý tín hiệu gửi đến như SIGHUP để nạp lại cấu hình.",
     "Tín hiệu hệ điều hành", "📶", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("SIGKILL", "/sɪɡ kɪl/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Tín hiệu diệt tiến trình ngay lập tức: tín hiệu số 9 ép hệ điều hành buộc dừng tiến trình ngay lập tức mà không thể bị chặn.",
     "SIGKILL terminates a frozen process instantly without allowing graceful cleanup.", "SIGKILL tiêu diệt một tiến trình bị treo tức thì mà không cho phép dọn dẹp dữ liệu.",
     "Tín hiệu hủy khẩn SIGKILL", "🛑", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("SIGTERM", "/sɪɡ tɜːm/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Tín hiệu yêu cầu kết thúc: tín hiệu số 15 yêu cầu tiến trình tự dọn dẹp và kết thúc hoạt động một cách an toàn.",
     "Kubernetes sends SIGTERM to allow containers 30 seconds to close active sockets.", "Kubernetes gửi tín hiệu SIGTERM để cho các bộ chứa 30 giây đóng các kết nối an toàn.",
     "Tín hiệu kết thúc SIGTERM", "🏁", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("GPU (Graphics Processing Unit)", "/ˌdʒiː.piːˈjuː/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Bộ xử lý đồ họa: vi xử lý chuyên dụng gồm hàng ngàn lõi nhỏ tối ưu cho các phép tính ma trận song song và đồ họa.",
     "NVIDIA GPUs are the premier hardware accelerator for training large deep neural networks.", "GPU của NVIDIA là phần cứng tăng tốc hàng đầu để huấn luyện mạng nơ-ron sâu quy mô lớn.",
     "Bộ xử lý đồ họa GPU", "🎮", "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=600&auto=format&fit=crop&q=80"),

    ("VRAM (Video RAM)", "/ˈviː.ræm/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Bộ nhớ RAM đồ họa: bộ nhớ chuyên biệt tốc độ cao tích hợp trên card GPU để chứa dữ liệu hình ảnh và trọng số AI.",
     "Running a 70-billion parameter LLM locally requires over 40 gigabytes of VRAM.", "Chạy mô hình LLM 70 tỷ tham số cục bộ đòi hỏi hơn 40 gigabyte bộ nhớ VRAM.",
     "Bộ nhớ đồ họa VRAM", "💾", "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=600&auto=format&fit=crop&q=80"),

    ("TPU (Tensor Processing Unit)", "/ˌtiː.piːˈjuː/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Bộ xử lý Tensor: chip ASIC do Google thiết kế chuyên biệt để tăng tốc tối đa các phép toán ma trận trong học sâu.",
     "Google Cloud TPUs accelerate transformer training with massive matrix multiplication units.", "Google Cloud TPU tăng tốc huấn luyện mô hình Transformer nhờ các đơn vị nhân ma trận cực lớn.",
     "Bộ xử lý Tensor TPU", "🧠", "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=600&auto=format&fit=crop&q=80"),

    ("Hardware Acceleration", "/ˈhɑːd.weər əkˌsel.əˈreɪ.ʃən/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Tăng tốc phần cứng: sử dụng phần cứng chuyên biệt (GPU, NPU) để thực hiện một số chức năng nhanh hơn phần mềm chạy trên CPU.",
     "Enabling hardware acceleration ensures 60 FPS 4K video rendering inside browsers.", "Bật tăng tốc phần cứng đảm bảo phát video 4K 60 FPS mượt mà bên trong trình duyệt.",
     "Tăng tốc phần cứng", "⚡", "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=600&auto=format&fit=crop&q=80"),

    ("Firmware", "/ˈfɜːm.weər/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Phần sụn Firmware: phần mềm cấp thấp nhúng vĩnh viễn vào chip phần cứng để điều khiển trực tiếp thiết bị đó.",
     "Updating SSD firmware resolved an issue causing sudden drive sleep freezes.", "Cập nhật phần sụn ổ SSD đã giải quyết sự cố làm đĩa bị đơ khi vào chế độ ngủ.",
     "Phần sụn Firmware", "🎛️", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Device Driver", "/dɪˈvaɪs ˈdraɪ.vər/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Trình điều khiển thiết bị: phần mềm cầu nối giúp hệ điều hành giao tiếp và ra lệnh cho một thiết bị phần cứng cụ thể.",
     "Install the latest graphics driver to support newly released 3D game engines.", "Cài đặt trình điều khiển đồ họa mới nhất để hỗ trợ các công cụ trò chơi 3D mới ra mắt.",
     "Trình điều khiển Driver", "🔌", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("I/O (Input/Output)", "/ˌaɪˈoʊ/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Nhập/Xuất: giao tiếp giữa hệ thống máy tính với thế giới bên ngoài hoặc giữa CPU với thiết bị ngoại vi.",
     "Asynchronous I/O prevents blocking worker threads during slow disk operations.", "I/O bất đồng bộ giúp tránh chặn các luồng thực thi trong các thao tác đọc đĩa chậm.",
     "Vào ra Nhập/Xuất I/O", "🔄", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Direct Memory Access (DMA)", "/daɪˈrekt ˈmem.ər.i ˈæk.ses/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Truy cập bộ nhớ trực tiếp: tính năng cho phép thiết bị phần cứng truyền dữ liệu thẳng tới RAM mà không cần CPU trung gian.",
     "DMA allows the network card to transfer gigabytes of packets without burdening the CPU.", "DMA cho phép card mạng truyền hàng gigabyte gói tin mà không tạo gánh nặng lên CPU.",
     "Truy cập bộ nhớ trực tiếp DMA", "⏩", "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=600&auto=format&fit=crop&q=80"),

    ("System Bus", "/ˈsɪs.təm bʌs/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Tuyến đường truyền hệ thống: đường dẫn vật lý gồm các đường dây vi mạch truyền tín hiệu giữa CPU, bộ nhớ và các bộ điều khiển.",
     "The system bus connects the central processor directly to the primary memory channels.", "Bus hệ thống kết nối trực tiếp bộ xử lý trung tâm với các kênh bộ nhớ chính.",
     "Tuyến truyền Bus", "🚌", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Northbridge", "/ˈnɔːθ.brɪdʒ/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Cầu Bắc: vi mạch điều khiển truyền thông tốc độ cao giữa CPU, RAM và card đồ họa (hiện đã tích hợp vào CPU).",
     "Historically, the Northbridge handled communications between the CPU and the system RAM.", "Trước đây, chip Cầu Bắc chịu trách nhiệm truyền thông giữa CPU và bộ nhớ RAM hệ thống.",
     "Chip Cầu Bắc Northbridge", "🧭", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Southbridge", "/ˈsaʊθ.brɪdʒ/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Cầu Nam: vi mạch điều khiển các kết nối ngoại vi tốc độ thấp hơn như cổng USB, âm thanh, SATA và BIOS.",
     "The Southbridge manages peripheral expansion slots, USB ports, and SATA drives.", "Chip Cầu Nam quản lý các khe cắm mở rộng ngoại vi, cổng USB và ổ đĩa SATA.",
     "Chip Cầu Nam Southbridge", "🧭", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Hyper-Threading", "/ˈhaɪ.pə ˈθred.ɪŋ/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Công nghệ siêu phân luồng: cho phép một lõi CPU vật lý hoạt động như hai lõi logic trước hệ điều hành.",
     "Hyper-threading increases multi-tasking throughput by utilizing idle pipeline stages.", "Siêu phân luồng tăng thông lượng đa nhiệm bằng cách tận dụng các giai đoạn đường ống rảnh rỗi.",
     "Siêu phân luồng Hyper-Threading", "🧵", "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=600&auto=format&fit=crop&q=80"),

    ("Instruction Set Architecture (ISA)", "/ɪnˈstrʌk.ʃən set/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Kiến trúc tập chỉ lệnh: tập hợp các chỉ lệnh và mô hình lập trình mà phần cứng CPU hiểu và thực thi.",
     "Compilers translate source code into the native ISA of the targeted target processor.", "Trình biên dịch dịch mã nguồn thành tập lệnh ISA bản địa của bộ xử lý mục tiêu.",
     "Kiến trúc tập lệnh ISA", "📜", "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=600&auto=format&fit=crop&q=80"),

    ("x86 Architecture", "/ˌeks.eɪ.tiˈsɪks/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Kiến trúc x86: kiến trúc tập lệnh vi xử lý phổ biến nhất trên máy tính để bàn và máy chủ do Intel phát triển.",
     "x86 architecture has powered PC workstations and enterprise data centers for decades.", "Kiến trúc x86 đã vận hành máy trạm PC và trung tâm dữ liệu doanh nghiệp trong nhiều thập kỷ.",
     "Kiến trúc x86", "💻", "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=600&auto=format&fit=crop&q=80"),

    ("ARM Architecture", "/ɑːm ˌɑː.kɪ.tek.tʃər/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Kiến trúc ARM: kiến trúc vi xử lý RISC tiết kiệm năng lượng vượt trội, thống trị điện thoại thông minh và chip Apple Silicon.",
     "ARM architecture powers virtually all modern smartphones and power-efficient edge devices.", "Kiến trúc ARM vận hành hầu như tất cả điện thoại thông minh và thiết bị biên tiết kiệm điện.",
     "Kiến trúc ARM tiết kiệm điện", "📱", "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=600&auto=format&fit=crop&q=80"),

    ("RISC (Reduced Instruction Set Computer)", "/rɪsk/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Máy tính với tập lệnh thu gọn: triết lý thiết kế CPU dùng các chỉ lệnh đơn giản, thực thi trong một chu kỳ xung nhịp duy nhất.",
     "RISC designs achieve extreme energy efficiency through simple, uniform instructions.", "Thiết kế RISC đạt hiệu quả năng lượng vượt bậc nhờ các chỉ lệnh đơn giản và đồng nhất.",
     "Tập lệnh thu gọn RISC", "⚡", "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=600&auto=format&fit=crop&q=80"),

    ("CISC (Complex Instruction Set Computer)", "/sɪsk/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Máy tính với tập lệnh phức tạp: triết lý thiết kế CPU trong đó một chỉ lệnh đơn lẻ có thể thực hiện nhiều thao tác cấp thấp.",
     "x86 processors maintain backward compatibility with legacy CISC instruction sets.", "Các bộ xử lý x86 duy trì khả năng tương thích ngược với các tập lệnh CISC cũ.",
     "Tập lệnh phức hợp CISC", "🏛️", "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=600&auto=format&fit=crop&q=80"),

    ("Virtual Machine (VM)", "/ˈvɜː.tʃu.əl məˈʃiːn/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Máy ảo: phần mềm mô phỏng một hệ thống máy tính hoàn chỉnh có hệ điều hành riêng chạy trên phần cứng vật lý.",
     "Cloud providers run thousands of isolated virtual machines on a single physical host.", "Các nhà cung cấp đám mây chạy hàng ngàn máy ảo cô lập trên một máy chủ vật lý.",
     "Máy ảo Virtual Machine", "📦", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Hypervisor", "/ˈhaɪ.pə.vaɪ.zər/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Phần mềm giám sát máy ảo: lớp phần mềm tạo, quản lý và phân bổ tài nguyên phần cứng cho các máy ảo chạy đồng thời.",
     "Type 1 bare-metal hypervisors like VMware ESXi run directly on physical server hardware.", "Bộ giám sát máy ảo Type 1 như VMware ESXi chạy trực tiếp trên phần cứng máy chủ vật lý.",
     "Phần mềm giám sát Hypervisor", "🛡️", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80"),

    ("Thermal Throttling", "/ˈθɜː.məl ˈθrɒt.lɪŋ/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Tự hạ xung do nhiệt: cơ chế bảo vệ tự động giảm tốc độ xung nhịp CPU/GPU khi nhiệt độ vượt quá ngưỡng an toàn.",
     "Poor thermal paste causes aggressive thermal throttling during heavy video rendering.", "Keo tản nhiệt kém dẫn đến việc tụt xung nhịp do nhiệt độ tăng quá cao khi render video nặng.",
     "Tự hạ xung do nhiệt", "🌡️", "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=600&auto=format&fit=crop&q=80"),

    ("Power Supply Unit (PSU)", "/ˈpaʊ.ər səˈplaɪ ˈjuː.nɪt/", "noun", "os_hardware", "Hệ điều hành & Phần cứng",
     "Bộ nguồn máy tính: thiết bị chuyển đổi dòng điện xoay chiều AC từ lưới điện thành các dòng điện một chiều DC cấp cho linh kiện.",
     "A modular 850W Gold-rated PSU provides stable clean voltages for power-hungry GPUs.", "Bộ nguồn module 850W chuẩn Gold cung cấp điện áp sạch ổn định cho card đồ họa tiêu thụ nhiều điện.",
     "Bộ nguồn máy tính PSU", "⚡", "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=600&auto=format&fit=crop&q=80")
]

if __name__ == "__main__":
    print(f"Domain 6 terms count: {len(terms)}")
