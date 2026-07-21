from http.server import SimpleHTTPRequestHandler, HTTPServer
import urllib.parse  # ዩአርኤል ዲኮድ ለማድረግ የሚያስፈልግ

class PostHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8', errors='ignore')
        
        # 1. የ URL-encode ዳታውን ወደ መደበኛ ጽሑፍ ዲኮድ ማድረግ (+ ወደ space ይቀይራል)
        decoded_data = urllib.parse.unquote_plus(post_data)
        
        # 2. ከፊት ለፊቱ 'logs=' የሚል ጽሑፍ ካለ ቆርጦ ማውጣት (ንፁህ ዳታ እንዲሆን)
        if decoded_data.startswith("logs="):
            decoded_data = decoded_data.replace("logs=", "", 1)
        
        # 3. የተስተካከለውን ንፁህ ሎግ በተርሚናልህ ላይ ያሳያል
        print("\n--- አዲስ መረጃ ደርሷል (ዲኮድ የተደረገ) ---")
        print(decoded_data)
        print("------------------------------------------")
        
        # 4. መረጃውን 'server_logs.txt' በሚል ፋይል ውስጥ ያስቀምጣል
        with open("server_logs.txt", "a") as f:
            f.write(decoded_data + "\n")
            
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Success")

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 6060), PostHandler)
    print("please start port forwarding on port 6060\nlistening port on 6060...")
    server.serve_forever()
