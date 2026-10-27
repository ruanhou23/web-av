# -*- coding: utf-8 -*-
"""Domain 2: Data Structures & Algorithms (100 core terms)"""

terms = [
    ("Data Structure", "/ˈdeɪ.tə ˈstrʌk.tʃər/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Cấu trúc dữ liệu: cách tổ chức, quản lý và lưu trữ dữ liệu để có thể truy cập và sửa đổi hiệu quả.",
     "Choosing the right data structure directly impacts system performance.", "Việc chọn đúng cấu trúc dữ liệu ảnh hưởng trực tiếp tới hiệu năng hệ thống.",
     "Cấu trúc dữ liệu", "🗄️", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Array", "/əˈreɪ/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Mảng: tập hợp các phần tử có cùng kiểu dữ liệu được lưu trữ tại các ô nhớ liên tiếp nhau.",
     "Arrays offer O(1) constant time index-based lookups.", "Mảng cung cấp khả năng tra cứu dựa trên chỉ số với thời gian hằng số O(1).",
     "Mảng liên tiếp Array", "📊", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Dynamic Array", "/daɪˈnæm.ɪk əˈreɪ/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Mảng động: mảng có khả năng tự động tăng gấp đôi kích thước bộ nhớ khi đầy các phần tử.",
     "std::vector in C++ and ArrayList in Java are dynamic arrays.", "std::vector trong C++ và ArrayList trong Java là các mảng động.",
     "Mảng động Dynamic Array", "📈", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Matrix", "/ˈmeɪ.trɪks/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Ma trận: mảng hai chiều biểu diễn dữ liệu dưới dạng các hàng và cột.",
     "2D grid pathfinding algorithms treat the map as a matrix.", "Các thuật toán tìm đường trên lưới 2D coi bản đồ như một ma trận.",
     "Ma trận hai chiều", "🔢", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Sparse Matrix", "/spɑːs ˈmeɪ.trɪks/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Ma trận thưa: ma trận trong đó phần lớn các phần tử đều có giá trị bằng 0.",
     "Compressing a sparse matrix saves substantial memory in machine learning.", "Nén ma trận thưa giúp tiết kiệm đáng kể bộ nhớ trong học máy.",
     "Ma trận thưa", "◽", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Linked List", "/lɪŋkt lɪst/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Danh sách liên kết: tập hợp tuyến tính các nút dữ liệu trong đó mỗi nút trỏ tới nút kế tiếp.",
     "Linked lists allow dynamic memory allocation without requiring contiguous RAM blocks.", "Danh sách liên kết cho phép cấp phát bộ nhớ động mà không đòi hỏi vùng RAM liên tiếp.",
     "Danh sách liên kết", "🔗", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Singly Linked List", "/ˈsɪŋ.ɡli lɪŋkt lɪst/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Danh sách liên kết đơn: mỗi nút chỉ chứa giá trị và một con trỏ trỏ tới phần tử kế tiếp.",
     "Traversal in a singly linked list can only proceed forward.", "Việc duyệt trong danh sách liên kết đơn chỉ có thể tiến về phía trước.",
     "DS liên kết đơn", "➡️", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Doubly Linked List", "/ˈdʌb.li lɪŋkt lɪst/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Danh sách liên kết đôi: mỗi nút chứa giá trị cùng hai con trỏ trỏ tới phần tử trước và sau.",
     "Doubly linked lists enable bidirectional navigation and O(1) removal of known nodes.", "Danh sách liên kết đôi cho phép duyệt hai chiều và xóa nút đã biết với độ phức tạp O(1).",
     "DS liên kết đôi", "↔️", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Circular Linked List", "/ˈsɜː.kjə.lər lɪŋkt lɪst/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Danh sách liên kết vòng: nút cuối cùng của danh sách trỏ ngược trở lại nút đầu tiên.",
     "Round-robin task scheduling commonly uses circular linked lists.", "Lập lịch tác vụ luân phiên Round-robin thường dùng danh sách liên kết vòng.",
     "DS liên kết vòng", "🔄", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Node", "/nəʊd/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Nút dữ liệu: đơn vị cấu trúc cơ bản chứa dữ liệu và liên kết đến các phần tử khác.",
     "Each node in the binary tree stores an integer key and child references.", "Mỗi nút trong cây nhị phân lưu trữ một khóa số nguyên và các tham chiếu con.",
     "Nút dữ liệu Node", "⚪", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Pointer/Next", "/ˈpɔɪn.tər nekst/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Con trỏ kế tiếp: địa chỉ hoặc liên kết trỏ tới phần tử tiếp sau trong cấu trúc dữ liệu.",
     "Setting node.next to null breaks the chain at that point.", "Thiết lập node.next thành null sẽ ngắt chuỗi liên kết tại điểm đó.",
     "Con trỏ tiếp theo", "👉", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Stack", "/stæk/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Ngăn xếp: cấu trúc dữ liệu tuân thủ nghiêm ngặt nguyên lý vào sau ra trước (LIFO).",
     "Function calls in CPUs are tracked using an execution call stack.", "Các lệnh gọi hàm trong CPU được theo dõi thông qua ngăn xếp thực thi cuộc gọi.",
     "Ngăn xếp Stack", "📚", "https://images.unsplash.com/photo-1532012164546-f432f2e3777f?w=600&auto=format&fit=crop&q=80"),

    ("Push", "/pʊʃ/", "verb", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Đẩy vào ngăn xếp: thêm một phần tử mới lên trên đỉnh của cấu trúc ngăn xếp.",
     "Push new state onto the undo stack whenever the document edits.", "Đẩy trạng thái mới vào ngăn xếp hoàn tác mỗi khi văn bản được chỉnh sửa.",
     "Đẩy vào Push", "⬆️", "https://images.unsplash.com/photo-1532012164546-f432f2e3777f?w=600&auto=format&fit=crop&q=80"),

    ("Pop", "/pɒp/", "verb", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Lấy ra khỏi ngăn xếp: loại bỏ và trả về phần tử nằm ở trên đỉnh ngăn xếp.",
     "Pop the top bracket from the stack to match closing parentheses.", "Lấy dấu ngoặc trên đỉnh ngăn xếp để ghép cặp với dấu ngoặc đóng.",
     "Lấy ra Pop", "⬇️", "https://images.unsplash.com/photo-1532012164546-f432f2e3777f?w=600&auto=format&fit=crop&q=80"),

    ("Peek", "/piːk/", "verb", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Xem đỉnh: kiểm tra giá trị phần tử trên đỉnh ngăn xếp mà không loại bỏ nó.",
     "Peek at the top element to decide if further processing is required.", "Xem giá trị phần tử đỉnh để quyết định có cần xử lý tiếp hay không.",
     "Xem đỉnh Peek", "👁️", "https://images.unsplash.com/photo-1532012164546-f432f2e3777f?w=600&auto=format&fit=crop&q=80"),

    ("LIFO (Last-In First-Out)", "/ˌlaɪ.fəʊ/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Vào sau ra trước: nguyên tắc xử lý trong đó phần tử được đưa vào cuối cùng sẽ được lấy ra đầu tiên.",
     "Stack operations strictly adhere to the LIFO discipline.", "Các thao tác trên ngăn xếp tuân thủ chặt chẽ quy tắc vào sau ra trước LIFO.",
     "Nguyên tắc LIFO", "📦", "https://images.unsplash.com/photo-1532012164546-f432f2e3777f?w=600&auto=format&fit=crop&q=80"),

    ("Queue", "/kjuː/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Hàng đợi: cấu trúc dữ liệu tuân thủ nguyên lý vào trước ra trước (FIFO).",
     "A print queue manages jobs in the exact order they arrive.", "Hàng đợi in ấn quản lý các lệnh in đúng theo thứ tự chúng được gửi đến.",
     "Hàng đợi Queue", "🚶‍♂️", "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    ("Enqueue", "/ɪnˈkjuː/", "verb", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Thêm vào hàng đợi: đưa một phần tử mới vào vị trí cuối của hàng đợi.",
     "Enqueue pending customer requests into the task buffer.", "Thêm các yêu cầu khách hàng đang chờ vào bộ đệm hàng đợi tác vụ.",
     "Thêm vào hàng đợi", "➡️", "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    ("Dequeue", "/diːˈkjuː/", "verb", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Lấy ra khỏi hàng đợi: loại bỏ và trả về phần tử nằm ở vị trí đầu tiên của hàng đợi.",
     "Dequeue the next message when an idle worker becomes available.", "Lấy tin nhắn tiếp theo khi có một tiến trình rảnh rỗi sẵn sàng.",
     "Lấy ra khỏi hàng đợi", "⬅️", "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    ("FIFO (First-In First-Out)", "/ˌfaɪ.fəʊ/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Vào trước ra trước: nguyên tắc trong đó phần tử xuất hiện đầu tiên sẽ được phục vụ trước.",
     "Message brokers use FIFO queues to preserve order consistency.", "Bộ truyền tải tin nhắn dùng hàng đợi FIFO để bảo toàn thứ tự ban đầu.",
     "Nguyên tắc FIFO", "📋", "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&auto=format&fit=crop&q=80"),

    ("Deque (Double-Ended Queue)", "/dek/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Hàng đợi hai đầu: cho phép chèn và xóa các phần tử ở cả hai đầu với chi phí O(1).",
     "A deque is optimal for implementing sliding window maximum algorithms.", "Deque là lựa chọn tối ưu để cài đặt thuật toán tìm giá trị lớn nhất trong cửa sổ trượt.",
     "Hàng đợi hai đầu Deque", "↔️", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Priority Queue", "/praɪˈɒr.ə.ti kjuː/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Hàng đợi ưu tiên: mỗi phần tử có mức độ ưu tiên, phần tử ưu tiên cao nhất được lấy ra trước.",
     "Dijkstra's shortest path algorithm uses a min-priority queue.", "Thuật toán tìm đường đi ngắn nhất Dijkstra sử dụng hàng đợi ưu tiên nhỏ nhất.",
     "Hàng đợi ưu tiên", "⭐", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Monotonic Stack", "/ˌmɒn.əˈtɒn.ɪk stæk/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Ngăn xếp đơn điệu: ngăn xếp duy trì các phần tử luôn tăng dần hoặc giảm dần theo thứ tự.",
     "Finding the next greater element in an array is solved via monotonic stack.", "Bài toán tìm phần tử lớn hơn tiếp theo trong mảng được giải bằng ngăn xếp đơn điệu.",
     "Ngăn xếp đơn điệu", "📈", "https://images.unsplash.com/photo-1532012164546-f432f2e3777f?w=600&auto=format&fit=crop&q=80"),

    ("Monotonic Queue", "/ˌmɒn.əˈtɒn.ɪk kjuː/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Hàng đợi đơn điệu: hàng đợi duy trì thứ tự tăng hoặc giảm đều của các giá trị bên trong.",
     "Monotonic queues find window extremes in amortized linear time.", "Hàng đợi đơn điệu tìm các giá trị cực trị của cửa sổ trong thời gian tuyến tính phân bổ.",
     "Hàng đợi đơn điệu", "📉", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Hash Table", "/hæʃ ˈteɪ.bəl/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Bảng băm: cấu trúc lưu cặp khóa - giá trị bằng cách dùng hàm băm ánh xạ khóa thành chỉ số mảng.",
     "Hash tables provide average O(1) lookup, insertion, and deletion.", "Bảng băm cung cấp khả năng tìm kiếm, chèn và xóa trung bình với thời gian O(1).",
     "Bảng băm Hash Table", "🗃️", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Hash Function", "/hæʃ ˈfʌŋk.ʃən/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Hàm băm: thuật toán biến đổi dữ liệu đầu vào kích thước bất kỳ thành chuỗi số nguyên có kích thước cố định.",
     "A good hash function distributes keys uniformly to avoid clusters.", "Một hàm băm tốt phân phối các khóa đồng đều để tránh tụ tập dữ liệu.",
     "Hàm băm dữ liệu", "⚙️", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Collision", "/kəˈlɪʒ.ən/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Đụng độ băm: hiện tượng hai khóa khác nhau tạo ra cùng một giá trị băm từ hàm băm.",
     "Handling collisions efficiently is essential for hash table performance.", "Xử lý đụng độ hiệu quả là điều cốt lõi cho hiệu năng của bảng băm.",
     "Đụng độ băm Collision", "💥", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Chaining", "/ˈtʃeɪ.nɪŋ/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Nối chuỗi: kỹ thuật giải quyết đụng độ băm bằng cách gắn một danh sách liên kết tại mỗi ô băm.",
     "Separate chaining keeps all collided entries in a local linked list.", "Nối chuỗi riêng biệt giữ tất cả các mục bị đụng độ trong một danh sách liên kết cục bộ.",
     "Kỹ thuật nối chuỗi", "⛓️", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Open Addressing", "/ˈoʊ.pən əˈdres.ɪŋ/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Định địa chỉ mở: kỹ thuật xử lý đụng độ bằng cách tìm ô trống tiếp theo trong mảng bảng băm.",
     "Linear probing is the simplest open addressing collision strategy.", "Dò tuyến tính là chiến lược định địa chỉ mở đơn giản nhất để xử lý đụng độ.",
     "Định địa chỉ mở", "🔍", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Hash Map", "/hæʃ mæp/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Bản đồ băm: cấu trúc lưu trữ tập hợp các ánh xạ giữa khóa duy nhất và giá trị tương ứng.",
     "Use a hash map to store frequencies of each character in a word.", "Dùng hash map để lưu số lần xuất hiện của mỗi ký tự trong từ.",
     "Bản đồ băm Hash Map", "🗺️", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Hash Set", "/hæʃ set/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Tập hợp băm: cấu trúc dữ liệu lưu trữ các phần tử phân biệt không trùng lặp dựa trên cơ chế băm.",
     "A hash set allows verifying membership in constant time.", "Tập hợp băm cho phép kiểm tra phần tử có thuộc tập hợp hay không trong thời gian hằng số.",
     "Tập hợp băm Hash Set", "⭕", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Tree", "/triː/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Cây dữ liệu: cấu trúc dữ liệu phi tuyến tính phân cấp gồm nút gốc và các nút con phân nhánh.",
     "Hierarchical file systems are naturally modeled using a tree structure.", "Hệ thống tệp phân cấp được mô hình hóa tự nhiên bằng cấu trúc cây.",
     "Cấu trúc cây Tree", "🌳", "https://images.unsplash.com/photo-1448375240586-882707db888b?w=600&auto=format&fit=crop&q=80"),

    ("Root Node", "/ruːt nəʊd/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Nút gốc: nút trên cùng cao nhất của cây dữ liệu, không có bất kỳ nút cha nào.",
     "Every tree traversal begins starting from the root node.", "Mọi thao tác duyệt cây đều bắt đầu xuất phát từ nút gốc.",
     "Nút gốc Root", "🌱", "https://images.unsplash.com/photo-1448375240586-882707db888b?w=600&auto=format&fit=crop&q=80"),

    ("Leaf Node", "/liːf nəʊd/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Nút lá: nút nằm ở tận cùng của cây dữ liệu, không có bất kỳ nút con nào.",
     "A leaf node has child pointer references pointing to null.", "Một nút lá có các con trỏ trỏ tới con đều là null.",
     "Nút lá Leaf", "🍃", "https://images.unsplash.com/photo-1448375240586-882707db888b?w=600&auto=format&fit=crop&q=80"),

    ("Binary Tree", "/ˈbaɪ.nər.i triː/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Cây nhị phân: cây dữ liệu trong đó mỗi nút cha có tối đa hai nút con (con trái và con phải).",
     "Binary trees form the foundation for binary search trees and heaps.", "Cây nhị phân tạo nền tảng cho cây tìm kiếm nhị phân và đống dữ liệu.",
     "Cây nhị phân", "🌿", "https://images.unsplash.com/photo-1448375240586-882707db888b?w=600&auto=format&fit=crop&q=80"),

    ("Binary Search Tree (BST)", "/ˈbaɪ.nər.i sɜːtʃ triː/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Cây tìm kiếm nhị phân: cây nhị phân có con trái nhỏ hơn cha, con phải lớn hơn cha.",
     "In-order traversal of a BST outputs values in sorted order.", "Duyệt trung thứ tự trên cây BST cho ra các giá trị theo thứ tự đã sắp xếp.",
     "Cây tìm kiếm BST", "🌲", "https://images.unsplash.com/photo-1448375240586-882707db888b?w=600&auto=format&fit=crop&q=80"),

    ("Balanced Tree", "/ˈbæl.ənst triː/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Cây cân bằng: cây tự động cân bằng chiều cao để đảm bảo độ sâu duy trì ở mức O(log N).",
     "Balanced trees prevent BST operations from degrading to O(N).", "Cây cân bằng ngăn các thao tác trên cây BST bị suy biến xuống độ phức tạp O(N).",
     "Cây cân bằng", "⚖️", "https://images.unsplash.com/photo-1448375240586-882707db888b?w=600&auto=format&fit=crop&q=80"),

    ("AVL Tree", "/ˌeɪ.viːˈel triː/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Cây AVL: cây tìm kiếm nhị phân tự cân bằng dựa trên chênh lệch chiều cao hai cây con không quá 1.",
     "AVL trees perform rotations upon insertions to maintain balance.", "Cây AVL thực hiện các phép quay cây khi chèn để duy trì trạng thái cân bằng.",
     "Cây tự cân bằng AVL", "🌲", "https://images.unsplash.com/photo-1448375240586-882707db888b?w=600&auto=format&fit=crop&q=80"),

    ("Red-Black Tree", "/red blæk triː/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Cây Đỏ-Đen: cây nhị phân cân bằng sử dụng màu đỏ hoặc đen trên các nút để đảm bảo cân bằng xấp xỉ.",
     "Java's TreeMap and C++'s std::map are implemented with Red-Black trees.", "TreeMap của Java và std::map của C++ được cài đặt bằng cây Đỏ-Đen.",
     "Cây Đỏ-Đen Red-Black", "🔴", "https://images.unsplash.com/photo-1448375240586-882707db888b?w=600&auto=format&fit=crop&q=80"),

    ("B-Tree", "/biː triː/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Cây B-Tree: cây tìm kiếm nhiều nhánh tự cân bằng, tối ưu hóa cho hệ thống đọc ghi đĩa và cơ sở dữ liệu.",
     "Relational database storage engines store primary tables using B-Trees.", "Bộ máy lưu trữ cơ sở dữ liệu quan hệ lưu trữ các bảng chính bằng B-Tree.",
     "Cây chỉ mục B-Tree", "📚", "https://images.unsplash.com/photo-1448375240586-882707db888b?w=600&auto=format&fit=crop&q=80"),

    ("B+ Tree", "/biː plʌs triː/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Cây B+ Tree: biến thể của B-tree lưu toàn bộ dữ liệu ở các nút lá nối tiếp nhau, tối ưu truy vấn khoảng.",
     "MySQL InnoDB uses B+ Trees to accelerate range scans.", "MySQL InnoDB dùng cây B+ Tree để tăng tốc các truy vấn quét theo khoảng giá trị.",
     "Cây chỉ mục B+ Tree", "📖", "https://images.unsplash.com/photo-1448375240586-882707db888b?w=600&auto=format&fit=crop&q=80"),

    ("Trie (Prefix Tree)", "/traɪ/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Cây tiền tố (Trie): cấu trúc cây chuyên dụng lưu trữ tập hợp các chuỗi ký tự phục vụ tìm kiếm từ nhanh.",
     "Search engine autocomplete bars are powered by trie data structures.", "Thanh tự động hoàn thành từ khóa của công cụ tìm kiếm được vận hành bởi cây tiền tố trie.",
     "Cây tiền tố Trie", "🔤", "https://images.unsplash.com/photo-1448375240586-882707db888b?w=600&auto=format&fit=crop&q=80"),

    ("Heap", "/hiːp/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Đống dữ liệu (Heap): cây nhị phân gần hoàn chỉnh thỏa mãn tính chất phần tử cha luôn lớn hơn hoặc nhỏ hơn con.",
     "A min-heap guarantees that the root element is always the minimum value.", "Min-heap đảm bảo phần tử gốc luôn có giá trị nhỏ nhất trong cây.",
     "Cấu trúc đống Heap", "⛰️", "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=600&auto=format&fit=crop&q=80"),

    ("Min-Heap", "/mɪn hiːp/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Đống cực tiểu: cây nhị phân trong đó giá trị của mỗi nút cha luôn nhỏ hơn hoặc bằng các nút con.",
     "Min-heaps efficiently extract the smallest element in O(log N) time.", "Min-heap trích xuất phần tử nhỏ nhất hiệu quả với thời gian O(log N).",
     "Đống cực tiểu Min-Heap", "📉", "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=600&auto=format&fit=crop&q=80"),

    ("Max-Heap", "/mæks hiːp/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Đống cực đại: cây nhị phân trong đó giá trị của mỗi nút cha luôn lớn hơn hoặc bằng các nút con.",
     "Max-heaps are utilized in heap sort to arrange numbers ascendingly.", "Max-heap được sử dụng trong sắp xếp vun đống để sắp xếp các số tăng dần.",
     "Đống cực đại Max-Heap", "📈", "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=600&auto=format&fit=crop&q=80"),

    ("Heapify", "/ˈhiː.pɪ.faɪ/", "verb", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Vun đống: thao tác sắp xếp lại các phần tử của một mảng để tạo thành một đống heap hợp lệ.",
     "The heapify procedure converts an unordered array into a heap in O(N).", "Thủ tục vun đống chuyển đổi một mảng chưa sắp xếp thành đống trong O(N).",
     "Vun đống Heapify", "🔄", "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=600&auto=format&fit=crop&q=80"),

    ("Graph", "/ɡrɑːf/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Đồ thị: cấu trúc dữ liệu gồm tập hợp các đỉnh (nút) và các cạnh kết nối các cặp đỉnh đó.",
     "Social networks and GPS navigation rely heavily on graph modeling.", "Mạng xã hội và bản đồ GPS định vị phụ thuộc rất lớn vào mô hình đồ thị.",
     "Cấu trúc đồ thị Graph", "🕸️", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Vertex (Node)", "/ˈvɜː.teks/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Đỉnh đồ thị: điểm nút đại diện cho một thực thể hoặc đối tượng trong đồ thị.",
     "Each vertex in the social graph represents an individual user.", "Mỗi đỉnh trong đồ thị xã hội đại diện cho một người dùng cá nhân.",
     "Đỉnh đồ thị Vertex", "📍", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Edge", "/edʒ/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Cạnh đồ thị: đoạn nối biểu diễn mối quan hệ hoặc đường liên kết giữa hai đỉnh trong đồ thị.",
     "A weighted edge denotes the physical road distance between two cities.", "Cạnh có trọng số biểu thị khoảng cách đường bộ giữa hai thành phố.",
     "Cạnh nối đồ thị", "➖", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Directed Graph (Digraph)", "/daɪˈrek.tɪd ɡrɑːf/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Đồ thị có hướng: đồ thị mà các cạnh đều có hướng một chiều đi từ đỉnh này sang đỉnh khác.",
     "Webpage hyperlinks form a massive directed graph of references.", "Các liên kết siêu văn bản trên trang web tạo thành một đồ thị có hướng khổng lồ.",
     "Đồ thị có hướng", "➡️", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Undirected Graph", "/ˌʌn.daɪˈrek.tɪd ɡrɑːf/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Đồ thị vô hướng: đồ thị mà các cạnh kết nối hai chiều tương hỗ không phân biệt chiều đi.",
     "Facebook friendship connections are modeled as an undirected graph.", "Quan hệ kết bạn trên Facebook được mô hình hóa thành một đồ thị vô hướng.",
     "Đồ thị vô hướng", "↔️", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Weighted Graph", "/ˈweɪ.tɪd ɡrɑːf/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Đồ thị có trọng số: đồ thị mà mỗi cạnh được gán một giá trị số biểu thị chi phí, khoảng cách.",
     "Shortest path algorithms require a weighted graph to compute optimal routes.", "Thuật toán đường đi ngắn nhất đòi hỏi đồ thị có trọng số để tính lộ trình tối ưu.",
     "Đồ thị có trọng số", "⚖️", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Directed Acyclic Graph (DAG)", "/ˌdiː.eɪˈdʒiː/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Đồ thị có hướng không chu trình: đồ thị có hướng mà không có bất kỳ đường đi khép kín nào quay lại đỉnh cũ.",
     "Build pipelines and git commit trees are modeled as DAGs.", "Quy trình xây dựng phần mềm và cây commit git được mô hình hóa dưới dạng DAG.",
     "Đồ thị DAG", "🔄", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Adjacency Matrix", "/əˈdʒeɪ.sən.si ˈmeɪ.trɪks/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Ma trận kề: bảng hai chiều kích thước V x V biểu diễn việc có cạnh nối giữa các đỉnh hay không.",
     "An adjacency matrix takes O(V^2) space regardless of edge density.", "Ma trận kề tiêu tốn O(V^2) bộ nhớ bất kể mật độ số cạnh ít hay nhiều.",
     "Ma trận kề đồ thị", "🔢", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Adjacency List", "/əˈdʒeɪ.sən.si lɪst/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Danh sách kề: mảng danh sách liên kết lưu các đỉnh kề của từng đỉnh, rất tiết kiệm bộ nhớ cho đồ thị thưa.",
     "Adjacency lists are space-efficient for graphs with few edges.", "Danh sách kề rất tiết kiệm không gian đối với các đồ thị có ít cạnh nối.",
     "Danh sách kề đồ thị", "📋", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Disjoint Set (Union-Find)", "/ˈdɪs.dʒɔɪnt set/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Tập hợp rời rạc: cấu trúc dữ liệu theo dõi việc chia tập hợp thành các tập con không giao nhau.",
     "Kruskal's algorithm uses Disjoint Set to detect cycles efficiently.", "Thuật toán Kruskal dùng Disjoint Set để phát hiện chu trình một cách hiệu quả.",
     "Tập hợp rời rạc Union-Find", "🔗", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Segment Tree", "/ˈseɡ.mənt triː/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Cây phân đoạn: cây nhị phân lưu trữ thông tin về các đoạn mảng, cho phép truy vấn khoảng trong O(log N).",
     "Segment trees allow range sum queries and dynamic element updates.", "Cây phân đoạn cho phép truy vấn tổng đoạn và cập nhật phần tử động trong O(log N).",
     "Cây phân đoạn Segment Tree", "🌲", "https://images.unsplash.com/photo-1448375240586-882707db888b?w=600&auto=format&fit=crop&q=80"),

    ("Fenwick Tree (Binary Indexed Tree)", "/ˈfen.wɪk triː/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Cây chỉ mục nhị phân: cấu trúc mảng cho phép tính tổng tiền tố và cập nhật phần tử cực nhanh trong O(log N).",
     "A Fenwick tree requires less memory overhead than a segment tree.", "Cây Fenwick tốn ít bộ nhớ bổ sung hơn so với cây phân đoạn.",
     "Cây Fenwick BIT", "🌳", "https://images.unsplash.com/photo-1448375240586-882707db888b?w=600&auto=format&fit=crop&q=80"),

    ("Bloom Filter", "/bluːm ˈfɪl.tər/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Bộ lọc Bloom: cấu trúc dữ liệu xác suất tiết kiệm không gian dùng kiểm tra một phần tử có thuộc tập hợp không.",
     "Bloom filters may return false positives but never false negatives.", "Bộ lọc Bloom có thể trả về dương tính giả nhưng không bao giờ trả về âm tính giả.",
     "Bộ lọc xác suất Bloom", "🌸", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Big O Notation", "/bɪɡ oʊ noʊˈteɪ.ʃən/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Ký hiệu Big O: thước đo chuẩn toán học mô tả cận trên của độ phức tạp thuật toán khi dữ liệu lớn dần.",
     "Binary search has an O(log N) time complexity in Big O notation.", "Tìm kiếm nhị phân có độ phức tạp thời gian là O(log N) theo ký hiệu Big O.",
     "Độ phức tạp Big O", "📈", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Time Complexity", "/taɪm kəmˈplek.sə.ti/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Độ phức tạp thời gian: số bước tính toán mà thuật toán cần thực thi theo kích thước đầu vào N.",
     "Nested loops over an array typically result in quadratic O(N^2) time complexity.", "Các vòng lặp lồng nhau trên một mảng thường dẫn tới độ phức tạp thời gian bậc hai O(N^2).",
     "Độ phức tạp thời gian", "⏱️", "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=600&auto=format&fit=crop&q=80"),

    ("Space Complexity", "/speɪs kəmˈplek.sə.ti/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Độ phức tạp không gian: lượng bộ nhớ bổ sung mà thuật toán tiêu tốn theo kích thước đầu vào N.",
     "In-place sorting algorithms feature constant O(1) auxiliary space complexity.", "Các thuật toán sắp xếp tại chỗ có độ phức tạp không gian bổ trợ là hằng số O(1).",
     "Độ phức tạp bộ nhớ RAM", "💾", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("Amortized Complexity", "/ˈæm.ər.taɪzd kəmˈplek.sə.ti/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Độ phức tạp phân bổ: chi phí trung bình trên mỗi thao tác khi thực hiện một chuỗi thao tác liên tiếp.",
     "Appending to a dynamic array has an amortized O(1) time complexity.", "Thao tác thêm vào cuối mảng động có độ phức tạp thời gian phân bổ là O(1).",
     "Độ phức tạp phân bổ", "📊", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=80"),

    ("Worst Case", "/wɜːst keɪs/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Trường hợp xấu nhất: trường hợp đầu vào khiến thuật toán tốn nhiều thời gian hoặc bộ nhớ nhất.",
     "Quick sort degrades to O(N^2) in its worst case without random pivots.", "Sắp xếp Quick sort bị suy biến về O(N^2) trong trường hợp xấu nhất nếu không chọn chốt ngẫu nhiên.",
     "Trường hợp xấu nhất", "⛈️", "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=600&auto=format&fit=crop&q=80"),

    ("Best Case", "/best keɪs/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Trường hợp tốt nhất: cấu hình đầu vào giúp thuật toán giải quyết nhanh nhất và tốn ít bước nhất.",
     "Insertion sort achieves O(N) in the best case on already sorted arrays.", "Thuật toán sắp xếp chèn đạt O(N) trong trường hợp tốt nhất trên mảng đã được sắp xếp sẵn.",
     "Trường hợp tốt nhất", "☀️", "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=600&auto=format&fit=crop&q=80"),

    ("Average Case", "/ˈæv.ər.ɪdʒ keɪs/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Trường hợp trung bình: thời gian hoặc không gian tính toán kỳ vọng trên phân phối dữ liệu ngẫu nhiên.",
     "The average case time complexity of hash table lookup is O(1).", "Độ phức tạp thời gian trong trường hợp trung bình khi tra cứu bảng băm là O(1).",
     "Trường hợp trung bình", "⚖️", "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=600&auto=format&fit=crop&q=80"),

    ("Linear Search", "/ˈlɪn.i.ər sɜːtʃ/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Tìm kiếm tuyến tính: duyệt tuần tự qua từng phần tử từ đầu đến cuối danh sách để tìm khóa.",
     "Linear search operates in O(N) time and requires no prior ordering.", "Tìm kiếm tuyến tính chạy trong thời gian O(N) và không yêu cầu dữ liệu phải sắp xếp trước.",
     "Tìm kiếm tuyến tính", "🔍", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Binary Search", "/ˈbaɪ.nər.i sɜːtʃ/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Tìm kiếm nhị phân: liên tục chia đôi khoảng tìm kiếm trên mảng đã sắp xếp để tìm kiếm trong O(log N).",
     "Binary search finds targets in a million sorted items in only 20 steps.", "Tìm kiếm nhị phân tìm thấy phần tử trong 1 triệu mục đã sắp xếp chỉ với 20 bước.",
     "Tìm kiếm nhị phân", "🎯", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Two Pointers", "/tuː ˈpɔɪn.tərz/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Kỹ thuật hai con trỏ: dùng hai biến chỉ mục di chuyển đồng thời để giải bài toán trên mảng hoặc chuỗi.",
     "Use two pointers moving inward to reverse a string in-place.", "Dùng hai con trỏ di chuyển vào trong để đảo ngược chuỗi tại chỗ.",
     "Kỹ thuật hai con trỏ", "👉👈", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Sliding Window", "/ˈslaɪ.dɪŋ ˈwɪn.dəʊ/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Cửa sổ trượt: kỹ thuật duy trì một khung cửa sổ kích thước động hoặc tĩnh trượt qua chuỗi/mảng.",
     "Sliding window computes maximum subarray sums in linear O(N) time.", "Kỹ thuật cửa sổ trượt tính tổng mảng con lớn nhất trong thời gian tuyến tính O(N).",
     "Cửa sổ trượt", "🪟", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Fast & Slow Pointers", "/fɑːst slow ˈpɔɪn.tərz/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Con trỏ rùa và thỏ: hai con trỏ chạy với tốc độ khác nhau để phát hiện chu trình hoặc tìm điểm giữa.",
     "Floyd's cycle detection algorithm utilizes fast and slow pointers.", "Thuật toán phát hiện chu trình Floyd sử dụng hai con trỏ nhanh và chậm.",
     "Con trỏ nhanh & chậm", "🐢🐇", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Divide and Conquer", "/dɪˈvaɪd ənd ˈkɒŋ.kər/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Chia để trị: chiến lược chia bài toán lớn thành các bài toán con độc lập, giải rồi kết hợp kết quả.",
     "Merge sort splits the array into halves using divide and conquer.", "Sắp xếp trộn chia mảng thành hai nửa bằng chiến lược chia để trị.",
     "Chia để trị", "⚔️", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Recursion", "/rɪˈkɜː.ʃən/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Đệ quy: giải pháp trong đó hàm gọi lại chính mình với dữ liệu đầu vào nhỏ hơn cho đến khi chạm trường hợp cơ sở.",
     "Tree traversals are naturally and elegantly implemented with recursion.", "Các phép duyệt cây được triển khai rất tự nhiên và thanh lịch bằng đệ quy.",
     "Thuật toán đệ quy", "🌀", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Backtracking", "/ˈbæk.træk.ɪŋ/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Quay lui: thuật toán tìm kiếm thử tất cả các khả năng và rút lui khi nhận thấy nhánh hiện tại không dẫn tới lời giải.",
     "Solving the N-Queens puzzle relies on backtracking with pruning.", "Giải bài toán N quân hậu dựa vào thuật toán quay lui kết hợp cắt tỉa nhánh.",
     "Thuật toán quay lui", "🔙", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Dynamic Programming (DP)", "/daɪˈnæm.ɪk ˈprəʊ.ɡræm.ɪŋ/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Quy hoạch động: phương pháp tối ưu hóa bằng cách chia bài toán thành các bài toán con gối nhau và lưu trữ kết quả.",
     "Dynamic programming reduces exponential recursion into polynomial runtime.", "Quy hoạch động giảm đệ quy hàm mũ xuống thời gian đa thức.",
     "Quy hoạch động DP", "🧩", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Memoization", "/ˌmem.oʊ.əˈzeɪ.ʃən/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Ghi nhớ kết quả (Top-Down): lưu lại kết quả của các lời gọi hàm tốn kém để dùng lại khi gặp lại cùng đầu vào.",
     "Memoization avoids redundant calculations in recursive Fibonacci.", "Ghi nhớ kết quả giúp tránh tính toán trùng lặp trong hàm Fibonacci đệ quy.",
     "Ghi nhớ Memoization", "🧠", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Tabulation", "/ˌtæb.jəˈleɪ.ʃən/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Lập bảng (Bottom-Up): giải các bài toán con nhỏ nhất trước rồi điền dần vào bảng để giải bài toán lớn.",
     "Tabulation computes dynamic programming solutions iteratively.", "Lập bảng tính toán lời giải quy hoạch động theo cách lặp từ dưới lên.",
     "Lập bảng Tabulation", "📊", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Overlapping Subproblems", "/ˌoʊ.vərˈlæp.ɪŋ/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Bài toán con gối nhau: tình huống trong đó các bài toán con tương tự được giải lặp đi lặp lại nhiều lần.",
     "Overlapping subproblems is a core indicator that DP is applicable.", "Bài toán con gối nhau là dấu hiệu then chốt cho thấy có thể áp dụng quy hoạch động.",
     "Bài toán con gối nhau", "🔄", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Optimal Substructure", "/ˈɒp.tɪ.məl ˈsʌbˌstrʌk.tʃər/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Cấu trúc con tối ưu: tính chất trong đó lời giải tối ưu của bài toán lớn được tạo thành từ lời giải tối ưu của các bài toán con.",
     "Shortest path problems exhibit clear optimal substructure properties.", "Các bài toán tìm đường đi ngắn nhất thể hiện rõ tính chất cấu trúc con tối ưu.",
     "Cấu trúc con tối ưu", "💎", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Greedy Algorithm", "/ˈɡriː.di ˈæl.ɡə.rɪ.ðəm/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Thuật toán tham lam: tại mỗi bước luôn đưa ra lựa chọn có vẻ tốt nhất trước mắt để tìm kiếm lời giải toàn cục.",
     "Huffman coding and Kruskal's algorithm employ greedy strategies.", "Mã hóa Huffman và thuật toán Kruskal áp dụng các chiến lược tham lam.",
     "Thuật toán tham lam", "🦊", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Bubble Sort", "/ˈbʌb.əl sɔːt/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Sắp xếp nổi bọt: liên tục so sánh và đổi chỗ hai phần tử liền kề nếu chúng sai thứ tự.",
     "Bubble sort has O(N^2) complexity and is primarily used for education.", "Sắp xếp nổi bọt có độ phức tạp O(N^2) và chủ yếu dùng cho mục đích giảng dạy.",
     "Sắp xếp nổi bọt", "🫧", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Selection Sort", "/sɪˈlek.ʃən sɔːt/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Sắp xếp chọn: tìm phần tử nhỏ nhất trong danh sách chưa sắp xếp rồi đổi chỗ nó về vị trí đầu.",
     "Selection sort performs a minimum number of swap operations.", "Sắp xếp chọn thực hiện số lượng phép hoán đổi vị trí tối thiểu.",
     "Sắp xếp chọn", "👉", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Insertion Sort", "/ɪnˈsɜː.ʃən sɔːt/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Sắp xếp chèn: lấy từng phần tử và chèn vào đúng vị trí tương đối trong đoạn đã sắp xếp phía trước.",
     "Insertion sort is exceptionally fast on nearly sorted or tiny arrays.", "Sắp xếp chèn đặc biệt nhanh đối với các mảng gần như đã sắp xếp hoặc mảng rất nhỏ.",
     "Sắp xếp chèn", "📥", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Merge Sort", "/mɜːdʒ sɔːt/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Sắp xếp trộn: thuật toán chia đôi mảng rồi trộn hai nửa đã sắp xếp lại, đảm bảo O(N log N) ổn định.",
     "Merge sort is a stable sorting algorithm requiring O(N) auxiliary space.", "Sắp xếp trộn là thuật toán sắp xếp ổn định đòi hỏi O(N) bộ nhớ phụ trợ.",
     "Sắp xếp trộn Merge Sort", "🔀", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Quick Sort", "/kwɪk sɔːt/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Sắp xếp nhanh: chọn một phần tử làm chốt (pivot), phân hoạch mảng thành hai phần và đệ quy.",
     "Quick sort is widely used in standard libraries due to great cache locality.", "Quick sort được sử dụng rộng rãi trong các thư viện chuẩn nhờ tận dụng bộ nhớ đệm tốt.",
     "Sắp xếp nhanh Quick Sort", "⚡", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Heap Sort", "/hiːp sɔːt/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Sắp xếp vun đống: xây dựng đống max-heap rồi liên tục rút phần tử gốc để xếp về cuối mảng.",
     "Heap sort guarantees O(N log N) worst-case time with O(1) extra space.", "Sắp xếp vun đống đảm bảo thời gian O(N log N) trong trường hợp xấu nhất với O(1) bộ nhớ.",
     "Sắp xếp vun đống Heap Sort", "⛰️", "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=600&auto=format&fit=crop&q=80"),

    ("Counting Sort", "/ˈkaʊn.tɪŋ sɔːt/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Sắp xếp đếm phân phối: thuật toán sắp xếp không so sánh đếm số lần xuất hiện của các phần tử.",
     "Counting sort achieves linear O(N + K) time when key ranges are small.", "Sắp xếp đếm đạt thời gian tuyến tính O(N + K) khi khoảng giá trị của khóa nhỏ.",
     "Sắp xếp đếm", "🔢", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Radix Sort", "/ˈreɪ.dɪks sɔːt/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Sắp xếp theo cơ số: sắp xếp các số bằng cách phân loại từng chữ số từ hàng đơn vị lên hàng cao nhất.",
     "Radix sort orders fixed-length integers in linear time.", "Sắp xếp cơ số sắp xếp các số nguyên có độ dài cố định trong thời gian tuyến tính.",
     "Sắp xếp cơ số Radix Sort", "🔣", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Topological Sort", "/ˌtɒp.əˈlɒdʒ.ɪ.kəl sɔːt/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Sắp xếp tô-pô: sắp xếp tuyến tính các đỉnh của đồ thị DAG sao cho mọi cạnh u->v thì u luôn đứng trước v.",
     "Package managers resolve dependency installation orders via topological sort.", "Trình quản lý gói xác định thứ tự cài đặt phụ thuộc thông qua sắp xếp tô-pô.",
     "Sắp xếp tô-pô", "📐", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Breadth-First Search (BFS)", "/bredθ fɜːst sɜːtʃ/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Tìm kiếm theo chiều rộng: duyệt đồ thị theo từng tầng mức khoảng cách dùng cấu trúc hàng đợi.",
     "BFS discovers the shortest path in unweighted graphs.", "BFS tìm ra đường đi ngắn nhất trên đồ thị không có trọng số.",
     "Tìm kiếm theo chiều rộng BFS", "🌊", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Depth-First Search (DFS)", "/depθ fɜːst sɜːtʃ/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Tìm kiếm theo chiều sâu: duyệt đồ thị bằng cách đi sâu vào từng nhánh nhất có thể trước khi quay lui.",
     "DFS is used to detect cycles and explore connected components.", "DFS được dùng để phát hiện chu trình và khám phá các thành phần liên thông.",
     "Tìm kiếm theo chiều sâu DFS", "⛏️", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Dijkstra's Algorithm", "/ˈdaɪk.strəz ˈæl.ɡə.rɪ.ðəm/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Thuật toán Dijkstra: tìm đường đi ngắn nhất từ một đỉnh nguồn tới tất cả các đỉnh khác trên đồ thị trọng số không âm.",
     "GPS systems apply Dijkstra's algorithm to compute shortest driving routes.", "Hệ thống bản đồ GPS áp dụng thuật toán Dijkstra để tính quãng đường lái xe ngắn nhất.",
     "Thuật toán Dijkstra", "🗺️", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Bellman-Ford Algorithm", "/ˈbel.mən fɔːrd/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Thuật toán Bellman-Ford: tìm đường đi ngắn nhất trên đồ thị có thể chứa cạnh mang trọng số âm.",
     "Bellman-Ford detects negative weight cycles in financial arbitrage detection.", "Bellman-Ford phát hiện chu trình trọng số âm trong việc tìm chênh lệch giá tài chính.",
     "Thuật toán Bellman-Ford", "📉", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Floyd-Warshall Algorithm", "/flɔɪd ˈwɑːr.ʃəl/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Thuật toán Floyd-Warshall: tìm đường đi ngắn nhất giữa mọi cặp đỉnh trong đồ thị bằng quy hoạch động trong O(V^3).",
     "Floyd-Warshall calculates all-pairs shortest paths using dynamic programming.", "Floyd-Warshall tính toán đường đi ngắn nhất giữa mọi cặp đỉnh bằng quy hoạch động.",
     "Thuật toán Floyd-Warshall", "🌐", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Prim's Algorithm", "/prɪmz ˈæl.ɡə.rɪ.ðəm/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Thuật toán Prim: thuật toán tham lam tìm cây khung nhỏ nhất (MST) bằng cách mở rộng từ một đỉnh.",
     "Prim's algorithm designs telecommunication cable layouts at minimal cost.", "Thuật toán Prim thiết kế sơ đồ cáp viễn thông với chi phí tiết kiệm nhất.",
     "Thuật toán cây khung Prim", "🌲", "https://images.unsplash.com/photo-1448375240586-882707db888b?w=600&auto=format&fit=crop&q=80"),

    ("Kruskal's Algorithm", "/ˈkrʌs.kəlz ˈæl.ɡə.rɪ.ðəm/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Thuật toán Kruskal: tìm cây khung nhỏ nhất bằng cách sắp xếp tất cả các cạnh theo trọng số tăng dần.",
     "Kruskal's algorithm connects pipeline networks with minimum total pipe length.", "Thuật toán Kruskal kết nối mạng lưới đường ống với tổng chiều dài ống nhỏ nhất.",
     "Thuật toán cây khung Kruskal", "🌉", "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"),

    ("A* Search Algorithm", "/eɪ stɑːr sɜːtʃ/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Thuật toán tìm kiếm A*: thuật toán tìm đường tối ưu kết hợp chi phí đã đi và hàm ước lượng heuristic.",
     "Video game AI characters use A* search to navigate through dynamic terrains.", "Nhân vật AI trong trò chơi điện tử dùng thuật toán A* để di chuyển qua địa hình.",
     "Thuật toán A* Heuristic", "🌟", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("Bit Manipulation", "/bɪt məˌnɪp.jəˈleɪ.ʃən/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Thao tác bít: các phép toán tác động trực tiếp trên từng bít nhị phân (AND, OR, XOR, dịch bít).",
     "Bit manipulation enables compact state representation and rapid calculations.", "Thao tác bít cho phép biểu diễn trạng thái cực gọn và tính toán siêu nhanh.",
     "Thao tác bít nhị phân", "⚡", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("In-Place Algorithm", "/ɪn pleɪs ˈæl.ɡə.rɪ.ðəm/", "noun", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Thuật toán tại chỗ: biến đổi cấu trúc dữ liệu mà không cần cấp phát thêm bộ nhớ phụ đáng kể O(1).",
     "Reversing an array using two pointers is an in-place algorithm.", "Đảo ngược một mảng dùng hai con trỏ là một thuật toán thực hiện tại chỗ.",
     "Thuật toán tại chỗ", "📍", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80"),

    ("NP-Complete", "/ˌen.piː kəmˈpliːt/", "adjective", "dsa", "Cấu trúc dữ liệu & Thuật toán",
     "Độ phức tạp NP-đầy đủ: lớp bài toán khó nhất trong NP mà chưa tìm ra thuật toán thời gian đa thức để giải quyết.",
     "The Traveling Salesperson Problem is a well-known NP-complete challenge.", "Bài toán người bán hàng chu du là một thách thức NP-đầy đủ nổi tiếng.",
     "Độ phức tạp NP-Complete", "🧩", "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80")
]

if __name__ == "__main__":
    print(f"Domain 2 terms count: {len(terms)}")
